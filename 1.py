# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

# пример - 8 11 0 -23 140 1 => 11 -23

string_num=input("Введите числа через пробел: ").split()
print(string_num)
string_num=filter(lambda i: len(str(abs(int(i))))==2,string_num)
string_num=list(string_num)
print(string_num)


# Или более кратко
# string_num=list(filter(lambda i: len(abs(i))==2,input("Введите числа через пробел: ").split()))
# print(string_num)

# ДРугой вариант решения ? не работает?
# string_num=list(map(input("Введите числа через пробел: ").split()))