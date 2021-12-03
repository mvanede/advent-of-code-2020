from pprint import pprint
import itertools

# Read input
f = open("ass-day-21-input.txt", "r")
lines = f.read().split("\n")

foods = []
for line in lines:
    ingredients, allergens =  line.split(' (')
    allergens = allergens[9:][:-1]
    foods.append({'ingredients': ingredients.split(' '), 'allergens': allergens.split(', ')})

dlist = {}
for food in foods:
    for allergen in food['allergens']:
        if allergen not in dlist:
            dlist[allergen] = food['ingredients']
        else:
            dlist[allergen] = list(set(dlist[allergen]).intersection(set(food['ingredients'])))

all_ingredients_unique = set(itertools.chain.from_iterable([x['ingredients'] for x in foods]))
all_ingredients = list(itertools.chain.from_iterable([x['ingredients'] for x in foods]))
ingredients_with_possible_allergens_unique = set(itertools.chain.from_iterable(dlist.values()))
ingredients_with_no_allergens = all_ingredients_unique.difference(ingredients_with_possible_allergens_unique)

print(all_ingredients_unique)
print(ingredients_with_possible_allergens_unique)
print(ingredients_with_no_allergens)

# Count total number of occurences of ingredients with no allergens
cnt = 0
for i in ingredients_with_no_allergens:
    cnt += all_ingredients.count(i)

print(cnt)
#2412