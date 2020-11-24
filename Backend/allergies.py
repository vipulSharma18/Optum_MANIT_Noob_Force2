import csv
import pandas as pd
import glob, os
import math
from math import radians, sin, cos, acos

path =r'C:\Users\ritwi\AppData\Local\Programs\Python\Python38' # use your path 
allFiles = glob.glob(path + "/*.csv") 
frame = pd.DataFrame() 
list_ = []
#lists_[0] contains Allergies
#lists_[1] contains Conditions
#lists_[2] contains Medications
#lists_[3] contains Organizations
#lists_[4] contains Patients
#lists_[5] contains Payers
#list_[6] contains Procedures
#lists_[7] contains Providers
file_count=0

#To be obtained in input
Patient_ID = "76982e06-f8b8-4509-9ca3-65a99c8650fe"

for file_ in allFiles: 
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
    if(file_count==0):
        allergies_list = (df["DESCRIPTION"].where (df["PATIENT"]==Patient_ID))
    file_count+=1

allergies = [x for x in allergies_list if str(x) != 'nan']

#Display the allergies on the site
print(allergies)
