
导入模块

```
from scapy.all import *
```

监听或处理数据包

```
sniff(iface='eth0',prn=handler)
sniff(offline="xxx.pcap",prn=handler)
```

定义处理函数

```
def handler(pkt):
    pass
```

定义数据包数组

```
pkts = PacketList()
```

添加包
```
pkts.append(pkt)

```

判断包是不是UDP
```
pkt.haslayer(UDP)
```

写pcap
```
wrpcap("xxx.pcap", pkts)
```
