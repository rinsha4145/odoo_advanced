/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component} from "@odoo/owl";

const actionRegistry = registry.category("actions");

class InventoryDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
    }

    async _fetch_data() {
        console.log(567)
        let stock_incoming_products = await this.orm.call("product.template", "action_fetch", [], {});
        print(6578493,stock_incoming_products)
        // document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
        // document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
        // document.getElementById('revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
    }
}

InventoryDashboard.template = "dashboard_view.InventoryDashboard";
actionRegistry.add("inventory_dashboard_tag", InventoryDashboard);
