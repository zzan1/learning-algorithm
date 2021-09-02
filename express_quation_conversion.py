# 中缀表达式转换成后缀表达式
from standard.stack import Stack
import unittest


def conversion(equation: str):
    listEquation = list(equation)
    token = {
        "(": 3,
        ")": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
    }
    result = []
    tokenStack = Stack()
    for item in listEquation:
        if item not in token:
            result.append(str(item))
        else:
            if item == ")":
                while True:
                    if tokenStack.peek() == "(":
                        tokenStack.pop()
                        break
                    else:
                        result.append(tokenStack.pop())
            else:
                while True:
                    if tokenStack.is_empty() or token[item] > token[tokenStack.peek()] or tokenStack.peek() == "(":
                        tokenStack.push(item)
                        break
                    else:
                        result.append(tokenStack.pop())

    # 思考的不够全面，流程图画的不好，要好好画，这里就是对上面的 for 循环的补充，因为当前栈里面还有东西，没抛空呢 。
    while not tokenStack.is_empty():
        result.append(tokenStack.pop())
    s = ""
    return s.join(result)


class CoversionTest(unittest.TestCase):
    def test_1(self):
        equation = "a + b * c + (d * e + f)*g".replace(" ", "")
        self.assertEqual(conversion(equation),
                         "a b c * + d e * f  + g * +".replace(" ", ""))


if __name__ == '__main__':
    unittest.main()
