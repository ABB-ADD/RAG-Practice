# ETL运行提示操作列名不能为空或无意义字段

**问题描述：**

ETL节点运行时提示操作列名不能为空或无意义字段，是什么原因导致的，该如何排查

![](https://dl.eteams.cn/site/66aacf00-dc8e-458f-9d79-adea3e665260?imageType=png)

**解决方式：**

检查已配置输出字段列，是否为中文、或是否包含了数字。中文和数字不符合字段规范，不可使用

![](https://dl.eteams.cn/site/d4e8d86b-5b7d-4a3b-b56a-8f6b4158219a?imageType=png)