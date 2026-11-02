import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";
import {onRendered, useState} from "@odoo/owl";
import {usePos} from "@point_of_sale/app/hooks/pos_hook";

patch(ControlButtons.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.orm = useService('orm')
        this.data =
        this.state = useState({
            value: 0
        });
        onRendered(async () => {
            await this.getdata()

        });

    },
    async getdata() {
        let order = this.pos.getOrder();
        const result = await this.orm.read("pos.session", [this.pos.session.id], ["total_discount_amount"])
            // this.result = this.pos.models["pos.session"].get(this.pos.session.id).total_discount_amount;

        let amount = order.getTotalDiscount() || 0
        this.state.value = Number(result[0].total_discount_amount + amount)
        // this.state.value = Number(this.result + amount)
        console.log('this.state.value', this.state.value)
        console.log('this.result', this.result)
        console.log('this.pos.session.id', this.pos.session.id)



    }
});
