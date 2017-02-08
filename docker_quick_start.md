# 在ubuntu 16.04下安装docker


# docker 常用命令
|操作|命令|
|---|----|
|查看docker的所有命令|docker --help|
|查看docker命令参数|docker COMMAND --help|
|查看docker版本信息|docker -v|
|拉取镜像(没有TAG时，默认latest)|docker pull REPOSITORY[:TAG]|
|查看镜像|docker images|
|删除镜像|docker rmi REPOSITORY[:TAG]/IMAGE_ID|
|删除所有镜像|docker rmi \`docker images -a -q\`|
|运行容器|docker run -it REPOSITORY[:TAG]|
|查看正在运行的容器|docker ps|
|查看所有容器|docker ps -a|
|删除容器|docker rm CONTAINER_ID|
|强制删除正在运行的容器|docker rm -f CONTAINER_ID|
|删除所有未运行容器|docker rm \`docker ps -a -q\`|
|强制删除所有容器|docker rm -f \`docker ps -a -q\`|
|保存容器到文件|docker export -o CONTAINER_ID/CONTAINER_NAME.tar CONTAINER_ID/CONTAINER_NAME|
|从文件(保存容器)中导入镜像|docker import CONTAINER_ID/CONTAINER_NAME.tar [REPOSITORY[:TAG]]
|保存镜像到文件|docker save -o IMAGE.tar REPOSITORY[:TAG]|
|从文件中导入容器|docker load -i IMAGE.tar REPOSITORY[:TAG]|


refer: https://docs.docker.com/
