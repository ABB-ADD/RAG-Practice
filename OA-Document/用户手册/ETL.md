# ETL

**一、功能背景**

**在企业存在多种数据源**（如Oracle/MySQL/SQL Server等），

格式和结构不统一，难以直接分析。

传统开发需手动处理数据清洗、转换，代码冗余且易出错。需快速实现数据迁移、**及智能化挖掘并适应大数据量和高性能场景**，传统方式难以满足。

**二、功能价值**

  

整合支持多种数据源输入（数据库表、TXT/EXCEL/CSV文件/E10数据源、REST接口等），实现数据统一管理。

**可视化操作通过拖拉拽组件完成多种数据转换需求**（字段拆分、行列转置、JSON解析等），降低技术门槛

，简化统计分析；与BI系统深度集成。

**安全可控行级**/列级权限控制，数据写入支持覆盖、全删、追加三种模式。

**三、功能概述**

**1.ETL新建与编辑**

+ [添加节点](https://eteams.cn/community/help/1974470605417394143#添加节点)
+ [节点操作](https://eteams.cn/community/help/1974470605417394143#节点操作)
+ [单节点数据保存](https://eteams.cn/community/help/1974470605417394143#单节点数据保存)
+ [ETL数据集保存和取消](https://eteams.cn/community/help/1974470605417394143#ETL数据集保存和取消)
+ [ETL数据集操作](https://eteams.cn/community/help/1974470605417394143#ETL%E6%95%B0%E6%8D%AE%E9%9B%86%E6%93%8D%E4%BD%9C)
+ [回收站](https://eteams.cn/community/help/1974470605417394143#%E5%9B%9E%E6%94%B6%E7%AB%99)

**2.
**ETL组件介绍****

+ [输入类](https://eteams.cn/community/help/1966020608303017440)
+ [转换类](https://eteams.cn/community/help/1974669575443696042)
+ [输出类](https://eteams.cn/community/help/1974669562580996041)
+ [其他类](https://eteams.cn/community/help/1974669583040596043)

**3.
**ETL数据集****

+ [建模图表](https://eteams.cn/community/help/1974470605417394143#%E5%BB%BA%E6%A8%A1%E5%9B%BE%E8%A1%A8)
+ [基础信息](https://eteams.cn/community/help/1974470605417394143#%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF)
+ [数据结构](https://eteams.cn/community/help/1974470605417394143#%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
+ [数据权限](https://eteams.cn/community/help/1974470605417394143#%E6%95%B0%E6%8D%AE%E6%9D%83%E9%99%90)
+ [使用/维护权限](https://eteams.cn/community/help/1974470605417394143#%E4%BD%BF%E7%94%A8/%E7%BB%B4%E6%8A%A4%E6%9D%83%E9%99%90)
+ [操作日志](https://eteams.cn/community/help/1974470605417394143#%E6%93%8D%E4%BD%9C%E6%97%A5%E5%BF%97)
+ [运行日志](https://eteams.cn/community/help/1974470605417394143#%E8%BF%90%E8%A1%8C%E6%97%A5%E5%BF%97)
+ [运行](https://eteams.cn/community/help/1974470605417394143#%E8%BF%90%E8%A1%8C%E5%81%9C%E7%94%A8%E7%BC%96%E8%BE%91)
+ [停用](https://eteams.cn/community/help/1974470605417394143#%E8%BF%90%E8%A1%8C%E5%81%9C%E7%94%A8%E7%BC%96%E8%BE%91)
+ [编辑](https://eteams.cn/community/help/1974470605417394143#%E8%BF%90%E8%A1%8C%E5%81%9C%E7%94%A8%E7%BC%96%E8%BE%91)

**四、
**业务流程图****

****![](https://dl.eteams.cn/site/4a845c30-7f3f-42bb-a8f0-6f4668507c6a?imageType=jpg)****

****五、功能详细说明****

**1.ETL新建与编辑**

+ 新建ETL:
  新建入口：数据加工-数据开发-选择分组-新建ETL

  ![](https://dl.eteams.cn/site/78bbd8b9-9d45-49ff-a5d3-73aaa75775e3?imageType=jpg)
+ **添加节点左侧组件可拖动到右侧画布上生成对应类型节点**

鼠标选中节点（输出节点）的锚点可拖动出节点连线，这时移动鼠标到其他节点（输入节点）对应锚点时，**点击锚点可连接两个节点输入表**、**文件不可相互连接一个完整的流程必须包含一个输入类**、一个输出类，中间可以添加转换类、其它类节点组件

![](https://dl.eteams.cn/site/6f9a4a2b-7def-449d-b1e5-0bcc63ad0b67?imageType=jpg)

+ **节点操作编辑**：双击画布中节点、点击节点上的编辑按钮、
或者通过鼠标右键点击节点配置
，**可以进入节点编辑弹窗删除**：点击节点上的删除按钮、
或者通过鼠标右键点击节点删除
，可以删除节点

![](https://dl.eteams.cn/site/a0a97699-9361-4288-ab4c-58a4cad8d04e?imageType=png)

+ 单节点数据保存

  当处于每个节点弹窗时，点击画布中的空白区域（见图）即可保存节点信息

  ![](https://dl.eteams.cn/site/d88d9aa5-d947-479d-9f3c-913db554929d?imageType=jpg)
+ ETL**数据集保存和取消必须填写**ETL数据集名称后才可保存，ETL**名称不能重复点击保存按钮**，可以保存ETL数据集内容，生成一个ETL**数据集点击取消按钮**，不保存ETL，直接关闭弹窗

![](https://dl.eteams.cn/site/0f8a0fb8-e217-436f-b5bd-15c376b65bf2?imageType=jpg)

+ ETL**数据集操作移动到**：点击移动到可以修改ETL**的所属分组重命名**：点击重命名可以修改ETL**的名称复制**：支持复制ETL流程ID或者点击复制可以复制一个新的ETL，复制出的ETL名称为：原ETL名称\_copy\_随机数，其他内容与原ETL**一致删除**：点击删除可以删除ETL

![](https://dl.eteams.cn/site/6cf16c57-0566-42d6-906e-12a69ac0f0da?imageType=jpg)

+ **回收站点击回收站可以查看已经删除了的数据集**

恢复：点击可以恢复数据集到原分组，**数据集可正常使用彻底删除**：点击彻底删除可以彻底删除数据集

![](https://dl.eteams.cn/site/e96217f8-5746-44d7-b66f-f2b9d0be5ad9?imageType=jpg)

**2.
**ETL组件介绍****

+ [输入类](https://eteams.cn/community/help/1974669540113396040)
+ [转换类](https://eteams.cn/community/help/1974669575443696042)
+ [输出类](https://eteams.cn/community/help/1974669562580996041)
+ [其他类](https://eteams.cn/community/help/1974669583040596043)

**3.
**ETL数据集****

+ 建模图表

  1是ETL流程展示，与ETL编辑搭建页面一致，鼠标移动到节点上展示对应节点的运行信息；以及图标展示节点的运行结果：成功、失败、等待。

  2是展示ETL运行的整体详细日志信息，可以通过日志信息分析判断运行情况

  3是运行结果，
  日志右侧展示输出表名，点击下方展示运行结果，若存在多个输出，则展示多张表

  ![](https://dl.eteams.cn/site/f8fbe865-e803-4fbe-8dfb-5cba32d2a09f?imageType=jpg)
  ![](https://dl.eteams.cn/site/ad904993-b0dc-439a-9375-d0828c043eb8?imageType=jpg)
+ 基础信息

  点击基础信息可以查看ETL所属分组、创建时间等信息，并且支持ETL描述信息修改

  ![](https://dl.eteams.cn/site/33b1bf98-ef13-4639-ab8a-0263d8c560be?imageType=jpg)
+ 数据结构

  数据结构可以查看输出表的数据结构，展示序号、字段名称、字段类型、备注名称等信息

  ![](https://dl.eteams.cn/site/b7631a96-6619-41bc-b991-1986f87e5a1e?imageType=jpg)
+ 数据权限

  1、可以对etl结果设置行权限、列权限、支持选择继承某个EB表单权限

  2、没有设置行权限、列权限的etl，只有系统管理员、创建人可以查看到运行结果

  3、行权限

- 可以对单独人员、部门、分部、角色、岗位、所有人设置权限
- 可以设置能查看到数据的条件
- 可以存在多个规则
- 设置了权限后，拥有权限的人只能查看到满足条件的数据
- 系统管理员和创建人可以看到所有数据

4、列权限

- 可以对单独人员、部门、分部、角色、岗位、所有人设置权限
- 选择条件展示所有字段，可以任意选择想要设置的字段
- 设置了权限后，拥有权限的人只能查看到选中的列
- 系统管理员和创建人可以看到所有列

5、
**设置继承权限当用户在通过**ETL对EB表单数据进行加工的过程中，如果也需要继承某个EB表单的权限，那么可通过选择继承权限的方式进行配置

![](https://dl.eteams.cn/site/7ee5fca6-0de1-4c6e-9227-bb1e3b3b13c3?imageType=jpg)

![](https://dl.eteams.cn/site/6c272454-0b3d-4d94-a176-19194ea2a3ad?imageType=jpg)

+ [使用/维护权限](https://eteams.cn/community/help/1974669270042995986#使用维护权限)
+ 操作日志

  点击操作日志可以查看对etl的所有操作日志，包括：查看、新增、编辑、停用数据集以及对应的操作用户与时间

  ![](https://dl.eteams.cn/site/b9730d97-d14f-40eb-8afd-94aa0d297eb9?imageType=jpg)
+ **运行日志每次运行后都会自动生成一条运行日志**，展示调度人、调度方式、运行状态、开始结束时间、输出类型、**详情调度方式**：

前台手动运行：在etl**卡片直接点击运行按钮运行定时调度**：定时调度调用etl**运行调度中心**：调度中心调度etl**运行运行状态**：运行中、运行失败、运行中断、**运行成功详情**：展示运行失败的具体错误信息

![](https://dl.eteams.cn/site/936803ac-06b0-4a79-a00c-584fbedace5f?imageType=jpg)

+ 运行、停用、编辑

  会先根据权限判断这些功能是否允许使用(参考
  [使用/维护权限](https://eteams.cn/community/help/1974669270042995986#使用维护权限)
  )

未运行时，**停用按钮置灰展示点击运行按钮**，运行etl，运行按钮变为运行中，置灰不可点击，停用按钮高亮展示，**编辑按钮置灰点击停用按钮**，停止运行etl

若etl搭建不存在运行条件，**运行会报错点击编辑按钮可以进入**etl编辑页面

![](https://dl.eteams.cn/site/823c4121-2494-47c5-81eb-da53d0f82f0d?imageType=jpg)

**六、
**更多场景示例****

**1.
定时调度：定时调度调用etl运行**

**![](https://dl.eteams.cn/site/b61c6b1d-c549-499d-a7a5-cd36204c9ee3?imageType=jpg)**

****2.
调度中心：调度中心调度etl运行****

****![](https://dl.eteams.cn/site/01144a43-fe3e-4e01-8fe8-f9165ee48581?imageType=jpg)****

******七、注意点******

字段命名规范：

使用小写字母、下划线、**数字的组合禁止数字开头**

禁止两个下划线中间只出现数字