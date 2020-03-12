<template>
  <div>
    <v-toolbar color="blue darken-3" dark app :clipped-left="$vuetify.breakpoint.mdAndUp" fixed>
      <v-toolbar-title style="width: 500px" class="ml-0 pl-3"></v-toolbar-title>
      <v-text style="width: 400px" class="headline">四川轻化工大学宿舍管理系统</v-text>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
    </v-toolbar>
  </div>
</template>

<script>
export default {
  props: {
  },
  data: () => ({
  }),
  methods: {
    Logout: function() {
      window.localStorage.clear();
      router.go(0);
    }
  }
};
</script>

<style>
.slim-text {
  font-weight: 300;
}
</style>
