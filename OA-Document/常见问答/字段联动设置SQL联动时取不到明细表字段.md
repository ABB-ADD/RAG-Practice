# 字段联动设置SQL联动时取不到明细表字段

**问题描述：**

表单中进行字段联动配置，在选择SQL联动时，只能找到主表字段，取不到明细表字段？
![](https://dl.eteams.cn/site/0a66363a-68a6-4649-94e5-04bb0246acd2?imageType=png)

**解决方式：**

需要先在触发动作值改变时选择明细表字段，之后才能在sql中取到明细表：

![](https://dl.eteams.cn/site/274b79a8-7277-4098-9d14-5cb3181d26d3?imageType=png)