#!/usr/bin/env python
# coding: utf-8

# In[36]:


# print("Enter")
patient_name = input("Enter patient's name : ")
upload = input("Enter the address of the image : ")


# In[38]:


import imageio
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
pic = imageio.imread(upload)
plt.figure(figsize=(5,5))
plt.imshow(pic)


# In[39]:


import cv2
import numpy as np
image = cv2.imread(upload,cv2.IMREAD_UNCHANGED)
print(image.shape)
image[:,:,0] = np.zeros([image.shape[0],image.shape[1]])
# cv2.imwrite(upload,image)
plt.imshow(image)


# In[ ]:





# In[ ]:





# In[ ]:




