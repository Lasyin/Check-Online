#!/usr/bin/env python

# Bryan Collins
# Check_Online logs uptime information on a given hostname(s)

import subprocess
from datetime import datetime
import pickle
import appdirs
import os
import time
import argparse
import json as JSON
import jsonpickle
import ping_event
import ping_event_list

LOCATIONS = [
    'list of',
    'hostnames',
    'to ping'
]
PING_COUNT = "1" # Just send 1 packet
PING_TIMEOUT = "5" # Wait 5 seconds before quitting

APP_NAME = "check_online"    #info for appdirs
APP_AUTHOR = "Bryan Collins" #info for appdirs
DATA = "check_online_data.pickle" # Save file for pickled data

SLEEP_TIME = 60 # Wait 1 min between pings


# Runs test, this is the starting point
def run_test():
    while(True):
        for location in LOCATIONS:
            if(ping(location)):
                store_result(True, location)
            else:
                store_result(False, location)
        time.sleep(SLEEP_TIME)

# Send ping with a specified number of packets and a timeout incase offline
# Returns True if packet(s) returned, False otherwise
def ping(location):
    check_for = PING_COUNT + ' packets received' # 1 packets received
    cmd = "ping -c " + PING_COUNT + " -t " + PING_TIMEOUT + " " + location
    proc = subprocess.Popen(["%s" % cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = proc.stdout.readlines()
    for i in result:
        if(check_for in str(i)):
            return True
    return False

# Fetches pickle file and returns the data
def load_data_file():
    dir = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)

    try:
        # file exists, load
        f = open(os.path.join(dir, DATA), 'rb')
    except IOError:
        # dir likely does not exist
        if(not os.path.exists(dir)):
            os.makedirs(dir)
        # or, dir already exists but file doesn't
        try:
            f = open(os.path.join(dir, DATA), 'wb')

            # create new class with an empty list for initialization
            event_list = ping_event_list.PingEventList([])
            pickle.dump(event_list, f)
            f.close()
            f = open(os.path.join(dir, DATA), 'rb')
        except IOError:
            print("ERROR: Could not create save file")
            exit()

    # load event_list then return
    new_event_list = pickle.load(f)
    f.close()
    return new_event_list

# Saves event_list to pickle file
def save_data_file(event_list):
    dir = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)
    try:
        f = open(os.path.join(dir, DATA), 'wb')
    except IOError:
        print("ERROR: Could not find save file")
        exit()
    pickle.dump(event_list, f)
    f.close()

# Gets loaded file and prints every event
def print_data_file():
    event_list = load_data_file()
    for event in event_list:
        print(event)

# Returns JSON Data from jsonpickle
def return_json_data():
    event_list = load_data_file()

    # Creates JSON data from pickle file
    json_data = jsonpickle.encode(event_list)

    # Dump json data because script that calls (Check_online_display) expects json
    json_data = JSON.dumps(json_data)

    return(print(json_data))

# Creates a new event and adds to the event list to store new data
def store_result(success, location):
    event_list = load_data_file()

    # Iterate throught event list in reverse (reverse-chronological order)
    for event in reversed(event_list):
        # If last recorded ping location is the current ping location
        if(event.ping_location == location):
            # found last record of this location
            if(event.success == success):
                # last record was the same as this one, exit by returning
                return
            else:
                # last record is different, break for loop so below code will execute
                break
    # Only runs if online value has changed
    date = datetime.now()
    curr_date = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    curr_time = str(date.hour) + ':' + str(date.minute)
    event = ping_event.PingEvent(location, curr_date, curr_time, success)

    event_list.insert(event)
    save_data_file(event_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--read", help="Prints out all saved events.", action="store_true")
    parser.add_argument("--json", help="Returns saved events in JSON format.", action="store_true")

    args = parser.parse_args()

    if(args.read):
        print_data_file()
        exit()
    if(args.json):
        return_json_data()
        exit()

    run_test()
