# ETL抽取第三方数据加工汇总

**1.
**场景说明****

公司领导希望统计各个部门在第三方系统中的回款金额、支出金额进行一个汇总，制作一个可视化图表进行汇总展示，**同时希望汇总数据可以进行二次加工处理再利用展示效果如下**：

![](https://dl.eteams.cn/site/2be1af54-aa89-4f12-9602-63298d9a706f?imageType=png)

**![](https://dl.eteams.cn/site/ff6093df-fa36-489d-8cb8-3a9b6678074c?imageType=png)**

**2.
**功能简介****

上述场景可以通过数据加工中的自助ETL功能通过数据连接，和第三方数据库获取数据连接访问，通过ETL表输入获取第三方库里的数据表，配合ETL中如连接、字段选择、分组汇总等功能对数据进行初步的加工统计汇总。数据抽取至指定库、指标表内，通过自助sql视图对数据进行二次加工处理，在使用页面、数据分析报表时可以通过获取sql视图展示最终的数据效果。

**3. 操作说明**

1.在数据加工中选择-数据连接，创建和第三方数据库的链接动作。

![](https://dl.eteams.cn/site/54fcc45a-66e4-4c2d-8055-d7fb219e6c1b?imageType=png)

2. 通过数据加工首页的
快捷入口自助ETL
或
数据开发
，进入ETL创建一个新的空白ETL

![](https://dl.eteams.cn/site/16b6d715-2627-4fe9-9093-943442d68dee?imageType=png)

3. 拖入一个表输入组件，配置需要连接的数据库，获取连接表信息，点击
预览
，可在底部查看表内数据；

此处拖入两个表输入组件，分别获取第三方库里的回款表、支出表

![](https://dl.eteams.cn/site/b26dc4d8-e9d0-4257-a5e5-77023971a986?imageType=png)

4.使用
连接动作
，配置两个输入表的关联关系，添加关联字段连接两个输入表

![](https://dl.eteams.cn/site/c1d3fa79-4ddc-47f9-aa7b-850657dd38b7?imageType=png)

5.使用
字段选择
动作，
获取全部字段
，此步确定需要最终输出是需要获取的字段，多余无需展示的字段通过删除按钮去掉

![](https://dl.eteams.cn/site/2c0d13d4-4804-4e0a-95c0-f71e30a7a0bc?imageType=png)

6.选择
表输出
动作，将配置好的数据，输出至
指定的库中
，配置一个
表名
，选择
数据写入方式
。保存后执行等待输出结果即可

![](https://dl.eteams.cn/site/005777f8-8e5b-42c1-b14a-be992007875b?imageType=png)

8.通过
数据准备配置一个sql数据集
，选择通过ETL输出之后的表名，对表进行查询操作进行数据二次加工操作

![](https://dl.eteams.cn/site/4e778868-640c-498b-aa78-61bd2cef9c09?imageType=png)

9.通过页面引擎、或数据报表，选择数据加工-sql数据集，进行数据引用获取

![](https://dl.eteams.cn/site/4eae73e8-f09e-48e3-ae55-5bf8dbd35994?imageType=png)

最终可视化效果展示如下:

![](https://dl.eteams.cn/site/4d2c9818-f6d9-4b8b-9892-8e10a01ffc9a?imageType=png)