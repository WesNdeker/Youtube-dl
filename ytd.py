#######
##Creator Zanuar
### #####
import csv
import os
import sys
import time
os.system("clear")
print ("\33[37;1m[*]Welcome To My Tools");
time.sleep (2);
#Buatnya Susah Anjing
#Jadi Jangan Direcode Ya Asu!!
print ("\33[31;1m[*]wait a few minutes for the fixing of the material :D ");
time.sleep(2);
os.sytem("pip install -U pip");
os.sytem("pip install pytube");
print ("\33[33;1m==>Thx For Install My Tools");
time.sleep(4);
os.system("clear")
from pytube import YouTube
time.sleep (3);
print ("\33[33;1m__      __  ________   ______     _____  ");
print ("\33[33;1m) \    / ( (___  ___) (_  __ \   (_   _)     ");
print ("\33[33;1m \ \  / /      ) )      ) ) \ \    | |    ");   
print ("\33[33;1m  \ \/ /      ( (      ( (   ) )   | |       ")
print ("\33[36;1m   \  /        ) )      ) )  ) )   | |   __  ");
print ("\33[36;1m    )(        ( (      / /__/ /  __| |___) ) ");
print ("\33[36;1m   /__\       /__\    (______/   \________/  ");                                            
time.sleep (2);
print ("\33[32;1m<==============================================>");
print ("\33[35;1m==>Tools   : \33[0;34mYt Downloader");
print ("\33[35;1m==>Creator : \33[0;34mZanuar");
print ("\33[35;1m==>IG      : \33[0;34m@Zanuar_f.19");
print ("\33[35;1m==>Github  : \33[0;34mhttps://github.com/WesNdeker");
print ("\33[32;1m<===============================================>");
print
#Tapi Boleh Pelajari Source Codenya :)
#Baik Kan Gw Cok :D
print("\33[31;1mEx> Link = https://youtu.be/MHSukrqxudU")
url = input("\33[34;1mLink : \33[32;1m");
yt = YouTube(url);
print("Title: ",yt.title);
yts = yt.streams.get_highest_resolution()
print("\nDownloading...")
yts.download()
print("\nDownload completed!!")
print()