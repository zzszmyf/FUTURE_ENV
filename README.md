# FUTURE_ENV
基于docker的build环境 or run环境
conf.yaml 进行相关配置

conf.yaml配置详解
```
base:
    #一些公共的配置
    local_path : /Users/xxxxx/yyyy/zzzzz/
    #这个是项目的本地编辑目录,自己可以根据情况修改
    container_path : /work/  
    #这个是本地编辑目录和容器目录挂载同步的路径,可以进行修改
    container_name : brpc_v2_c
    #这个是容器实例化的容器名称,可以进行修改
    use_sudo : 1
    #这个开关是shell命令是否加上sudo,0为不加,1为加
    code_path : /root/work/
    #这个路径是镜像里git clone命令的默认执行路径
init:
    #环境初始化工作
    from : zqmath1994/brpc-in-centos
    #docker镜像名称，一般是项目可以进行编译的容器镜像
    git : https://github.com/brpc/brpc.git
    #项目的代码仓库地址
    user : root
    #容器的使用账户
    image_name : brpc_test
    #容器build之后的镜像名
build:
    version : v1
    #TBD
run:
    version : v2
    #TBD
```

目前已经实现功能:
1. 可以配置代码仓库和编译环境,拉下代码
2. 项目文件从容器中同步到本地

近期开发计划
1. 完成C/C++ 编译功能
2. 完成Python 编译功能
