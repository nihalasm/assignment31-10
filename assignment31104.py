def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()

def middle(lst):
    if len(lst) >= 3:
        return lst[1:-1]
    else:
        return []
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

chop(my_list)
print("After chop:", my_list)

my_list = [1, 2, 3, 4, 5]
new_list = middle(my_list)
print("New List after middle:",new_list)