import  rcute_cozmars.util as util
import numpy as np
import cv2
o=cv2.imread('./extBG.jpeg')
o=cv2.resize(o,(600,372))
on=cv2.bitwise_not(o)
i=cv2.imread('./eye.png',cv2.IMREAD_UNCHANGED)
i=cv2.resize(i,(200,200))
z=np.zeros((*o.shape[:2],4), np.uint8)
y=np.zeros((*o.shape[:2],3), np.uint8)
zw,zh=z.shape[:2][::-1]
iw,ih=i.shape[:2][::-1]
y[:,:]=util.bgr('orange')
z[(zh-ih)//2:(zh+ih)//2,(zw-iw)//2:(zw+iw)//2]=i
added_image = cv2.addWeighted(o,0.25,y,1,0)
added_image[np.where(z[:,:,3]!=0)]=0
cv2.imwrite('./eye.png',added_image)