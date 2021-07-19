site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
def create_site(name,struct):
    if 'h2' in struct:
        struct['h2'] = 'У нас самая низкая цена на ' + name
    elif 'title' in struct:
        struct['title'] = 'Куплю/продам {} недорого'.format(name)
    for sub_struct in struct.values():
        if (isinstance(sub_struct,dict))
            create_site(name,sub_struct)


n = int(input("Сколько сайтов: "))
for  _ in range(n):
    name = input("Введите название продукта для нового сайта:")
    create_site(name,site)
