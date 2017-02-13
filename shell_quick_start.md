

脚本第一行
#! /bin/sh - 

变量 开头是字母或下划线 后接任意长度字母数字或下划线
```
first=issac middle=bashevis last=singer
fullname="issac bashevis singer"
fullname2="$first $middle $last"
oldname=$fullname
```

重定向与管道
```
< 改变标准输入
cat < hello.txt
> 改变标准输出
echo hello > hello.txt
>> 附加到文件
将输出附加到文件结尾
| 建立管道
程序1 | 程序2 将程序1的标准输出作为程序2的标准输入

```

/dev/null 输出到该文件的数据会被系统丢弃


sh -x 打开执行命令跟踪
set -x 打开执行命令跟踪（脚本中）

|命令|作用|语法|参数|例子|
|-----|----|---|----|----|
|echo|显示|echo [string...]|||
|printf|显示|printf format-string [arguments]||printf "Test '%s,%s'\n" Hello world|
|wc|字数统计|wc [OPTION]... [FILE]...|-l 计算行数 -w 计算字数 -m 计算字符数 -b 计算字节数|||
|tr|转换字符|tr [OPTION]... SET1 [SET2]|-d 删除SET1里的字符 -s 将SET1里连续重复出现的字符压缩为1个||
|grep|查找文本|grep [OPTION]... PATTERN [FILE]...|-i 忽略大小写 -G 基本正则 -E 扩展正则||
|sed|文本替换|sed [OPTION]... {script-only-if-no-other-script} [input-file]...||
|head|显示文件前几行|head [OPTION]... [FILE]...|-n 指定行数||
|tail|显示文件后几行|tail [OPTION]... [FILE]...|-n 指定行数||



dd 拷贝数据
file识别文件类型
od八进展码转存
strings查找文件中的可打印字符

test 
-d file 目录
-e file 存在
-f file 一般文件
-w file 可写入
-r file 可读取
-x file 可执行
-z string string为null
s1 = s2 字符串s1等于s2
s1 != s2 字符串s1不等于s2
n1 -eq n2 整数n1等于n2
n1 -ne n2 整数n1不等于n2
n1 -lt n2 整数n1小于n2
n1 -gt n2 整数n1大于n2
n1 -le n2 整数n1小于等于n2
n1 -ge n2 整数n1大于等于n2

df 磁盘可用空间
du 占用空间
cmp 比较文件
diff 比较文件有什么不同

md5sum 
gpg
gpg 导入公钥
验证签名

uptime 显示开机指引的时间用户数 及平均负载
ps
