'''
-------------------------------------------------------------------------------
This script is for testing EasyGUI
-------------------------------------------------------------------------------
'''
# Separated namespace
import easygui as g
# Local functions
import dbquery

opening_msg = "What would you like to look up?"
title = "DB Query Application"
choices = ["Department", "IP", "Hostname", "Device Type"]
choice = g.choicebox(opening_msg, title, choices)

if choice == "Department":
    department = g.enterbox("What is the dept you want to search for?", title)
    RDept = dbquery.querydept(department)
    g.msgbox(RDept, title);

elif choice == "IP":
    ip = g.enterbox("What is the ip you want to search for?", title)
    RIP = dbquery.queryip(ip)
    g.msgbox(RIP, title);

elif choice == "Hostname":
    hostname = g.enterbox("What is the hostname you want to search for?", title)
    RHost = dbquery.queryip(hostname)
    g.msgbox(RHost, title);

elif choice == "Device Type":
    device_type = g.enterbox("What is the device type you want to search for?", title)
    RdType = dbquery.queryip(device_type)
    g.msgbox(RdType, title);
