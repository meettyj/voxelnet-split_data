# import os
import shutil

with open("./ImageSets/" + "train.txt", 'r') as f:
    for line in f.readlines():
        shutil.copy("./data_object_image_2/training/image_2/"+line[:-1]+".png", "./training/image_2/")
        shutil.copy("./data_object_label_2/training/label_2/"+line[:-1]+".txt", "./training/label_2/")
        shutil.copy("./data_object_velodyne/training/velodyne/"+line[:-1]+".bin", "./training/velodyne/")
with open("./ImageSets/" + "val.txt", 'r') as f:
    for line in f.readlines():
        shutil.copy("./data_object_image_2/training/image_2/"+line[:-1]+".png", "./validation/image_2/")
        shutil.copy("./data_object_label_2/training/label_2/"+line[:-1]+".txt", "./validation/label_2/")
        shutil.copy("./data_object_velodyne/training/velodyne/"+line[:-1]+".bin", "./validation/velodyne/")
