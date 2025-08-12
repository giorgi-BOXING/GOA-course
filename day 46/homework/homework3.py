# 3) შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიაში უდიდეს რიცხვს.n
def max_in_list(numbers):
    if not numbers:  
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
nums = [5, 12, 7, 3, 20]
print(max_in_list(nums))