# java_Laplace_Fluid_Maid
javaweb的流量监控脚本，基于filter，也有jar版本，那天曹佬说它就取名叫拉普拉斯的流量女仆(java_Laplace_Fluid_Maid)好了

## 简要说明

由于时间有限，又要产出有价值的工具，所以决定先整个能用的：

- 一个摆烂jar包，比如说这次比赛，完全可以全程宕机（没几个修上的），这个jar包可以狠狠的监控流量偷师学艺，并且jar纯静态，不会被打，实现不被攻击但是宕机

- 几个摆烂class文件（基于Inceptor和filter），监控别人的流量，于此同时把流量都转发到自己机器的服务端（flask服务），且流量不进入控制器，实现不被攻击但是宕机



## 摆烂的jar



部署方式就是直接运行

```
java -jar demo.jar
```



默认8081端口



功能

- 控制台输出全部访问流量，方便抄流量上车
- 纯静态，无漏洞不会被打，但是会宕机







## 摆烂的Class



基于filter开发的流量监控，具体原理是将流量转发到`127.0.0.1:3307`(请用户自定义) 的服务端，在服务端接受流量后回显至控制台，在这个过程中，流量不进入控制器（也可以自行选择是否需要进入控制器）



部署方法：

java源码编译为class，再将class打包进jar包

上诉步骤具体操作：

```
1.
首先修改package路径，比如说我计划在controller同级目录下新建Myfilter目录，将java文件放于这个路径中，所以package路径就是controller的package/Myfilter
2.
javac -extdirs BOOT-INF/lib/ -classpath BOOT-INF/classes/....package.../Myfilter MyObjectInputStream.java
3.
注意这里的打开目录要和javaweb目录一致，inputfile的目录要符合javawebpath
jar uf ctf-0.0.1-SNAPSHOT.jar BOOT-INF/classes/....package.../Myfilter/MyObjectInputStream.class
```



然后新生成的jar包就可以了！
