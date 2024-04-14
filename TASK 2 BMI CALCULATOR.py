import matplotlib.pyplot as plt

class BMIUser:
    def __init__(self, name):
        self.name = name
        self.weights = []
        self.heights = []

    def add_record(self, weight, height):
        self.weights.append(weight)
        self.heights.append(height)


def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    """
    Classify BMI into categories based on predefined ranges.
    """
    categories = {
        (0, 18.5): "Underweight",
        (18.5, 25): "Normal weight",
        (25, 30): "Overweight",
        (30, float('inf')): "Obese"
    }
    
    for (lower, upper), category in categories.items():
        if lower <= bmi < upper:
            return category


def plot_bmi_trend(user):
    """
    Plot BMI trend over time for a user.
    """
    if not user.weights:
        print("No records found for this user.")
        return
    
    bmis = [calculate_bmi(w, h) for w, h in zip(user.weights, user.heights)]
    plt.plot(range(1, len(bmis) + 1), bmis, marker='o')
    plt.title(f"{user.name}'s BMI Trend")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()


def main():
    users = {}

    while True:
        try:
            print("\n1. Add User")
            print("2. Calculate BMI")
            print("3. Plot BMI Trend")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter user's name: ")
                users[name] = BMIUser(name)
                print(f"User {name} added successfully.")

            elif choice == 2:
                name = input("Enter user's name: ")
                if name not in users:
                    print("User not found. Please add the user first.")
                    continue

                weight = float(input("Enter weight in kilograms: "))
                height = float(input("Enter height in meters: "))

                if weight <= 0 or height <= 0:
                    print("Weight and height must be positive numbers.")
                    continue

                users[name].add_record(weight, height)
                bmi = calculate_bmi(weight, height)
                category = classify_bmi(bmi)
                print(f"User: {name}, BMI: {bmi:.2f}, Category: {category}")

            elif choice == 3:
                name = input("Enter user's name: ")
                if name not in users:
                    print("User not found.")
                    continue

                plot_bmi_trend(users[name])

            elif choice == 4:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
