def bike_charges(x):
    return(x * 10)
def car_charges(x):
    return(x * 20)

vehicle = input("Mention your vehicle type (Options Available: car and bike): ").lower()

if vehicle == 'bike':
    bike_hrs = int(input("Enter no. of hours of your 2-wheeler parking: "))
    if bike_hrs > 24:
        print("Value Error! ", end="Please Try Again! The Valid range is from 1 to 24")  
    else:
        print("You have to pay INR", bike_charges(bike_hrs))
        
elif vehicle == 'car':
    car_hrs = int(input("Enter no. of hours of your 4-wheeler parking: "))
    if car_hrs > 24:
        print("Value Error! ", end= "Please Try Again! The Valid range is from 1 to 24")  
    else:
        print("You have to pay INR", car_charges(car_hrs))
        
else:
    print("Sorry! Only car and bike parking is allowed here.")
