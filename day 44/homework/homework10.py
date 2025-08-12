# 10) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს
def max_of_two(a, b):
    return max(a, b)
print(max_of_two(10, 25))  
print(max_of_two(100, 42))  
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b