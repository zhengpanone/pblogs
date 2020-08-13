===================================
5.文本处理
===================================

grep
=========================

参数

.. note::

    * -d #取反
    * -v #显示不包含匹配关键字的所有行。
    * -l #显示包含匹配关键字的文件
    * -L #显示不包含匹配关键字的文件
    * -r #递归搜索
    * -i #忽略大小写
    * -n #显示关键字所在行号
    * -A n #显示关键字后n行
    * -B n #显示关键字前n行
    * --exclude #搜索时排除某些文件
    * --exclude-dir #搜索时排除某些目录
    * -f #指定规则文件进行搜索


- grep Aug /var/log/messages  在文件 '/var/log/messages'中查找关键词"Aug" 

- grep ^Aug /var/log/messages 在文件 '/var/log/messages'中查找以"Aug"开始的词汇 

- grep [0-9] /var/log/messages 选择 '/var/log/messages' 文件中所有包含数字的行 

- grep Aug -R /var/log/* 在目录‘/var/log’及随后的目录中搜索字符串Aug

- grep -v auto 排除不相关信息使用参数-v 

- ps -ef | grep readis -c  只想统计结果数量使用 **-c**

- grep -n "test" /opt/work/linux_command_debug.md 显示关键字的行号使用参数 **-n**

- grep -rn "test" --exclude=*.txt  使用--exclude参数来排除某些文件，例如，查找包含test，但是排除txt文件

- grep -rn "test" --exclude-from=skip.txt 要排除的条件比较多，可以将要排除的条件存储在另外一个文件里

- grep -rn "test" --exclude-dir=aaa  排除指定目录，它需要用到--exclude-dir参数：

- grep -rn "int main(void)"  在当前目录下所有文件查找包含“int main(void)”字符串的文件 -r参数表示递归查找当前目录的文件，-n会显示查找位置的行号，如果只想显示包含该指定关键字的文件名，可使用-l（--file-with-matches）参数

- grep -rLn "int main(void)"  查找不包含指定关键字的文件  使用-L参数,要找的是不包含该关键字的文件

- grep -rni "int MAIN(void)"  搜索时忽略大小写 ,使用-i（--ignore-case）参数

- grep -rnv "int main(void)"  搜索显示不包含指定关键字的行

- grep -rn "int main(void)" -A 1 -B 1  显示指定关键字前后内容  查看包含指定关键字行附近的行，前面的方式是没有办法看到的，不过我们可以用-A(--after-context=)和-B(--before-context=)参数来显示前后的行

- cat filename | grep -f key.txt  把关键字写在一个文件，搜索时指定文件即可，例如规则文件为key.txt
 

sed 
==============================

- sed 's/stringa1/stringa2/g' example.txt 将example.txt文件中的 "string1" 替换成 "string2" 

- sed '/^$/d' example.txt 从example.txt文件中删除所有空白行

paste
=========================

- paste file1 file2 合并两个文件或两栏的内容 

- paste -d '+' file1 file2 合并两个文件或两栏的内容，中间用"+"区分

sort
==========================

- sort file1 file2 排序两个文件的内容 
- sort file1 file2 | uniq 取出两个文件的并集(重复的行只保留一份) 
- sort file1 file2 | uniq -u 删除交集，留下其他的行 
- sort file1 file2 | uniq -d 取出两个文件的交集(只留下同时存在于两个文件中的文件)

comm
==========================

- comm -1 file1 file2 比较两个文件的内容只删除 'file1' 所包含的内容 
- comm -2 file1 file2 比较两个文件的内容只删除 'file2' 所包含的内容 
- comm -3 file1 file2 比较两个文件的内容只删除两个文件共有的部分