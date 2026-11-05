/** @odoo-module **/
import {registry} from "@web/core/registry";
import {Component, useState, onMounted} from "@odoo/owl";
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {useInputField} from "@web/views/fields/input_field_hook";
import {CharField} from "@web/views/fields/char/char_field";


export class CharCounter extends CharField {
    static template = "character_counter.widget";
    static props = {
        ...standardFieldProps,
        max_count: {type: Number},
        max_field: {type: String},
    };

    setup() {
        this.state = useState({
            length: 0,
        });
        useInputField({
            getValue: () => this.props.record.data[this.props.name] || "",
            refName: "input",
            parse: (v) => this.parse(v),
        });

        onMounted(() => {
            this.state.length = this.props.record.data[this.props.name].length
        })

        this.max_field = this.props.record.data[this.props.max_field] || this.props.max_count
    }

    onInputText(ev) {
        this.state.length = ev.target.value.length;
    }

}

export const charCounter = {
    component: CharCounter,
    supportedTypes: ["char", "text"],
    extractProps({options}) {
        return {
            max_count: options.max_count || 25,
            max_field: options.max_field
        };
    },
};
registry.category("fields").add("char_counter", charCounter);
