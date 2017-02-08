# 在ubuntu 16.04下安装docker


# docker 常用命令
|操作|命令|
|---|----|
|拉取镜像(没有TAG时，默认latest)|docker pull IMAGE[:TAG]|
|查看镜像|docker images|
|查看正在运行的容器|docker ps|
|查看所有容器|docker ps -a|
|删除容器|docker rm CONTAINER_ID|
|强制删除正在运行的容器|docker rm -f CONTAINER_ID|
|删除所有容器|docker rm \`docker ps -a -q\`|
|强制删除所有容器(包括正在运行)|docker rm -f \`docker ps -a -q\`|



refer: https://docs.docker.com/
