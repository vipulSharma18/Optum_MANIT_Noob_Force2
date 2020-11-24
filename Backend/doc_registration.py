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
#Type of specialist needed
speciality = "GENERAL PRACTICE"

for file_ in allFiles: 
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
    if(file_count == 4):
        lat_p_list = (df["LAT"].where (df["Id"]==Patient_ID))
        lon_p_list = (df["LON"].where (df["Id"]==Patient_ID))
    if(file_count == 7):
        lat_d_list = (df["LAT"].where (df["SPECIALITY"]==speciality))
        lon_d_list = (df["LON"].where (df["SPECIALITY"]==speciality))
        address_d_list = (df["ADDRESS"].where (df["SPECIALITY"]==speciality))
        name_list = (df["NAME"].where (df["SPECIALITY"]==speciality))
        city_d_list = (df["CITY"].where (df["SPECIALITY"]==speciality))
        state_d_list = (df["STATE"].where (df["SPECIALITY"]==speciality))
        org_d_id_list = (df["ORGANIZATION"].where (df["SPECIALITY"]==speciality))
    file_count+=1

lat_p = [x for x in lat_p_list if str(x) != 'nan']
lon_p = [x for x in lon_p_list if str(x) != 'nan']
lat_d = [x for x in lat_d_list if str(x) != 'nan']
lon_d = [x for x in lon_d_list if str(x) != 'nan']
address_d = [x for x in address_d_list if str(x) != 'nan']
name_d = [x for x in name_list if str(x) != 'nan']
city_d = [x for x in city_d_list if str(x) != 'nan']
state_d = [x for x in state_d_list if str(x) != 'nan']
org_id = [x for x in org_d_id_list if str(x) != 'nan']
min_dis_index = -1
min_dis = float('inf')
for i in range(len(lat_d)):
    if(min_dis_index == -1):
        min_dis_index = i
        continue
    slat = lat_p[0]
    slon = lon_p[0]
    elat = lat_d[i]
    elon = lon_d[i]
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    if (dist < min_dis):
        min_dis = dist
        min_dis_index = i


hos_name_list = (list_[3]["NAME"].where (list_[3]["Id"] == org_id[min_dis_index]))
hos_name = [x for x in hos_name_list if str(x) != 'nan']
hos_phone_list = (list_[3]["PHONE"].where (list_[3]["Id"] == org_id[min_dis_index]))
hos_phone = [x for x in hos_phone_list if str(x) != 'nan']

#Displays the closest doctor of given speciality
print(name_d[min_dis_index])
print(hos_name[0])
print(address_d[min_dis_index])
print(city_d[min_dis_index] , state_d[min_dis_index])
print(hos_phone[0])    





    
