from tkinter import *

class EntryVerification :
    def __init__(self):
        pass

    def Verification(self,data):
        if data.isdigit() :
            return True
        else :
            return False
