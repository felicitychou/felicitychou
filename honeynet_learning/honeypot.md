
Refer：
VIRTUAL HONEYPOTS From Botnet Tracking to Intrusion Detection 
虚拟蜜罐 从僵尸网络追踪到入侵检测 
Niels Provos/Thorsten Holz 著 
中国水利水电出版社

蜜罐是一个信息系统资源，其价值在于未经授权或非法使用该资源。
检测为知的攻击
分析蜜罐收集的数据所产生的误报比入侵检测系统收集到的数据导致的误报少

高交互蜜罐 低交互蜜罐 物理蜜罐 虚拟蜜罐

高交互蜜罐 真实的服务、操作系统或应用程序 高风险 难以部署和维护 捕获大量的信息

低交互蜜罐 模拟的TCP/IP协议栈、漏洞等 低风险 容易部署和维护 捕获有关攻击的定量信息

虚拟蜜罐 可度量性 易维护性 容易部署 风险低

相关工具 tcpdump wireshark nmap vmware 

高交互虚拟蜜罐 网络数据 阻止出站流量 入侵检测系统 IDS

Sebek 

用户模式Linux UML tty设备
tty_log.pl playlog.pl


Argos
动态污点分析
第一步 标记所有通过网络接收到的数据 通过内存追踪这些标记数据
一旦 这种标记数据被使用 影响执行流程，Argos检测到这些并产生一个攻击的内存痕迹
检测到一个缓冲区溢出或者另一类攻击，它将生成一个内存转存

Argos TCP 1347端口

连接上之后 Argos 将发送一个当前Argos进程工作目录的列表，编码为字符串以换行符终止，还收到Argos生成的所有报警

报警有两种不同类型

（1）[ARGOS]Attack detected,code <3_letter_alert_description>，通知你Argos已经检测到一个成功的入侵，例如，code JMP
（2）[ARGOS]Log generated <argos.csi.random_id>，通知你Argos已经产生一个用于以后分析的、带有随机ID的内存转储

发出命令 命令包含一个字符串，以换行符结束。Argos支持以下命令
RESET 重置虚拟机
SHUTDOWN 关闭虚拟机
PAUSE 暂停虚拟机
RESUME 从之前的展厅状态恢复虚拟机运行

保护你的蜜罐 蜜墙

蜜墙是第三代蜜网的核心 完成以下蜜网的所有主要任务
数据捕捉 数据控制 数据分析
蜜墙 透明网桥
iptables snort_inline IPS

Argus IP网络流量审计工具 p0f 远程操作系统被动指纹识别工具

Sebek 跟踪一下系统调用
read/readv/pread
open
socketcall
fork/vfork
clone






