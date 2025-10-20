import pandas as pd

#List each row of process data and column headers
rows = []
header = []
#Open and read psscan output file
with open("psscan.txt", "r") as f:
    for line in f:
        line = line.strip()
        #Skip empty lines or name start with Volatility
        if line == "" or line.startswith("Volatility"):
            continue
        parts = line.split()
        #Detect header row is 'PID' and store first 5 columns as headers
        if parts[0] == "PID":
            header = parts[:5]    
            continue
        rows.append(parts[:5])  
#Create a DataFrame using rows with column names.
df = pd.DataFrame(rows, columns=header)
df.to_csv("psscan.csv", index=False)
print("Done")
