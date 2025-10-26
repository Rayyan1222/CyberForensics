import pandas as pd

mal = pd.read_csv("/Users/rayyanbasathia/Downloads/MalwareArtifact.csv")
net = pd.read_csv("/Users/rayyanbasathia/Downloads/flagged_connections.csv")

# Filtering valid PIDs
net = net.rename(columns={"PID":"pid","Flagged Reason":"flag"})
mal = mal[mal["pid"].astype(str).str.isdigit()] 
net = net[net["pid"].astype(str).str.isdigit()]

# Converting PID to Integer
mal["pid"] = mal["pid"].astype(int)
net["pid"] = net["pid"].astype(int)

# Aggregating Network Data by PID (By Groups)
n = net.groupby("pid").agg(
    num_connections=("pid","count"),
    num_external_ips=("Foreign Address",lambda s:s.nunique()),
    num_uncommon_ports=("flag",lambda s:s.str.contains("Uncommon Port",na=False).sum())
).reset_index()

n["has_flag"] = (n["num_uncommon_ports"]>0).astype(int) # Flagging suspicious activity 
df = mal.merge(n,on="pid",how="left").fillna(0) # Merging

# Attack Types grouped in their respoinding order
df["AttackType"] = df.apply(lambda x: 
    "Malware" if x.malwareflag==1 or x.hasinjection==1 or x.hiddenproc==1 else
    "MITM" if x.num_uncommon_ports>0 and x.num_external_ips>=2 else
    "DOS" if x.num_connections>50 else "Benign", axis=1)

#Exporting final results
df[["pid","hiddenproc","hasinjection","malwareflag",
    "num_connections","num_external_ips","num_uncommon_ports","has_flag","AttackType"]
  ].to_csv("/Users/rayyanbasathia/Downloads/svm.csv",index=False)
