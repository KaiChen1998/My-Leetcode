import time
import random

########################################################
# For overview: https://www.cnblogs.com/onepixel/articles/7674659.html
# Way       Average     Worst   best                space   stable(a=b且a在b前面，排序后a是不是一定在b前面)
# select    O(n^2)      O(n^2)  O(n^2)              O(1)    不稳定(abc，其中a=b但是c是最小的，最后的结果是cba)
# bubble    O(n^2)      O(n^2)  O(n)(last_visited)  O(1)    稳定
# insert    O(n^2)      O(n^2)  O(n)                O(1)    稳定
# merge     O(nlogn)    O(nlogn)O(nlogn)            O(n)    稳定
# quick     O(nlogn)    O(n^2)  O(nlogn)            O(1)    不稳定（相等的值应该归到其中一边，但是原来的位置两边都可能）
# heap      O(nlogn)    O(nlogn)O(nlogn)            O(1)    不稳定（堆的最后一步相当于select，所以不稳定）
########################################################

def exchange(a, b):
    temp = b
    b = a
    a = temp
    return a, b

def API_sort(num_list, reverse = False):
    num_list = sorted(num_list, reverse = reverse)
    return num_list

##########################################################
# 选择排序
# Idea: 每次选择剩下元素当中的最小值或者最大值放到队列头指针位置处
##########################################################

def select_sort(num_list):
    for i in range(len(num_list)):
        min_value = float('+inf')
        index = -1
        for j in range(i, len(num_list)):
            if(num_list[j] < min_value):
                index = j
                min_value = num_list[j]
        num_list[i], num_list[index] = exchange(num_list[i], num_list[index])
    return num_list

##########################################################
# 冒泡排序
# Idea: 每次循环从前到后比较任意相邻两个元素，如果前者大于后者就将两者交换
# 这样做可以保证每次循环的最后一个元素都是最大的那个元素
# trick: 记录最近的一次交换的位置，我们可以保证从这个位置开始到结尾都是有序的，因此就可以跳过这些元素
##########################################################

def bubble_sort(num_list):
    i = len(num_list)
    while(i > 0):
        last_visited = 0
        for j in range(i - 1):
            if(num_list[j] > num_list[j + 1]):
                last_visited = j + 1
                num_list[j], num_list[j + 1] = exchange(num_list[j], num_list[j + 1])
        i = last_visited
    return num_list
 
##########################################################
# 插入排序
# Idea: 队列分为两部分，一部分有序，另一部分无序，每次找到当前元素的位置并插入
##########################################################

def insert_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i, 0, -1):
            if(num_list[j] < num_list[j - 1]):
                num_list[j], num_list[j - 1] = exchange(num_list[j], num_list[j - 1])
    return num_list

##########################################################
# 归并排序
# Idea: 分治法
# root case: len(num_list) <= 1
##########################################################

def merge_sort(num_list):
    if(len(num_list) <= 1):
        return num_list
    half = int(len(num_list) / 2)
    left = merge_sort(num_list[:half])
    right = merge_sort(num_list[half:])
    result = []
    index1 = index2 = 0
    while(index1 < len(left) and index2 < len(right)):
        if(left[index1] < right[index2]):
            result.append(left[index1])
            index1 += 1
        else:
            result.append(right[index2])
            index2 += 1
    while(index1 < len(left)):
        result.append(left[index1])
        index1 += 1
    while(index2 < len(right)):
        result.append(right[index2])
        index2 += 1
    return result

##########################################################
# 快速排序
# Idea: 随机选一个pivot，找到它的位置使得左边的元素都比他小，右边的元素都比他大
##########################################################

def quick_sort(num_list, start, end):
    if(start >= end - 1):
        return num_list
    # find index
    pivot = num_list[start]
    pos = start
    for i in range(start + 1, end):
        if(num_list[i] <= pivot):
            pos += 1 # 保证比pivot小的元素又多了一个，这里pos所指的元素和pivot之间的大小关系并不一定，只代表下一个交换的位置
            if(pos != i):
                num_list[pos], num_list[i] = exchange(num_list[pos], num_list[i])
    num_list[start], num_list[pos] = exchange(num_list[start], num_list[pos])
    quick_sort(num_list, start, pos)
    quick_sort(num_list, pos + 1, end)
    return num_list

##########################################################
# 堆排序
# Idea: 
# 堆: 一棵完全二叉树，且满足父节点的值小于两个孩子节点
# 首先构建堆，代价是logn，但是堆只能保证堆顶是最值，整个堆仍然是无序的
# 然后我们从最后一个叶子节点开始，和堆顶交换，从而保证这个叶子节点是最值，然后再调整剩余元素使其恢复成一个堆，代价是logn
# 循环n次，因此代价是nlogn
##########################################################

def heap_adjust(num_list, start, end):
    while(2 * start + 1 < end): # child exists
        child = 2 * start + 1
        if(child + 1 < end and num_list[child] > num_list[child + 1]):
            child += 1
        if(num_list[start] > num_list[child]):
            num_list[start], num_list[child] = exchange(num_list[start], num_list[child])
            start = child
        else:
            # each child tree is a heap
            # so if root doesn't violate each child tree, it's a heap now
            break

def heap_sort(num_list):
    # it's a heap but not sorted
    # but we know the root is the minimum
    for i in range(int(len(num_list) / 2 - 1), -1, -1):
        heap_adjust(num_list, i, len(num_list))
    for i in range(len(num_list) - 1, -1, -1):
        num_list[0], num_list[i] = exchange(num_list[0], num_list[i])
        heap_adjust(num_list, 0, i)
    return num_list[::-1]

def create():
    return [1, 8, 4, 7, 5, 3, 2, 6]

if __name__ == '__main__':
    num_list = create()
    print(API_sort(num_list))
    num_list = create()
    print(select_sort(num_list))
    num_list = create()
    print(bubble_sort(num_list))
    num_list = create()
    print(insert_sort(num_list))
    num_list = create()
    print(merge_sort(num_list))
    num_list = create()
    print(quick_sort(num_list, 0, len(num_list)))
    num_list = create()
    print(heap_sort(num_list))