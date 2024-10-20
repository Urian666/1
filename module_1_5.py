immutable_var = 1, True, "apple"
print(immutable_var)
immutable_var[0] = 22
print(immutable_var)
# Так как кортеж не поддерживает обращение по элементам, его изменение не возможно
mutable_list = [1,2,3,4,5,6,7,8,9]
print(mutable_list)
mutable_list [0] = 10
print(mutable_list)