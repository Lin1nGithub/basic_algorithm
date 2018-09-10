# -*- coding: UTF-8 -*-
# 二分查找法 （有序的数组）
def binary_search(list,item):
    low = 0             # 数组最小数字的位置
    high = len(list)-1  # 数组最大数字的位置

    while low <= high:
        mid = (low + high)/2  # 如果在(low + high) 不是偶数 Python自动将mid向下取整
        guess = list[mid]
        if guess == item:   # 找到了元素
            return mid
        if guess > item:    # 数组大了
            high = mid - 1
        else:
            low = mid + 1   # 数组小了
    return None


my_list = [1,3,5,7,9]
print binary_search(my_list,3)
print binary_search(my_list,-1)