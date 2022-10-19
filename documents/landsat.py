import tarfile
from datetime import date
import requests
import wget
import os

from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

global tries, flag
count = 0

api = API('username', 'password')  # username ,password of earth explorer
scenes = api.search(
    dataset='landsat_8_c1',
    latitude= 20.479,
    longitude= 71.847,
   
    start_date='2015-12-31',
    end_date='2016-01-29',
    
)

print(f"{len(scenes)} scenes found.")

with open("output.txt", "w") as f:
    for scene in scenes:
        f.write(scene['landsat_product_id'])
        f.write("\n")

ee = EarthExplorer('sudhakarab.217it006@gmail.com', 'sudhausgs0904')
with open("output.txt", "r") as f:
    line = f.readline()[:-1]

    while line:
        flag = 0
        yr = int(line[17:21])
        mon = int(line[21:23])
        dy = int(line[23:25])
        doy = date(yr, mon, dy).timetuple().tm_yday
        tries = 0
      

        output_dir = 'E:\Landsat MM5/' + str(yr) + '/'
        is_exist = os.path.exists(output_dir)
        if not is_exist:
            os.makedirs(output_dir)
        if not(os.path.exists(output_dir + line + '.tar.gz')):
            ee.download(line, output_dir)
            file = tarfile.open(output_dir + line + '.tar.gz')
            file.extractall(output_dir + line + '/')
            file.close()
            os.remove(output_dir + line + '.tar.gz')
            count += 1
            line = f.readline()[:-1]
        
ee.logout()
api.logout()
print('\n', count, 'Downloads Complete')
