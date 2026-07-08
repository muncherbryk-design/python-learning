device_name = "switch01" #保存设备名称。设备名称是文本，所以加引号。
ip_address = "192.168.1.1"#保存 IP 地址。IP 地址虽然有数字，但它不是拿来做加减乘除的，所以也加引号。
port  = 22 #保存端口号。端口号是数字，所以不加引号。
device_count = 5 #保存当前设备数量。设备数量可以计算，所以不加引号。
print(f"设备名称:{device_name}")#用 f-string 输出设备名称。
print(f"管理地址：{ip_address}")
print(f"登陆端口：{port}")
print(f"当前设备数量：{device_count}")

new_device_count = device_count + 3 #把原来的设备数量 5 加上 3，结果保存到 new_device_count。

print(f"新增3台设备后，总设备数量：{new_device_count}") #输出新增后的总设备数量。


firewall_name = "firewall01"
firewall_ip = "10.0.0.1"
firewall_ssh_port = 22
firewall_web_port = 80
firewall_count = 6
"""
firewall_name 是设备名称，要加引号
firewall_ip 是 IP 地址，要加引号
firewall_ssh_port 是端口号，不加引号
firewall_web_port 是端口号，不加引号
firewall_count 是数量，不加引号
"""
print(f"防火墙名称：{firewall_name}")
print(f"防火墙管理地址：{firewall_ip}")
print(f"SSH端口：{firewall_ssh_port}")
print(f"Web端口：{firewall_web_port}")
print(f"当前防火墙数量：{firewall_count}")

new_firewall_count = firewall_count + 4

print(f"增加4台防火墙后，总数量：{new_firewall_count}")


