# являнтся ли полиндромом с помощью рекурсии

# def Is_palindrom(word, k = 0):
#     if word[k] != word[-(k + 1)]:
#         return False
#     else:
#         if k == len(word) // 2 + 1:
#             return True
#         else:
#             return Is_palindrom(word, k + 1)
# print(Is_palindrom('kazak'))

# второй вариант срезом

def is_palindrome(word):
    if len(word) == 0:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

word = input("Введите слово: ")
result = is_palindrome(word.lower())

if result:
    print(f"{word} - палиндром.")
else:
    print(f"{word} - не палиндром.")