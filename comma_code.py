


def my_list_to_string(l):
    my_string = ""
    for i in range(len(l)):
        if i == len(l) - 1:
            my_string += "and " + l[i]
        else:
            my_string += l[i] + ", "

    return my_string


my_list = []
print("Add something to your new list, you can leave it blank to end the loop.")
while True:
    item = input(str(len(my_list) + 1) + ": " )
    #In case of a mistyped space(Yes, I may have done it.)
    if item.replace(" ", "") == "":
        if len(my_list) <= 1:
            print("We'll need at least two items to start with.")
            continue
        else:
            break
    my_list.append(item)

print() #New blank line
print("You have entered:")
print(my_list_to_string(my_list) + ".")