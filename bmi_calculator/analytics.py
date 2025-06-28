from statistics import mean
from collections import Counter
import csv
import os

def show_analytics(users):
    bmis = [u["bmi"] for u in users]
    categories = [u["category"] for u in users]

    print(f"Average BMI: {round(mean(bmis), 2)}")
    print(f"Highest BMI: {max(bmis)}")
    print(f"Lowest BMI: {min(bmis)}\n")

    counts = Counter(categories)
    total = len(users)

    print("Category-wise Count & Percentage:")
    for cat, count in counts.items():
        print(f"{cat}: {count} user(s) - {(count/total)*100:.2f}%")

def export_to_csv(users):
    # Ensure `mydata` folder exists inside current directory
    folder_path = os.path.join(os.path.dirname(__file__), "mydata")
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "users.csv")

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)
