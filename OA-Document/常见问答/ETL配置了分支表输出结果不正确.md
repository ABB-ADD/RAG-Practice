# ETL配置了分支表输出结果不正确

**问题描述：**

在数据加工中配置了分支，表输出时只执行了其中一条分支，另外一条分支未执行

![](https://dl.eteams.cn/site/72009648-d324-4608-98ce-1cdbeb20a011?imageType=png)

**解决方式：**

ETL配置了分支，表输出的数量和分支数量成正比。即分支中配置了两条分支路线，则需要配置两个表输出动作进行对应。

![](https://dl.eteams.cn/site/39b263eb-3c70-44cd-9adb-c85df6fa6c3d?imageType=png)