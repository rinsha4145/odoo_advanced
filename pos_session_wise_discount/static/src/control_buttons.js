import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";
import {onRendered, onWillStart, useState} from "@odoo/owl";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";

patch(ControlButtons.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.orm = useService('orm')
        this.state = useState({
            value: 0
        });
        onRendered(async () => {
            await this.getdata()
            console.log(2)


        });

    },
    async getdata() {
        let order = this.pos.getOrder();
        const result = await this.orm.read("pos.session", [this.pos.session.id], ["total_discount_amount"])
        let amount = order.getTotalDiscount() || 0
        this.state.value = Number(result[0].total_discount_amount + amount)
        console.log(78, this.state.value)
        // console.log(78, result[0].id)
        // console.log(78, amount)


    }
});
