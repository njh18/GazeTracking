# -*- coding: utf-8 -*-

import os


def extractPinCodes(user, directory):
    sensorsFile = user + "_Sensors"
    os.chdir(directory + "\\" + sensorsFile)
    pinCodeFile = user + "_Pins" + ".txt"

    text_file = open(pinCodeFile, "r")
    pin_codes = [line[:-1] for line in text_file]
    return pin_codes
