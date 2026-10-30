/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {PosStore} from "@point_of_sale/app/services/pos_store";
import {AlertDialog} from "@web/core/confirmation_dialog/confirmation_dialog";
import {_t} from "@web/core/l10n/translation";


patch(PosStore.prototype, {
    async pay() {
        let order = this.getOrder();
        if (!order) {
            return await super.pay(...arguments);
        }
        let session = order.session_id
        let total_discount_amount = 0
        let discount_amount_limit = 0
        const result = await this.data.read("pos.session", [session.id], ["total_discount_amount"])
        console.log(222, result[0].total_discount_amount)

        total_discount_amount = result[0].total_discount_amount
        console.log(6666, total_discount_amount)
        discount_amount_limit = this.config.discount_amount_limit
        if (discount_amount_limit > 0) {
            let amount = order.getTotalDiscount()

            total_discount_amount = total_discount_amount + amount

            if (total_discount_amount > discount_amount_limit) {
                this.dialog.add(AlertDialog, {
                    title: _t("Discount Limit Exceed"),
                    body: _t("From the discount limit: %s & you have  remaining of %s amount can add", discount_amount_limit, Math.max(0,(discount_amount_limit -  result[0].total_discount_amount).toFixed(2))),
                });
            }
            console.log(2222, total_discount_amount)

        }
        return super.pay(...arguments);
    },
})