# TODO здесь писать код
file = input("Название файла:")
if (file.startswith("@")  or file.startswith("(") or file.startswith(")")
or file.startswith("&") or file.startswith("^") or file.startswith("%") or file.startswith("$") or file.startswith("№")):
    print("Ошибка: название начинается на один из специальных символо")
elif not  file.endswith(".docx") or file.endswith(".txt"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")
