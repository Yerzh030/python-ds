# TODO здесь писать код
site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
def find_key(struct,key,h):

    if key in struct :
        return struct[key]
    for sub_struct in struct.values():
        if (isinstance(sub_struct,dict)) and h > 1:
            result  =find_key(sub_struct,key,h - 1)
            if result:
                break
    else:
        result = None
    return  result


user_key = input("Какой ключ Вам нужен?")
user_h = int(input("Максимальная глубина:"))

value = find_key(site,user_key,user_h)
if value:
    print(value)
else:
    print("Такого ключа нет")