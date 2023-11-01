<script setup>
import { reactive, ref } from 'vue'
const link = reactive([
    { path: '/blog', name: "首页" },
    { path: '/comment_top10', name: "评论数Top10" },
    { path: '/digg_top10', name: "点赞数top10" },
    { path: '/views_top10', name: "观看数top10" }
])
const topidnex = ref(sessionStorage.getItem('index') ? sessionStorage.getItem('index') : 0);
const toLink = (index) => {
    sessionStorage.setItem('index', index)
    topidnex.value = index
}
</script>
<template>
    <div>
        <h1 class="title">数据可视化</h1>
        <div class="content">
            <div class="nav">
                <router-link :to="item.path" v-for="(item, index) in link" :key="index"
                    :class="topidnex == index ? 'a-click' : ''" @click="toLink(index)">{{ item.name }}</router-link>
            </div>
            <div class="main">
                <router-view></router-view>
            </div>
        </div>

    </div>
</template>
<style scoped>
.title {
    text-align: center;
}

.content {
    display: flex;
    flex-wrap: wrap;

    .nav {
        display: flex;
        flex-direction: column;
        font-size: 20px;

        a {
            padding: 10px 20px;
            text-decoration: none;
            color: rgb(53, 43, 200);
            transition: all .5s;

            &:hover {
                color: rgb(129, 66, 66);
                background-color: #fff;
            }
        }
    }
    
}

.a-click {
    color: rgb(225, 29, 29) !important;
    background-color: #fff;
}
</style>