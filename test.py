#calculator easy


def startCalculator():
    print("Choose calculation: Sum")
    operation= input()
    if operation =="sum":
        
        total_sum=0
    
    while True:
        user_input= input("Enter a number, or write done")
        
        if user_input =="done":
            break
        try:
            user_input=float(user_input)
            total_sum+= user_input
            print(f"Number is: {user_input}")
        except:
            print("invalid number")    
    print(f"Total sum is: {total_sum}")      
    
      
startCalculator()