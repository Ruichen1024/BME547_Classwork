def interface():
    print("Blood test analysis")
    while True:
        print("\nOptions")
        print("1-HDL")
        print("9-Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()

def HDL_driver():
    # Get data
    data = get_data()
    # Analyze data
    result = analyze_data(data)
    # Output data
    output_data(data, result)


def get_data():
    data = input("Enter the HDL level: ")
    return data

def analyze_data(d):
    d = int(d)
    if d>=60:
        return "Normal"
    elif d>=40 and d<60:
        return "Borderline low"
    else:
        return "Low"

def output_data(a, b):
    a = int(a)
    print("Your HDL level is %d\n"%a)
    print("This level is %s\n"%b)


interface()
