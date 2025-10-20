import pandas as pd
#List to store rows, column names
data = []
header = []
#Flag to detect when headers are found
header_found = False
#Open and read the malfind output
with open("malfind.txt", "r") as file:
    for line in file:
        line = line.strip()
        #Skip empty lines or lines starting with volatlity
        if line == "" or line.startswith("Volatility"):
            continue
        parts = line.split()
        #Check if header row starts with PID
        if parts[0] == "PID":
            #Add column called Hexdump to store memory dump data
            header = parts + ["Hexdump"]
            header_found = True
            continue
        #Check if a data row starts with column PID
        if header_found and parts[0].isdigit():
            data.append(parts + [""])
        #Check if line starts with PID and append line to last row
        elif header_found and data:
            data[-1][-1] += " " + line
#Make sure row matches number of columns in header
rows = []
for row in data:
    #Fill missing values with empty strings
    if len(row) < len(header):
        row += [""] * (len(header) - len(row))
    else:
        row = row[:len(header)]
    rows.append(row)
#Create dataframe
df = pd.DataFrame(rows, columns=header)
df.to_csv("malfind.csv", index=False)

print("Done")
