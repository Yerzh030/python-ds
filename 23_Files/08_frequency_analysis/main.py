# TODO здесь писать код
def collect_stats(file_name):
    result = {}
    text = open(file_name,'r',encoding="utf-8")
    sum = 0
    for i_line  in text:
        for j_char in i_line:
            if j_char.lower() in 'qwertyuiopasdfghjklmnbvcxz' :
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] +=1
                sum +=1
    text.close()
    for key in result.keys():
        result[key] = result[key] / sum
    return  result
file_name = "text.txt"
stats = collect_stats(file_name)
for key,value in stats.items():
    print(key," " ,value)
