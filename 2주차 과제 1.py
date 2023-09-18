def rev_str(input_str):
    if len(input_str) <= 1:
        return input_str
    
    first_char = input_str[0]
    rest_of_str = input_str[1:]

    reversed_rest = rev_str(rest_of_str)
    return reversed_rest + first_char

if __name__ == '__main__':
    print(rev_str('ABCDE'))