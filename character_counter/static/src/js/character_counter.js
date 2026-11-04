/** @odoo-module **/
import {registry} from "@web/core/registry";
import {Component, useState} from "@odoo/owl";
import {standardFieldProps} from "@web/views/fields/standard_field_props";

export class CharCounter extends Component {
    static template = "character_counter.widget";
    static props = {
        ...standardFieldProps,
        max_count: {type: Number},
        max_field: {type: String},
    };

    setup() {
        this.state = useState({
            text: this.props.value || "",
        });
        this.options
    }

    get options() {
        const max_field = this.props.record.data[this.props.max_field];
        console.log(456789,max_field)

        // return this.props.record.filter(([value, _]) => max_field.includes(value));

    }

    onInputText(ev) {
        const val = ev.target.value;
        this.state.text = val;
        this.props.record.update({[this.props.name]: val})
    }
}

export const charCounter = {
    component: CharCounter,
    supportedTypes: ["integer"],
    extractProps({options}) {

        return {
            max_count: options.max_count || 25,
            max_field: options.max_field
        };
    },
};
registry.category("fields").add("char_counter", charCounter);
