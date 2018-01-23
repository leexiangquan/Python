# DownloadGFS.py
import os
import datetime
import wget
import pandas as pd
import urllib.request
import urllib
import time
import random


def download_gfs(url, folder):
    os.chdir(folder)
    gfs_hours = ['000', '006', '012', '018', '024', '030', '036',
                 '042', '048', '054', '060', '066', '072', '078',
                 '084', '090', '096', '102', '108', '114', '120',
                 '126', '132', '138', '144', '150', '156', '162',
                 '168']
    for i in range(len(gfs_hours)):
        full_url = url + gfs_hours[i] + '.grb2'
        filename = full_url[-28:]
        while True:
            if not os.path.exists(filename):
                try:
                    urllib.request.urlopen(full_url)
                    download_file = wget.download(full_url, bar=wget.bar_thermometer)
                    if os.path.exists(download_file):
                        print(download_file + " has been successfully downloaded")
                    else:
                        print(download_file + " downloaded failed")
                except urllib.error.URLError:
                    wait_time = round(random.random() * 60)
                    print("Wait for " + str(wait_time) + " seconds")
                    time.sleep(wait_time)
                    print("Try again")
            else:
                print(filename + " already existed")
                break



def create_date_list(begin_date, end_date, date_format="%Y%m%d"):
    return [datetime.datetime.strftime(x, date_format)
            for x in list(pd.date_range(start=begin_date, end=end_date))]


def main():
    source_url = "ftp://nomads.ncdc.noaa.gov/GFS/Grid4"
    ymd_series = create_date_list("20171201", "20171231")
    ym_series = create_date_list("20171201", "20171231", date_format="%Y%m")
    folder = "/Users/lixiangquan/Downloads"
    # loops: for date
    for i in range(len(ymd_series)):
        file_url = source_url + '/' + ym_series[i] + '/' + ymd_series[i] + '/' + 'gfs_4_' \
                   + ymd_series[i] + '_1200_'
        mon_folder = folder + "/" + ym_series[i]
        if not os.path.exists(mon_folder):
            os.mkdir(mon_folder)
        day_folder = mon_folder + '/' + ymd_series[i]
        if not os.path.exists(day_folder):
            os.mkdir(day_folder)
        download_gfs(file_url, day_folder)

    # All downloaded
    print("All GFS data downloaded completely")


main()