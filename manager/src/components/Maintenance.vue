<template>
  <v-card>
    <v-layout row wrap>
      <v-flex xs5>  
      <v-card-title><p class="display-1">维修信息登记</p></v-card-title>
      <v-card-text>               
        <v-flex>
          宿舍楼号：<v-select
          :items="items"
          v-model="dva"
          laBel="请选择你的宿舍楼"
          solo
          ></v-select>
        </v-flex> 
        <v-flex>
         寝室号： <v-text-field
            laBel="Solo"
            v-model="qva"
            placeholder="请输入你的寝室号,例如：A112"
            solo
          ></v-text-field>
        </v-flex>            
        <v-flex>
          维修物品： <v-text-field
          laBel="Solo"
          v-model="mname"
          placeholder="请输入你的维修物"
          solo
          ></v-text-field>
        </v-flex>  
        <v-flex>
        损坏情况：<v-textarea
          solo
          laBel="例如：门把坏了"
          v-model="content"
          ></v-textarea>
        </v-flex>
              </v-card-text>
        <v-card-actions>
        <v-spacer></v-spacer>
        <v-Btn color="primary" Bottom @click="NewMaintenance">提交</v-Btn>
        <v-Btn color="primary" Bottom @click="setup" style="margin-right: 10px">重新输入</v-Btn>
        </v-card-actions>
        <v-dialog v-model="dialog" max-width="300px" dark>
          <v-card>
            <v-card-text>添加成功，请点击确认返回。</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="green" @click="dialog = false">确认</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-flex>
      <v-flex xs7>
      <v-card-title><p class="display-1">维修信息列表</p></v-card-title>
      <v-card-text> 
        <v-card>             
        <v-list two-line>
        <div v-for="(item, index) in weixiu" :key="index">
          <v-list-tile avatar ripple @click=";">
            <v-list-tile-content>
              <v-list-tile-title>{{ item.dwx }}</v-list-tile-title>    
            </v-list-tile-content>
            <v-list-tile-action>
              <v-list-tile-action-text>{{ item.dsun}}</v-list-tile-action-text>
            </v-list-tile-action>
          </v-list-tile>
          <v-divider v-if="index + 1 < items.length" :key="`divider-${index}`">
          </v-divider>
        </div>
      </v-list>
      </v-card> 
      </v-card-text>
      </v-flex>
    </v-layout>
  </v-card> 
</template>
<script>
import axios from 'axios'
  export default {
    data: () => ({
      dva: '',
      qva: '',
      mname: '',
      content: '',
      dialog: false,
      items: ['B15','B14','B13','B12','B11','B10', 'B09', 'B08', 'B07', 'B06', 'B05', 'B04', 'B03', 'B02', 'B01'],
      weixiu: [
      ]
    }),
    methods: {
      MaintenanceGet: function() {
        let self = this;
        axios.get('http://127.0.0.1:8000/api/ServiceViewSet/'
        ).
        then(function(response) {
          self.weixiu=response.data.results;
        }).
        catch(function(error) {
          console.log(error);
        });
      },
      NewMaintenance: function() {
        let self = this;
        let myDate = new Date();
        axios.post('http://127.0.0.1:8000/api/ServiceViewSet/', {
          'dlou_id': self.dva,
          'dno_id': self.qva,
          'dwx': self.mname,
          'dsun': self.content,
        }).
        then(function(response){
          self.dialog = true;
        }).
        catch(function(error) {
          console.log(error);
        });     
      },
    },
    mounted() {
      this.MaintenanceGet();
    },
  }
</script>
