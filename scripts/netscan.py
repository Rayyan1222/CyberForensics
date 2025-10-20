import pandas as pd
#List to store row, header data
rows = []
header = []
#Flag to indicate header was found
found = False
#Open they netscan output file
with open("netscan.txt", "r") as f:
    for line in f:
        line = line.strip()
        #Skip empty lines or line that start with volatility
        if line == "" or line.startswith("Volatility"):
            continue
        #Split line into seperate values
        parts = line.split()
        #Detect header row, iff oofset store it once.
        if parts[0] == "Offset" and not found:
            header = parts
            found = True
            continue
        #Process data rows only after header is found
        if found:
            #Make sure header is more than parts
            while len(parts) < len(header):
                parts.append("")
            #Only take up to the number of header columns
            rows.append(parts[:len(header)])
#Create Dataframe with rows and columns
df = pd.DataFrame(rows, columns=header)
df.to_csv("netscan.csv", index=False)
print("Done")

