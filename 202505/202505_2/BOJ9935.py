if __name__ == "__main__":
    input_string = input()
    boom_string = input()

    stack = []
    for char in input_string:
        stack.append(char)
        if len(stack) >= len(boom_string):
            if "".join(stack[-len(boom_string):]) == boom_string:
                for _ in range(len(boom_string)):
                    stack.pop()
    if stack:
        print("".join(stack))
    else:
        print("FRULA")