# 6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
nums = [10, 20, 30, 40]
avg = average(nums)
print(avg)