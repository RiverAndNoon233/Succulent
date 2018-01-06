const mutations = {
    change_type(state,user_info){
        state.user_info = user_info
        localStorage.user_info = JSON.stringify(user_info)
    },
    initLogin(state,data){
        state.LoginOnData=data
    },
    changeTitle_know(state,title){
    	state.title_know = title
    },
}
export default mutations