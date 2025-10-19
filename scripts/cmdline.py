import pandas as pd
#List to store rows
rows = []
#Open and read cmdline output file
with open("cmdline.txt", "r") as file:
    for line in file:
        line = line.strip()
        #Skip lines that start with Volatility and empty lines
        if line == "" or line.startswith("Volatility"):
            continue
        #Split line into at most 3 parts: PID, Process Name, Command-Line
        parts = line.split(maxsplit=2)
        #If line only has PID, add empty placeholders
        if len(parts) == 1:
            parts = [parts[0], "", ""]
        #If only PID and Process Name, add empty argument field
        elif len(parts) == 2:
            parts = [parts[0], parts[1], ""]
        #Add parts to list
        rows.append(parts)
#Create a DataFrame with rows and columns.
df = pd.DataFrame(rows, columns=["PID", "Process", "Args"])
df.to_csv("cmdline_cleaned.csv", index=False)

print("Done")
