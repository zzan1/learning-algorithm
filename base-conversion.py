from standard.stack import Stack
import unittest


# 进制转换，base conversion

def baseConversion(number: int):
    binStack = Stack()
    while number != 0:
        remainder = number % 2
        binStack.push(remainder)
        number = number // 2

    result = []
    # 如果元素是 0，这里也会变成 False 终止循环的。不能这样来判断栈空的，会 list index out of range
    # 判断应该这么判断，判空。
    while not binStack.is_empty():
        result.append(str(binStack.pop()))
    print(result)
    # join 方法的使用
    # 必须指定一个 s 字符串
    # 列表不能是 int 型，只能是 str 类型
    s = ""
    # 0b 是 表示二进制的，bin 之后就有这个。
    return "0b" + s.join(result)


class baseConversionTest(unittest.TestCase):
    def test_1(self):
        number = 100
        self.assertEqual(baseConversion(number), bin(number))

    def test_2(self):
        number = 6700
        self.assertEqual(baseConversion(number), bin(number))


if __name__ == '__main__':
    unittest.main()
