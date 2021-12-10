'''
异或性质
a ^ b = b ^ a
a ^ (b^c) = (a^b) ^ c

0 ^ n = n
n ^ n = 0
'''

# a与b交换
a = 1
b = 2
a = a^b
b = a^b
a = a^b
print('a: ', a)
print('b: ', b)

# 选出一个数二进制中右侧第一个1
n = 5^2
rightOne = n & (~n + 1)
print('n: ', bin(n))
print('rightOne: ', bin(rightOne))
