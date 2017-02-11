

脚本第一行通常为```#! /bin/sh -```



变量 开头是字母或下划线 后接任意长度字母数字或下划线

```sh
first=issac middle=bashevis last=singer
fullname="issac bashevis singer"
fullname2="$first $middle $last"
oldname=$fullname
```



重定向与管道

```sh
# < 改变标准输入
cat < hello.txt
# > 改变标准输出
echo hello > hello.txt
# >> 附加到文件 将输出附加到文件结尾
# | 建立管道
# 程序1 | 程序2 将程序1的标准输出作为程序2的标准输入
```



/dev/null 输出到该文件的数据会被系统丢弃



命令追踪

```sh
# 终端中打开执行命令跟踪
$ sh -x 
# 脚本中打开执行命令追踪
set -x
```



shell  命令

| 命令     | 作用   | 语法                               | 参数                                    | 例子                                  |
| ------ | ---- | -------------------------------- | ------------------------------------- | ----------------------------------- |
| echo   | 显示   | echo [string...]                 |                                       |                                     |
| printf | 显示   | printf format-string [arguments] |                                       | printf "Test '%s,%s'\n" Hello world |
| wc     | 字数统计 | wc [OPTION]... [FILE]...         | -l 计算行数 -w 计算字数 -m 计算字符数 -b 计算字节数     |                                     |
| tr     | 转换字符 | tr [OPTION]... SET1 [SET2]       | -d 删除SET1里的字符 -s 将SET1里连续重复出现的字符压缩为1个 |                                     |



查找文本
grep string
-i 忽略大小写
