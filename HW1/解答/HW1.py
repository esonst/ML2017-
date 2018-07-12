
# coding: utf-8

# In[65]:


import csv 
import numpy as np
from numpy.linalg import inv
import random
import math
import sys


# ## read data

# In[66]:


data=[]
for i in range(18):
    data.append([])
n_row = 0
with open(r'../题目/train.csv', 'r', encoding='big5') as text: 
    row = csv.reader(text , delimiter=",")
    for r in row:
        # 第0列沒有資訊
        if n_row != 0:
            # 每一列只有第3-27格有值(1天內24小時的數值)
            for i in range(3,27):
                if r[i] != "NR":
                    data[(n_row-1)%18].append(float(r[i]))
                else:
                    data[(n_row-1)%18].append(float(0))	
        n_row = n_row+1


# ## parse data to (x,y)

# In[67]:


x=[]
y=[]
for i in range(12):
    for j in range(471):
        x.append([])
        for t in range(18):
            for s in range(9):
                x[471*i+j].append(data[t][480*i+j+s])
        y.append(data[9][480*i+j+9])
x=np.array(x)
y=np.array(y)


# ## init weight & other hyperparams

# In[68]:


w=np.zeros(len(x[0]))
l_rate=10
repeat=10000


# ## check your ans with close form solution

# In[69]:


# use close form to check whether ur gradient descent is good
# however, this cannot be used in hw1.sh 
# w = np.matmul(np.matmul(inv(np.matmul(x.transpose(),x)),x.transpose()),y)


# ## start training

# ### linear regression function
# $$\widehat{y}=\sum_{i=1}^m \omega_ix_i+b$$
# ### gradient+regularization+adagrad
# $$\theta^`=\sum_{i=1}^m x_i$$

# In[70]:


def train(x,y,w):
    x_t=x.transpose()
    s_gra=np.zeros(len(x[0]))

    for i in range(repeat):
        hypo=np.dot(x,w)                        
        loss=hypo-y
        cost=np.sum(loss**2)/len(x)
        cost_a=math.sqrt(cost)
        gra=np.dot(x_t,loss)
        # s_gra是什么东西
        s_gra += gra**2
        ada = np.sqrt(s_gra)
        w = w - l_rate * gra/ada
        print ('iteration: %d | Cost: %f  ' % ( i,cost_a))
    return w
w=train(x,y,w)


# save/read model

# In[71]:


# save model
np.save('model.npy',w)
# read model
w = np.load('model.npy')


# read testing data

# In[82]:


test_x = []
n_row = 0
text = open(r'../题目/test.csv' ,"r")
row = csv.reader(text , delimiter= ",")

for r in row:
    if n_row %18 == 0:
        test_x.append([])
        for i in range(2,11):
            test_x[n_row//18].append(float(r[i]) )
    else :
        for i in range(2,11):
            if r[i] !="NR":
                test_x[n_row//18].append(float(r[i]))
            else:
                test_x[n_row//18].append(0)
    n_row = n_row+1
text.close()
test_x = np.array(test_x)

# add square term
# test_x = np.concatenate((test_x,test_x**2), axis=1)

# add bias


# get ans.csv with your model 

# In[84]:


ans = []
for i in range(len(test_x)):
    ans.append(["id_"+str(i)])
    a = np.dot(w,test_x[i])
    ans[i].append(a)

filename = "predict.csv"
text = open(filename, "w+")
s = csv.writer(text,delimiter=',',lineterminator='\n')
s.writerow(["id","value"])
for i in range(len(ans)):
    s.writerow(ans[i]) 
text.close()


# In[83]:


test_x

