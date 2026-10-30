import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {patch} from "@web/core/utils/patch";
import {useService} from "@web/core/utils/hooks";


patch(ControlButtons.prototype, {
    setup() {
        super.setup(...arguments);
        this.orm = useService('orm')
        this.getdata()
    },
    async getdata() {
        const result = await this.orm.read("pos.session", [this.pos.session.id], ["total_discount_amount"])
        console.log(78, result[0].total_discount_amount)
        return {value:result[0].total_discount_amount}
    }
});
