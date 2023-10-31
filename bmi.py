def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Height = " + str(weight))

    bmi = weight / (height * height)

    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("Underweight")
        return -1
    elif bmi >= 18.5 and bmi <= 20.5:
        print("Normal weight")
        return 0
    else:
        print("Overweight")
        return 1


calculate_bmi(weight=57, height=1.73)

