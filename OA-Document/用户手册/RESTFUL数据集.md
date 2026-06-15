# RESTFUL数据集

**一、功能背景**

客户在使用泛微数据加工的过程中，可以通过数据库连接将其它业务系统的数据集接入到数据仓库。但是有些业务客户并不能暴露数据库信息到泛微数据加工或者原本就是提供的接口的形式。这样就无法接入到泛微的系统，让客户使用数据加工的局限性比较大。

**二、功能价值**
  
在实现restful数据链接对接esb连接器和restful数据集接入到泛微数据加工后，可以让客户的业务可以和数仓的业务有更多的联动。例如可以实现在加入restful数据链接和创建restful数据集，在创建后可以直接在数据源提供给各个业务模块使用。

**三、功能概述**

1.restful数据连接

+ 支持使用ESB中的连接器作为连接使用

2.restful参数配置

+ restful数据集支持一键获取连接器参数，配置参数值，支持使用数据加工参数中心参数

**3.restful结果集JSON过滤**

+ restful获取数据集的结果集支持使用json解析和过滤

****4.restful结果集循环配置****

+ restful数据集可以设置循环参数，进行循环获取restful接口值

**四、业务流程图**

**五、功能详细说明**

**1.restful数据集连接管理**

+ restful数据集连接器管理参考
  [esb连接器](https://eteams.cn/community/help/1971160554476822443)

**2.restful数据集新增**

**![](https://dl.eteams.cn/site/add0379c-cc27-47f2-a00d-ff92e7b0cb1b?imageType=png)**

**3.restful数据集配置**

+ 配置得连接器都来自ESB连接器，可以参考ESB连接器。

  ![](https://dl.eteams.cn/site/75384898-dcd0-4590-9e0d-dd78a5e106d7?imageType=png)

+ 选定连接器配置可以进行restful参数配置，包括对连接器参数的配置、JSON查询语句配置、输出字段配置。

  ![](https://dl.eteams.cn/site/9c7a13a6-bfd4-4137-ab5f-36395521feb0?imageType=png)

+ 配值restful数据集请求参数为从连接器初始化的参数，包括Params、Header、Body、Url、Cookie五个部分

  ![](https://dl.eteams.cn/site/9f165859-3cef-458b-a7a8-4e6fc9b928fd?imageType=png)

+ 配值JSON查询语句为对连接器返回结果进行过滤，可以使用JSON查询语法过滤

  ![](https://dl.eteams.cn/site/73aa0122-bf9c-431f-b036-7751c06d611d?imageType=png)

  ![](https://dl.eteams.cn/site/5972b57e-b302-48f8-be8b-b671d278fc49?imageType=png)

**4.restful数据集循环配置**

+ 点击设置循环参数可以对restful数据集参数进行配置

  ![](https://dl.eteams.cn/site/de048c83-2c7a-4992-b356-d62129e22a34?imageType=png)

**5.restful数据集数据刷新**

+ 点击刷新数据可以将restful接口的数据按照循环配置存到数据加工数据集里面。

  ![](https://dl.eteams.cn/site/dec7950b-5252-4f46-9293-10275b69d410?imageType=png)