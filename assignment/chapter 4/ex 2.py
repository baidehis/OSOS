def check_balance(text):
    stack = stack()
    pairs = 0


    opening = "(([{"
    closing = ")]}"

    for i in range(len(text)):
        char = text[i]

        # if opening bracket - push to stack
        if char in opening:
            stack.push(char)

        # if closing bracket - check match
        elif char in closing:
            # if stack is empty - error
            if len(stack) == 0:
                return f"Match error at position {i}"
            
            top = stack.pop()

            # check if they match
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return f"Match error at position {i}"
            
            pairs += 1

            # After checking all text
            if len(stack) != 0:
                return f"Match error at position {len(text)}"
            

            return f"Ok - {pairs}"
        


        
        print(check_balance("a(b)c[d]e{f}g"))
