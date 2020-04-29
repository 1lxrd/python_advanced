new_dict = {'Germany': 'Berlin', 'Italy': 'Rome', 'Spain': 'Madrid', 'France': 'Paris'}
new_list = ['Germany', 'USA', 'Spain', 'Ukraine']

for i in new_list:
    if i in new_dict:
        print(new_dict.get(i))
