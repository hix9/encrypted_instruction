def decode(data: str) -> str:
    """Программа расшифровывает входящую строчную команду."""
    stack: list = []
    current_string: str = ''
    prev_string: str = ''
    prev_num: int = 0
    num_token: str = ''

    for character in data:
        if character.isdigit():
            num_token += character
        elif character == '[':
            stack.append((current_string, int(num_token)))
            current_string = ''
            num_token = ''
        elif character == ']':
            prev_string, prev_num = stack.pop()
            current_string = prev_string + current_string * prev_num
        else:
            current_string += num_token
            num_token = ''
            current_string += character

    return current_string


if __name__ == '__main__':
    instruction: str = input()
    print(decode(instruction))
