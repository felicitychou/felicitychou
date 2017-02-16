# 在ubuntu 16.04下安装kvm

1. 安装必要软件包

     ```$ sudo apt-get install qemu-kvm libvirt-bin virtinst bridge-utils```
 - libvirt-bin 提供libvirtd来使用libvirt管理qemu和kvm实例
 - qemu-kvm (kvm in Karmic and earlier) is the backend
 - ubuntu-vm-builder 强大的创建虚拟机的命令行工具
 - bridge-utils 提供虚拟机桥接网络
 
2. 添加当前用户到组

    ```$ sudo adduser `id -un` libvirtd```
 - 重新登录机器，使修改生效。libvirtd组的用户可以运行虚拟机。

3. 验证安装

    ```$ virsh list --all```
 - 虚拟机列表表头显示Id Name与State，列表内容为空。

4. 可安装 virt-manager 带界面虚拟机管理工具

    ```$ sudo apt-get install virt-manager```
 - 安装后可在应用中找到Virtual Machine Manager 。

5. virt-manager通过ssh连接远程管理虚拟机需要安装ssh-askpass

    ```$ sudo apt-get install ssh-askpass```

Refer：

https://help.ubuntu.com/community/KVM/Installation

http://www.cyberciti.biz/faq/installing-kvm-on-ubuntu-16-04-lts-server/ 

```
#!/bin/sh
sudo apt-get install qemu-kvm libvirt-bin virtinst bridge-utils
sudo adduser `id -un` libvirtd
sudo apt-get install virt-manager
sudo apt-get install ssh-askpass
```
