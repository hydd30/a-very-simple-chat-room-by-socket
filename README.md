# a-very-simple-chat-room-by-socket

详见Client与Server中的README.md

大一下Python选修课的大作业，使用pyQt和socket模块的多线程简单聊天室，原作业要求是这样的

#### 1.5.2.	Python在线测试系统(CS模式或BS模式)
##### 项目目的:
熟悉Python网络编程模块.掌握基于C/S模式网络编程技术.

##### 项目任务:
设计一个图形界面,编写一个文件传输、信息传输小型软件.可以是C/S模式,也可以是B/S模式.要求数据源是存储在数据库文件当中，如sqlite3或MySQL。
如果是C/S模式，需要分别编写客户端程序、服务端程序。
传输文件分为两大类：
1.	程序文件：如果是程序文件，与系统的参考程序比对结果.【老师提供一个评判程序】；注意多个题目序号。【类似课堂用的在线测试系统--功能注意集中在判断各个题目程序解答正确性】
2.	非程序文件：主要是记录

##### 主要操作内容:
~~1.	客户端注册账号（用户名，密码）~~<br/>
2.	客户端发送消息（短文本，长文本）<br/>
设消息内容有纯文本（单行或者多行）格式，也有富文本格式，可以支持把图片作为长文本发送。<br/>
短文本一般小于2048字节，超过的视为长文本。<br/>
3.	服务端广播消息<br/>
4.	客户端上传文件--支持同时发送N个文件(N>=2)<br/>
允许发到到服务端存储，也可以存储到云（url）。（解决服务端存储不足问题）<br/>
5.	服务端共享文件--支持同时共享K个文件(K>=2)，允许客户端下载。<br/>
文件既可以在本地，~~也可以在云（解决服务端存储不足问题）。~~<br/>
(4,5为客户端、服务端双向文件传输服务)<br/>
~~6.	客户端发送一般请求(设计通用格式)(便于扩充服务功能)<br/>
如从服务端数据库获取指定查询请求<br/>
开发C/S服务器、客户端程序。~~<br/>
~~7.	*完成类似QQ好友消息互传功能。<br/>
假设消息内容有纯文本（单行或者多行）格式，也有富文本格式，或者更复杂的包含图片等。<br/>
包括完成客户之间的文件互传功能。<br/>~~

注：打“*”表示选作。

然而当时能力和时间都是在有限，只完成了2、3、4功能
