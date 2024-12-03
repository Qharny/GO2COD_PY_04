def get_valid_float_input(prompt):
    """
    Safely collect and validate float input from the user.
    
    Args:
        prompt (str): The input prompt for the user
    
    Returns:
        float: A valid positive numeric input
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (kg) and height (m).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: Calculated BMI
    """
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """
    Categorize BMI into standard weight categories.
    
    Args:
        bmi (float): Calculated Body Mass Index
    
    Returns:
        str: BMI category description
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to run the BMI calculator.
    """
    print("=== BMI Calculator ===")
    
    # Collect height (in meters)
    height = get_valid_float_input("Enter your height in meters (e.g., 1.75): ")
    
    # Collect weight (in kg)
    weight = get_valid_float_input("Enter your weight in kilograms (e.g., 70): ")
    
    # Calculate BMI
    try:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        # Display results
        print(f"\n--- Results ---")
        print(f"Height: {height:.2f} m")
        print(f"Weight: {weight:.2f} kg")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()