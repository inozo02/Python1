def startCalculator():
    print("------------------------------")
    print("Welcome to the easy calculator")
    print("------------------------------")
    print("Choose calculation: Sum, Subtract, Multiply, or Divide")
    operation = input().lower()

    number_list = []

    while True:
        print("\n-----------------------------------")
        user_input = input("Enter a number, or type 'done' when finished: ").lower()

        if user_input.strip() == "done":
            print("\n-----------------------------------")
            break

        try:
            number = float(user_input)
            number_list.append(number)
            print(f"Added: {number}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
            
    if not number_list:
        print("No numbers were entered for calculation.")
        print("------------------------------")
        return 
    
    if operation == "sum":
        result = 0
        print("Performing sum...")
        for number in number_list:
            result += number
            
    elif operation == "subtract" or operation == "sub":
        print("Performing subtraction...")
        result = number_list[0]
        for i in range(1, len(number_list)):
            result -= number_list[i]
            
    elif operation == "multiply" or operation == "multi":
        result = 1
        print("Performing multiplication...")
        for number in number_list:   
            result *= number
        
    elif operation == "division" or operation == "div":
        print("Performing division...")
        result = number_list[0]

        for i in range(1, len(number_list)):
            divisor = number_list[i]
            if divisor == 0:
                print("Error: Cannot divide by zero!")
                print("------------------------------")
                return
            result /= divisor
    else:
        print("Invalid operation chosen. Please choose 'Sum', 'Subtract', 'Multiply', or 'Divide'.")
        print("------------------------------")
        return
    
    print("\n------------------------------")
    print(f"Results: {result}")
    print("------------------------------")
      
startCalculator()