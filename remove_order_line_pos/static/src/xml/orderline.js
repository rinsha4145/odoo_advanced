/** @odoo-module */
import {patch} from "@web/core/utils/patch";
import {Orderline} from "@point_of_sale/app/components/orderline/orderline";

patch(Orderline.prototype, {
    onClickMessage(vals) {
        console.log(123, vals)
        console.log(45, this.props.line.PosOrder)
    },
});
