# BMI calculator 
    
# This fuction take users height and weight as an input and also prints the answer
def value_input():
    weight=float(input("enter your weight in kg:"))
    height=float(input("enter your height in meter's:"))
    bmi=calc_BMI(weight,height)
    category=BMI_category(bmi)
    print(f"your bmi is:{bmi}")
    print(category)

# This function performs calculations on the user inputs(height and weight) and calculate's the BMI
def calc_BMI(weight,height):
    bmi= weight / (height ** 2)
    return bmi
# This fuction provides the category of the user as per the BMI 
def BMI_category(bmi):
    if bmi<18.5:
        return "you are under weight "
    elif 18.5<=bmi<=24.9: 
        return "you are normal"
    elif 25<=bmi<29.9:
        return "you are overweight"
    else :
        return "you are obese"

# Calling function for the operation 
value_input()


    