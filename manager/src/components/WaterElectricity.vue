<template>
  <div>
    <p class="display-1">水电费查询</p>
    <v-layout wrap row>
      <v-flex class="px-4" xs3>
        <v-select :items="campuses" v-model="cva" label="请选择校区:"></v-select>
      </v-flex>
      <v-flex class="px-4" xs3>
        <v-select :items="dormitoryBuildings" v-model="dva" label="请选择宿舍楼号:"></v-select>
      </v-flex>
      <v-flex class="px-4" xs4>
        <v-text-field v-model="dormitorys" label="请输入宿舍号(例如 A112):"></v-text-field>
      </v-flex>
      <v-flex class="px-4" xs2>
        <v-btn color="info" block @click="WaterElectricityGet">点击查询</v-btn>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs5>
        <v-card style="margin-left: 20px">
          <v-card-title>{{ name1 }}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <p>校区:     {{ item1.xiaoqu }}</p>
            <p>宿舍号: {{ item1.dlou_id }}-{{ item1.dno_id}}</p>
            <p>剩余电费: {{ item1.wwt }}元</p>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs5>
        <v-card style="margin-left: 20px">
          <v-card-title>{{ name2 }}</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <p>校区:     {{ item2.xiaoqu }}</p>
            <p>宿舍号: {{ item2.dlou_id }}-{{ item2.dno_id}}</p>
            <p>剩余水费: {{ item2.wdt }}元</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    components: {
    },
    data: () => ({
      cva: '',
      dva: '',
      dormitorys: '', //宿舍号
      campuses: [ //校区
        {value: '汇南校区', text: '汇南校区'},
        {value: '汇北校区', text: '汇北校区'},
        {value: '营盘校区', text: '营盘校区'},
        {value: '宜宾校区', text: '宜宾校区'},
        {value: '黄岭校区', text: '黄岭校区'},
      ],
      dormitoryBuildings: [ //宿舍楼号
        {value: 'B15', text: 'B15'},
        {value: 'B14', text: 'B14'},
        {value: 'B13', text: 'B13'},
        {value: 'B12', text: 'B12'},
        {value: 'B11', text: 'B11'},
        {value: 'B10', text: 'B10'},
        {value: 'B09', text: 'B09'},
        {value: 'B08', text: 'B08'},
        {value: 'B07', text: 'B07'},
        {value: 'B06', text: 'B06'},
        {value: 'B05', text: 'B05'},
        {value: 'B04', text: 'B04'},
        {value: 'B03', text: 'B03'},
        {value: 'B02', text: 'B02'},
        {value: 'B01', text: 'B01'},
      ],
      name1: '电费详情表',
      name2: '水费详情表',
      item1: { },
      item2: { },         
    }),
    methods: {
      WaterElectricityGet: function() {
        let self = this;
        axios.get(`http://127.0.0.1:8000/api/WaterViewSet/?dlou_id=${self.dva}&dno_id=${self.dormitorys}`
        ).   
        then(function(response) {
          self.item1=response.data.results[0];
          self.item2=response.data.results[0];
        }).
        catch(function(error) {
          console.log(error);
        });
      },
    }
  }
</script>