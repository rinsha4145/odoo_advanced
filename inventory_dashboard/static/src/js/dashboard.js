/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, onWillStart, useRef, onMounted} from "@odoo/owl";
import {loadBundle} from "@web/core/assets";

const actionRegistry = registry.category("actions");

class InventoryDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.canvasRef = useRef("canvas");
        this.chart = null;

        onWillStart(async () => {
            // Loads Odoo's built-in Chart.js bundle before rendering
            await loadBundle("web.chartjs_lib");
        });
        onMounted(() => {
            this._fetch_data();
        });
    }

    async _fetch_data() {
        console.log(567)

        let product_data = await this.orm.call("product.template", "action_fetch", [[]], {});
        // let inventory_location = await this.orm.call("stock.location", "action_fetch", [], {});
        // console.log(4567,inventory_location)
        if (this.canvasRef.el) {
            if (this.chart) {
                this.chart.destroy();
            }
        }
        const chartLabels = product_data.product_stock;
        const data = [{
            'chart_id': 'product_incoming_chart',
            'type': 'bar',
            'label': 'Products',
            'data': chartLabels.filter((v) => v.incoming_qty > 0).map(item => item.incoming_qty),
            'labels': chartLabels.filter((v) => v.incoming_qty > 0).map(item => item.name),
            'text': 'Product Incoming Stock'
        }, {
            'chart_id': 'product_outgoing_chart',
            'type': 'bar',
            'label': 'Products',
            'data': chartLabels.filter((v) => v.outgoing_qty > 0).map(item => item.outgoing_qty),
            'labels': chartLabels.filter((v) => v.outgoing_qty > 0).map(item => item.name),
            'text': 'Product Outgoing Stock'
        }]
        for (const i of data) {
            new Chart(i.chart_id, {
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
                            position: 'top',
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
}

InventoryDashboard.template = "dashboard_view.InventoryDashboard";
actionRegistry.add("inventory_dashboard_tag", InventoryDashboard);
