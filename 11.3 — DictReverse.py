# Дан словарь ключами которого являются английские слова, а значениями - списки латинских слов. 
# Необходимо развеннуть словарь. Другими словани, необходимо, на основании заданного словаря, 
# создать новый словарь, у которого в качестве ключей будут взяты латинские слова, из первого словаря, 
# а значениями будут, соответствующие им, английские слова.

from pprint import pprint

dct = {
    	'apple': ['malum', 'pomum', 'popula'],
    	'fruit': ['baca', 'bacca', 'popum'],
    	'punishment': ['malum', 'multa']
}

n_dct = {}
for key in dct:
    for value in dct[key]:
        if value not in n_dct:
        	n_dct[value] = key
        else:
            n_dct[value] = n_dct[value] + ' ' + key

pprint(n_dct)


# Value is list version

# n_dct = {}
# for key in dct:
#     for value in dct[key]:
#         if value in n_dct:
#             if type(n_dct[value]) == str:
#                 temp_lst = list()
#                 temp_lst.append(n_dct[value])
#                 n_dct[value] = temp_lst
#             n_dct[value].append(key)
#         else:
#             n_dct[value] = key