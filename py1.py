#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rgcet
#
# Created:     10/03/2018
# Copyright:   (c) rgcet 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
list = raw_input()

def zho(x):
     print x * 5


def my_pro(fu, list):
     for item in list:
         fu(item)


my_pro(zho, list)