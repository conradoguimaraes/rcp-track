# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:41:07 2022

@author: Conrado
"""


#%%
def sPrint(string, flag):
    if flag:
        print(string)
    return

def numberOfOrders(data):
    '''
    [INPUT]: Order String [STR]
    [Output]: Order count [INT]
    '''
    printFlag = False

    TagBeginCount = data.count("<order>")
    TagEndCount = data.count("</order>")

    if (TagBeginCount != TagEndCount):
        sPrint("TagBeginCount is not equal to the TagEndCount.\n", printFlag)
    
    OrderCount = TagBeginCount
    sPrint("Number of Orders: " + str(OrderCount), printFlag)
    
    return OrderCount

