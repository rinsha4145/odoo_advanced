/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {ControlButtons,} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";
import {Orderline} from "@point_of_sale/app/components/orderline/orderline";


patch(Orderline.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
    },

    get totalDiscount() {
        let order = this.pos.getOrder();
        let total_discount_amount = 0;



        let discount_amount_limit = this.pos.config.discount_amount
        total_discount_amount = total_discount_amount + order.getTotalDiscount()
            // Number(sessionStorage.getItem("total_discount_amount")) + order.getTotalDiscount();
        // console.log(56789,order.currencyDisplayPriceIncl)
        if (total_discount_amount > discount_amount_limit) {
            alert('discount limit is over')
        }
        console.log(456789,total_discount_amount)
        if(total_discount_amount > 0)
            // sessionStorage.setItem("total_discount_amount", total_discount_amount);
        return {
            discount_amount: total_discount_amount
        }
    },

})