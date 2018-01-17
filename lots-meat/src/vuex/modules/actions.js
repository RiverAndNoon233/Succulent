import axios from "axios"

import state from "./state.js"

const actions = {
    addGood({commit}){
        axios({
                method: 'get',
                url: '/static/api/car.json',
            }).then((res)=>{
                console.log(res)
                if(res.data.islogin == 0){
                    commit('addGood','')
                }else if(res.data.islogin == 1){
                    console.log(res.data)
                    commit('addGood',res.data.data)
                    
                }
            })
        },
    }
export default actions