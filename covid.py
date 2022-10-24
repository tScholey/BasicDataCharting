import pandas as pd
import os
import matplotlib.pyplot as plt

cwd = os.getcwd()

sets = []

for root, dirs, files in os.walk(cwd):
    for name in files:
        if name.endswith("csv"):
            sets.append(name)
#%%
cfrlist = []
cfruklist = []

for i in sets:
    latest = pd.read_csv(cwd + "\\" + i)
    try: uk = latest.loc[latest['Country_Region'] == 'United Kingdom']
    except KeyError:
        uk = latest.loc[latest['Country/Region'] == 'United Kingdom']
    cfr = latest['Deaths'].sum()/latest['Confirmed'].sum()*100
    cfrlist.append(cfr)
    if uk['Confirmed'].sum() != 0:
        cfruk = uk['Deaths'].sum()/uk['Confirmed'].sum()*100
        cfruklist.append(cfruk)
    else:
        cfruklist.append(0)

    
    print(i + " " + str(uk['Confirmed'].sum()))
#%%
plt.plot(sets,cfrlist, linestyle='none', marker = 'o')
plt.title("Global CMR")
plt.show()

plt.plot(sets,cfruklist, linestyle='none', marker = 'o')
plt.title("UK CMR")
plt.show()