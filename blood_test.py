def interface():
    print("Blood test analysis")
    while True:
        print("\nOptions")
        print("1-HDL")
        print("2-Total cholesterol")
        print("9-Quit")
        choice = input("Enter an option: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            TC_driver()

def HDL_driver():
    # Get data
    data = get_HDLdata()
    # Analyze data
    result = analyze_HDLdata(data)
    # Output data
    output_HDLdata(data, result)


def get_HDLdata():
    data = input("Enter the HDL level: ")
    return int(data)

def analyze_HDLdata(d):
    if d>=60:
        return "Normal"
    elif d>=40 and d<60:
        return "Borderline low"
    else:
        return "Low"

def output_HDLdata(a, b):
    print("Your HDL level is %d\n"%a)
    print("This level is %s\n"%b)

def TC_driver():
    # Get Data
    data = get_TCdata()
    # Analyze data
    result = analyze_TCdata(data)
    # Output data
    output_TCdata(data, result)

def get_TCdata():
    data = input("Enter the Total cholesterol level: ")
    return int(data)

def analyze_TCdata(d):
    if d<200:
        return "Normal"
    elif 200<=d<=239:
        return "Borderline high"
    else:
        return "high"

def output_TCdata(a, b):
    print("Your Total cholesterol level is %d\n"%a)
    print("This level is %s\n"%b)

interface()
