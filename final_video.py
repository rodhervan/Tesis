import cv2
import numpy as np
import glob
import os

img_array = []

# # # Using global path to folder
# folder_path = 'D:........./Fully_processed/20230807'
# if os.path.exists(folder_path):
#     direction = glob.glob(f'{folder_path}/*.png')
# else:
#     print(f"Folder '{folder_path}' does not exist.")

# # # Using a relative path instead of an absolute path
folder_path = 'Fully_processed/20230807'
folder_path = os.path.join(os.getcwd(), folder_path)
if os.path.exists(folder_path):
    direction = glob.glob(os.path.join(folder_path, '*.png'))
else:
    print(f"Folder '{folder_path}' does not exist.")

for filename in direction:
    img = cv2.imread(filename)
    # cv2.putText(img, os.path.basename(filename), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
fps = 30
os.makedirs('Generated_videos', exist_ok=True)
out = cv2.VideoWriter('Generated_videos/' + folder_path[-8:] + '.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()