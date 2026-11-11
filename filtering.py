from pydoc_data import module_docs

import numpy as np

#Filtering = refers to the process of selecting elements
#            from an array that match a given condition

# ages = np.array([[12,23,33,44,55,62,72,82,92],
#                  [32,43,23,64,55,52,32,22,52]])

#filter teenagers
# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18 ) & (ages <= 45)]
# seniors = ages[ages >= 65]
# evens = ages[ages % 2 == 0]
# odd = ages[ages % 2 != 0]
#
# print(teenagers)
# print(adults)
# print(seniors)
# print(evens)
# print(odd)

ages = np.array([[12,23,33,44,55,62,72,82,92]])

adults = np.where(ages >= 18, ages, 0)

print(adults)