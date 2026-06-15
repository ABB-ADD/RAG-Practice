# 关联e-builder字段利用关联视图选择数据

***1.***
**编写目的**

在使用关联eb字段的过程中，很容易遇到以下几个问题：快捷搜索只有一个字段、数据不能以树形展示、数据太多了不好找等问题。如果遇到了这些问题，那么关联视图，便是对这类问题的优秀解法。本期内容将会讲解如何通过关联视图实现数据快速选择，优化关联eb字段数据不好挑选的问题。

如下图所示，相较于传统的关联eb字段，使用关联视图会有更清晰的结构，更多的筛选方法，可以帮助操作者更快的定位到所需的数据。

![](https://dl.eteams.cn/site/5f1742b0-af8a-4b0c-9259-7509550f8b9c?imageType=png)

![](https://dl.eteams.cn/site/fd3d1443-adc4-4fef-b5ab-35aff6135a7c?imageType=png)

***2.***
**思路分析**

为了实现上述场景，我们需要准备两张表单：公司架构表以及公司管理表。

在公司架构表下新建关联视图

，并配置显示列，列宽，查询字段，关联字段等信息，使表单字段与关联视图绑定。设置完成后，即可实现在关联e-buidler字段中进行搜索，筛选，如果需要的话，还可以设置树形结构。

***3.***
**操作说明**

***3.1***
**搭建**
**公司架构表与关联视图**

如下图所示，新增公司架构表，记录公司名称，公司状态等，

![](https://dl.eteams.cn/site/e1ea3bb2-95fc-4486-94c5-2e03cdb617cf?imageType=png)

在公司架构表下新建关联视图，并进入信息配置界面。

![](https://dl.eteams.cn/site/2e4bc843-a80e-4ccd-bd62-706ba4740229?imageType=png)

设置显示列，列宽，添加需要的筛选条件，配置及效果如下：

![](https://dl.eteams.cn/site/8e9c91cb-71d4-453f-92ef-e5ac5933e236?imageType=png)

![](https://dl.eteams.cn/site/529c967f-cf93-4628-b557-e806e650b372?imageType=png)

***3.2***
**新建公司管理表**

新建公司管理表，包含公司名（关联e-builder），公司情况等信息。

之后，在公司管理表的公司名字段处选择“启用关联视图”，并选择刚才所配置好的关联视图。

![](https://dl.eteams.cn/site/80325faa-66ac-4e62-b98e-7a4d8425894f?imageType=png)

***3.3***
**最终效果查看**

上述配置完成后，我们打开公司管理表，在选择公司名处展开，即可看到更清晰明了的数据，效果如下：

![](https://dl.eteams.cn/site/f4f30ccc-1cc1-4766-a01a-ca7535db6ff8?imageType=png)

***4.***
**树形结构**

如果数据中有着明显的上下级关系，想在关联视图中展示出来的的话，只需要对“启用上下级”处进行配置即可。在本场景中，我们选择公司信息表中的“上级公司”字段作为“启用上下级”处的关联字段（

关联字段目前仅支持关联了当前表单的关联类型单选字段

）。

![](https://dl.eteams.cn/site/5309ed0c-10f9-45cd-852b-ae4563bfad5e?imageType=png)

![](https://dl.eteams.cn/site/3c2babf5-fbdf-4b22-91b1-3c1fc9b50333?imageType=png)

![](https://dl.eteams.cn/site/8cb9d653-4e29-4110-b774-d91a4d8e085a?imageType=png)

其他配置不变，效果如下：

![](https://dl.eteams.cn/site/6a59e060-4bd1-49d3-be54-15ed735501e0?imageType=png)