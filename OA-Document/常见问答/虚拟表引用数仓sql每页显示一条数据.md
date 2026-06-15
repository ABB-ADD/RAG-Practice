# 虚拟表引用数仓sql每页显示一条数据

**问题描述：**

表单使用虚拟表引用数仓sql数据源，表单每页仅显示一条数据

![](https://www.e-cology.com.cn/api/file/preview?type=redirect&fileId=100500139030881682)
![](https://dl.eteams.cn/site/9ff2e795-74fa-413b-b526-695ba9f6f020?imageType=png)

![](https://dl.eteams.cn/site/9ad53ab9-dc66-4db6-b402-326052e069f9?imageType=png)

**解决方式：**

主要通过以下三种方式进行排查

1、自查下有没有id列 必须要有id列

2、id不能重复

3
、数据库列名不能用中文