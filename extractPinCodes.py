# -*- coding: utf-8 -*-

import os


def extractPinCodes(user, directory):
    os.chdir(directory)
    print(os.getcwd())
    pinCodeFile = user + ".txt"

    text_file = open(pinCodeFile, "r")
    pin_codes = [line.replace("\n", "") for line in text_file]
    return pin_codes
