/** @odoo-module **/
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { patch } from "@web/core/utils/patch";
import { OrderDisplay } from "@point_of_sale/app/components/order_display/order_display";

patch(OrderDisplay.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        // console.log(43, this.pos)
    },
    onClick() {
        let order = this.pos.getOrder();
        let lines = order.getOrderlines()
        // console.log(75843,lines)
        if (lines.length) {
            lines.filter(line => line.getProduct()).forEach(line => order.removeOrderline(line))
        }
    }
})
