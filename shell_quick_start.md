

Refer: 《Shell 脚本学习指南》

脚本第一行
```
#! /bin/sh - 
```

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
|dd|拷贝数据|
|file|识别文件类型|
|od|八进制码转存|
|strings|查找文件中的可打印字符|
|df|磁盘可用空间|
|du|占用空间|
|cmp|比较文件|
|diff|比较文件有什么不同|
|md5sum|计算md5值|
|gpg|加密或数字签名|
|uptime|显示开机指引的时间用户数及平均负载|
|ps|进程情况|
|top|实时进程情况及资源使用情况|
|kill|结束进程|
|strace|跟踪进程的系统调用| 
|sleep|延迟|
|at|延迟至特定时间|
|batch|为资源控制而延迟|
|crontab|计划任务|
|chmod|修改文件权限|

test 参数表
```
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
```


安全性shell脚本提示
```
勿将当前目录置于PATH下
为bin目录设置保护（$PATH 下每一个目录都只有它的拥有者可以写入）
写程序前，先想清楚要做什么如何实施，开始运作前，不断测试，错误与失败的处理也应该设计在程序里。
应对所有输入参数检查其有效性
对所有可返回错误的命令，检查错误处理代码
不要信任传进来的环境变量
从已知的路径开始
命令上使用完整路径
使用syslog(8)保留审计跟踪
当使用该输入时，一定将用户输入引用起来
勿在用户输入上使用eval
引用通配字符展开的结果
检查用户输入是否有meta字符
尽可能使用setgid而不要用setuid
使用新用户而不是root
尽可能限制使用setuid的代码
```


重要的UNIX命令

Shell与内置命令
```
. 在当前Shell下，读取与执行指定文件
break 切断循环
cd 更改当前目录
command 直接执行正轨的内置命令
continue 开始下一个虫谷
eval 给定文本视为shell命令
exec 无参数改变shell打开的文件，带参数则以其他程序置换shell
exit 退出shell
export 将变量导出到接下来的程序环境中
false 逻辑假
getopts 处理命令行选项
read 读取
readonly 变量标记为制度
return 返回
ser 显示shell变量与变量值、设置shell选项、设置命令行参数
shift 一次移动一个或多个命令行参数
test 计算表达式
trap 管理操作系统信号
true 逻辑真
type 命令类型
typeset 生命变量与管理它们的类型与属性
ulimit 设置或显示系统对每个进程所加的限制
unset 删除shell变量与函数
basename 显示路径名称最后文件名
dirname 显示文件路径
env 处理命令的环境
id 显示用户与组ID及名称信息
date 显示现在的日期与时间
who 显示已登录的用户列表
stty 处理终端设备的状态
```

文本处理
```
awk
cat
cmp 文件比较
cut
dd
echo
egrep 扩展grep
expand 展开制表字符与空格字符
fgrep 快速grep
fmt 将文本格式化为段落
grep 
iconv 字符编码转换工具
join
less 交互式分页工具
more 原始的交互式分页程序
pr 文件合适化
printf echo的提高版
sed 刘编辑器
sort 排序文本文件
spell 拼字检查程序
tee 将标准输入拷贝到标准输入
tr 转换、删除或减少重复字符的执行
unexpand 将空格字符转换成适当数量的制表字符
uniq 删除或计算已排序输入中的重复航
wc 计算行、单词、字符或字节
```

文件处理
```
bzip2 bunzip2 及高品质的文件压缩与解压缩
chgrp 更改文件与目录的组
chmod 更改文件与目录的权限
chown 更改文件或目录的所有权
cksum 显示文件的校验和
comm 显示或省略两个排序后的文件之间具有唯一新或共有的行
cp 复制文件与目录
df 显示可用磁盘空间
diff 比较文件显示其差异
du 显示文件与目录所使用的磁盘快
file 判断文件的类型
find 查找文件
gzip gunzip 文件压缩与解压缩
head 显示文件前几行
locate 查找文件
ls 累出文件
md5sum 打印文件校验和 md5
mktemp 建立独一无二的临时文件
od 八进制输出
patch 通过读取diff的输出，跟新文件
pwd 显示当前的工作路径
rm 删除文件或目录
rmdir 删除空目录
strings 查找二进制文件中可打印的字符串
tail 显示文件末尾几行
tar 打包
touch 更新文件的秀修改或访问时间
umask 设置默认文件建立权限掩码
zip unzip 打包与压缩解压缩程序
```

进程
```
at 指定时间执行工作
batch 等待资源执行工作
cron 在指定时间执行工作，周期性
crontab 修改cron文件，指定执行命令与命令执行时间
fuser 寻找使用特定文件或socket的进程
kill 传送信号到疑惑多个进程
nice 在进程执行前 更改其优先级
ps 显示进程有关的信息
renice 进程启动后，更改其优先级
sleep 停止一定描述
top 交互式显示系统的进程，及资源占用情况
wait 等待一个或多个进程完成
xargs 读取 标准输入上的字符串
```

其他
```
cvs 源代码管理
info 在线文件浏览
locale 显示可用的locale相关信息
logger 通过syslog(3)
lp lpr 将嘎因缓冲区文件传送给打印机
lpq 显示正在处理中在队列等待中的打印工作列表
mail 传送电子邮件
make 编译与重新编译
man 显示在线手册页
scp 安全进行文件的复制
ssh 远程shell
uptime 显示系统一开机多久及其负载信息
```
