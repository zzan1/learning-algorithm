from standard.stack import Stack
import unittest


# 计算后缀表达式的值

def calc(equation: str):
    equaList = list(equation)

    token = ["*", "/", "+", "-"]

    dataStack = Stack()
    for item in equaList:
        if item.isdigit():
            dataStack.push(item)
        else:
            top_1 = dataStack.pop()
            top_2 = dataStack.pop()
            dataStack.push(simpleCalc(top_2, top_1, token.index(item)))

    return dataStack.pop()


def simpleCalc(item_1, item_2, order):
    item_1 = int(item_1)
    item_2 = int(item_2)
    if order == 0:
        return item_1 * item_2
    if order == 1:
        return item_1 / item_2
    if order == 2:
        return item_1 + item_2
    if order == 3:
        return item_1 - item_2


class CalcTest(unittest.TestCase):
    def test_1(self):
        equation = "9 6 5 + 2 * + 7 -".replace(" ", "")
        self.assertEqual(calc(equation), 24)


if __name__ == '__main__':
    unittest.main()
