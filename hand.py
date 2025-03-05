import functions



def reverse_string():
    if functions.reverse_string("Привет") == "тевирП":
        print("Функция string работает успешно")
    else:
        print("Тест string не прошел проверку")

def is_palindrome():
    if functions.is_palindrome("мадам"): # if defput.is_palindrome("race car") = True: - тоже работает
        print("Функция palindrome работает успешно")
    else:
        print("Тест palindrome не прошел проверку")

def count_vowels():
    if functions.count_vowels("оловянный") == 4:
        print("Функция count_vowels работает успешно")
    else:
        print("Тест count_vowels не прошел проверку")

def remove_first_occurrence():
    if functions.remove_first_occurrence("aabbcc") == "abc":
        print("Функция remove_duplicates работает успешно")
    else:
        print("Тест remove_duplicates не прошел проверку")

reverse_string()
is_palindrome()
count_vowels()
remove_first_occurrence()
