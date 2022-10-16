
import pandas as pd

#load latest-customers.txt file into pandas dataframe
customers = pd.read_csv('latest-customers.txt')
#Filter age of customers between 40 and 59
effected_customers = (customers[(customers['age']>40) & (customers['age']<59)])
#load the effected customers into text file
effected_customers.to_csv("EffectedCustomers.txt",index=False)

"""
improvisation(Phase2 Changes):
1. Remove hardcoded filepaths and filter conditions.
2. Add exception handling(example: file not found exception)
"""