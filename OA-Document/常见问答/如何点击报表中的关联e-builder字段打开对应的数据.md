# 如何点击报表中的关联e-builder字段打开对应的数据

**问题描述：**

报表中的放入关联e-Builder字段，如何能够像在表格视图台账中那样，点击能够穿透到被关联的数据，如下图所示，点击能够打开供应商名称：

![](https://dl.eteams.cn/site/02258a57-83d8-4d6c-ad28-61b48ab7d42c?imageType=png)

**解决方式：**

首先需要复制被关联表单的页面地址-显示布局，本场景中复制供应商信息表的显示布局：

![](https://dl.eteams.cn/site/09e48280-bc98-487c-b0ee-68f47ad89013?imageType=png)

复制完成之后，将地址中的$dataid$替换成{关联字段所在的单元格}：

![](https://dl.eteams.cn/site/90dc9bf9-0b40-41bc-b5df-840e2985c982?imageType=gif)