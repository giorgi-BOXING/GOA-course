# 6) შექმენით ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს, არის თუ არა ეს სიტყვა პალინდრომი. როგორი სიტყვებია პალინდრომი, შეგიძლიათ გაეცნოთ ქვემოთ დართულ წყაროში:
def is_palindrome(word):
  
    word = word.lower()
   
    return word == word[::-1]

print(is_palindrome("მანამ"))   
print(is_palindrome("რესტორანი"))  
print(is_palindrome("Radar"))