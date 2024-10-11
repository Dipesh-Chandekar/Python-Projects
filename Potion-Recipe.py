# Initial potion ingredients
potion_ingredients = {
    "unicorn_hair": 3,
    "dragon_scale": 5,
    "phoenix_feather": 2,
    "mandrake_root": 7,
    "nightshade": 1
}

print("Initial Potion Recipe:", potion_ingredients)

# Add a new ingredient
potion_ingredients["fairy_dust"] = 4

# Double the quantity of "phoenix_feather"
potion_ingredients["phoenix_feather"] *= 2

# Remove the cursed ingredient "nightshade"
del potion_ingredients["nightshade"]

# Print the updated potion recipe
print("Updated Potion Recipe:", potion_ingredients)
