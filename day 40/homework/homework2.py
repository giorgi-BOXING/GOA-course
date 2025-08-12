# 2) შექმენით 5 ელემენტიანი სიტყვების სია. მომხმარებელს შემოატანინეთ სიტყვა და რიცხვი(ეს იქნება პოზიცია სადაც დაამატებთ შემოტანილ სიტყვას). დაბეჭდეთ განახლებული სია.

word_list = ["Lion", "Dog", "Cat", "Elephant", "Tiger"]

new_word = input("Enter new word: ")

position = int(input("Enter a position number: "))

word_list.insert(position, new_word)

print(word_list)