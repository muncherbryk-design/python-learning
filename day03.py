# 第三天：列表 list
# 学习目标：
# 1. 用列表保存多个设备名
# 2. 用列表保存多个 IP 地址
# 3. 用列表保存多个端口号
# 4. 学会用 [0] 取第一个数据
# 5. 学会用 len() 统计数量

device_list = ["switch01","router01","firewa1101"]
ip_list = ["192.168.1.1","192.168.10.1","10.0.0.1"]
port_list = [22,80,443]

print(f"设备列表：{device_list}")
print(f"IP地址列表：{ip_list}")
print(f"端口列表：{port_list}")

print(f"第一台设备：{device_list[0]}")
print(f"第一个IP地址：{ip_list[0]}")
print(f"第一个端口：{port_list[0]}")

print(f"设备数量：{len(device_list)}")
print(f"IP地址数量：{len(ip_list)}")
print(f"端口数量：{len(port_list)}")

#新增设备
device_list.append("server01")
#修改数据
device_list[0] = "core-switch01"
#删除数据
device_list.remove("router01")

print("------ 列表的增加、修改、删除 ------")

device_list = ["switch01", "router01", "firewall01"]#一共三个
print(f"原始设备列表：{device_list}")

device_list.append("server01")#在最后加
print(f"新增后第一台设备：{device_list}")#现在四个设备

device_list[0] = "core-switch01"#修改第一个为core-switch01
print(f"修改后第一台设备：{device_list[0]}")#打印第一个设备名称
print(f"修改后的所有设备：{device_list}")#打印所有设备

device_list.remove("router01")#删除这个设备
print(f"删除router01后的：{device_list}")#删除后三个设备了

print(f"最终设备数量：{len(device_list)}")#最终数量

server_list = ["server01","server02","server03"]
print(f"原始服务器列表:{server_list}")

server_list.append("server04")
print(f"新增后的总设备:{server_list}")

server_list[0] = "web_server01"
print(f"修改后的总设备：{server_list}")

server_list.remove("server02")
print(f"删除后的总设备：{server_list}")

print(f"最后剩余服务器数量为：{len(server_list)}")


#提交试验

#提交代码试验1



