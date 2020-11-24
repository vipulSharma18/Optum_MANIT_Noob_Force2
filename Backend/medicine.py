import csv
import pandas as pd
import glob, os
import math
from math import radians, sin, cos, acos

path =r'C:\Users\ritwi\AppData\Local\Programs\Python\Python38' # use your path 
allFiles = glob.glob(path + "/*.csv") 
frame = pd.DataFrame() 
list_ = []
#list_[0] contains Allergies
#list_[1] contains Conditions
#list_[2] contains Medications
#list_[3] contains Organizations
#list_[4] contains Patients
#list_[5] contains Payers
#list_[6] contains Procedures
#list_[7] contains Providers
file_count=0

#To be obtained in input
Patient_ID = "76982e06-f8b8-4509-9ca3-65a99c8650fe"

for file_ in allFiles: 
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

# code_list , description_list , base_cost , dispenses.

code_list = list_[2]["CODE"].where (list_[2]["PATIENT"] == Patient_ID)
code = [x for x in code_list if str(x) != 'nan']

description_list = list_[2]["DESCRIPTION"].where (list_[2]["PATIENT"] == Patient_ID)
description = [x for x in description_list if str(x) != 'nan']

base_cost_list = list_[2]["BASE_COST"].where (list_[2]["PATIENT"] == Patient_ID)
base_cost = [x for x in base_cost_list if str(x) != 'nan']

dispenses_list = list_[2]["DISPENSES"].where (list_[2]["PATIENT"] == Patient_ID)
dispenses = [x for x in dispenses_list if str(x) != 'nan']
size = len(code)

#Displays payment history vs most cost effective substitute.
print("Transaction History:\n")
for i in range(size):
    print(description[i] , base_cost[i] , (int)(dispenses[i]))
print("\n\n")
print("Most Cost Effective Substitute\n")
for i in range(size):
    subs_meds_list = list_[2]["DESCRIPTION"].where (list_[2]["CODE"] == code[i])
    subs_meds = [x for x in subs_meds_list if str(x) != 'nan']
    subs_base_cost_list = list_[2]["BASE_COST"].where (list_[2]["CODE"] == code[i])
    subs_base_cost = [x for x in subs_base_cost_list if str(x) != 'nan']
    min_index = -1
    min_cost = float('inf')
    for x in range(len(subs_meds)):
        if min_cost > subs_base_cost[x]:
            min_cost = subs_base_cost[x]
            min_index = x

    print(subs_meds[min_index] , subs_base_cost[min_index])
    




