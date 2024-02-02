def bmiweight(Height, Weight):
    Height = (Height)*12
    Weight = (Weight)*2.20462
    BMI = ((Weight / (Height) ** 2))*703
    BMI = round(BMI,2)
    if BMI <= 18.5:
        return(str(BMI) + "\n" + " Underweight")
    elif (BMI >= 18.5) and (BMI <= 24.9):
        return(str(BMI) + "\n" +" Normal")
    elif (BMI >= 25.0) and (BMI <= 29.9):
        return(str(BMI) + "\n" +" Overweight")
    elif (BMI >=30.0):
        return(str(BMI) + "\n" +  " Obese")
# print(bmiweight(2.7,25))