/** @odoo-module **/
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";
export class CharCounter extends Component {
    static template = "character_counter.widget";
    static props = {
        ...standardFieldProps,
    };
    updateValue(val) {
        this.props.record.update({ [this.props.name]: val });
    }
    get value() {
        return this.props.record.data[this.props.name];
    }
}
export const charCounter = {
    component: CharCounter,
    supportedTypes: ["integer"],
};
registry.category("fields").add("char_counter", charCounter);
