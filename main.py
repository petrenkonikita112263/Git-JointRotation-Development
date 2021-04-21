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

# Save info to two separated txt files
with open("data/pBody.txt", "w") as file:
    column_names = "frequency\t\t\tamplitude\t\t\tenergy/time\t\t\tmaxBigTheta\t\t\tminBigTheta\t\t\taverageBigTheta\t\t\tperiodTheta(before)\t\t\tperiodTheta(after)\t\t\tvelocityBigPhi\t\t\tphaseBigPhi\t\t\tmode\n"
    file.write(column_names)

with open("data/mMoment.txt", "w") as file:
    column_names = "frequency\t\t\tamplitude\t\t\tenergy/time\t\t\tmaxSmallTheta\t\t\tminSmallTheta\t\t\taverageSmallTheta\t\t\tperiodTheta(before)\t\t\tperiodTheta(after)\t\t\tvelocitySmallPhi\t\t\tphaseSmallPhi\t\t\tmode\n"
    file.write(column_names)
