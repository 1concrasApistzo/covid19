import requests
import re
import os
from os import path
from os import listdir
from os.path import isfile, join

import bs4
from bs4 import BeautifulSoup
import couchdb
import subprocess
import csv
from datetime import datetime

covid_db_full_url = str(os.environ.get("covid_db_full_url"))
archive_folder_path = str(os.environ.get("archive_folder_path")).format("cumulative_vaccination_coverage/") 
couchdb_db_name = "covid19"
couch = couchdb.Server(covid_db_full_url)
database = couch[couchdb_db_name]


def todays_file():
        now = datetime.now()
        print("now =", now)
        #current_date_time = now.strftime("%d-%m-%YT%H-%M-%S")
        datepart =  now.strftime("%Y-%m-%d") 
        #datepart =  "2021-07-08"
        timepart = "-at-07-00-AM.pdf"
        current_date_time = datepart +timepart  
        return current_date_time


states = {}
states["Andhra Pradesh"]="AP"
states["Arunachal Pradesh"]="AR"
states["Assam"]="AS"
states["Bihar"]="BR"
states["Chattisgarh"]="CT"
states["Chhattisgarh"]="CT"
states["Goa"]="GA"
states["Gujarat"]="GJ"
states["Haryana"]="HR"
states["Himachal Pradesh"]="HP"
states["Jharkhand"]="JH"
states["Jharkhand#"]="JH"
states["Karnataka"]="KA"
states["Kerala"]="KL"
states["Madhya Pradesh"]="MP"
states["Madhya Pradesh#"]="MP"
states["Maharashtra"]="MH"
states["Manipur"]="MN"
states["Meghalaya"]="ML"
states["Mizoram"]="MZ"
states["Nagaland"]="NL"
states["Nagaland#"]="NL"
states["Odisha"]="OR"
states["Punjab"]="PB"
states["Rajasthan"]="RJ"
states["Sikkim"]="SK"
states["Tamil Nadu"]="TN"
states["Telengana"]="TG"
states["Telangana***"]="TG"
states["Tripura"]="TR"
states["Uttarakhand"]="UT"
states["Uttar Pradesh"]="UP"
states["West Bengal"]="WB"
states["Andaman and Nicobar Islands"]="AN"
states["Chandigarh"]="CH"
states["Dadra and Nagar Haveli"]="DN"
states["Dadar Nagar Haveli"]="DN"
states["Daman and Diu"]="DD"
states["Daman & Diu"]="DD"
states["Delhi"]="DL"
states["Jammu and Kashmir"]="JK"
states["Ladakh"]="LA"
states["Lakshadweep"]="LD"
states["Pondicherry"]="PY"
states["Puducherry"]="PY"
states["Dadra and Nagar Haveli and Daman and Diu"]="DN_DD"
states["Telangana"]="TG"

country_datarow_exceptions = {
    "2021-08-09-at-07-00-AM.pdf" :{"skip":"yes"},
    "2021-07-12-at-07-00-AM.pdf" :{"skip":"yes"}
}

def get_datetime(file_name):
    date_time = file_name.replace("-at-07-00-AM.pdf","")
    date_time = date_time + "T09:00:00.00+05:30"
    return date_time

def get_country_data(file_name):
    data_file = archive_folder_path + file_name
    csv_file_name = file_name +"_vaccine_country.csv"
    #print(data_file)
    s = subprocess.call(["tabula-java","--lattice","-a", "54.695,29.022,142.505,588.623", "-p", "1", data_file ,">",csv_file_name])
    file = open(csv_file_name)    
    csvreader = csv.reader(file)
    report_time = get_datetime(file_name)
    data = {}
    data["_id"] = report_time +"|vaccinations"
    data["report_time"] = report_time

    if file_name in country_datarow_exceptions :
        return None
    else:
        pass

    rows = []
    row_num = 1
    data_row = []
    for row in csvreader:
        print(row)
        rows.append(row)
    file.close()

    data_row = None
    print(len(rows))    
    if report_time > "2022-08-07":
        data_row = rows[3]
    elif report_time > "2022-08-05":
        data_row = rows[1]
    elif report_time > "2022-03-23":
        data_row = rows[3]
    elif report_time > "2022-03-16":
        data_row = rows[3]
    elif report_time > "2022-03-14":
        data_row = rows[4]
    elif report_time > "2022-03-13":
        data_row = rows[3]
    elif "2021-02-25" in report_time or "2021-02-28" in report_time :
        data_row = rows[0]
    elif "2021-02-26" in report_time or "2021-02-27" in report_time :
        data_row = rows[1]
    elif report_time in country_datarow_exceptions:
        data_row = rows[country_datarow_exceptions[report_time]]
    elif report_time > "2022-01-10":
        data_row = rows[3]
    elif report_time > "2021-07-03":
        data_row = rows[2]

    # elif len(rows) == 3:
    #     data_row = rows[2]
    # elif len(rows) > 3:
    #     data_row = rows[3]
    
    
    print("data_row", data_row)   


    start = 1
    if report_time > "2022-03-23":
        start = 1
    elif report_time > "2022-03-13":
        start = 1
    elif report_time > "2022-03-13":
        start = 0
    elif "2021-02-25" in report_time:
        start = 3
    elif "2021-02-26" in report_time or "2021-02-27" in report_time or "2021-02-28" in report_time:
        start = 2
    elif len(data_row) > 3:
        new_data_row = data_row 
        print("new_data_row",new_data_row)
        data_row = []
        for r in new_data_row:
            print(r)
            if r == "":
                pass            
            else:
                data_row.append(r) 
        start = 1
    else:
        start = 0
    
    print("Starting at", start)
    print("data_row", data_row)  
    print("_id", data["_id"])
    data["source"] = "mohfw"
    data["type"] = "vaccinations"
    data["first_dose"] = int(data_row[start].replace(",",""))
    data["second_dose"] = int(data_row[start+1].replace(",",""))
    data["first_dose_15_18"] = int(data_row[start+2].replace(",",""))
    data["second_dose_15_18"] = int(data_row[start+3].replace(",",""))
    data["first_dose_12_14"] = int(data_row[start+4].replace(",",""))
    data["second_dose_12_14"] = int(data_row[start+5].replace(",",""))
    data["precaution_dose_18_59"] = int(data_row[start+6].replace(",",""))
    data["precaution_dose"] = int(data_row[start+7].replace(",",""))
    data["total"] = int(data_row[start+8].replace(",",""))
    return data


# def get_state_data(file_name):
#     print(s) 



def parse_country_data(file_name):
    data = get_country_data(file_name)    
    if data:
        _id = data["_id"]
        try:
            if database[_id]:
                print("##### UPDATING #####")
                existing_data = database[_id]
                _rev = existing_data["_rev"]
                data["_rev"] = _rev        
                database.save(data)
        except couchdb.http.ResourceNotFound:
                print("##### ADDING #####")
                database.save(data) 
    print("saved", data)


# def parse_all_country_again():
#     only_files = ([f for f in listdir(archive_folder_path) if isfile(join(archive_folder_path, f))])
#     only_files.sort()
#     for file_name in only_files:
#         report_time = get_datetime(file_name)
#         if report_time > "2021-07-11":
#             print(report_time)
#             parse_country_data(file_name)





# def parse_state_data(file_name):
#     data_file = archive_folder_path + file_name
#     csv_file_name = file_name +"_vaccine_state.csv"
#     #print(data_file)
#     s = subprocess.call(["tabula-java","-a", "170.0,49.0,783.821,488.719", "-p", "1", data_file ,">",csv_file_name])
    
#     file = open(csv_file_name)    
#     csvreader = csv.reader(file)
#     data_rows = []
#     report_time = get_datetime(file_name)
#     for row in csvreader:
#         print(row)
#         data = {}
#         state = row[1]
        
#         if state in states:
#             state_code = states[state]
#         else:
#             print("state", state)
#             break

#         data["_id"] = report_time +"|vaccinations|"+state_code
#         data["state"] = state_code
#         data["report_time"] = report_time
#         data["source"] = "mohfw"
#         data["type"] = "vaccinations"
#         data["total"] = (row[6]).replace(",","")
#         data["1stdose"] = (row[4]).replace(",","")
#         data["2nddose"] = (row[5]).replace(",","")        
#         data_rows.append(data_row)

#     file.close()



#     return data_rows


if __name__ == "__main__":
    FILE_NAME = todays_file()
    #FILE_NAME = "2022-10-15-at-07-00-AM.pdf"
    print(FILE_NAME)
    parse_country_data(file_name=FILE_NAME)
    #parse_all_country_again()

    # for dt in range(30,31):
    #     fname = "2022-09-{dt}-at-07-00-AM.pdf".format(dt=dt)
    #     print(fname)
    #     parse_country_data(file_name=fname)

    #parse_country_data(file_name=FILE_NAME)
