# 1
```
par(mfrow=c(3,1)) # 3x1 figure matrix
plot(acf(arima.sim(model=list(ma=c(.5,.4)), n=100), plot = FALSE), main="1a")
plot(acf(arima.sim(model=list(ma=c(1.2,-.7)), n=100), plot = FALSE), main="1b")
plot(acf(arima.sim(model=list(ma=c(-1,-.6)), n=100), plot = FALSE), main="1c")
```
<div align="center">
        
![](https://github.com/vladdoster/t_s/blob/master/p1.png)

</div>

# 2
```
par(mfrow=c(3,1)) # 3x1 figure matrix
plot(acf(arima.sim(model=list(ar=c(.6)), n=100), plot = FALSE), main="2a")
plot(acf(arima.sim(model=list(ar=c(.95)), n=100), plot = FALSE), main="2b")
plot(acf(arima.sim(model=list(ar=c(.4), ma=c(.5)), n=100), plot = FALSE), main="2c")
```
<div align="center">
        
![](https://github.com/vladdoster/t_s/blob/master/p2.png)

</div>

# 3
```
#install.packages("TSA")
#install.packages("forecast")
library("forecast")
library("TSA")
```
### 3a
```
data(tempdub)
plot(tempdub, main="Temp Dub TS")     
plot(decompose(tempdub))
```

<div align="center">
        
![](https://github.com/vladdoster/t_s/blob/master/3a.png)
![](https://github.com/vladdoster/t_s/blob/master/3a1.png)

</div>

### 3b
```
td_acf<-acf(tempdub, lag.max=30, plot = FALSE)
plot(td_acf, main="ACF to 30 lags")
```
<div align="center">
        
![](https://github.com/vladdoster/t_s/blob/master/3b.png)

</div>

### 3c
```
auto.arima(tempdub)
```
#### output
```
Series: tempdub 
ARIMA(0,0,0)(2,1,0)[12] 
Coefficients:
        sar1     sar2
      -0.5403  -0.3078
s.e.   0.0906   0.0937

sigma^2 estimated as 17.25:  log likelihood=-376.58
AIC=759.17   AICc=759.35   BIC=767.81
```

##### You would use an ARIMA model of AR=2, D=1, and MA=0 to
##### model the tempdub dataset

### 3d
```
training<-head(tempdub,.75*length(tempdub))
testing<-tail(tempdub,.25*length(tempdub))
t<-arima(training, c(0,0,0), seasonal=list(order=c(2,1,0), period=12))
predicted<-predict(t, 36)$pred
plot(tempdub, main="Predicted tempdub values in red")
points(predicted, col="red", type="l")
```
<div align="center">
        
![](https://github.com/vladdoster/t_s/blob/master/3d.png)

</div>

### 3e
```
mean((testing-predicted)^2)
```

#### output
```
[1] 22.34734
```
