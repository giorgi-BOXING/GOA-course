# 1) შექმენით 3 ელემენტიანი სახელების სია. მომხმარებელს შემოატანინეთ 0-დან 2-ის ჩათვლით ნებისმიერი რიცხვი, სანამ მომხმარებელი არ შემოიტანს
# რიცხვს საჭირო დიაპაზონში, ხელახლა ვთხოვოთ რიცხვის შემოტანა.(გამოიყენეთ while loop-ი)

# დაბეჭდეთ სახელების სიაში მომხმარებლის მიერ შემოტანილ ინდექსზე მყოფი ელემენტი
#          0        1        2
names = ["Nika", "Luka", "Giorgi"]

index = int(input("Please enter a number(0-2): "))

while index < 0 or index > 2:
    print("The number out of range")
    index = int(input("Please enter a number(0-2): "))

print(names[index])
