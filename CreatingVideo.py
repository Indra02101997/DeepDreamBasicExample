import cv2
import os

dream_name="starry_night"
dream_path="D://Personal Files/Python Programs/Unconventional Neural Networks/deep_dreaming_start/dream/{}".format(dream_name)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('{}.avi'.format(dream_name),fourcc,10.0,(800,450))

length=51
for i in range(length+1):
    img_path=os.path.join(dream_path,'img_{}.jpg'.format(i))
    print(img_path)
    frame=cv2.imread(img_path)
    out.write(frame)

out.release()
