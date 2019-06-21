===================================
5.文本处理
===================================

grep
=========================

- grep Aug /var/log/messages  在文件 '/var/log/messages'中查找关键词"Aug" 
- grep ^Aug /var/log/messages 在文件 '/var/log/messages'中查找以"Aug"开始的词汇 
- grep [0-9] /var/log/messages 选择 '/var/log/messages' 文件中所有包含数字的行 
- grep Aug -R /var/log/* 在目录‘/var/log’及随后的目录中搜索字符串Aug

sed 's/stringa1/stringa2/g' example.txt 将example.txt文件中的 "string1" 替换成 "string2" 
sed '/^$/d' example.txt 从example.txt文件中删除所有空白行

paste
=========================

paste file1 file2 合并两个文件或两栏的内容 
paste -d '+' file1 file2 合并两个文件或两栏的内容，中间用"+"区分

sort
==========================

sort file1 file2 排序两个文件的内容 
sort file1 file2 | uniq 取出两个文件的并集(重复的行只保留一份) 
sort file1 file2 | uniq -u 删除交集，留下其他的行 
sort file1 file2 | uniq -d 取出两个文件的交集(只留下同时存在于两个文件中的文件)

comm
==========================

comm -1 file1 file2 比较两个文件的内容只删除 'file1' 所包含的内容 
comm -2 file1 file2 比较两个文件的内容只删除 'file2' 所包含的内容 
comm -3 file1 file2 比较两个文件的内容只删除两个文件共有的部分