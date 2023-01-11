import os
import csv

dir = 'jpg/from_videos'

with open('y.csv', "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for pic in os.listdir(dir):
        pic_loc =  "/".join([dir, pic])
        print(pic_loc)
        y = pic.split('_')[0]
        data = [pic_loc,y]
        writer.writerow(data)