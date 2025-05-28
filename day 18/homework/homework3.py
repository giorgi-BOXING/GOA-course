# 3) მოხმარებელს შემოატანინეთ გამოცდის ქულა და შეინახეთ score ცვლადში ინტეჯერად, თუ ქულა მეტია 70-ზე დაუბეჭდეთ რომ გამოცდა გადალახა
# "passed" სხვა შემთხვევაში კი რომ ჩაიჭრა "failed"
score=int(input("enter score"))
if score > 80:
    print("A")
elif score > 60:
    print("B")

elif score > 40:
    print("C")

elif score > 20:
    print("D")

else:
    print("F")