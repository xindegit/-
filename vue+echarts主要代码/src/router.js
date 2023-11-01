import { createRouter, createWebHistory } from 'vue-router'


import blog from './components/blog.vue';
import comment_top10 from './components/comment_top10.vue';
import digg_top10 from './components/digg_top10.vue';
import views_top10 from './components/views_top10.vue';


const router=createRouter({
    history: createWebHistory(),
    routes:[
        {path:'/blog', component:blog},
        {path:'/comment_top10',component:comment_top10},
        {path:'/digg_top10',component:digg_top10},
        {path:'/views_top10',component:views_top10}
    ]
})

export default router