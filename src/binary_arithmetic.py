"""
Binary Arithmetic

Performs binary arithmetic operations on two binary numbers entered
by the user in the console.

"""

def displayDescription():
    """ Display the program description """
    print("-    ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~    -")
    print("-  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  -")
    print("| ~ ~ ~ ~ ~                                                  ~ ~ ~ ~ ~ |")
    print("|~ ~ ~ ~ ~                  Binary Arithmetic                 ~ ~ ~ ~ ~|")
    print("|~ ~ ~ ~ ~              written by: Kenneth Berry             ~ ~ ~ ~ ~|")
    print("| ~ ~ ~ ~ ~                                                  ~ ~ ~ ~ ~ |")
    print("-  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  -")
    print("-    ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~    -")
    print("   ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~   ")
    print("  ~ ~ ~ ~ ~                                                  ~ ~ ~ ~ ~  ")
    print(" ~ ~ ~ ~ ~     This program accepts two binary numbers as     ~ ~ ~ ~ ~ ")
    print(" ~ ~ ~ ~ ~     inputs, and then comepletes the arithmetic     ~ ~ ~ ~ ~ ")
    print(" ~ ~ ~ ~ ~     operation chosen by the user.                  ~ ~ ~ ~ ~ ")
    print("  ~ ~ ~ ~ ~                                                  ~ ~ ~ ~ ~  ")
    print("   ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~   ")
    print("     ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~     ")
    print("\n")

def binaryAddition(binary_list1, binary_list2):
    """ Add two base[2] numbers in lists, and return the result in a list """
    count = len(binary_list1) - 1
    carry = 0
    binary_list3 = []
    while count >= 0:
        result = binary_list1[count] + binary_list2[count] + carry
        if result == 3:
            binary_list3.insert(0, 1)
            carry = 1
        elif result == 2:
            binary_list3.insert(0, 0)
            carry = 1
        elif result == 1:
            binary_list3.insert(0, 1)
            carry = 0
        elif result == 0:
            binary_list3.insert(0, 0)
            carry = 0
        else:
            print("Result Error!")
            break
        if count == 0:
            if carry == 1:
                binary_list3.insert(0, 1)
        count = count - 1
    return binary_list3

def stringToList(char_string):
    """ Take user inputs, convert them to integers, and place them in lists """
    char_list = []
    for i in char_string:
        if i.isdigit():
            i = int(i)
            char_list.append(i)
        else:
            char_list.append(i)
    return char_list

def listToString(char_list):
    """ Take a list of base2 integers and converts to string """
    char_string = ''
    for i in char_list:
        char_string = char_string + str(i)
    return char_string

def equalizeLength(base2_int_list1, base2_int_list2):
    """ Add a zero to the number with fewest bits until equal in length """
    equal_len = False
    while not equal_len:
        if len(base2_int_list1) > len(base2_int_list2):
            base2_int_list2.insert(0, 0)
        elif len(base2_int_list2) > len(base2_int_list1):
            base2_int_list1.insert(0, 0)
        else:
            equal_len = True

def normalBinary(binary_list):
    """ Make list length divilsible by 4 by adding zeros to the front """
    while binary_list[0] == 0:
        binary_list.pop(0)
    while len(binary_list) % 4 != 0:
        binary_list.insert(0, 0)
    new_binary_list = []
    position = 0
    for i in binary_list:
        position = position + 1
        new_binary_list.append(i)
        if position == 1:
            pass
        elif position % 4 == 0:
            new_binary_list.append(' ')
    return new_binary_list

def typeCheck(char_list, base):
    """ Check that the number is the proper base """
    if base == 2:
        for i in char_list:
            if i == 0 or i == 1:
                proper_type = True
            else:
                proper_type = False
                break
    return proper_type

def main():
    """ Main loop """
    done = False
    while not done:
        base2_input_string1 = input("Enter the first binary number >> ")
        base2_input_list1 = stringToList(base2_input_string1)
        print(("You entered: {}").format(base2_input_string1))
        if typeCheck(base2_input_list1, 2):
            base2_input_string2 = input("Enter the second binary number >> ")
            base2_input_list2 = stringToList(base2_input_string2)
            print(("You entered: {}").format(base2_input_string2))
            if typeCheck(base2_input_list2, 2):
                equalizeLength(base2_input_list1, base2_input_list2)
                base2_list3 = normalBinary(
                    binaryAddition(base2_input_list1, base2_input_list2))
                base2_string3 = listToString(base2_list3)
                print(("{} + {} = {}").format(
                    base2_input_string1, base2_input_string2, base2_string3))
                print("\n")
            else:
                print("Error, you entered the wrong number type, start over")
                print("\n")
        else:
            print("Error, you entered the wrong number type, start over")
            print("\n")

if __name__ == "__main__":
    displayDescription()
    main()
