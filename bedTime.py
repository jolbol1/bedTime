#!/usr/bin/env python3
import time
import os
import sys
from threading import Thread
from datetime import datetime, time

server = None
watchlist = []
ip_watchlist = {}


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    print("Check Time: ", check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def should_kick_stream(username, session_id, message):
    file_path = "/scripts/bedTime/userFiles/" + username.upper() + ".txt"
    print(file_path)
    try:
        with open(file_path) as fp:
            bedtime_str = fp.read()
            print("String :", bedtime_str)
    except IOError:
        print("Could not find file")
        return
    bedtime = bedtime_str.split(':')
    print("Bedtime: ",bedtime)
    hour = int(bedtime[0])
    minute = int(bedtime[1])
    hour2 = hour + 1;
    print("BEDTIME CHECK", bedtime, hour, minute, hour2)
    if is_time_between(time(hour, minute), time(hour2, minute)):
        cmd = '/scripts/plexpy/kill_stream.py --jbop stream --username {username} --sessionId {session_id} --killMessage {message}'.format(
            username=username, session_id=session_id, message=message)
        res = os.system(cmd)
        print("Returned Value: ", res)


should_kick_stream(sys.argv[1], sys.argv[2], sys.argv[3])

