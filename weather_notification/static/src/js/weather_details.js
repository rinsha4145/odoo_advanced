/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, onMounted, useState} from "@odoo/owl";
import {Dropdown} from "@web/core/dropdown/dropdown";
import {user} from "@web/core/user";


class SystrayDate extends Component {
    setup() {
        this.action = useService("action");
        onMounted(async () => {
            // this.position = await new Promise((resolve, reject) => {
            //     navigator.geolocation.getCurrentPosition(resolve, reject);
            // })

            navigator.geolocation.getCurrentPosition(this.successr, this.fail)

        });
        this.orm = useService("orm");
        this.state = useState({
            weather_data: null,
            imageurl: "",
            today: null,
            api: "",
            error_message: ""
        });
    }

    successr(result) {
        console.log(123123123, result.coords)
        this.lat = result.coords.latitude;
        this.lon = result.coords.longitude;

    }

    fail(error) {
        console.log(123123123, error.message)
        return this.state.error_message(error.message)

    }

    // fetch the weather data
    async getdata() {
        const API = await this.orm.read("res.company", [user.activeCompany.id])

        console.log(6789, API[0].api_key)
        // const API_key = '9efa5421bce73745f9286139d344a4d0'
        this.state.api = API[0].api_key


        if (this.state.api) {
            const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${this.lat}&lon=${this.lon}&appid=${this.state.api}`)
            if (response.status == 200) {
                this.state.weather_data = await response.json();
                this.state.imageurl = `http://openweathermap.org/img/w/${this.state.weather_data.weather[0].icon}.png`
                this.state.today = new Date().toDateString()
            } else {
                return this.state.error_message = "Invalid  API KEY"

            }
        } else
            return false
    }
}

SystrayDate.template = "systray_dropdown";
SystrayDate.components = {Dropdown};
export const systrayItem = {
    Component: SystrayDate,
};
registry.category("systray").add("SystrayDate", systrayItem, {sequence: 1});
