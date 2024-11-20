#Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
#Convert a number to a string
def number_to_string(num):
    return str(num)
print(number_to_string(2048))
#Vowel Count
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count