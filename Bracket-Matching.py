from standard.stack import Stack
import unittest


# basic version
def bracketsMatching(brackets: str):
    bracketsStack = Stack()
    stillOk = True
    for item in list(brackets):
        if item == "(":
            bracketsStack.push(item)
        elif item == ")":
            if bracketsStack.is_empty():
                stillOk = False
                break
            else:
                bracketsStack.pop()
    if not bracketsStack.is_empty():
        stillOk = False

    return stillOk


# advance version
def bracketsMatching(brackets: str):
    bracketsStack = Stack()
    stillOk = True
    for item in list(brackets):
        if item in "({[<":
            bracketsStack.push(item)
        elif item in ")}]>":
            if bracketsStack.is_empty() or (not match(bracketsStack.peek(), item)):
                stillOk = False
                break
            else:
                bracketsStack.pop()
    if not bracketsStack.is_empty():
        stillOk = False

    return stillOk


def match(item_1_left: str, item_2_right: str):
    token_left = "({[<"
    token_right = ")}]>"
    isMatch = False
    if token_left.index(item_1_left) == token_right.index(item_2_right):
        isMatch = True
    return isMatch


class TestBracketsMatching(unittest.TestCase):
    def test_1(self):
        testString = "(((((((((())))))))))"
        self.assertTrue(bracketsMatching(testString))

    def test_2(self):
        testString = "((((((((())))))))))"
        self.assertFalse(bracketsMatching(testString))

    def test_3(self):
        testString = "((((((()<({((({})))})>))))))"
        self.assertTrue(bracketsMatching(testString))

    def test_4(self):
        testString = "((((((<((())))))))))"
        self.assertFalse(bracketsMatching(testString))

    def test_5(self):
        testString = "(((((((((<))))))))))"
        self.assertFalse(bracketsMatching(testString))

if __name__ == '__main__':
    unittest.main()
