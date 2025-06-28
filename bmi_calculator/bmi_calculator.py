def convert_units(feet, inches, weight_lbs):
    total_inches = feet * 12 + inches
    height_cm = total_inches * 2.54
    weight_kg = weight_lbs * 0.453592
    return height_cm, weight_kg

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
