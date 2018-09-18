## auto report module（arm）使用手册

[TOC]

---

### 声明

**arm** 是用来生成HTML结题报告的一个模块，模块重新设计模板，自定义了一些模块化的函数，方便快速的生成结题报告。

反馈邮箱：<sunyong@microanaly.com>
后期维护人：<zhengpan@microanaly.com>

---

### 版本
目前版本为 `arm V1.2`，所在路径：`/home/suny/test/learnpy/autoreportmodule/`。

#### V1.2
2018.09.05 新增double_image方法，按列表同时显示两个图片
2018.09.04 修复部分表格标题显示缺失问题，新增table方法sortable参数，默认为True（排序），False为不排序
2018.09.03 添加单组图片展示方法bimage ；调整table方法，可展示表格标题 

2018.08.14 撰写V1版本

---

### 使用说明

1. 安装python3.6以上版本，并安装pandas模块（运行报错，请注意可能含有未安装的模块）
2. 将模块目录放在一个固定且安全的目录下
3. 写结题报告的程序引入模块时添加模块目录，详见使用示例

#### 使用示例

```python
# 导入模块及环境
import sys
# linux
sys.path.apppend('/home/suny/test/learnpy/autoreportmodule/')
# windows
# sys.path.append(r'C:\myprogram\learnpy\autoreportmodule')
from arm import arm

workdir = sys.argv[1]

# 初始化模块
report = arm('文库质检报告', workdir)

report.starthtml()

# 一级目录
report.menu('项目概述')
# 二级目录（可不设置）
report.submenu('test')
report.text('微生物多样性分析基于第二代高通量测序技术对16S rRNA/18S rRNA/ITS等基因序列进行测序.')
report.table('qcstat/20180801.xlsx', ttype='excel', head=0,sortable=False)
report.image('qcstat', special='ladder')

...

report.menu('分析概述')
report.image('sv', key="cytoscape",title='图片标题')
report.text('1. micro', '2. RNA')
report.table('sv/sv.txt')
report.text('De novo测序也叫基因组从头测序，在不依赖参考基因组的情况下，对某个物种的全基因组序列进行测序.')
report.bimage('sv/sv.png', tilte='sv')
report.bimage(src='fastq/r1.png', src2='fastq/r2.png', title='r1', tilte2='r2')
report.double_image(src='fastq', key1='clean_R', key2='raw_R')
report.single_image(src='fastq', key='clean_R', title='')
...

report.endhtml()

```

#### 示例程序

简单示例程序路径：`/home/suny/test/html.css.js/htmlv2/tests.py`
复杂示例程序路径：`/home/suny/test/html.css.js/htmlv2/test.py`

#### 示例结果
简单示例结果路径：`/home/suny/test/html.css.js/htmlv2/v2.rar`

---

### arm()

#### starthtml()
> **使用方法**
> `report.starthtml()`
> 
> **功能**
> 复制文件及创建主体内容
> 
> **返回值**
#### endhtml()
> **使用方法**
> `report.endhtml()`
> 
> **功能**
> 结束主体内容及写入文件
> 
> **返回值**
> 无
> 
> **参数**
> 无

#### menu()
> **使用方法**
> `report.menu('text')`
> 
> **功能**
> 在结题报告中创建侧边栏一级主题及主体一级主题
> 
> **返回值**
> 无
> 
> **参数**
> 无

#### submenu()
> **使用方法**
> `report.submenu('text')`
> 
> **功能**
> 在结题报告中创建侧边栏二级主题及主体二级主题
> 
> **返回值**
> 无
> 
> **参数**
> 无

#### text()
> **使用方法**
> `report.text('text', ['text'...])`
> 
> **功能**
> 在结题报告中插入一段或几段文字描述。
> 
> **返回值**
> 无
> 
> **参数**
> 无

#### table()
> **使用方法**
> `report.table(src, ttype='txt', head=1, tsep='\t', top=100, sheet=1,title='',sortable=True)`
>  
> **功能**
> 将excel或文本文件转成结题报告中的表格
> 
> **返回值**
> 无
> 
> **参数**
> + **src：** 输入文件路径，**不可缺省**。
> + **ttype：** 表格类型，支持excel文件和文本文件，参数为 **txt（默认参数）** 和 **excel**。
> + **head：** 有无行头，参数为 **1（默认参数）** 和 **0**。
> + **tsep：** 文本文件分隔符，默认为 *\t*。
> + **top：** 在html中只显示文件的前 ***top*** 行，默认为 **100**。
> + **sheet：** 处理excel文件第几张表，默认为第 **1** 张表。
> + **title：** 显示表格标题，默认为空值。
> + **sortable：** 设置表格是否排序，默认为排序，参数为 **True（默认参数）** 和 **Flase**。

#### image()
> **使用方法**
> `report.image(src, special=None, key=".",title='',bi=False)`
>  
> **功能**
> 将目录中的图像转成结题报告中的图像列表
> 
> **返回值**
> 无
> 
> **参数**
> + **src：** 输入目录路径，**不可缺省**。
> + **special：** 将包含特殊字符串的图像放到图像列表内第一个展示，默认为 **None（没有特殊图片）**。
> + **key：** 将目录下包含某种字符串的图像放到图像列表内展示，默认为 **.（全部）**。
> + **title：** 对image设置一个统一的标题，默认为 **空**，。
> + **bi：** 针对生物信息样本名称处理（命名规则：name.xxoo.png），默认为 **False**，。

#### bimage()
> **使用方法**
> `report.bimage(src, src2=None, title='', title2=None)`
>  
> **功能**
> 将目录中的图像转成结题报告中的一组图像
> 
> **返回值**
> 无
> 
> **参数**
> + **src：** 输入路径下的第一个图片路径，**不可缺省**，当为单张图片时居中显示。
> + **src2：** 输入路径下的第二个图片路径，默认为空，当不为空时两图片并排居中显示。
> + **title：** 显示图片1标题，默认为空值。
> + **title2：** 显示图片2标题，默认为空值。

#### double_image()
> **使用方法**
> `report.double_image(src, key1, key2)`
>  
> **功能**
> 将目录中的图像按**两个图像为一组**，转成结题报告中的图像列表
> 
> **返回值**
> 无
> 
> **参数**
> + **src：** 输入图片所在的文件夹，**不可缺省**。
> + **key1：** 输入路径下的第一个图片名具有的共有的关键字，**不可缺省**。
> + **key2：** 输入路径下的第二个图片名具有的共有的关键字，**不可缺省**。

#### single_image()
> **使用方法**
> `report.single_image(src, key, title)`
>
> **功能**
> 将目录中的图像按**具有共同的关键字为一组**，转成结题报告中的图像列表
>
> **返回值**
> 无
>
> **参数**
> + **src：** 输入图片所在的文件夹，**不可缺省**。
> + **key：** 输入路径下的所有图片名具有的共有的关键字，**不可缺省**。
> + **title：** 图片的标题。
