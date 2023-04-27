import statistics
def display_main_menu():
    print("Enter some numbers seperated by commas (e.g 5,67,32)")

def get_user_input():
    temp1 = input().split(",")
    temp2 = [int(x) for x in temp1]
    return temp2

def calc_average(temp):
    #print("calc_average")
    avg = sum(temp)/len(temp)
    print(avg)

def find_min_max(temp):
    #return min_temp, max_temp
    min_temp = min(temp)
    max_temp = max(temp)
    print(min_temp, max_temp)
def sort_temperature(temp):
    temp.sort()
    print(temp)
def calc_median_temperature(temp):
    print (statistics.median(temp))

def main():
    print("ET7035 - Introduction to DevOps for AIOT - Lab 2 - Introduction to Python")
    display_main_menu()
    temp = get_user_input()
    find_min_max(temp)
    sort_temperature(temp)
    calc_median_temperature(temp)
    calc_average(temp)
if __name__ == "__main__":
    main()
def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    bmi = weight / (height **2)
    print(bmi)


