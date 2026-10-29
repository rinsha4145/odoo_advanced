/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {PosStore} from "@point_of_sale/app/services/pos_store";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {useService} from "@web/core/utils/hooks";
import {AlertDialog} from "@web/core/confirmation_dialog/confirmation_dialog";
import {_t} from "@web/core/l10n/translation";



patch(PosStore.prototype, {
    setup() {
        super.setup(...arguments);
        // this.pos = usePos();
        // this.orm = useService("orm");
    },
    async pay() {
        let order = this.getOrder();
        if (!order) {
            return await super.pay(...arguments);
        }
        let session = order.session_id
        let total_discount_amount = 0
        let discount_amount_limit = 0
        const result = await this.data.read("pos.session", [session.id], ["total_discount_amount"])
        console.log(222, result)

        // result.then((currentTotalDiscountAmount) => {
        total_discount_amount = 0
        console.log(6666, total_discount_amount)
        discount_amount_limit = this.config.discount_amount_limit
        if (discount_amount_limit > 0) {
            let amount = order.getTotalDiscount()

            total_discount_amount = total_discount_amount + amount
            // Number(sessionStorage.getItem("total_discount_amount")) + order.getTotalDiscount();

            if (total_discount_amount > discount_amount_limit) {
                // alert('discount limit is over')
                this.dialog.add(AlertDialog, {
                    title: _t("Validation Error"),
                    body: 'discount limit exceeded',
                });
            }
            console.log(2222, total_discount_amount)

            // sessionStorage.setItem("total_discount_amount", total_discount_amount);
            // if (payment) {
            //     console.log(789, payment)
            this.data.write("pos.session", [session.id], {total_discount_amount: total_discount_amount});
            // }
        }


        // }).catch((error) => {
        //     console.error("Error fetching discount:", error);
        // });
        const paymentResult = await super.pay(...arguments);
        return paymentResult
    },
})