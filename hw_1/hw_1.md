#### Needed libraries
```r
install.packages("TTR")
library("TTR")
```

### Problem 1 ###

#### Simulate a completely random process of length 100 with independent, normal values. Plot the time series plot. Does it look random? Discuss if it follows any pattern, seasonality, and cyclic.

```r
plot(main='Problem 1', as.ts(rnorm(100)))
```

![fig1](https://github.com/vladdoster/t_s/blob/master/hw_1/figs/p1.png)

Seems to be randomly distributed. Has no dicernable pattern
that I can see. Seems to similar to a sine wave but with no real pattern. It is random.

### Problem 2 ###

#### Simulate a completely random process of length 50 with independent, chi-square distributed values, each with 2 degrees of freedom. Display the time series plot. Does it look random and non normal?

```r
plot(main='Problem 2', as.ts(rchisq(n=50, df=2)))
```

![fig1](https://github.com/vladdoster/t_s/blob/master/hw_1/figs/p2.png)

It does not look normal because it is chisquared, there is a cylical pattern created.


### Problem 3 ###
#### Simulate a completely random process of length 50 with independent, t-distributed values each with 5 degrees of freedom. Construct the time series plot. Does it look random and non normal?

```r
plot(main='Problem 3', as.ts(rt(48, 5)))
```

![fig1](https://github.com/vladdoster/t_s/blob/master/hw_1/figs/p3.png)


### Problem 4 ###
#### Describe your data set, what is it and where it come from.
Time series I chose was kings dataset about lifespans.
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
![fig1](https://github.com/vladdoster/t_s/blob/master/hw_1/figs/p4.png)

By smoothing the data, we can see that after the first 20 kings, lifespans increased which gives us insight
about possible technological or medicine advances. This could give historians a easy way to boil down periods of history to look at.

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
