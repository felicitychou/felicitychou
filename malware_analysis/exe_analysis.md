
# Windows 可执行程序 动态分析



## 注册表操作相关API

RegCreateKey 创建或打开注册表项。默认为创建，当注册表中有此项时。为打开。

RegOpenKey 打开一个指定的注册表键

RegCloseKey 释放指定注册键的句柄

RegDeleteKey 用来删除一个注册表键值。

RegEnumKey 枚举键

RegDeleteVale   删除值

RegQueryValue 取得指定项或子项的默认（未命名）值

RegSetValue 设置指定项或子项的默认值

RegEnumValue 枚举值