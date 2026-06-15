# 批量导入数据时，关联eb字段显示存在重复数据

**问题描述：**

在用excel表格导入数据时，关联e-Builder类型的字段显示导入失败，生成的失败数据显示此项存在重复数据，表单中并未设置字段重复校验：

![](https://dl.eteams.cn/site/192e69bb-64cd-4c7c-ab61-51a76e9a452a?imageType=png)

**解决方式：**

这是由于关联e-Builder字段所关联的表单中，设置标题栏字段有重复的，例如在该场景中，关联e-Builder字段关联表单后设置标题栏为单行文本字段

![](https://dl.eteams.cn/site/d370f34d-0107-4d61-8cab-bad4218983a5?imageType=png)

但是被关联表单中单行文本字段有相同的数值“调试”，所以在导入数据时，无法判断这个关联e-Builder字段关联的是哪一条数据，就会出现这样的提示：

![](https://dl.eteams.cn/site/bf4bb73f-216a-49ad-bfbe-47a73bbee2f8?imageType=png)