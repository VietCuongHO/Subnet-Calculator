# Chương trình chia địa chỉ IP sử dụng phương pháp thủ công
import ipaddress
import math
print('Subnet calculator')
print('--------------------------------------------------')
print('Phương pháp thủ công (manual)')
a = input('Nhập địa chỉ IP. ex: 192.168.1.0/24\n')
k = int(input('Nhập số mạng con cần chia: '))
n = math.ceil(math.log(k,2))
print('Số bit cần mượn:',n)
b = ipaddress.IPv4Network(a)
c = list(b.subnets(prefixlen_diff=n))
print('Subnet mask: ',c[0].netmask)
l = a.split('/')
k = l[0].split('.')
if int(k[0]) >= 0 and int(k[0]) <= 127:
    print('Class A')
elif int(k[0]) >= 128 and int(k[0]) <= 191:
    print('Class B')
elif int(k[0]) >= 192 and int(k[0]) <= 223:
    print('Class C')
elif int(k[0]) >= 224 and int(k[0]) <= 239:
    print('Class D')
elif int(k[0]) >= 240 and int(k[0]) <= 255:
    print('Class E')
print('-----------------------------------------')
for i in range(len(c)):
    t = []
    print('Subnet {}:'.format(i+1))
    for j in c[i].hosts():
        t.append(str(j))
    print('Network Address: {}'.format(c[i].network_address))
    print('Broadcast Address: {}'.format(c[i].broadcast_address))
    print('Host range: {} --> {}'.format(t[0],t[-1]))
    print('-----------------------------------------')












