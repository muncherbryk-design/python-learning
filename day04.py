# 第四天：for 循环
# 学习目标：
# 1. 理解 for 循环的作用
# 2. 学会遍历列表
# 3. 用 for 输出多个设备名
# 4. 用 for 输出多个 IP 地址

device_list = ["switch01","router01","firewall01"]
ip_list = ["192.168.1.1","192.168.10.1","10.0.0.1"]

print("-----输出设备列表------")

for device in device_list:
    print(f"设备名称：{device}")

print("-----输出ip地址列表-----")

for ip in ip_list:
    print(f"管理地址：{ip}")


port_list = [22,80,443,3306]
for port in port_list:
    print(f"检测端口:{port}")


print("-----同时输出设备名，ip，端口-----")
device_list = ["switch01","router01","firewall01"]
ip_list = ["192.168.1.1","192.168.10.1","10.0.0.1"]
port_list = [22,22,443]

for device,ip,port in zip(device_list,ip_list,port_list):#从三个列表里按顺序各取一个数据
    print(f"设备名称：{device},管理地址：{ip},检测端口：{port}")

print("------------------------------------练习--------------------------------")
#练习
server_list = ["server01","server02","server03"]
server_ip_list = ["172.16.1.10","172.16.1.11","172.16.1.12"]
server_port_list = [22,80,443]

for server,server_ip,server_port in zip(server_list,server_ip_list,server_port_list):
    print(f"服务器名称：{server}，服务器IP：{server_ip}，检测端口：{server_port}")
