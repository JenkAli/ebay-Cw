import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    isAuthenticated: false,
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.isAuthenticated = true;
        state.token = localStorage.getItem("token") || "";
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
