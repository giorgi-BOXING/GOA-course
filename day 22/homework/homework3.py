# 3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ for loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში 
# შეინახავთ ჯამს, მეორეში რაოდენობას)
jami=0
raodenoba=0
for i in range(2,100,2):
    jami+=i
    raodenoba+=1

sashualo=jami//raodenoba
print(sashualo)
