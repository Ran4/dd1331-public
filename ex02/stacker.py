    
def update_stack(stack, input_value):
    try:
        number = float(input_value)
        stack.append(number)
    except ValueError:
        if input_value in ["e", "evaluate"]:
            update_stack(stack, stack.pop())
        elif input_value == "+":
            stack.append(stack.pop() + stack.pop())
        elif input_value == "-":
            stack.append(stack.pop() - stack.pop())
        elif input_value == "*":
            stack.append(stack.pop() * stack.pop())
        elif input_value == "flip" or input_value == "~":
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif input_value == "pop":
            stack.pop()
        elif input_value == "clear":
            stack = []
        elif input_value == "p":
            print(stack)
        elif input_value == "":
            pass
        else:
            print("???")

def main():
    stack = []
    while True:
        PROMPT_STRING = "> "
        input_string = input(PROMPT_STRING)
        input_values = [v.strip() for v in input_string.split(" ")]
        
        for input_value in input_values:
            if input_value.startswith("'"):
                input_value = input_value[1:]
                stack.append(input_value)
            else:
                update_stack(stack, input_value)
                
            print(stack)

main()
