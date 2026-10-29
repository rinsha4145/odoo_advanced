/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {ControlButtons,} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {Orderline} from "@point_of_sale/app/components/orderline/orderline";
import {useService} from "@web/core/utils/hooks";


patch(Orderline.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.orm = useService("orm");
    },

    get totalDiscount() {
        let order = this.pos.getOrder();
        let payment = order.getSelectedPaymentline()
        let current_total_discount_amount = this.value()
        // let current_total_discount_amount = this.pos.config.total_discount_amount;
        let total_discount_amount = 0
        console.log(6666, current_total_discount_amount)

        let discount_amount_limit = this.pos.config.discount_amount_limit
        if (discount_amount_limit > 0) {
            let amount = order.getTotalDiscount()
            let total_discount_amount = current_total_discount_amount + amount
            // Number(sessionStorage.getItem("total_discount_amount")) + order.getTotalDiscount();

            if (total_discount_amount > discount_amount_limit) {
                alert('discount limit is over')
            }
            console.log(2222, total_discount_amount)

            // sessionStorage.setItem("total_discount_amount", total_discount_amount);

            // let success = payment.validateOrder()
            if (payment) {
                console.log(789, payment)
                this.orm.write("pos.config", [this.pos.config.id], {total_discount_amount: total_discount_amount});
            }
        }

        return {discount_amount: total_discount_amount || 0}


    },
    async value() {
        const result = await this.pos.data.read("pos.config", [this.pos.config.id], ["total_discount_amount"]);
        return result[0].total_discount_amount
    }

})