# Log File Reader
try:
    with open("system.log", "r") as file:
        lines = file.readlines()

    info = warning = error = 0

    for line in lines:
        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1

    print("\nLog Summary")
    print("INFO:", info)
    print("WARNING:", warning)
    print("ERROR:", error)

except FileNotFoundError:
    print("system.log was not found. Keep it in the same folder as this program.")
