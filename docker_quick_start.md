# 在ubuntu 16.04下安装docker

## Step 1:设置docker安装包来源库

1. 安装需要的软件包

   ``````sh
   $ sudo apt-get -y --no-install-recommends install \ curl \ apt-transport-https \ ca-certificates \ software-properties-common
   ``````

2. 添加Docker 官方 GPG key

   ``````sh
   $ curl -fsSL https://apt.dockerproject.org/gpg | sudo apt-key add -
   ``````

   验证key ID为 58118E89F3A912897C070ADBF76221572C52609D

   ``````sh
   $ apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D
   ``````

3. 添加docker稳定版安装包来源库

   ``````sh
   $ sudo add-apt-repository \
          "deb https://apt.dockerproject.org/repo/ \
          ubuntu-$(lsb_release -cs) \
          main"
   ``````

## Step 2:安装Docker

1. 更新apt包索引

   ``````sh
   $ sudo apt-get update
   ``````

2. 安装最新版本的docker

   ``````sh
   $ sudo apt-get -y install docker-engine
   ``````

3. 添加当前用户到docker
   ```sh
   $ sudo usermod -aG docker $USER
   ```
---

# docker 常用命令

| 操作                    | 命令                                       |
| --------------------- | ---------------------------------------- |
| 查看docker的所有命令解释       | docker --help                            |
| 查看docker命令具体用法        | docker COMMAND --help                    |
| 查看docker版本信息          | docker -v                                |
| 拉取镜像(没有TAG时，默认latest) | docker pull REPOSITORY[:TAG]             |
| 查看镜像                  | docker images                            |
| 删除镜像                  | docker rmi REPOSITORY[:TAG]/IMAGE_ID     |
| 删除所有镜像                | docker rmi \`docker images -a -q\`       |
| 运行容器                  | docker run -it REPOSITORY[:TAG]          |
| 查看正在运行的容器             | docker ps                                |
| 查看所有容器                | docker ps -a                             |
| 删除容器                  | docker rm CONTAINER_ID/CONTAINER_NAME    |
| 强制删除正在运行的容器           | docker rm -f CONTAINER_ID/CONTAINER_NAME |
| 删除所有未运行容器             | docker rm \`docker ps -a -q\`            |
| 强制删除所有容器              | docker rm -f \`docker ps -a -q\`         |
| 保存容器到文件               | docker export -o CONTAINER.tar CONTAINER_ID/CONTAINER_NAME |
|从文件(保存容器)中导入镜像|docker import CONTAINER.tar [REPOSITORY[:TAG]]
|保存镜像到文件|docker save -o IMAGE.tar REPOSITORY[:TAG]|
|从文件(保存镜像)中导入镜像|docker load -i IMAGE.tar REPOSITORY[:TAG]|


refer: https://docs.docker.com/
