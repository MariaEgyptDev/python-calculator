"""
Python Calculator
By Maria - First GitHub Project
"""

def display_menu():
    print("╔══════════════════════════════╗")
    print("║     🧮 PYTHON CALCULATOR     ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Addition (+)              ║")
    print("║ 2. Subtraction (-)           ║")
    print("║ 3. Multiplication (*)        ║")
    print("║ 4. Division (/)              ║")
    print("║ 5. Exit                      ║")
    print("╚══════════════════════════════╝")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
    print("\n🌟 Welcome to Python Calculator! 🌟")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nChoose operation (1-5): ")
            
            if choice == '5':
                print("\n👋 Thank you for using Python Calculator!")
                print("   Goodbye! 💫")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("❌ Please enter a number between 1 and 5")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"\n✅ Result: {num1} + {num2} = {result}")
                
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n✅ Result: {num1} - {num2} = {result}")
                
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n✅ Result: {num1} × {num2} = {result}")
                
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(f"\n❌ {result}")
                else:
                    print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
            
            print("\n" + "="*40)
            
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Program stopped by user")
            break

if __name__ == "__main__":
    main()