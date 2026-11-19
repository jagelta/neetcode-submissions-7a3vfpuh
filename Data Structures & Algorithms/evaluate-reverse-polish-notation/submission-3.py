import operator as ops
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operations = {
            "+": ops.add,
            "-": ops.sub,
            "*": ops.mul,
            "/": ops.truediv
        }
        
        for i in tokens:
            if i in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operations[i](a,b)))
            else:
                stack.append(int(i))
        return int(stack[0])