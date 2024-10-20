class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {} # ()
        curly = {}    # {}
        square = {}  # []
        to_close_next = []
        brackets['open'] = 0
        curly['open'] = 0
        square['open'] = 0
        for e in s:
            if e == '(':
                brackets['open'] += 1
                to_close_next.append('b')
            if e == '{':
                curly['open'] += 1
                to_close_next.append('c')
            if e == '[':
                square['open'] += 1
                to_close_next.append('s')

            if e == ')':
                if brackets['open'] == 0 or to_close_next[-1]!='b':
                    return False
                brackets['open'] -= 1
                to_close_next.pop()
            if e == '}':
                if curly['open'] == 0 or to_close_next[-1]!='c':
                    return False
                curly['open'] -= 1
                to_close_next.pop()

            if e == ']':
                if square['open'] == 0 or to_close_next[-1]!='s':
                    return False
                square['open'] -= 1
                to_close_next.pop()

        return (brackets['open'] == 0) and (square['open'] == 0) and (curly['open'] == 0)
