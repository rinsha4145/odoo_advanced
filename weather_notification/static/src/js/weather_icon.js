/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, onRendered, useState} from "@odoo/owl";
import {Dropdown} from "@web/core/dropdown/dropdown";
import {DropdownItem} from "@web/core/dropdown/dropdown_item";

class SystrayDropdown extends Component {
    setup() {
        this.action = useService("action");
        onRendered(async () => {
            await this.getdata()

        });
        this.state = useState({
            weather_data: null,
            imageurl:"",
            today:null,
        });
    }

    // Open Sale Orders in a list view
    async getdata() {
        const API_key = '9efa5421bce73745f9286139d344a4d0'

        const position = await new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(resolve, reject);
        });
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_key}`)
        this.state.weather_data = await response.json();
        console.log(56789, this.state.weather_data)
        this.state.imageurl=`http://openweathermap.org/img/w/${this.state.weather_data.weather[0].icon}.png`
        this.state.today= new Date().toDateString()

    }

}

SystrayDropdown.template = "systray_dropdown";
SystrayDropdown.components = {Dropdown};
export const systrayItem = {
    Component: SystrayDropdown,
};
registry.category("systray").add("SystrayDropdown", systrayItem, {sequence: 1});
