#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    value = 0
    for i in range(0, list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            value = 0
            print("division by 0")
            continue
        except TypeError:
            value = 0
            print("wrong type")
            continue
        except IndexError:
            value = 0
            print("out of range")
            continue
        finally:
            div.append(value)
    return div
