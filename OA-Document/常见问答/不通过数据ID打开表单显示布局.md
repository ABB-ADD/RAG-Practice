# 不通过数据ID打开表单显示布局

**问题描述：**

如何通过不使用数据id的情况下也可以打开对应数据的显示布局页面。

![](https://dl.eteams.cn/site/44cd9209-2338-40db-9b5a-b8e8877f26a2?imageType=png)

**解决方式：**

第一步：设置字段打开动作，链接地址放固定地址：
/sp/ebdfpage/formmode/view/convertPage?objId=表单id&pkfield=rkdh；

此处链接地址为固定地址。直接粘贴复制即可，需要手动修改的是
objid 、
pkfield
，如图1；

如何获取表单objid，

如图2；

如何获取

pkfield，如图3；

图1
![](https://dl.eteams.cn/site/addee559-037e-4ad3-9afa-19a6baa24375?imageType=png)

图2

![](https://dl.eteams.cn/site/e795b3a6-dda0-4f7c-8719-304d11b32759?imageType=png)

图3

![](https://dl.eteams.cn/site/d12ee801-28d6-40ca-b9c0-c0044fa43b34?imageType=png)

第二步：设置参数；左侧参数名称为固定值：
pkvalue ；
右侧参数值可选择表单字段；

**pkvalue和pkfield必须对应的是同一个字段。**

![](https://dl.eteams.cn/site/033f5ce4-84ba-43a1-9075-77c50f6a56da?imageType=png)

第三步：配置完成即可保存查看效果

![](https://dl.eteams.cn/site/79661170-e7b7-42a8-8791-483087b10cc6?imageType=png)