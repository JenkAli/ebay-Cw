import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VueNumberInput from "@chenfengyuan/vue-number-input";

import "./assets/main.css";

const app = createApp(App);

app.use(router);
app.component(VueNumberInput.name, VueNumberInput);
app.mount("#app");
