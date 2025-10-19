import pandas as pd

#Initialize empty list to store row data
data = []
header_found = False
#Open and read the pslist output file
with open("pslist.txt", "r") as file:
    for line in file:
        line = line.strip()
        #Skip lines that start with "Volatility"
        if line == "" or line.startswith("Volatility"):
            continue
        #Identify and store header (column names)
        if line.startswith("PID") and not header_found:
            columns = line.split()
            header_found = True
            continue
        #Capture and process data after header is found
        if header_found and line.split()[0].isdigit():
            row = line.split()
            #Ensure row and columns match
            if len(row) > len(columns):
                row = row[:len(columns)]
            elif len(row) < len(columns):
                row += [""] * (len(columns) - len(row))
            data.append(row)
#Create dataframe 
df = pd.DataFrame(data, columns=columns)
#Convert columns to the proper data types
for col in ["PID", "PPID", "Threads", "Handles"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
#convert to csv file
df.to_csv("pslist.csv", index=False)

print("Done")
