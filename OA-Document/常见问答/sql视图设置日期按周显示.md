# sql视图设置日期按周显示

**问题描述：**

通过sql视图如何设置日期字段按照自然周显示

**解决方式：**

第一步：设置函数语法

CEILING(

(

DAY(字段名称) + WEEKDAY(字段名称 - INTERVAL DAY(字段名称) -1 DAY)

) / 7

) as **周第二步**；运行查看结果

![](https://dl.eteams.cn/site/5b3ca635-6702-4ec4-8a17-3900a933bc18?imageType=png)