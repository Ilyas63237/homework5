immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
#immutable_var[2]='c' # кортежи относятся к неизменяемому типу данных
mtable_list= [1, 2, 'a', 'b', 'Modified']
print(mtable_list)
mtable_list[2]='c'
print(mtable_list)