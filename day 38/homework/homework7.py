# 7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და 
# დაამატებთ სიაში append() ფუნქციით. შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, ასვეე საბოლოო სია.
students = []
for i in range(3):
    name = input(f"{i+1}) შეიყვანეთ სტუდენტის სახელი: ")
    students.append(name)
students.insert(0, "Teacher")
students.pop()
print("სიის სიგრძე:", len(students))
print("საბოლოსია:", students)
