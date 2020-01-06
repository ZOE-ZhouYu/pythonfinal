# pythonfinal
# 期末项目（17级交互式设计可视化与18级Python）

* 项目小组成员
1. 17级，王楚滢
2. **18级，周雨，学号：181013054，18级网络与新媒体3班**

## 项目简要描述：中国不同省份的年收入与其人口总数及其他因素的影响

* 主题：研究影响我国不同省份的年收入的因素。
* 主要调查方向：省份人口总数。
* 其他因素：1.生产总值；2.钢铁产量；3.氮氧化物排放量

## 关于项目

### [代码Github URL](https://github.com/ZOE-ZhouYu/pythonfinal)
### [Pythonanywhere 的部署 URL](http://zoebridge.pythonanywhere.com/)
### 一共有三个URL页面
1. 主页面（.../）
2. 主页面按钮点击跳转(.../tochart)
3. Awesome-pyecharts数据可视化地图图表(.../map)
---
## HTML文档描述
* 运用内部联合嵌套的CSS样式渲染丰富页面，设置background-color
* 对render.html中，针对box模型中div元素进行设计，添加背景颜色

## Python文档描述
* 包含了基本的templates、static、app.py，以及CSV数据文档，实现了基本的交互，并运用相关数据体现项目。
* 使用了pyecharts模块，实现了数据可视化地图、图表展示。
* 通过pandas提供的相关函数【df=pd.read_csv("###.csv",encoding='gbk')】读取csv文件中的文本数据。
* Flask架构中，调用render_template的功能，对results2.html以及后面传入的参数进行修改渲染。
* 运用“@app.route()”装饰器传递参数，通过GRT/POST展示页面。

## Web App动作描述：
* 拥有点击按钮功能，可进行页面切换，实现交互功能。
* 手动进入(.../map)页面，显示地图、图表，地图具有缩放效果，每个box中均可选择点击查看不同年份的效果。
