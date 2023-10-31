def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def calc_average_temperature(res):
    average = sum(res) / len(res)
    print("Average = " + str(average))
    return
def calc_min_max_temperature(res):
    print("Min value = " + str(min(res)))
    print("Max value = " + str(max(res)))
    return
def get_user_input():
    x = input("Numbers : ")
    x = x.split(",")
    res = list(map(float, x))
    return res

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    res = get_user_input()
    calc_average_temperature(res)
    calc_min_max_temperature(res)

if __name__ == "__main__":
    main()