import {PaymentScreen} from "@point_of_sale/app/screens/payment_screen/payment_screen";
import {patch} from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { useService } from "@web/core/utils/hooks";


patch(PaymentScreen.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.orm = useService('orm')
    },

    async validateOrder(line) {
        let order = this.pos.getOrder();
        let session = order.session_id
        let total_discount_amount = 0

        const result = await this.orm.read("pos.session", [session.id], ["total_discount_amount"])
        total_discount_amount = result[0].total_discount_amount
        let amount = order.getTotalDiscount()

        total_discount_amount = total_discount_amount + amount
        this.orm.write("pos.session", [session.id], {total_discount_amount: total_discount_amount});

        return super.validateOrder(...arguments);
    },
});
