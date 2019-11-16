import  os
import re

file_list = os.listdir("C:/Users/Abhinav/Downloads")

Others = list()
EEE = list()
HUM = list()
PHY = list()
CSE = list()
MAT = list()
for file in file_list:
    if 'EEE' in file:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/EEE  1001 Stuff/EEE 1001  Downloads/" + file
        os.replace(initial, final)
        file_list.remove(file)
    elif 'HUM' in file:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/HUM 1021/HUM  1021 Downloads/" + file
        os.replace(initial, final)
    elif 'PHY' in file:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/PHY 1701 Stuff/Physics 1701 Downloads/" + file
        os.replace(initial, final)
        file_list.remove(file)
    elif 'CSE' in file:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/CSE 1001 Stuff/CSE 1001 Downloads/" + file
        os.replace(initial, final)
        file_list.remove(file)
    elif 'MAT' in file:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/MAT 1011 Stuff/MAT  1011 Downloads/" + file
        os.replace(initial, final)
        file_list.remove(file)
    """else:
        initial = "C:/Users/Abhinav/Downloads/" + file
        final = "C:/Users/Abhinav/OneDrive/Desktop/Class Material/Misc/" + file
        os.replace(initial, final)
        file_list.remove(file)"""
"""print(file_list)
print(pdfs)
print(word)
print(other)"""
