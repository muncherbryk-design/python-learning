# 第五天：if 判断
# 学习目标：
# 1. 理解 if 的作用
# 2. 学会判断端口类型
# 3. 学会使用 if、elif、else
# 4. 理解 = 和 == 的区别
from idlelib.editor import index2line

from day04 import server_port

port = 22

if port == 22:
    print("这是 SSH 端口")
elif port == 80:
    print("这是 HTTP 端口")
elif port == 443:
    print("这是 HTTPS 端口")
else:
    print("这是其他端口")


device_count = 12

if device_count > 10:
    print("设备数量较多")
else:
    print("设备数量正常")


device_count = 9
if device_count > 10:
    print("设备数量较多")
else:
    print("设备数量正常")

server_port = 443
if server_port == 22:
    print("SSH服务")
elif server_port == 80:
    print("HTTP服务")
elif server_port == 443:
    print("HTTPS服务")
else:
    print("未知服务")

# for 循环配合 if 判断

port_list = [22, 80, 443, 3306]

for port in port_list:
    if port == 22:
        print(f"端口 {port}：SSH 服务")
    elif port == 80:
        print(f"端口 {port}：HTTP 服务")
    elif port == 443:
        print(f"端口 {port}：HTTPS 服务")
    else:
        print(f"端口 {port}：其他服务")

test_list = [21,22,80,443,8080]
for test in test_list:
    if test == 21:
        print(f"端口{test}FTP端口")
    elif test == 22:
        print(f"端口{test}SSH端口")
    elif test == 80:
        print(f"端口{test}HTTP端口")
    elif test == 443:
        print(f"端口{test}HTTPS端口")
    else:
        print(f"未知端口")


# 第三节
device_list = ["switch01","server01","web01","database01"]
ip_list = ["192.168.1.1","172.16.1.10","172.16.1.20","172.6.1.30"]
port_list = [22,80,443,3306]

for device,ip,port in zip(device_list,ip_list,port_list):
    if port == 22:
        service = "SSH服务"
    elif port == 80:
        service = "HTTP服务"
    elif port == 443:
        service = "HTTPS服务"
    elif port == 3306:
        service = "MYSQL服务"
    else:
        service = "未知服务"
    print(f"设备名称：{device},管理地址：{ip},端口：{port},服务：{service}")

app_list = ["router01","web_server01","file_server01","unknown01"]
ip_list = ["10.0.0.1","10.0.0.10","10.0.0.20","10.0.0.30"]
port_list = [22,443,21,8080]

for app,ip,port in zip(app_list,ip_list,port_list):
    if port == 22:
        service = "SSH服务"
    elif port == 21:
        service = "FTP服务"
    elif port == 443:
        service = "HTTPS服务"
    else:
        service = "其他服务"
    print(f"设备名称：{app},IP：{ip},端口：{port},服务：{service}")

device_ip = "192.168.1.1"
port = 22

if device_ip == "192.168.1.1" and port == 22:
    print("交换机 SSH 信息正确")
else:
    print("设备信息不匹配")

device_ip = "192.168.1.1"
port = 80

if device_ip == "192.168.1.1" and port == 22:
    print("交换机 SSH 信息正确")
else:
    print("设备信息不匹配")


port = 443

if port == 80 or port == 443:
    print("这是 Web 服务端口")
else:
    print("这不是 Web 服务端口")


#多个条件：and和or

device_name = "switch01"
device_ip = "192.168.1.1"
poet = 22
if device_name == "switch01" and device_ip == "192.168.1.1":
    print("switch01使用SSH服务")
else:
    print("设备名称或端口不匹配")

web_port = 443

if web_port == 80 or web_port == 443:
    print(f"端口{web_port}是web服务端口")
else:
    print(f"端口{web_port}不是web服务端口")

device_name = "firewall01"
device_ip = "10.0.0.1"
port = 443
status = "online"

if device_name == "firewall01" and status == "online":
    print(f"防火墙在线")
else:
    print(f"防火墙状态异常")

if port == 80 or port == 443:
    print(f"这是Web服务端口")
else:
    print("这不是Web服务端口")


# in：判断数据是否存在于列表中

allowed_port_list = [22, 80, 443]
test_port = 443

if test_port in allowed_port_list:
    print(f"端口 {test_port} 在允许列表中")
else:
    print(f"端口 {test_port} 不在允许列表中")

allowed_ip_list = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]
device_ip = "10.0.0.1"

if device_ip in allowed_ip_list:
    print(f"IP {device_ip} 允许访问")
else:
    print(f"IP {device_ip} 不允许访问")

allowed_ip_list = ["10.0.0.1", "10.0.0.2"]
allowed_port_list = [22, 443]

device_ip = "10.0.0.1"
device_port = 443

if device_ip in allowed_ip_list and device_port in allowed_port_list:
    print("设备 IP 和端口都允许访问")
else:
    print("设备 IP 或端口不允许访问")

allowed_device_list = ["switch01","router01","firewall01"]
allowed_port_list = [22,80,443]
device_name = "router01"
device_port = 443

if device_name in allowed_device_list and device_port in allowed_port_list:
    print(f"设备:{device_name}，端口：{device_port},允许检测")
else:
    print("设备或端口不在允许列表中")

allowed_port_list = [22, 80, 443]
test_port = 8080

if test_port not in allowed_port_list:
    print(f"端口 {test_port} 不在允许列表中")
else:
    print(f"端口 {test_port} 在允许列表中")

# not in：判断数据不在列表中

known_device_list = ["switch01", "router01", "firewall01"]
device_name = "server01"

if device_name not in known_device_list:
    print(f"发现未知设备：{device_name}")
else:
    print(f"设备 {device_name} 已在设备清单中")

allowed_ip_list = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]
test_ip = "192.168.1.100"

if test_ip not in allowed_ip_list:
    print(f"IP {test_ip} 未授权")
else:
    print(f"IP {test_ip} 已授权")

allowed_device_list = ["switch01", "router01"]
allowed_port_list = [22, 443]

device_name = "server01"
device_port = 8080

if device_name not in allowed_device_list or device_port not in allowed_port_list:
    print("设备名称或端口未授权")
else:
    print("设备名称和端口均已授权")

trusted_ip_list = ["10.0.0.1","10.0.0.2","10.0.0.3"]
test_ip = "10.0.0.100"

if test_ip not in trusted_ip_list:
    print(f"发现未知IP：{test_ip}")
else:
    print(f"IP {test_ip}已在可信列表中")

# 布尔值 True 和 False

device_name = "switch01"
device_online = True

if device_online:
    print(f"设备 {device_name} 在线")
else:
    print(f"设备 {device_name} 离线")

device_name = "router01"
device_online = False
if device_online:
    print(f"设备{device_name}在线")
else:
    print(f"设备{device_name}离线")

device_name = "server01"
device_ip = "172.16.1.10"
device_online = False

if device_online:
    print(f"{device_name}({device_ip})在线")
else:
    print(f"{device_name}({device_ip})离线")

device_online = True
if not device_online:
    print(f"{device_name}正在连接")
else:
    print(f"请检查{device_name}的网络连接")

