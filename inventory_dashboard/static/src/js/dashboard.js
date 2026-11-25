/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, onWillStart, useRef, onMounted, useState, onRendered, useEffect} from "@odoo/owl";
import {loadBundle} from "@web/core/assets";
import {serializeDateTime} from "@web/core/l10n/dates";

const actionRegistry = registry.category("actions");

class InventoryDashboard extends Component {
    setup() {
        super.setup();
        this.state = useState({
            sort: {year: false, month: false},// the month,year from filter
            product_data: null,
            filtering: {},// the data used for filtering
            warehouses: [], // all warehouses
            location: [],
            inventory_location: [],
            location_data: {},

        });
        this.orm = useService('orm');
        this.canvasRef = useRef("canvas");
        this.chart = null;
        this.sort = {}
        this.startDate = false
        this.endDate = false
        //get the past 5 year from current year
        const {DateTime} = luxon;
        const currentYear = DateTime.now().year;
        this.state.filtering.years = Array.from({length: 5}, (_, i) => currentYear - i);
        useEffect(
            () => {
                const fetchData = async () => {
                    this.state.product_data = await this.orm.call(
                        "inventory.dashboard",
                        "action_fetch",
                        [[]],
                        {date: this.state.sort}
                    );
                    this._fetch_data();
                };
                fetchData();
            },
            () => [this.state.sort.month]
        );


        onWillStart(async () => {
            // Loads Odoo's built-in Chart.js bundle before rendering
            await loadBundle("web.chartjs_lib");
        });

    }

    async updateOperator(value) {
        this.state.sort.year = parseInt(value)
        this.state.filtering.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    }

    async onselectFilter(value) {
        this.state.sort.month = parseInt(value)
        console.log(1, this.state.sort)
    }

    async _fetch_data() {
        console.log(567)
        // fetch all warehouses
        this.state.warehouses = await this.orm.searchRead("stock.warehouse",
            [],
            ["name", "id"]
        )
        // let inventory_location = await this.orm.call("stock.location", "action_fetch", [[]], {});

        if (this.chart) {
            console.log(1111, this.chart)
            this.chart.destroy();
        }
        const chartLabels = this.state.product_data.product_stock;
        const avg_expense_product = this.state.product_data.avg_expense_by_product
        const picking_type = this.state.product_data.picking_group
        const internal_transfer_move = this.state.product_data.internal_transfer_move

        const data = [{
            'chart_id': 'product_incoming_chart',
            'type': 'bar',
            'label': 'Products',
            'data': chartLabels.filter((v) => v.incoming_qty > 0).map(item => item.incoming_qty),
            'labels': chartLabels.filter((v) => v.incoming_qty > 0).map(item => item.name),
            'text': 'Product Incoming Stock',
            'position': 'top'
        }, {
            'chart_id': 'product_outgoing_chart',
            'type': 'bar',
            'label': 'Products',
            'data': chartLabels.filter((v) => v.outgoing_qty > 0).map(item => item.outgoing_qty),
            'labels': chartLabels.filter((v) => v.outgoing_qty > 0).map(item => item.name),
            'text': 'Product Outgoing Stock',
            'position': 'top'

        }, {
            'chart_id': 'avg_product_cost',
            'type': 'pie',
            'label': 'Products',
            'data': avg_expense_product.map(item => item.cost),
            'labels': avg_expense_product.map(item => item.product_id),
            'text': 'Average Expense of A product',
            'position': 'right'

        }, {
            'chart_id': 'group_by_picking_type',
            'type': 'pie',
            'label': 'Transfer Count',
            'data': picking_type.map(item => item[1]),
            'labels': picking_type.map(item => item[0]),
            'text': 'Transfer Count By Picking Type',
            'position': 'right'

        }, {
            'chart_id': 'internal_tranfer_product_count',
            'type': 'bar',
            'label': 'Product',
            'data': internal_transfer_move.map(item => item[1]),
            'labels': internal_transfer_move.map(item => item[0]),
            'text': 'Internal Transfer By Product',
            'position': 'top'

        }]

        for (const i of data) {
            this.chart = new Chart(i.chart_id, {
                type: i.type,
                data: {
                    labels: i.labels,
                    datasets: [{
                        label: i.label,
                        data: i.data,
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: i.position,
                        },
                        title: {
                            display: true,
                            text: i.text
                        }
                    }
                },
            });
        }

    }

// Warehouse and its location
    async onSelectItem(recordId) {

        this.state.inventory_location = await this.orm.searchRead("stock.location",
            [["warehouse_id", "=", recordId], ['create_date', '<=', this.startDate], ['create_date', '>=', this.endDate]],
            ["complete_name", "quant_ids", "usage", "location_id", 'warehouse_id']
        )
    }

// Location wise stock info
    async onselectWarehouse(recordId) {
        this.state.location = await this.orm.searchRead("stock.location",
            [["warehouse_id", "=", recordId], ["usage", '=', 'internal']], []
                ["complete_name"]
        )
    }

    async onselectLocation(recordId) {
        const location = await this.orm.searchRead("stock.location",
            [["id", "=", recordId], ['create_date', '<=', this.startDate], ['create_date', '>=', this.endDate]], []
        )
        const quants = await this.orm.searchRead(
            "stock.quant",
            [["id", "in", location[0]?.quant_ids], ['create_date', '<=', this.startDate], ['create_date', '>=', this.endDate]],
            ["product_id", "quantity", "reserved_quantity", "lot_id", "product_uom_id"]
        )
        this.state.location_data =
            {
                'data': location[0],
                'quants': quants
            }
    }
}

InventoryDashboard.template = "dashboard_view.InventoryDashboard";
actionRegistry.add("inventory_dashboard_tag", InventoryDashboard);
