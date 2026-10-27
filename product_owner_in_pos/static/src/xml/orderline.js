/** @odoo-module **/
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {patch} from "@web/core/utils/patch";
import {Orderline} from "@point_of_sale/app/components/orderline/orderline";

patch(Orderline.prototype, {
    get lineScreenValues() {
        return {
            ...super.lineScreenValues,
            owner_id: this.line?.product_id.owner_id?.name,
        };
    },

})
