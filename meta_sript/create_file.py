import os
#import subprocess

#for i in range(1, 51):
#	os.mkdir('/home/xiaofeng/Desktop/Practice_Repo/Practice/' + str(i))

for i in os.listdir('/home/xiaofeng/Desktop/Practice_Repo/Practice/'):
    try:
        if (int(i) < 55):
            os.remove(os.path.join('/home/xiaofeng/Desktop/Practice_Repo/Practice/', i ,"test"))
            fp = open(os.path.join('/home/xiaofeng/Desktop/Practice_Repo/Practice/', i, "python"), 'w')
            fp = open(os.path.join('/home/xiaofeng/Desktop/Practice_Repo/Practice/', i, "cpp"), 'w')
    except Exception as No_Name:
	pass

