/** @odoo-module **/
import {registry} from "@web/core/registry";
import {Component, useState} from "@odoo/owl";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {useInputField} from "@web/views/fields/input_field_hook";


export class CharCounter extends Component {
    static template = "character_counter.widget";
    static props = {
        ...standardFieldProps,
        about: {type: String},
        max_count: {type: Number},
        max_field: {type: String},
    };

    setup() {
        this.state = useState({
            text:  "",
        });

        useInputField({
            getValue: () => this.props.record.data[this.props.name] || "",
            parse: (v) => this.parse(v),
        });
        this.options

    }

    get options() {
        this.max_field = this.props.record.data[this.props.max_field] || this.props.max_count
        console.log(456789, this.props.record.data[this.props.max_field])
        console.log(456789, this.max_field)
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
    extractProps({options,name}) {
        console.log(123,name)
        return {
            max_count: options.max_count || 25,
            max_field: options.max_field,
            about: name
        };
    },
};
registry.category("fields").add("char_counter", charCounter);
