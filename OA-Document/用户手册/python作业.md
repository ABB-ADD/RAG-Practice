# python作业

一、**功能背景用户在数据加工时无法通过编写**python脚本进行数据的处理和结果的展示，用户需要通过数据加工中python作业功能进行python脚本的编写和调试，并且对数据进行深度加工、深度处理和展示。

二、功能价值

python作业提供了一种灵活的代码编写的方式处理数据，对于熟悉python编程语言的用户来说可以大大提升数据处理的效率。

三、功能概述

1.SSH连接的新建、修改和测试

2.python作业的新建、编辑、修改以及保存

3.python**作业的运行和停止四**、业务流程图

![](https://dl.eteams.cn/site/4480db14-78a2-450f-a072-5b3647a85ee8?imageType=png)

五、功能详细说明

1. 新建SSH连接

+ 点击数据加工--> 设置 --> SSH连接--> 新增连接

  ![](https://dl.eteams.cn/site/1c9195bd-e429-4061-bd5d-32a4892095e5?imageType=png)

+ 进行SSH连接的新增、保存和测试

  ![](https://dl.eteams.cn/site/9f7728ca-e58d-4c4a-adb2-1ee8f25371a3?imageType=png)

2. python脚本的新建

+ 点击数据加工--> 数据开发--> 默认分组（选择自己的分组）--> 新建Python作业

  ![](https://dl.eteams.cn/site/ca53be7f-dc7a-42bf-84d3-781f484a21a3?imageType=png)
+ 在下面的页面中输入python作业的名称、需要选择的SSH连接以及需要执行的远程python编译器的路径，点击运行即可运行python脚本，点击停止可以停止当前运行的python作业

  ![](https://dl.eteams.cn/site/4ebb17fd-5482-4949-b09e-18d0561ace00?imageType=png)

  ![](https://dl.eteams.cn/site/71148609-216f-449a-b049-6c21a6190aac?imageType=png)

3. python作业的删除

+ 点击保存后，页面展示保存的python作业，可以通过下图页面操作进行python作业的删除

  ![](https://dl.eteams.cn/site/e08870d2-834e-4ae2-99eb-623f1e763676?imageType=png)

六、**使用和维护权限该功能用于设置数据集的使用**、编辑权限

![](https://dl.eteams.cn/site/7b4cb0e1-39e6-4202-acf2-4bb3645e329d?imageType=png)

维护权限：

* 可以对数据集的操作：查看、编辑、删除、移动分组、重命名、开启关闭缓存、给他人分配权限
* 系统管理员：拥有租户下的所有数据集的维护权限
* 创建人：**拥有自己创建的数据集的维护权限使用权限**：

* 可以对数据集的操作：
  查看、**卡片预览数据权限分配**：人员、部门、分部、角色、岗位、**所有人七**、**上下游关联功能点无**

八、注意点

1. 使用python作业需要先新建SSH连接，确保服务器的SSH协议端口是开放的。

2. 使用python作业需要
在本地的服务器上安装python编译器，在python作业页面上编译器的路径。