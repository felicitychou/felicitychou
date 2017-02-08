# 在ubuntu16.04下安装wine

1. 64位系统添加支持32位架构。
`sudo dpkg --add-architecture i386`

2. 添加库
`sudo add-apt-repository ppa:wine/wine-builds`

3. 更新包
`sudo apt-get update`

4. 选择需要的代码分支安装

    开发分支（较稳定） `sudo apt-get install --install-recommends winehq-devel`

    Staging 分支 `sudo apt-get install --install-recommends winehq-staging`

refer:https://wiki.winehq.org/Ubuntu

```
#!/bin/sh
sudo dpkg --add-architecture i386
sudo add-apt-repository ppa:wine/wine-builds
sudo apt-get update
sudo apt-get install --install-recommends winehq-devel
```

