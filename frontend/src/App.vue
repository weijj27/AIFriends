<script setup>

import NavBar from "@/components/navbar/NavBar.vue";
import {onMounted} from "vue";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const route = useRoute()     // useRoute 获取当前页面信息
const router = useRouter()   // useRouter 跳转页面

onMounted(async () => {
  try {
    const res = await api.get('/api/user/account/get_user_info/')
    const data = res.data
    if (data.result === 'success') {
      user.setUserInfo(data)
    }
  } catch (err) {
    console.log(err)
  } finally {
    user.setHasPulledUserInfo(true)
    if (route.meta.needLogin && !user.isLogin()) {
      await router.replace({
        name: 'user-account-login-index',
      })
    }
  }
})
</script>

<template>
  <NavBar>
    <RouterView />   
  </NavBar>
</template>

<style scoped>

</style>
