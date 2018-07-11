
# coding: utf-8

# # 图片处理

# In[10]:


import numpy


# In[11]:


from PIL import Image
img=Image.open('westbrook.jpg')


# In[46]:


matrix = numpy.asarray(img)
ss=(matrix/2).astype(int)


# In[51]:


image = Image.fromarray(ss.astype(numpy.uint8))


# In[52]:


image.show()

