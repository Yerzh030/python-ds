# TODO здесь писать код
def collect_stats(file_name):
    result = {}
    text = open(file_name,'r',encoding="utf-8")
    for i_line  in text:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] +=1
    text.close()
    return  result
file_name = "voyna-i-mir.txt"
stats = collect_stats(file_name)
print(stats)
