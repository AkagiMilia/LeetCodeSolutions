'''

    二分查找
    O(log n)

'''

#
# Type1: 在有序数组中找到需要的数
#

def type1(nums, target):
    left = 0
    right = len(nums)-1
    ref = nums[:]           
    middle = (right+left)//2
    while(len(ref) > 1):
        if (nums[middle] == target):
            return middle
        if (nums[middle] > target):
            ref = nums[left:middle]
            right = middle-1
        else:
            ref = nums[middle+1:right+1]
            left = middle+1
        middle = (right+left)//2
        
    if (len(ref) == 1):
        if ref[0] == target:
            return middle
        else:
            return -1
    if (not len(ref)):
        return -1

#
# Type2: 在有序数组中找到需要的数并且是最偏左的那一个
# e.g. array = [1,2,2,3,3] target = 2
#       result = 1
#

def type2(nums, target):
    def doit(left, right, target, leftMost):
        theOne = right if leftMost else left
        middle = (left+right)//2
        find = False
        while(left<=right):
            if leftMost:
                if (nums[middle] >= target):
                    if (theOne >= middle and nums[middle] == target):
                        theOne = middle
                        find = True
                    right = middle - 1
                else:
                    left = middle+1
            else:
                if (nums[middle] <= target):
                    if (theOne <= middle and nums[middle] == target):
                        theOne = middle
                        find = True
                    left = middle+1
                else:
                    right = middle-1
            middle = (left+right)//2
        return theOne if find else -1
    left, right = 0, len(nums)-1
    if not right:
        return [0,0] if nums[0] == target else [-1,-1]
    ans1 = doit(left, right, target, True)
    ans2 = doit(left, right, target, False) if ans1 > -1 else -1
    return [ans1, ans2]

if __name__ == '__main__':
    result = type1([0,1,3,6,9,10,22], 22)
    print(result)


