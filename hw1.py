import random


# .1 רשימות comprehension
#
#
alist: list[int] = [i for i in range(95, 106)]
print(alist)

# b. בשורה אחת - צור רשימה של מספרים זוגיים מ 10-20
list_even: list[int] = [i for i in range(2, 20 + 2, 2)]
print(list_even)

# # בשורה אחת - צור רשימה של 5 איברים אקראיים של False True
random_boolian = [random.choice([True, False]) for _ in range(5)]

# בשורה אחת - צור רשימה של 5 איברים אקראיים של False True
list_random: list[int] = [random.randint(1, 100) for _ in range(10)]
print(list_random)

# # בשורה אחת - מהרשימה שיצרת בסעיף הקודם, צור רשימה המכילה רק את המספרים
# # הגדולים מ- 50

list_random: list[int] = [number for number in list_random if number > 50]
print('only_positive', list_random)

# mix ???
list_random = [x for x in [random.randint(1, 100) for _ in range(10)] if x > 50]

# bonus g
sentence: str = input('Enter strings')
without_spaces_andt: list[str] = []
for letter in sentence:  # 'give me a sentence?'
    if letter != 't':
        without_spaces_andt.append(letter)
print(without_spaces_andt)
without_spaces: list[str] = [letter for letter in sentence if letter != ' t ']

# h
random_numbers_10 = [random.randint(10, 99) for _ in range(10)]
ones_digits = [x % 10 for x in random_numbers_10]
