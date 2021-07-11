students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for id,student in dict.items():
        lst += student['interests']
        string += student['surname']
    return lst, len(string)


pairs = []
for  id,student in students.items():
    print(id,student["age"])

my_lst, l = f(students)

print(my_lst, l)

# TODO исправить код
