# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python


def cakes(recipe, available):
    common_keys = recipe.keys() & available.keys()
    results = [available[ingredient] // recipe[ingredient] for ingredient in common_keys]
    if 0 in results or not set(recipe).issubset(available):
        return 0
    else:
        return min(results)


print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
