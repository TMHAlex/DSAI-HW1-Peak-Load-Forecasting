# DSAI-HW1-Peak-Load-Forecasting
DSAI HW1 Peak Load Forecasting


資料集使用 : 2017/01/01-2019/03/31 台灣電力公司_過去電力供需資訊並且創立新的DataFrame 將日期當作index 並輸入對應的 尖峰負載(MW)

預測模型採用 : 時間序列模型 statsmodels的 差分整合移動平均自迴歸模型(整合移動平均自回歸模型ARIMA(Autoregressive Integrated Moving Average))
