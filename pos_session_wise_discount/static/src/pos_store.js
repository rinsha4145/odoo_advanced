/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {PosStore} from "@point_of_sale/app/services/pos_store";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {useService} from "@web/core/utils/hooks";


patch(PosStore.prototype, {
    setup() {
        super.setup(...arguments);
        // this.pos = usePos();
        // this.orm = useService("orm");
    },
    async pay() {
        console.log(5678)
        await super.pay(...arguments);

        let order = this.getOrder();
        let payment = order.getSelectedPaymentline()
        let session = order.session_id
        let total_discount_amount = 0
        let discount_amount_limit = 0
        this.value().then((currentTotalDiscountAmount) => {
            total_discount_amount = currentTotalDiscountAmount
            console.log(6666, total_discount_amount)
            discount_amount_limit = this.pos.config.discount_amount_limit
            if (discount_amount_limit > 0) {
                let amount = order.getTotalDiscount()

                total_discount_amount = total_discount_amount + amount
                // Number(sessionStorage.getItem("total_discount_amount")) + order.getTotalDiscount();

                if (total_discount_amount > discount_amount_limit) {
                    alert('discount limit is over')
                }
                console.log(2222, total_discount_amount)

                // sessionStorage.setItem("total_discount_amount", total_discount_amount);
                if (payment) {
                    console.log(789, payment)
                    this.orm.write("pos.session", [session.id], {total_discount_amount: total_discount_amount});
                }
            }


        }).catch((error) => {
            console.error("Error fetching discount:", error);
        });
        // let current_total_discount_amount = Number(this.pos.config.total_discount_amount);

        return {discount_amount: total_discount_amount || 0}
    },
    async value() {
        let order = this.pos.getOrder();
        let session = order.session_id
        const result = await this.pos.data.read("pos.session", [session.id], ["total_discount_amount"]);
        return result[0].total_discount_amount
    }

})