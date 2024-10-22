from db_connection import DBConnection, initialize
from operations import (
    insert_flavor,
    display_flavors,
    remove_flavor,
    insert_ingredient,
    display_ingredients,
    remove_ingredient,
    insert_suggestion,
    display_suggestions,
    remove_suggestion
)


def main():

    db_location = '/yourPath/yourDatabase.db'
    with DBConnection(db_location) as connection:
        initialize(connection)  # Create tables and setup

    while True:
        print("\nWelcome to the Chocolate Shop Management!")
        print("1. Add New Flavor")
        print("2. Show All Flavors")
        print("3. Delete a Flavor")
        print("4. Add New Ingredient")
        print("5. Show Ingredient List")
        print("6. Delete an Ingredient")
        print("7. Add Customer Suggestion")
        print("8. View Customer Suggestions")
        print("9. Remove a Suggestion")
        print("10. Exit")

        option = input("Please select an option: ")

        if option == '1':
            flavor_name = input("Enter the flavor name: ")
            is_seasonal = input(
                "Is it a seasonal flavor? (yes/no): ").lower() == 'yes'
            insert_flavor(flavor_name, is_seasonal)
            print("New flavor added successfully.")

        elif option == '2':
            all_flavors = display_flavors()
            print("Available Flavors:", all_flavors)

        elif option == '3':
            delete_flavor_id = int(
                input("Enter the ID of the flavor to delete: "))
            remove_flavor(delete_flavor_id)
            print("Flavor removed successfully.")

        elif option == '4':
            ingredient_name = input("Enter the ingredient name: ")
            stock_amount = int(input("Enter the quantity available: "))
            insert_ingredient(ingredient_name, stock_amount)
            print("New ingredient added.")

        elif option == '5':
            all_ingredients = display_ingredients()
            print("Ingredient Inventory:", all_ingredients)

        elif option == '6':
            delete_ingredient_id = int(
                input("Enter the ID of the ingredient to remove: "))
            remove_ingredient(delete_ingredient_id)
            print("Ingredient removed successfully.")

        elif option == '7':
            customer_name = input("Enter your name: ")
            suggested_flavor = input("Enter the flavor suggestion: ")
            allergy_note = input("Mention any allergy concerns: ")
            insert_suggestion(customer_name, suggested_flavor, allergy_note)
            print("Customer suggestion recorded.")

        elif option == '8':
            all_suggestions = display_suggestions()
            print("Customer Suggestions:", all_suggestions)

        elif option == '9':
            delete_suggestion_id = int(
                input("Enter the ID of the suggestion to remove: "))
            remove_suggestion(delete_suggestion_id)
            print("Suggestion removed.")

        elif option == '10':
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    main()
