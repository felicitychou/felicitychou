# python 计算crc32 值


### python 2.x 计算crc32 

有符号整数：范围 [-2^31, 2^31-1] 

与C计算的结果作对比，需要转换为无符号整数，才能与C语言计算出来的值一样。

```
>>> binascii.crc32('test')
-662733300
>>> binascii.crc32('test') & 0xffffffff
3632233996L
>>>
>>> crc = binascii.crc32('te')
>>> binascii.crc32('st',crc) & 0xffffffff
3632233996L
```

### python 3.x 计算crc32 

无符号整数，范围 [0, 2^32-1]）

```
>>> binascii.crc32(b'test')
3632233996
```

### 分段计算crc32
```
crc = binascii.crc32(str,crc) & 0xffffffff  
```