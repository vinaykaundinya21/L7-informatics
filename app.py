import streamlit as st
from functions import (
    add_flavor,
    view_flavors,
    delete_flavor,
    add_ingredient,
    view_ingredients,
    delete_ingredient,
    add_suggestion,
    view_suggestions,
    delete_suggestion
)


def main():
    # Title of the app
    st.title("Chocolate House")

    # Sidebar navigation
    st.sidebar.header("Navigation")
    options = ["Add Flavor", "View Flavors", "Delete Flavor", "Add Ingredient", "View Ingredients",
               "Delete Ingredient", "Add Suggestion", "View Suggestions", "Delete Suggestion"]
    choice = st.sidebar.selectbox("Select an option", options)

    # Add Flavor
    if choice == "Add Flavor":
        st.subheader("Add a New Flavor")
        name = st.text_input("Flavor Name")
        seasonal = st.selectbox("Is it seasonal?", ["Yes", "No"])

        if st.button("Add Flavor"):
            add_flavor(name, seasonal == "Yes")
            st.success(f"Flavor '{name}' added successfully!")

    # View Flavors
    elif choice == "View Flavors":
        st.subheader("Available Flavors")
        flavors = view_flavors()
        for flavor in flavors:
            st.write(
                f"ID: {flavor[0]}, Name: {flavor[1]}, Seasonal: {'Yes' if flavor[2] else 'No'}")

    # Delete Flavor
    elif choice == "Delete Flavor":
        st.subheader("Delete a Flavor")
        flavor_id = st.number_input("Flavor ID", min_value=1)

        if st.button("Delete Flavor"):
            delete_flavor(flavor_id)
            st.success(f"Flavor with ID '{flavor_id}' deleted successfully!")

    # Add Ingredient
    elif choice == "Add Ingredient":
        st.subheader("Add a New Ingredient")
        name = st.text_input("Ingredient Name")
        quantity = st.number_input("Quantity", min_value=1)

        if st.button("Add Ingredient"):
            add_ingredient(name, quantity)
            st.success(f"Ingredient '{name}' added successfully!")

    # View Ingredients
    elif choice == "View Ingredients":
        st.subheader("Available Ingredients")
        ingredients = view_ingredients()
        for ingredient in ingredients:
            st.write(
                f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}")

    # Delete Ingredient
    elif choice == "Delete Ingredient":
        st.subheader("Delete an Ingredient")
        ingredient_id = st.number_input("Ingredient ID", min_value=1)

        if st.button("Delete Ingredient"):
            delete_ingredient(ingredient_id)
            st.success(
                f"Ingredient with ID '{ingredient_id}' deleted successfully!")

    # Add Suggestion
    elif choice == "Add Suggestion":
        st.subheader("Submit a Flavor Suggestion")
        customer_name = st.text_input("Your Name")
        flavor_suggestion = st.text_input("Flavor Suggestion")
        allergy_concern = st.text_input("Allergy Concern")

        if st.button("Submit Suggestion"):
            add_suggestion(customer_name, flavor_suggestion, allergy_concern)
            st.success("Suggestion submitted successfully!")

    # View Suggestions
    elif choice == "View Suggestions":
        st.subheader("Customer Suggestions")
        suggestions = view_suggestions()
        for suggestion in suggestions:
            st.write(
                f"ID: {suggestion[0]}, Customer: {suggestion[1]}, Suggestion: {suggestion[2]}, Allergy Concern: {suggestion[3]}")

    # Delete Suggestion
    elif choice == "Delete Suggestion":
        st.subheader("Delete a Suggestion")
        suggestion_id = st.number_input("Suggestion ID", min_value=1)

        if st.button("Delete Suggestion"):
            delete_suggestion(suggestion_id)
            st.success(
                f"Suggestion with ID '{suggestion_id}' deleted successfully!")


if __name__ == "__main__":
    main()
