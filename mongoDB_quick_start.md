# mongoDB

Refer:https://docs.mongodb.com/master/tutorial/install-mongodb-on-ubuntu/

##　Ubuntu 16.04 安装 MongoDB


1. 导入公钥
    ```
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
    ```

2. 添加MongoDB软件包列表
    ```
    echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
    ```

3. 更新本地软件库
    ```
    sudo apt-get update
    ```

4. 安装MongoDB软件包
    ```
    sudo apt-get install -y mongodb-org
    ```

开启MongoDB
```
sudo service mongod start

```

MongoDB GUI

https://robomongo.org/
