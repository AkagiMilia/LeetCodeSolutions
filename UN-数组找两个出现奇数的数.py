'''

    一个数组， 其中有两个输出现基数次，剩下全部偶数次，找出这两个出现基数次数的是谁

'''

array = [3,3,4,4,4,4,5,5,1,1,2,2,1,2]
# 答案：1 和 2

eor = 0
for num in array:
    eor ^= num
print(bin(eor))
rightOne = eor & (~eor + 1)
print(bin(rightOne))
eor2 = 0
for num in array:
    if (num & rightOne):
        eor2 ^= num

print('num1:', eor2)
print('num2:', eor^eor2)


# Tips
'''

    异或性质
    a ^ b = b ^ a
    a ^ (b^c) = (a^b) ^ c

    0 ^ n = n
    n ^ n = 0

'''

# a与b交换
def note1():
    a = 1
    b = 2
    a = a^b
    b = a^b
    a = a^b
    print('a: ', a)
    print('b: ', b)

# 选出一个数二进制中右侧第一个1
def note2():
    n = 5^2
    rightOne = n & (~n + 1)
    print('n: ', bin(n))
    print('rightOne: ', bin(rightOne))