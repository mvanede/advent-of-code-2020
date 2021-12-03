import copy

# Read input
f = open("ass-day-21-input.txt", "r")
lines = f.read().split("\n")

foods = []
for line in lines:
    ingredients, allergens =  line.split(' (')
    allergens = allergens[9:][:-1]
    foods.append({'ingredients': ingredients.split(' '), 'allergens': allergens.split(', ') })

dlist = {}
for food in foods:
    for allergen in food['allergens']:
        dlist[allergen] = food['ingredients'] if allergen not in dlist else list(set(dlist[allergen]).intersection(set(food['ingredients'])))


# Time for deduction
def round_of_deduction(dlist_):
    dlist_copy = copy.deepcopy(dlist_)
    for k, v in dlist_.items():
        if len(v) == 1:
            for e, f in dlist_copy.items():
                if k != e and v[0] in f:
                    f.remove(v[0])
    return dlist_copy


prev_list_length = sum(len(v) for k,v in dlist.items())
dlist = round_of_deduction(dlist)
while prev_list_length > sum(len(v) for k,v in dlist.items()):
    prev_list_length = sum(len(v) for k, v in dlist.items())
    dlist = round_of_deduction(dlist)


allergens = [v for v in dlist.keys()]
allergens.sort()
canonical_dangerous_ingredients = []
for a in allergens:
    canonical_dangerous_ingredients.append(dlist[a][0])

print(','.join(canonical_dangerous_ingredients))
# mfp,mgvfmvp,nhdjth,hcdchl,dvkbjh,dcvrf,bcjz,mhnrqp