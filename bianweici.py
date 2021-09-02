from timeit import timeit


# 1. 逐字比较法
def compare_1(s1, s2):
    s2List = list(s2)

    stillOk = True
    for item_s1 in s1:
        isFound = False
        for index, item_s2 in enumerate(s2List):
            # 找到了，赋值 none， 终止循环。
            if item_s2 == item_s1:
                isFound = True
                del s2List[index]
                break
        # 判断这个数有没有被找到，没有，结束循环，找到了，继续下一个。
        if not isFound:
            stillOk = False
            break
    return stillOk


# 2. 排序比较法
def compare_2(s1, s2):
    # list.sort() return none, need sorted(list)
    # s1List = list(s1).sort()
    # s2List = list(s2).sort()

    # string cannot change, this not work.
    # list(s1).sort()
    # list(s2).sort()

    s1List = sorted(s1)
    s2List = sorted(s2)

    stillOk = True
    for index, _ in enumerate(s1List):
        if s1List[index] != s2List[index]:
            stillOk = False
            break
    return stillOk


def compare_3(s1, s2):
    s1Count = [0] * 26
    s2Count = [0] * 26

    for item in s1:
        s1Count[(ord(item) - 97)] += 1
    for item in s2:
        s2Count[(ord(item) - 97)] += 1
    stillOk = True

    for index, _ in enumerate(s1Count):
        if s1Count[index] != s2Count[index]:
            stillOk = False
            break

    return stillOk


t1 = timeit('compare_1("pythonfaas", "thpyonfaas")',setup="from __main__ import compare_1",  number=1000)

t2 = timeit('compare_2("pythonfaas", "thpyonfaas")',setup="from __main__ import compare_2",  number=1000)

t3 = timeit('compare_3("pythonfaas", "thpyonfaas")',setup="from __main__ import compare_3",  number=1000)

print(t1, t2, t3)
