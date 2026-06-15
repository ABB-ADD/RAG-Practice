# EB显示单位支持动态单位

**功能背景**

企业网盘模块在搭建过程中使用饼状图显示个人空间和全部空间时，需要根据空间大小显示不同的单位，比如空间小于1024B时，显示单位B，大于1024B时，显示单位KB。

**功能描述**

显示单位组件支持动态化单位

**功能说明**

1.  EB组件功能入口：数字面板、排行榜、图表、进度条、新二维报表。

2.  显示单位弹窗：无单位（默认选中）、固定单位、动态单位。

无单位：

![](https://dl.eteams.cn/site/ba4a9c3f-2f9a-41f6-b466-00a631ca7eeb?imageType=png)

固定单位（注意“二维报表”组件不支持时间单位）：

![](https://dl.eteams.cn/site/15a2604f-f380-4682-bb89-b5c63a6cff23?imageType=png)

动态单位：

![](https://dl.eteams.cn/site/8ca95d50-149a-4cae-8bb8-ddf52407d050?imageType=png)

3.  动态单位自定义：【单位量级】第一行不允许删除（无删除icon）

![](https://dl.eteams.cn/site/292670da-44e0-4ca0-a505-edd7dbd26a83?imageType=png)

每一行上的“+”表示：在此行下方添加一行

![](https://dl.eteams.cn/site/94c45d02-0659-486b-ac7f-756e482c68b6?imageType=png)

【数据单位基准】的单位自动填充到【单位量级】第一行，除第一行外右侧输入框后的单位名称默认填充上一行左侧的单位名称。

![](https://dl.eteams.cn/site/8c3fe964-906c-463b-9d98-6cf1e52c6579?imageType=png)

4.  历史数据：“无单位”对应类型：“无”；其他配置对应类型：“固定单位”。

5.  效果示例：

![](https://dl.eteams.cn/site/7765eea3-293a-408d-b5ce-b9d958f562e6?imageType=png)