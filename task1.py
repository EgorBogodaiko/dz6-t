# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
input_list=["йцу", "фыв", "ячс", "цук", "йцукен"]
print('список: ', input_list, 'ищем: ', input_list[0])
index=-1
try:
    index=input_list.index(input_list[0],2,)
except   ValueError: 
    index=-1
print('Ответ: ', index )
