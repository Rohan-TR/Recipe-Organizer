# Recipe organizer using dictionaries
recipes = {}

# Function to add a recipe
def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter instructions: ")
    recipes[name] = {
        'ingredients': ingredients,
        'instructions': instructions
    }
    print(f"Recipe '{name}' added successfully!")

# Function to delete a recipe
def delete_recipe():
    name = input("Enter recipe name to delete: ")
    if name in recipes:
        del recipes[name]
        print(f"Recipe '{name}' deleted successfully!")
    else:
        print(f"Recipe '{name}' not found.")

# Function to display all recipes
def display_recipes():
    if recipes:
        print("All Recipes:")
        for name, recipe in recipes.items():
            print(f"Recipe: {name}")
            print("Ingredients:", ', '.join(recipe['ingredients']))
            print("Instructions:", recipe['instructions'])
            print()
    else:
        print("No recipes found.")

# Function to search for a recipe by name
def search_recipe():
    name = input("Enter recipe name to search: ")
    if name in recipes:
        recipe = recipes[name]
        print(f"Recipe: {name}")
        print("Ingredients:", ', '.join(recipe['ingredients']))
        print("Instructions:", recipe['instructions'])
    else:
        print(f"Recipe '{name}' not found.")

# Main menu loop
def main_menu():
    while True:
        print("\nRecipe Organizer Menu:")
        print("1. Add Recipe")
        print("2. Delete Recipe")
        print("3. Display All Recipes")
        print("4. Search Recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            delete_recipe()
        elif choice == '3':
            display_recipes()
        elif choice == '4':
            search_recipe()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main menu
if name == "main":
    main_menu()