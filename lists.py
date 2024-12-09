immutable_war=(1,2,3, True, int)      #- кортеж может содержать в себе разные типы данных.
print(type(immutable_war))    # тип переменной указывает на тип tuple.
#immutable_war[0]=5         #- кортеж не поддерживает назначение элементов, компьютер сообщает об ошибке.
#print(immutable_war)
print(immutable_war[0])        #-из типа tuple можно вывести любой символ как в 'списке'.
mutable_list=[1,2,3, True,int]      #- в переменной создали список с разными элементами.
print(mutable_list)
mutable_list[3]= 'string'        #- для замены элемента в списке ,укажем нужный индекс
print(mutable_list)             #-третий индекс  поменял заданый элемент.