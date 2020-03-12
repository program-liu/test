<template>
  <v-navigation-drawer
    fixed
    clipped
    class="grey lighten-4"
    app
    v-model="drawer"
    style="z-index: 1"
    :mini-variant="mini"
    width="200"
    permanent="false"
  >
    <v-toolbar flat class="transparent">
      <v-list class="pa-0" dense>
        <v-list-tile>
          <v-list-tile-action>
            <v-btn icon @click="mini = !mini">
              <v-icon v-if="!mini">chevron_left</v-icon>
              <v-icon v-if="mini">chevron_right</v-icon>
            </v-btn>
          </v-list-tile-action>
          <v-list-tile-content style="font-size:12px; color: grey">
            收回菜单
          </v-list-tile-content>
        </v-list-tile>
        <v-divider></v-divider>
      </v-list>
    </v-toolbar>
    <v-list dense class="grey lighten-4">
      <template v-for="(item, i) in items">
        <v-layout row v-if="item.heading" align-center :key="i">
          <v-flex xs6>
            <v-subheader v-if="item.heading">{{ item.heading }}</v-subheader>
          </v-flex>
        </v-layout>
        <v-divider dark v-else-if="item.divider" class="my-3" :key="i"></v-divider>
        <v-list-tile :key="i" v-else :to="item.link">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              <span class="grey--text text--darken-1">{{ item.text }}</span>
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  // props: {
  //   isUserLogged: Boolean
  // },
  data: () => ({
    mini: false,
    items: [
      { icon: "forum", text: "学生管理", link: "/studentMangement" },
      { icon: "forum", text: "发布公告", link: "/announcement" },
      { icon: "school", text: "维修登记", link: "/maintenance" },
      { icon: "shopping_cart", text: "修改密码", link: '/passwordChange'},
      { icon: "group", text: "退出系统" }
    ]
  }),
  methods: {
  }
};
</script>

<style scoped>
</style>
