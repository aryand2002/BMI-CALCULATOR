from bmi_calculator import calculate_bmi, categorize_bmi, convert_units
from analytics import show_analytics, export_to_csv
import os

users = []

def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    unit = input("Choose unit system - Metric (M) or Imperial (I): ").strip().upper()

    if unit == 'M':
        height_cm = float(input("Enter height in cm: "))
        weight_kg = float(input("Enter weight in kg: "))
    elif unit == 'I':
        feet = int(input("Enter height - feet: "))
        inches = int(input("Enter height - inches: "))
        weight_lbs = float(input("Enter weight in lbs: "))
        height_cm, weight_kg = convert_units(feet, inches, weight_lbs)
    else:
        print("❌ Invalid unit system.")
        return None

    bmi = calculate_bmi(height_cm, weight_kg)
    category = categorize_bmi(bmi)

    return {
        "name": name,
        "age": age,
        "height_cm": round(height_cm, 2),
        "weight_kg": round(weight_kg, 2),
        "bmi": round(bmi, 2),
        "category": category
    }

def main():
    print("\n📊 Welcome to the BMI Calculator App\n")

    while True:
        user_data = get_user_input()
        if user_data:
            users.append(user_data)
        cont = input("Add another user? (Y/N): ").strip().upper()
        if cont != 'Y':
            break

    print("\n=== 📈 BMI Analytics ===\n")
    show_analytics(users)
    export_to_csv(users)
    print("\n✅ Data exported to `data/users.csv`")

if __name__ == "__main__":
    main()
