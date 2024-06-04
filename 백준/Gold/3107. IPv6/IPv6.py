import ipaddress

input_ip = input()
base = ipaddress.ip_address(input_ip).exploded
print(base)