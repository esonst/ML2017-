
# coding: utf-8

# # 作业0：词频统计

# ## 打开文件

# In[39]:


with open('words.txt') as f:
    ans=""+f.read()[:-1]#去掉“\n”符号


# In[40]:


"""
本函数判断字符a是否存在于列表index中，并完成频率统计。返回值为a在index中是否存在。
a: 待匹配词

"""
def checkin (a,index,freq):
    for ind in range(len(index)):
        if(a==index[ind]):
            freq[ind]+=1
            return True
    return False


# index: 待匹配列表
# 
# freq: 对应词频率

# In[41]:


index=[]
freq=[1]*len(ans.split(" "))
for i in ans.split(" "):
    if not checkin(i,index,freq):
        index.append(i)


# In[49]:


#输出
for i in range(len(index)):
    print(index[i],i,freq[i] )

