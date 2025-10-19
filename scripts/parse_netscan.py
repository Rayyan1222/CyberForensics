import csv
 
 #Read file netscan.txt, then writes in flagged_connections.csv and then proper breakes
with open('netscan.txt', 'r') as infile, open('flagged_connections.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile) #creats CSV files and gives permation to write
    #Row heading for CSV files
    writer.writerow(['Local Address', 'Local Port', 'Foreign Address', 'Foreign Port', 'State', 'PID', 'Process', 'Created', 'Flagged Reason'])

    for line in infile: # Loops and reads the netscan.txt file, It also skips headers and spaces 
        if line.startswith('Offset') or line.strip() == '':
            continue
        parts = line.strip().split('\t')
        if len(parts) < 10: # Skips lines that don't have at least 10 fields
            continue

        # Extracts the relevant fields
        local_ip, local_port = parts[2], parts[3]
        foreign_ip, foreign_port = parts[4], parts[5]
        state, pid, process, created = parts[6], parts[7], parts[8], parts[9]

        #Flaged if the following criteria
        flagged = []
        if not (foreign_ip.startswith('192.168.') or foreign_ip.startswith('10.') or foreign_ip.startswith('172.')):
            flagged.append('External IP')
        if foreign_port not in ['80', '443', '22', '135', '445']:
            flagged.append('Uncommon Port')
        if process.lower() in ['backgroundtask', 'searchapp.exe']:
            flagged.append('Suspicious Process Name')

        if flagged:
            writer.writerow([local_ip, local_port, foreign_ip, foreign_port, state, pid, process, created, ', '.join(flagged)])
