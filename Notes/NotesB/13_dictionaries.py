# dictionaries

# list, tuple, int, float, bool, str, set and dict

# sets (not generally used often)
# a unique list of items (no items)
# use {} instead of []
import random

my_set ={1, 2, 3, 4, 4, 5}
print(my_set)
my_list = ['milk', 'toilet paper', 'yeast', 'blackberries', 'milk']
print(set(my_list))
print(my_list)
print(type(my_list))

# can add and subtract sets and not have duplicates

# dictionaries
mia = [16, 'English', 'Python', 'Wichman']
mia = {'age': 16, 'spoken languages': ['English', 'French'], 'favorite coding language': 'Python', 'last name': 'Wichman'}
print(mia)

community = {'genre': 'Comedy',
             'created by': 'Dan Harmon',
             'starring': ['Joel McHale', 'Gillian Jacobs', 'Danny Pudi', 'Yvette Nicole Brown', 'Alison Brie', 'Donald Glover', 'Chevy Chase'],
             'opening theme': 'At Least It Was Here'
             }
print('opening theme')

# add to a dictionary
community['number of seasons'] = 6
community['number of episodes'] = 110
print(community)

# add to value
print()
community['starring'].append('Ken Jeong')
print(community)

# keys?
print()
print(community.keys())  # iterable dict_key object

HIMYM = {'genre': ['Sitcom', 'Romantic Comedy'],
         'created by': ['Carter Bays', 'Craig Thomas'],
         'starring': ['Josh Radnor', 'Jason Segel', 'Cobie Smulders', 'Neil Patrick Harris', 'Alyson Hannigan', 'Cristin Millioti'],
         'opening theme': 'Hey, Beautiful',
         'number of seasons': 9,
         'number of episodes': 208}

shows = [community, HIMYM]

flips = [random.choice(['heads', 'tails']) for x in range(100)]

head_tails = {}

for flip in flips:
    if flip == 'heads':
        if flip == head_tails:
            head_tails['heads'] += 1
        else:
            head_tails['heads'] = 1
    if flip == 'tails':
        if flip == head_tails:
            head_tails['tails'] += 1
        else:
            head_tails['tails'] = 1

print(head_tails)

