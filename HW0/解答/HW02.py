
# coding: utf-8

# # 图片处理

# In[1]:


import numpy


# In[2]:


from PIL import Image
img=Image.open(r'..\题目\westbrook.jpg')


# In[3]:


matrix = numpy.asarray(img)
ss=(matrix/2).astype(int)


# In[4]:


image = Image.fromarray(ss.astype(numpy.uint8))


# In[5]:


image.show()

