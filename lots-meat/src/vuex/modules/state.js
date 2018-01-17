const state = {
    user_info:localStorage.user_info?localStorage.user_info:'',
    LoginOnData:'',
    title_know:'多多',
    find_type:"",
    detail_type:'',
    car:localStorage.car?JSON.parse(localStorage.car):[],
    gid:'',
    carprice:''
}
export default state