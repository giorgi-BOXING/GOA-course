# 8) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში
def reverse_list(lst):
    return lst[::-1]
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
def reverse_list(lst):
    lst_copy = lst[:]
    lst_copy.reverse()
    return lst_copy