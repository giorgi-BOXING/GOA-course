# 5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია
def is_even(num):
    if num % 2 == 0:
        return "the number is even"
    else:
        return "the number is odd"
print(is_even(15))