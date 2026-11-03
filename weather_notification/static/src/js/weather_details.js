/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, onWillStart, useState} from "@odoo/owl";
import {Dropdown} from "@web/core/dropdown/dropdown";

class SystrayDropdown extends Component {
    setup() {
        this.action = useService("action");
        onWillStart(async () => {
            this.position = await new Promise((resolve, reject) => {
                navigator.geolocation.getCurrentPosition(resolve, reject);
            });

        });
        this.state = useState({
            weather_data: null,
            imageurl: "",
            today: null,
        });
    }

    // fetch the weather data
    async getdata() {
        const API_key = '9efa5421bce73745f9286139d344a4d0'

        const lat = this.position.coords.latitude;
        const lon = this.position.coords.longitude;

        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_key}`)
        this.state.weather_data = await response.json();
        this.state.imageurl = `http://openweathermap.org/img/w/${this.state.weather_data.weather[0].icon}.png`
        this.state.today = new Date().toDateString()

    }

}

SystrayDropdown.template = "systray_dropdown";
SystrayDropdown.components = {Dropdown};
export const systrayItem = {
    Component: SystrayDropdown,
};
registry.category("systray").add("SystrayDropdown", systrayItem, {sequence: 1});
