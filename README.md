# DSAI-HW1-Peak-Load-Forecasting
DSAI HW1 Peak Load Forecasting


資料集使用 : 2017/01/01-2019/03/31 台灣電力公司_過去電力供需資訊並且創立新的DataFrame 將日期當作index 並輸入對應的 尖峰負載(MW)

預測模型採用 : 時間序列模型 statsmodels的 差分整合移動平均自迴歸模型(整合移動平均自回歸模型ARIMA(Autoregressive Integrated Moving Average))

ARIMA模型是由兩種模型組合分別為自迴歸模型AR（Autoregressive model）與 移動平均模型MA(Moving Average model)所合併

根據所識別出來的特徵建立相應的時間序列模型。平穩化處理後，若偏自相關函數是截尾的，而自相關函數是拖尾的，則建立AR模型；若偏自相關函數是拖尾的，而自相關函數是截尾的，則建立MA模型；若偏自相關函數和自相關函數均是拖尾的，則序列適合ARMA模型


ARIMA（p，d，q）中，AR是"自回歸"，p為自回歸項數；MA為"滑動平均"，q為滑動平均項數，d為使之成為平穩序列所做的差分次數

而此次預測的 尖峰負載(MW) 本身即為一個平穩序列 所以不須再去做差分 因此參數d為0

經由ACF與PACF圖 觀察LAG數猜測其p q 參數為5 3(此處可以使用迴圈測試所有p q 的排列組合來找出最佳參數)

最後將參數代入模型預測電量  (除了p d q參數外，這裡可以增加seasonal參數，利用季節性去增加預測準確度)

https://nbviewer.jupyter.org/github/TMHAlex/DSAI-HW1-Peak-Load-Forecasting/blob/master/HW1/app.ipynb
