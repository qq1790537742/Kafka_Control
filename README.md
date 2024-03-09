#kafka控制系统

系统采用的是官网2.4.0版本的kafka包名为：kafka2.12-2.40

需要准备的环境：除了大赛系统配置的python环境外还需要配置java环境，java建议选择java17

#系统使用
直接运行DataQt.py,运行后会自动运行该目录下的kafka，此时需要看控制台输入的指令，当没有出现shutdown时说明kafka启动成功

如果显示shutdown，先关闭DataQt.py然后再运行Kafka_Stop.py。然后重新启动DataQt.py

kafka启动成功后点击连接建议topic等待客户端接入

客户端在Neuracle_demo每个模块的DataQto中，使用者可以选择和本系统一样使用qt界面进行开发或者直接运行每个模块的main.py

