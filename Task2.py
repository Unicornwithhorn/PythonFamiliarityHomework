#  Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

import random
a = random.randint(100,999)
print("Число {}. Сумма цифр в числе {} (= {} + {} + {})".format(a, a//100 + a%100//10 + a%10, a//100, a%100//10, a%10))