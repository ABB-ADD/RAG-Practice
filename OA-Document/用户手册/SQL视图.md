# SQL视图

**一、功能背景**

客户想要将多张表的数据整合在一起，形成统一视图供分析使用，这样方便使用在各种查询场景中（页面、报表），SQL视图功能可以将多表关联、子查询、聚合计算等复杂SQL逻辑封装成视图，用户只需调用视图即可获取数据

**二、功能价值**

SQL视图的核心价值在于简化数据操作、提升效率、增强安全性和统一数据管理

**三、功能概述**

SQL视图是一个基于SQL查询结果的虚拟表。它不存储实际数据，而是存储查询定义

**四、功能详细说明**

**1、SQL视图新建入口**

* 进入数据加工模块，选中数据准备tab，点击任意分组，右侧顶部出现新建按钮，默认为自助视图，点击箭头展示各功能新建入口，选择新建SQL视图按钮，点击可以进入SQL视图新建页面

  ![](https://dl.eteams.cn/site/265ed513-950f-4cc0-a13a-11464f5788a7?imageType=jpg)

**2、SQL视图总览**

* 1是SQL视图名称、2是数据连接、3是数据连接选中库下的表、4是SQL语句填写处、5可配置输出字段、参数等信息、6为数据结果展示、7是美化SQL和中断SQL运行、8为保存运行按钮
* ![](https://dl.eteams.cn/site/efd00b82-c670-4307-bd05-bc1ac0817c12?imageType=png)

**3、SQL视图新建保存**

* 新建SQL视图必须要填写的点：

+ 数据连接
+ SQL语句
+ SQL视图名称

* 注意：

+ SQL视图名称，在同一个分组下，数据集的名称不能相同，若填写了相同的名称后保存，toast提示名称不能相同

  ![](https://dl.eteams.cn/site/fed209ff-cfb0-45ab-a215-aa38a7cdf3f3?imageType=png)
+ SQL语句需要是能正常执行成功的SQL才可以保存，若SQL有误，保存时会toast提示错误信息，可根据错误信息排查SQL，举例：当SQL使用的表不存在，报错如图

  ![](https://dl.eteams.cn/site/c555898e-0137-454b-acdc-81b2b0f89ff4?imageType=png)
+ SQL语句不能以分号结尾，结尾不用写分号

  ![](https://dl.eteams.cn/site/948faa8f-2a90-49cf-9c5f-5429403d4fd0?imageType=png)

**4、SQL视图数据集**

* 展示：数据集类型（SQL视图）、数据集名称、创建人、创建时间、操作

  ![](https://dl.eteams.cn/site/0ff9d061-13cf-4716-a336-39481cb95002?imageType=png)
* 操作按钮

+ 箭头符号，鼠标放在箭头符号上展示可进行的操作：移动分组、重命名、复制ID、删除

  ![](https://dl.eteams.cn/site/2506cf69-f11d-4829-9227-578e3393a010?imageType=png)
+ 当对SQL视图数据集只有使用权限时，操作按钮隐藏

  ![](https://dl.eteams.cn/site/8c53d819-e872-4ae0-9c76-88fc512b134c?imageType=png)
+ 移动分组：可以将数据集移动到任意分组

  ![](https://dl.eteams.cn/site/0f5a3ed7-3442-4250-8754-32a118539f3f?imageType=png)
+ 重命名：可以修改数据集的名称，不能与同一分组的其他数据集名称相同

  ![](https://dl.eteams.cn/site/c2edbb40-effc-4554-90ba-f571be11dd34?imageType=png)
+ 复制ID：点击后复制的是该数据集的datasetid

  ![](https://dl.eteams.cn/site/112628ab-2a4b-44ef-a828-aca2926e627b?imageType=png)
+ 删除：点击删除可以删除SQL视图，视图存放在回收站中

  ![](https://dl.eteams.cn/site/422f78bb-5ead-437b-85c2-cb59f8f63841?imageType=png)

**5、SQL视图卡片**

* 点击SQL视图数据集，会进入SQL视图卡片页

  ![](https://dl.eteams.cn/site/4da97422-f47e-4c34-be8d-eb2d7ec0f9d6?imageType=png)
* 模型视图：展示SQL语句、字段设置信息、输出字段信息、可预览SQL执行结果

  字段设置、输出字段信息只能查看，若需要修改需要点击编辑按钮进入编辑页

  ![](https://dl.eteams.cn/site/65b5c4fc-6453-4ce3-b518-979b98d119fc?imageType=png)
  ![](https://dl.eteams.cn/site/fd64eea3-36f0-4fa7-aaef-bde7d67fd4d7?imageType=png)
* 基础信息：可填写数据集的基础信息，用于AI提问使用数据集；填写了描述信息后需要点击保存才能保存填写的数据

  ![](https://dl.eteams.cn/site/505574ae-896c-4507-a33f-a14625b16c0f?imageType=png)
* 血缘关系

+ 若该数据集未被任何eb页面、报表使用，则空态展示：
  ![](https://dl.eteams.cn/site/d72cc0a2-9963-45e6-8cca-21f81fa3ed27?imageType=png)
+ 若在其他地方被引用，则展示具体引用信息，举例：报表、页面

  ![](https://dl.eteams.cn/site/d922580b-0a7e-4393-83e5-9c16a4bb0df9?imageType=png)

* 使用/维护权限：用于设置数据集的使用、编辑权限

+ 默认：系统管理员默认拥有该租户下的所有数据集的维护权限；数据集创建人默认拥有自己创建的数据集的维护权限
+ 维护权限：可以对数据集的操作：查看、编辑、删除、移动分组、重命名、开启关闭缓存、给他人分配权限
+ 使用权限：拥有使用权限只可以查看此数据集，不可编辑数据集，
  [操作按钮](https://eteams.cn/community/help/1974669270042995986#操作按钮)
  隐藏，可以在数据源中被选中使用
+ 具体配置：使用、维护权限配置方式都是一样的

  鼠标放在选择人员处，可以选择分配权限的对象，可以对人员、部门、分部、角色、岗位、所有人设置权限，选择好对象后会自动保存，直接生效

  ![](https://dl.eteams.cn/site/a3e825ff-e846-4eac-a9b7-3f15347a3c8d?imageType=png)

  若想要删除权限，直接点击x即可，会自动保存

  ![](https://dl.eteams.cn/site/30e05215-ecc7-42ca-922e-52594dc1172c?imageType=png)

* 操作日志

+ 总览：操作日志展示对数据集进行的各种操作信息

  ![](https://dl.eteams.cn/site/fb9850b7-d04b-48c6-98f9-dc3092e3502d?imageType=png)
+ 可以通过操作时间、对象、操作类型对操作日志进行过滤

  ![](https://dl.eteams.cn/site/6edec5ae-1186-4e7d-bbd9-6f1f072bacd7?imageType=png)
+ 操作类型：新增、编辑、查看、删除、恢复、移动
  ![](https://dl.eteams.cn/site/d68db058-203a-4098-94b4-f034d18ccecd?imageType=png)
+ 修改详情，点击明细可以查看到该操作具体修改的详情

  ![](https://dl.eteams.cn/site/d3bd42eb-fd52-40bc-9cee-dbe339fb8706?imageType=png)

* 缓存设置

+ 缓存按钮开启是高亮

  ![](https://dl.eteams.cn/site/af89d586-6e74-42de-b3c8-49420f6dd506?imageType=png)
  ![](https://dl.eteams.cn/site/f8e54ab7-bf86-48a8-90d8-4df7a11abb5a?imageType=png)
+ 开启了缓存，数据源查询该SQL视图数据会有缓存，缓存时间为设置页系统设置中缓存设置配置的缓存时间

  ![](https://dl.eteams.cn/site/d82d5736-eebb-4780-8e36-86f00c66983c?imageType=png)
+ 缓存是否开启

  当设置-系统设置-缓存设置中开启（关闭）了缓存设置，新建一个SQL视图，缓存按钮会默认开启（关闭）

  在SQL视图卡片上手动点击按钮开启（关闭）了缓存，之后再去
  设置-

  系统设置-缓存设置中的关闭（开启）缓存，
  该SQL视图得缓存都保持开启（关闭）

* SQL审核

+ SQL审核具体如何配置可以查看设置页-
  [SQL审核帮助文档](https://eteams.cn/community/help/1974669197233895978#SQL审核)
+ 当设置页SQL审核配置为关闭，则SQL视图新建后直接能被数据源使用
+ 当设置页
  SQL审核配置为开启，则新建SQL视图、编辑SQL视图保存后需要审核通过了才能被数据源使用

  ![](https://dl.eteams.cn/site/9f7a1df0-e038-4ce8-9a8d-32331a5ac199?imageType=png)

**6、SQL视图编辑**

* [数据连接](https://eteams.cn/community/help/1974721109009796581)
* [SQL语句](https://eteams.cn/community/help/1974721514696296610)
* [SQL片段](https://eteams.cn/community/help/1974721624658396632)
* [字段设置](https://eteams.cn/community/help/1974727573748096666)
* [输出字段](https://eteams.cn/community/help/1974727877878596683)
* [多数据源配置](https://eteams.cn/community/help/1974728641623196747)

**五、应用场景示例**

**1、数据源使用**

* 可以选择数据源的功能，进入数据源选择页后点击数据加工-数据准备列表下可以选择有权限的SQL视图数据集

![](https://dl.eteams.cn/site/f9769e75-2fea-4dad-a352-1d6cc687f8ce?imageType=png)

* 举例

+ eb页面：可以使用SQL视图的结果搭建列表、柱状图、二维报表等组件

  ![](https://dl.eteams.cn/site/9e20dea5-f7f0-4d6d-8c18-d9ba7695d2c8?imageType=png)

  ![](https://dl.eteams.cn/site/3100986c-4522-47ab-a429-9c85b7e5e14e?imageType=png)
+ eb报表

  ![](https://dl.eteams.cn/site/436b6c3b-13ed-432d-99b5-ba89b6c5d8cf?imageType=png)
+ 虚拟表

  ![](https://dl.eteams.cn/site/f8a5789f-27b5-4a64-a25f-b65e68e1b75a?imageType=png)
  ![](https://dl.eteams.cn/site/fee45e21-7494-4d22-94df-812a1dd718e0?imageType=png)

**2、自助视图再建模**

* 自助视图可以选择已经创建好的SQL视图，自助视图使用的数据连接和SQL视图使用的数据连接需要是同一个数据连接才可以正常使用

  ![](https://dl.eteams.cn/site/52e6e5f4-8d7c-411a-b3b0-9677f05bc099?imageType=png)

**3、数据服务**

* 数据服务功能可以将SQL数据集的结果生成一个api接口，提供给其他功能使用，具体数据服务功能可查看
  [数据服务功能帮助文档](https://eteams.cn/community/help/1974669185764795977)

  ![](https://dl.eteams.cn/site/0b0f7744-33ba-4070-abdf-2d34b2b3a1a6?imageType=png)