# 2) იგივე სიაში მე-3 და მე-4 ელემენტებს შორის ჩასვით თქვენი სახელი. მე-5 ინდექსზე ჩაამატეთ თქვენი ასაკი. სიის თავში ჩაამატეთ თქვენი სიმაღლე.
# სიის ბოლოში კი თქვემი საყვარელი რიცხვი. საბოლოოდ დაბეჭდეთ ეს სია
my_list = [3, 7, 12, 5]
my_name = "გიორგი"
my_age = 9
my_height = 28
favorite_number = 9
my_list.insert(my_name)
my_list.insert(9, my_age)
my_list.insert(28, my_height)
my_list.append(9, favorite_number)
print(my_list)