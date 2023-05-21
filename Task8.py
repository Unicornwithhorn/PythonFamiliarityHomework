# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
answer = 'no'
size = input('введите длину сторон шоколадки двумя числами через пробел: ').split(" ", 1)
size[0] = int(size[0])
size[1] = int(size[1])
resultFaultCount = int(input('введите желаемое количество долек: '))
if (resultFaultCount % size[0] == 0 and resultFaultCount / size[0] < size[1]) or (resultFaultCount % size[1] == 0 and resultFaultCount / size[1] < size[0]):
  answer = 'yes'

print(f'{size[0]} {size[1]} {resultFaultCount} -> {answer}')