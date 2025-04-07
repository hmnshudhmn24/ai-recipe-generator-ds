import random

# Sample recipe database
RECIPE_DB = {
    "pasta": {
        "ingredients": ["pasta", "tomato", "garlic", "onion", "olive oil"],
        "steps": [
            "Boil water and cook pasta.",
            "Heat olive oil in a pan.",
            "Sauté garlic and onion until golden.",
            "Add chopped tomatoes and cook into a sauce.",
            "Mix in the pasta and serve hot."
        ]
    },
    "omelette": {
        "ingredients": ["egg", "salt", "pepper", "onion", "tomato"],
        "steps": [
            "Crack eggs into a bowl and beat well.",
            "Add chopped onion and tomato.",
            "Season with salt and pepper.",
            "Pour into a hot pan and cook until set.",
            "Fold and serve."
        ]
    },
    "fried rice": {
        "ingredients": ["rice", "egg", "soy sauce", "vegetables", "onion"],
        "steps": [
            "Heat oil in a pan.",
            "Add chopped vegetables and stir fry.",
            "Push veggies to the side, scramble eggs in the same pan.",
            "Add cooked rice and soy sauce.",
            "Mix everything well and serve hot."
        ]
    }
}

# Function to find matching recipes
def suggest_recipes(available_ingredients):
    suggestions = []
    for recipe, details in RECIPE_DB.items():
        if all(item in available_ingredients for item in details["ingredients"]):
            suggestions.append(recipe)
        elif any(item in available_ingredients for item in details["ingredients"]):
            suggestions.append(recipe + " (partial match)")
    return suggestions

# Function to show recipe steps
def show_recipe(recipe_name):
    base_name = recipe_name.replace(" (partial match)", "")
    recipe = RECIPE_DB.get(base_name)
    if recipe:
        print(f"\nRecipe for {base_name.capitalize()}:")
        print("Ingredients:", ", ".join(recipe["ingredients"]))
        print("Steps:")
        for i, step in enumerate(recipe["steps"], 1):
            print(f"{i}. {step}")
    else:
        print("Recipe not found.")

# Main function
def main():
    print("=== AI-Powered Recipe Generator ===")
    ingredients = input("Enter available ingredients (comma-separated): ").lower().split(",")
    ingredients = [ing.strip() for ing in ingredients]
    
    matches = suggest_recipes(ingredients)
    if matches:
        print("\nRecipes you can try:")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match}")
        
        choice = input("\nEnter the recipe name to view steps or 'exit' to quit: ").strip().lower()
        if choice != "exit":
            show_recipe(choice)
    else:
        print("Sorry, no recipes found with the given ingredients.")

if __name__ == "__main__":
    main()
