#### Needed libraries
```r
install.packages("TTR")
library("TTR")
```

### Problem 1 ###
plot(main='Problem 1', as.ts(rnorm(100)))
Seems to be randomly distributed. Has no dicernable pattern
that I can see. Seems to similiar to a sine wave but with no real pattern.

### Problem 2 ###
plot(main='Problem 2', as.ts(rchisq(n=50, df=2)))

### Problem 3 ###
plot(main='Problem 3', as.ts(rt(48, 5)))

### Problem 4 ###
#### Describe your data set, what is it and where it come from.
Time series I chose was kings dataset
This dataset was chosen after looking for cool time series ds.
This one is cool because you can see how long kings lasted for over time.
```r
kings <- scan("http://robjhyndman.com/tsdldata/misc/kings.dat",skip=3)
ts_king <- ts(kings)
```

## Give a summary statistics about the data set.

| Min.  | 1st Qu. | Median |    Mean 3rd Qu.   |  Max. |
| ----  | ------- | ------ | ----------------- | ----- |
| 13.00 |  44.00  |  56.00 |    55.29   67.75  | 86.00 |

```r
summary(ts_king)
plot(main='Problem 4 king ts', ts_king)
```

# By smoothing the data, we can see that after the first 20 kings,
# lifespans increased
```r
sma8_kts <- SMA(ts_king,n=8)
plot.ts(main='Problem 4 king ts SMA=8', sma8_kts)
```

The data is not stationary as it has a fluctuating mean and std dev 
which is due to the lack of stability around those times and how if a king did
not please his people, they would rebel. Kings did not last a long time.

### Problem 5 ###
#### Simulation 100 such observation of Yt and plot a time series plot.
Not too sure.

#### E[Yt]?
Not too sure.

#### Does the variance look constant?
Yes the variance looks the same due to the dataset being iid.

#### Is it stationary? Why? or Why not?
Yes, because it is iid with zero mean iid.