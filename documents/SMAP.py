import tarfile
from datetime import date
import requests
import wget
import os
from datetime import datetime,timedelta

from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

global tries, flag
count = 0


year=2021


start_date = date(year, 1, 1)

for i in range(365): 
    print(start_date)
    #dt=datetime.strptime(start_date, '%Y/%m/%d')
    dt=start_date
    #print(dt)
    d = dt.timetuple().tm_yday
    #print(yr,'\n',mon,'\n',dy,'\n',date(yr, mon, dy),'\n',d)
    dey = d + 4
    #print(dey,'\n')
    if 9 < d < 100:
        day_n = '0' + str(d)
    elif d < 10:
        day_n = '00' + str(d)
    elif 99 < d < 367:
        day_n = str(d)
    else:
        flag = -1
        

    if 9 < dey < 100:
        dey_n = '0' + str(dey)
    elif dey < 10:
        dey_n = '00' + str(dey)
    elif 99 < dey < 371:
        dey_n = str(dey)
    else:
        flag = -1


    yr=dt.year
    dataset_location = str(yr) + '/' + day_n
    dataset_name = 'RSS_smap_SSS_L3_8day_running_' + str(yr) + '_' + dey_n + '_FNL_v04.0.nc'
    url = 'https://podaac-opendap.jpl.nasa.gov/opendap/allData/smap/L3/RSS/V4/8day_running/SCI/'  + dataset_location + '/' + dataset_name
    print(url)
   
    save_location = 'E:\SMAP MM5_test/'+ str(yr)  + '/' 
    
    #r = requests.head(url, allow_redirects=True, )

    save_file = save_location + dataset_name
    print(save_file)
    is_exist = os.path.exists(save_location)
    if not is_exist:
        os.makedirs(save_location)
    if not(os.path.exists(save_file)): #or os.path.exists((save_location + line + '.nc'))):
        print("downloading.. ",url) 
        wget.download(url, save_file)
           
    start_date += timedelta(days=1)
    


print('\n', 'Downloads Complete')
