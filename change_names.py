import os

dir = 'videos'

for folder in os.listdir(dir):
    f = os.path.join(dir, folder)
    if os.path.isdir(f):
        vid_dir = f
        print(folder)
        c = 0
        for pic_name in os.listdir(vid_dir):
            pic_path = 'C:/Users/antda/Documents/Developments/ai/03_pills/videos' + '/' + folder + '/' + pic_name
            new_pic_path = 'C:/Users/antda/Documents/Developments/ai/03_pills/videos' + '/' + folder + '/'  + folder + '_' + str(c) + '.jpg'
            os.rename(pic_path, new_pic_path)
            c+=1
