def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    bmi = weight / (height **2)
    print(bmi)
    if bmi < 18.5:
        return -1
    elif bmi <= 18.5 and bmi <= 25.0:
        return 0
    else:
        return 1

calculate_bmi(13,14)