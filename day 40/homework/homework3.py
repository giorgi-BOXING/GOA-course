# 3) გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს პირიქით.

# Input: "helloWorld" -> Output: "Hello world"

word = input("Enter a camelCase word: ")
res = ''

for i in word:
    if i == i.upper():
        res += " " + i.lower()
    else:
        res += i

res = res.capitalize()
print(res)