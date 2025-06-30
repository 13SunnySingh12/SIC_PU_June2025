# Find sum of list elements(Using recursion)

def sum_of_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])
    
number_list = list(map(int, input("Enter the numbers:").split()))
print(number_list)

print("sum of the list of elements are:", sum_of_list(number_list))
