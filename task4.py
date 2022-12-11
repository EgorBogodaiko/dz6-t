# https://gb.ru/lessons/281597/homework


input_file=open('for4-1.txt','r',encoding='UTF-8')
output_file=open('for4-2.txt','w',encoding='UTF-8')
output_file.writelines([(line.split('/')[2]+'\n') for line in input_file])
input_file.close
output_file.close