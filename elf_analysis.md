# Linux 可执行文件 ELF 动态分析

1. 先确认样本是X86/X64的，然后在Linux运行起来，看看是否正常运行。

    有些32位的ELF不能在64位上的Linux运行，需要安装32位兼容包。
    ```
    sudo dpkg --add-architecture i386
    sudo apt install libc6:i386
    ```

2. 运行网络抓包
    ```
    tcpdump -C 100 -i 主机网卡名 -w 网络数据存放路径 -U
    ```

3. 运行样本
    ```
    strace -ttt -x -y -yy -s 64 -o 日志存放路径 -f 样本路径
    ```
4. 等待一段时间，比如5分钟，终止上述进程，取出网络数据和日志进行分析。

5. 网络数据的分析：与windows样本分析类似，只要是观察连接哪些IP，进行哪些DNS请求，发出了什么数据包，接收什么数据包。

6. 日志分析

 - 文件操作：
    - 创建（一个open，一个write）
    - 复制（两个open，一个read，一个write）
    - 修改权限 chmod
 - 网络：
    - 建立TCP连接 connect
    - 发送tcp数据 send
    - 接收tcp数据 recv
    - 发送udp数据 sendto
    - 接收udp数据 recvfrom
 - 进程：
    - 创建进程 clone
    - 进程结束 exit_group(0)

