from google.colab import files
from IPython.display import Image
upload=files.upload()

#Image('images.png')
Image('images.png', height=250, width=250)


from PIL import Image
img=Image.open('images.png')
img=img.resize((200,200))
display(img)


import cv2
from matplotlib import pyplot as plt
img=cv2.imread('images.png')
plt.imshow(img)
plt.show()
img1=img[:,:,::-1]
plt.imshow(img1)
plt.show()


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
