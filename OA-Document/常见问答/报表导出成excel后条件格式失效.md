# 报表导出成excel后条件格式失效

**问题描述：**

报表写了条件格式，用的“文本包含”，预览时候条件格式正常，导出excel不生效了

![](https://dl.eteams.cn/site/ff3afad5-8f2f-4317-9480-0f30be53efc0?imageType=png)

![](https://dl.eteams.cn/site/7a9c3433-3d43-48c4-ab83-3e02f60e9cf6?imageType=png)

![](https://dl.eteams.cn/site/2939bb88-cfaa-4dd9-a0d4-2920c16269aa?imageType=png)

**解决方式：**

条件格式-文本对最后的显示有影响，

如果报表无分页，可能是受撰写的代码块影响，提流程给开发写代码解决；

如果报表分页了，建议避免用文本的条件格式

，**或者导出**

excel

后在

excel

中重新设置下颜色显示。