# -*- coding: utf-8 -*-

def extractPinCodes(textfile):
    text_file = open(textfile, "r")
    pin_codes = [line[:-1] for line in text_file]
    return
