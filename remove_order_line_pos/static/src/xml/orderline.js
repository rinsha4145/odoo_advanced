/** @odoo-module **/
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {patch} from "@web/core/utils/patch";
import {Orderline} from "@point_of_sale/app/components/orderline/orderline";

patch(Orderline.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        console.log(89,this.pos)
    },
    onClick() {
        let order = this.pos.getOrder();
        order.removeOrderline(this.props.line)
    }
})
