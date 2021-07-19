import os
import shutil
from sklearn.model_selection import train_test_split

#path to images and labels (modify for convenience)
img_path = "Data_1000_yolov5/images"
label_path = "Data_1000_yolov5/labels"

# output directory for train and valid (modify for convenience)
train_img_dir = ("train/images")
train_lab_dir = ("train/labels")
valid_img_dir = ("valid/images")
valid_lab_dir = ("valid/labels")

# make a list of image names and label names from the source
img_data = os.listdir(img_path)
label_data = os.listdir(label_path)

# train_test_split function 
train_images, valid_images, train_labels, valid_labels = train_test_split(img_data, label_data, test_size=0.3, 
                                                         shuffle=True, random_state=20)

# Check the correlation b/w images and labels
print(train_images[0])
print(train_labels[0])
print(valid_images[0])
print(valid_labels[0])
print(len(train_images))
print(len(valid_images))

# delete if existing and create a new directory
if os.path.isdir(train_img_dir):
    shutil.rmtree(train_img_dir)
os.makedirs(train_img_dir)

if os.path.isdir(train_lab_dir):
    shutil.rmtree(train_lab_dir)
os.makedirs(train_lab_dir)

if os.path.isdir(valid_img_dir):
    shutil.rmtree(valid_img_dir)
os.makedirs(valid_img_dir)

if os.path.isdir(valid_lab_dir):
    shutil.rmtree(valid_lab_dir)
os.makedirs(valid_lab_dir)


# copy the image and label names from the source dataset
for name in train_images:
    source = img_path + "/" + name
    destination = train_img_dir + "/" + name
    shutil.copy(source, destination)

for name in train_labels:
    source = label_path + "/" + name
    destination = train_lab_dir + "/" + name
    shutil.copy(source, destination)

for name in valid_images:
    source = img_path + "/" + name
    destination = valid_img_dir + "/" + name
    shutil.copy(source, destination)

for name in valid_labels:
    source = label_path + "/" + name
    destination = valid_lab_dir + "/" + name
    shutil.copy(source, destination)

print("Split success")
