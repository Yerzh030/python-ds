# TODO здесь писать код
word = input("Введите слово: ")
word_list = list(word)
reversed_word = ""
for i in range(len(word_list)-1, -1,-1):
    reversed_word = reversed_word + word_list[i]
if reversed_word == word:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")