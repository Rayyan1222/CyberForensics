# Volatile Memory Forensics with Malware Detection and Network Traffic Analysis

This project extends the research on volatile memory forensics by focusing on detecting malware artifacts and analyzing network traffic within memory dumps. Our approach works on identifying malicious activity through the detection of suspicious processes and abnormal network connections.

## Research Objectives:

1. Malware Artifact Detection: Detect traces of malware in volatile memory by analyzing suspicious processes, unusual memory patterns, and signatures of known malicious software.
2. Network Traffic Analysis: Analyze network connections from memory dumps to identify unauthorized or suspicous communication, such as data exfiltration or command-and-control.
3. AI-Based Attack Classification: Use machine learning models to classify various attack types (Malware, MITM, and DOS) based on patterns identified in the memory dumps.

## Methodology:

Step 1: Data Collection and Memory Acquisition
Data: Collect Data such as running processes, network connections, and memory allocations.

Step 2: Organizing and Preparing the Data
Clean The Data: Fix any missing or incomplete information in the memory dumps, like missing timestamps or network connection details.

Step 3: Malware Artifact Detection
Malware Analysis: Identify known malware by matching behaviors that associate with malicious software. Flag any processes or hidden processes that indicate malware activity.

Step 4: Network Traffic Analysis
Monitor Network Connections: Look for unusual IP addresses or connections to unknown ports. Track processes that are connecting to multiple external IP addresses.

Step 5: Machine Learning
Machine Learning Models: Train machine learning models, such as SVM to classify different attack types based on memory dump data, focusing on attack types such as Malware, MITM, and DOS.
Model Evaluation: Measure the accuracy, precision, recall, and F1-score of the model in detecting and classifying attacks based on the memory features.

## Expected Contributions:

1. Malware Detection: Extend traditional memory forensics to include the detection of malware artifacts and hidden processes in volatile memory.
2. Network Traffic Insights: Provide a method for analyzing network traffic from memory dumps, helping to detect data exfiltration and Command-and-Control communications.
3. AI-Models: Implement AI-based models to detect various attack types helping with detection and accuracy.

Link to Video: https://www.loom.com/share/47a2ac65d22d435d9d522d645167bfba?sid=b120b489-e524-4281-8f7b-7d2db2c0a4cd 
