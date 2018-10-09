
'''
--------------------------------------------------------------------------------
Copies all images between two hours. Also, you can choose to include weekends
or not.

Have you ever thought about how your behavior from 9 am to noon differs
from your behavior from 6 pm to 9 pm?

This file helps you to grab photos (or other files) you took in a time frame.
--------------------------------------------------------------------------------
'''


'''
--------------------------------------------------------------------------------
CONTROLS
--------------------------------------------------------------------------------
'''

old_destination = "" # Directory, like "/Users/me/Docs/dir"
new_destination = ""
hour_1 = 9 # Change this
hour_2 = 11 # Change this
exclude_weekend = False # Change this
copy_f = True # Change this


'''
--------------------------------------------------------------------------------
MAIN CODE
--------------------------------------------------------------------------------
'''

import time
import datetime
import os
import shutil

def files_interval(old_destination, new_destination, hour_1, hour_2,
        exclude_weekend = False, copy_f = True):
    '''
    old_destination = string
    new_destination = string
    exclude_weekend = Boolean
    hour_1 = int
    hour_2 = int

    Outputs:
        list_good_files = list of strings (files which fit the criteria)
    '''

    # All the files in the directory
    list_elements = os.listdir(old_destination)

    # Verify consistency of directories strings
    if old_destination[-1] != "/":
        old_destination = old_destination + "/"

    if new_destination[-1] != "/":
        new_destination = new_destination + "/"

    if exclude_weekend:
        # Note: Monday is zero and Sunday is 6.
        cut_off_day = 4
    else:
        cut_off_day = 6

    # Filter only files that we want
    list_good_files = []
    for element in list_elements:
        mtime = os.path.getmtime(old_destination + element)
        value = datetime.datetime.fromtimestamp(mtime)
        # print(value.strftime('%Y-%m-%d %H:%M:%S'))
        if (value.hour > hour_1 and value.hour < hour_2
            and value.weekday() <= cut_off_day):
            list_good_files.append((element,value.hour, value.minute))


    if copy_f:
        for image in list_good_files:
            shutil.copy2(old_destination + image[0],
                new_destination + image[0])

    return list_good_files



files_to_move = files_interval(old_destination, new_destination, hour_1, hour_2,
        exclude_weekend, copy_f)

print("The files to move are: ", files_to_move)
