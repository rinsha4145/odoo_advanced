/** @odoo-module **/
import {registry} from "@web/core/registry";
import {Component,useState} from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class CharCounter extends Component {
    static template = "character_counter.widget";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        this.maxCount = 100;
        this.state = useState({
            text: this.props.value || "",
        });
    }

    onInputText(ev) {
        const val = ev.target.value;
        this.state.text = val;
        console.log(567,this.props.record)
    }
}

export const charCounter = {
    component: CharCounter,
    supportedTypes: ["integer"],
};
registry.category("fields").add("char_counter", charCounter);
