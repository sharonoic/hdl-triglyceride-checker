def ask_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").lower()
        if ans in ["y", "n"]:
            return ans
        else:
            print("Please input 'y' or 'n'.")

def enter_value(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def hdl_cal():
    ans = ask_yes_no("Input HDL in mmol/L? y/n")
    if ans == "y":
        hdl_mol = enter_value("Enter HDL in mmol/L: ")
        return hdl_mol * 38.67
    else:
        return enter_value("Enter HDL in mg/dL: ")
       


def tri_cal():
    ans = ask_yes_no("Input Triglycerides in mmol/L? y/n")
    if ans == "y":
        tri_mol = enter_value("Enter triglycerides in mmol/L: ")
        return tri_mol * 88.57
    else:
        return enter_value("Enter triglycerides in mg/dL: ")


hdl_mg = hdl_cal()
tri_mg = tri_cal()

ratio = tri_mg / hdl_mg

if ratio > 2:
    print(f"Your HDL/Triglycerides ratio is not ideal, you have a HDL/Triglycerides ratio of {ratio:.2f}")
elif ratio > 1.5:
    print(f"Your HDL/Triglycerides ratio is not ideal but acceptable, you have a HDL/Triglycerides ratio of {ratio:.2f}")
else:
    print(f"Congrats! Your HDL/Triglyverides ratio is ideal, you have a HDL/Triglycerides ratio of {ratio:.2f}")