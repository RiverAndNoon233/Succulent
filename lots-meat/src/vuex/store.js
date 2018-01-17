import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

import state from './modules/state'
import mutations from './modules/mutations'
import getters from './modules/getters'
import actions from './modules/actions'


//可以设置store管理的state/getter，mutations,actions
const store = new Vuex.Store({
    state,mutations,getters,actions
})

export default store