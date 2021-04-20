# Read the config file.
# Save the content as the dictionary: keys and values are separated by '=' sign
# Remove spaces in dictionary
with open("data/input.cfg", "r") as file:
    data = {}
    for line in file:
        k, v = line.strip().split("=")
        data[k] = v
    data = {k.replace(" ", ""): v.replace(" ", "") for k, v in data.items()}

# Save info to log file.
# At the time safe the data from dictionary that is based on config file
with open("data/log.txt", "w") as file:
    for k, v in data.items():
        dict_content = "# " + k + " = " + v + "\n"
        file.write(dict_content)

# Added to log file additional info.
# At the time only skipPeriods value and column names
with open("data/log.txt", "a") as file:
    skip_text = f"===== Skipping {data['skipPeriods']} periods =====\n"
    column_names = f"period\t\t\ttime\t\t\tsmallTheta\t\t\tbigTheta\t\t\tsmallPhi\t\t\tbigPhi\t\t\tenergy\t\t\tenergy/time\t\t\t{data['variable']}"
    skip_text += column_names
    file.write(skip_text)
