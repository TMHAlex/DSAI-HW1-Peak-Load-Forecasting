#!/usr/bin/env python
# coding: utf-8

# ##### 套件載入

# In[23]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.api import tsa 


# ##### 資料載入並且轉換日期欄位的格式

# In[24]:


inputDATA1 = pd.read_csv("20171120171231.csv")
inputDATA2 = pd.read_csv("台灣電力公司_過去電力供需資訊.csv")
inputDATA = pd.concat([inputDATA1,inputDATA2], ignore_index=True, sort=False)
inputDATA.drop_duplicates("日期" , inplace=True)
inputDATA.reset_index(drop=True ,inplace=True)
inputDATA["日期"] = pd.to_datetime(inputDATA["日期"], format="%Y%m%d")

#TWtest = pd.read_csv("台灣電力公司_未來一週電力供需預測.csv",encoding = "big5")
#TWtest["日期(年/月/日)"] = pd.to_datetime(TWtest["日期(年/月/日)"], format="%Y/%m/%d")
#print(inputDATA1.head())
#print(inputDATA2.head())
#inputDATA
#appenMarch
#TWtest


# ##### 手動新增3月份資料並且併入    新增DateFrame 格式的 trainDatePL變數 由日期當作index column資料為尖峰負載 

# In[25]:


appenMarch = pd.DataFrame(index = pd.date_range("2019-3-1", periods=31) , columns = ["尖峰負載(MW)"])
newnumber = ["24689","24734","24102","27688","28241","28032","28147","27951","25870","24801",
             "27730","27936","28145","28417","27757","25318","24681","28338","28882","29645",
             "30343","29618","25265","24812","28535","28756","29140","30093","29673","25810","24466"]
newnumber = pd.Series(newnumber)
appenMarch["尖峰負載(MW)"] = newnumber.values.astype(np.float32)

#X_train, X_test = train_test_split(inputDATA, test_size=0.1,shuffle=False)
#X_trainDate = X_train["日期"].values
#X_trainPL = X_train["尖峰負載(MW)"].values.astype(np.float32)
#trainDatePL = pd.DataFrame(index = X_trainDate)
#trainDatePL["尖峰負載(MW)"]=X_trainPL

#X_testDate = X_test["日期"].values
#X_testPL = X_test["尖峰負載(MW)"].values.astype(np.float32)
#testDatePL = pd.DataFrame(index = X_testDate)
#testDatePL["尖峰負載(MW)"]=X_testPL

inputDate = inputDATA["日期"].values
inputDATAPL = inputDATA["尖峰負載(MW)"].values.astype(np.float32)
trainDatePL = pd.DataFrame(index = inputDate)
trainDatePL["尖峰負載(MW)"]=inputDATAPL
trainDatePL = pd.concat([trainDatePL,appenMarch], sort=False)

#trainDatePL.plot()
#plt.show()
#trainDatePL
#plot_acf(trainDatePL).show()
#plot_pacf(trainDatePL).show()

#trainDatePL


# ###### 觀察acf pacf圖 確認order參數(因為是穩地態所以不用做差分處理)

# In[26]:


arima = ARIMA(trainDatePL, order=(5, 0, 3))
result = arima.fit(disp=True)
resid = result.resid
r, q, p = tsa.acf(resid.values.squeeze(), qstat=True)
pred = result.predict("20190401", "20190409")
print(pred)
#plt.plot(trainDatePL)
#plt.plot(pred , color="red")
#plt.plot(trainDatePL["20180401":"20180409"] , color="black")
#plt.show()
pred.iloc[1:8].to_csv("submission.csv")


# In[13]:


#print(pred)
#plt.plot(pred.iloc[32:40])
#plt.plot(pred)
#plt.show()


# In[14]:


#plt.plot(pred,color="red")
#plt.plot(TWtest["日期(年/月/日)"],TWtest["預估淨尖峰供電能力(萬瓩)"] , color="black")
#plt.show()


# In[15]:


#print(np.sqrt(metrics.mean_squared_error(pred.values,trainDatePL["20180401":"20180409"]["尖峰負載(MW)"].values)))


# In[16]:


#print(np.sqrt(metrics.mean_squared_error(pred.iloc[1:9].values,TWtest["預估淨尖峰供電能力(萬瓩)"].values)))

