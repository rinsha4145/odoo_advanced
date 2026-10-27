/** @odoo-module **/
import {Component} from "@odoo/owl";
import {ConfirmationDialog} from "../../../../../addons/web/static/src/core/confirmation_dialog/confirmation_dialog";
import {_t} from "../../../../../addons/web/static/src/core/l10n/translation";
import {usePos} from "../../../../../addons/point_of_sale/static/src/app/hooks/pos_hook";
import {useService} from "../../../../../addons/web/static/src/core/utils/hooks";
import {ProductScreen} from "../../../../../addons/point_of_sale/static/src/app/screens/product_screen/product_screen";

export class DeleteOrderLines extends Component {
    static template = "Orderline";

    setup() {
        this.pos = usePos();
        this.popup = useService('popup')
        this.notification = useService('pos_notification')
    }
   async onClick(){
        var order = this.pos.get_order();
        var lines = order.get_order_lines()
       if (lines.length){
           await this.popup.add(ConfirmationDialog,{title:'Clear Order',body:'are you want'})
               .then(({confirmed})=>{
                   if (confirmed == true){
                       lines.filter(line => line.get_product())
                           .foreach(line => order.removeOrderline(line))
                   }
                   else{
                       return false
                   }
               })
       }
       else{
           this.notification.add('no item removed')
       }
   }
}
ProductScreen.addControlButton({
    component:DeleteOrderLines,
});