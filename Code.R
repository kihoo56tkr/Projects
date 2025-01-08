setwd("C:/Users/Asus/Documents/NUS/Y1S2/ST1131")

###################################### Uploading of Data #####################################

data = read.csv("bike_day.csv")

attach(data)

# Factoring all Categorical Variables
data$season = factor(data$season)
data$weathersit = factor(data$weathersit)
data$workingday = factor(data$workingday)


############################## Part I - Exploring the Variables ##############################
################## Part 1.1 - Checking Normality of Response Variable ########################
boxplot(cnt)
hist(cnt, xlab = "Daily Count of Rental Bikes", main = "Histogram of Daily Count of Rental Bikes")
# It shows under-dispersed data

qqnorm(cnt)
qqline(cnt, col = "red")
# It shows under-dispersed data


# Part 1.2 - Checking for Possible Association between Response Variable and Other Variables #
plot(temp, cnt, xlab = "Temperature", ylab = "Daily Count of Rental Bikes")
cor(temp, cnt) # Positive Linear Association
plot(hum, cnt)
cor(hum, cnt) # Not observable linear association
plot(windspeed, cnt) 
cor(windspeed, cnt) # Not observable linear association

boxplot(cnt~season, xlab = "Season", ylab = "Daily Count of Rental Bikes") # Possible association
data$season = ifelse(data$season == "1", "1", "2-4")
boxplot(data$cnt~data$season, xlab = "Season", ylab = "Daily Count of Rental Bikes")

boxplot(cnt~weathersit, xlab = "Weather Situtation", ylab = "Daily Count of Rental Bikes") # Possible association
data$weathersit = ifelse(data$weathersit == "3", "3", "1-2") 
boxplot(data$cnt~data$weathersit, xlab = "Weather Situtation", ylab = "Daily Count of Rental Bikes")

boxplot(cnt~workingday) # Median and Range approximately the same - no association

# Testing of transformation of response variable
boxplot(log(cnt))
hist(log(cnt), xlab = "Daily Count of Rental Bikes", main = "Histogram of Daily Count of Rental Bikes")
# It shows left-skewed data with possible outliers
qqnorm(log(cnt))
qqline(log(cnt), col = "red")
# It shows left-skewed

boxplot(1/(cnt))
hist(1/(cnt), xlab = "Daily Count of Rental Bikes", main = "Histogram of Daily Count of Rental Bikes")
# It shows right-skewed data with possible outliers (alot)
qqnorm(1/(cnt))
qqline(1/(cnt), col = "red")
# It shows right-skewed data with possible outliers (alot)

boxplot(sqrt(cnt))
hist(sqrt(cnt), xlab = "Daily Count of Rental Bikes", main = "Histogram of Daily Count of Rental Bikes")
# It shows slightly left-skewed with possible outliers
qqnorm(sqrt(cnt))
qqline(sqrt(cnt), col = "red")
# It shows slightly left-skewed

################################### Part II - Building Model ###################################
# Model 1 - All Variables + All Interactions based on preliminary findings
model1 = lm(formula = sqrt(cnt) ~ season + workingday + weathersit + temp + hum + windspeed + season*workingday + season*weathersit + season*temp + season*hum + season*windspeed + workingday*weathersit + workingday*temp + weathersit*temp + weathersit*hum + weathersit*windspeed + temp*hum + temp*windspeed, data = data)
summary(model1)
anova(model1)

# Analysis for Model 1
raw.resM1 = model1$res
SR1 = rstandard(model1)
hist(SR1, xlab = "Standard Residuals for Model 1", main = "Graph of Standard Residuals for Model 1") # A Few outliers
qqnorm(SR1) # Possible outlier
qqline(SR1, col = "red")
plot(model1$fitted.values, SR1, xlab = "Predicted Values", ylab = "Standard Residuals for Model 1") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied

boxplot(SR1~data$season, xlab = "Season", ylab = "Standard Residuals for Model 1") # Most values are between -3 to 3 + Median is around same for all levels => constant var assumption satisfied
boxplot(SR1~data$workingday) # Most values are between -3 to 3 + Median is around same for all levels => constant var assumption satisfied
boxplot(SR1~data$weathersit) # Most values are between -3 to 3 + Median is around same for all levels => constant var assumption satisfied
plot(data$temp, SR1, xlab = "Temperature", ylab = "Standard Residuals for Model 1") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied
plot(data$hum, SR1) # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied
plot(data$windspeed, SR1) # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied

indexofout = which(SR1>3|SR1<(-3)) # index 87, 239
C1 = cooks.distance(model1)
influpt = which(C1>1) # index 69

# Model 2 - Model 1 but remove outliers & influential points
model2 = lm(formula = sqrt(cnt) ~ season + workingday + weathersit + temp + hum + windspeed + season*workingday + season*weathersit + season*temp + season*hum + season*windspeed + workingday*weathersit + workingday*temp + weathersit*temp + weathersit*hum + weathersit*windspeed + temp*hum + temp*windspeed, data = data[c(-69, -87, -239),])
summary(model2)
anova(model2)
# From Adjusted R-squared value: Removing points impact model (improves)

# Model 3: Removal of coefficients based on p-value from t-test (>0.05)
model3 = lm(formula = sqrt(cnt) ~ season + weathersit + temp + hum + windspeed + season*temp + weathersit*hum + weathersit*windspeed + temp*hum, data = data[c(-69, -87, -239),])
summary(model3)
anova(model3)
# Model 3.1: Removal of coefficients based on p-value from t-test (>0.01)
model3d1 = lm(formula = sqrt(cnt) ~ season + weathersit + temp + hum + windspeed + season*temp + weathersit*windspeed, data = data[c(-69, -87, -239),])
summary(model3d1)
# Model 3.2: Removal of coefficients based on p-value from t-test (>0.01)
model3d2 = lm(formula = sqrt(cnt) ~ season + temp + hum + windspeed + season*temp, data = data[c(-69, -87, -239),])
summary(model3d2)

# Model 4: Removal of outlier/influential points as p-values of coefficients seem stable (coefficients in Model 4 in same as Model 3.2)
model4 = lm(formula = sqrt(cnt) ~ season + temp + hum + windspeed + season*temp, data = data[c(-69, -87, -239),])
summary(model4)
anova(model4)

# Analysis for Model 4
raw.resM4 = model4$res
SR4 = rstandard(model4)
hist(SR4, xlab = "Standard Residuals for Model 4", main = "Graph of Standard Residuals for Model 4") # Outliers observed
qqnorm(SR4) # Outlier observed
qqline(SR4, col = "red")
plot(model4$fitted.values, SR4, xlab = "Predicted Values", ylab = "Standard Residuals for Model 4") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied

indexofout = which(SR4>3|SR4<(-3)) # index 668
C4 = cooks.distance(model4)
influpt = which(C4>1) # None

# Model 5: Further detection of outlier/influential points
model5 = lm(formula = sqrt(cnt) ~ season + temp + hum + windspeed + season*temp, data = data[c(-69, -87, -239, -668),])
summary(model5)
anova(model5)

# Analysis for Model 5
raw.resM5 = model5$res
SR5 = rstandard(model5)
hist(SR5, xlab = "Standard Residuals for Model 5", main = "Graph of Standard Residuals for Model 5") # Possible Outlier
qqnorm(SR5) # Possible Outlier
qqline(SR5, col = "red")
plot(model5$fitted.values, SR5, xlab = "Predicted Values", ylab = "Standard Residuals for Model 5")

indexofout = which(SR5>3|SR5<(-3)) #  index 328
C5 = cooks.distance(model5)
influpt = which(C5>1) # None

# Final Model
# Model 6
model6 = lm(formula = sqrt(cnt) ~ season + temp + hum + windspeed + season*temp, data = data[c(-69, -87, -239, -668, -328),])
summary(model6)
anova(model6)

# Analysis for Model 6
raw.resM6 = model6$res
SR6 = rstandard(model6)
hist(SR6, xlab = "Standard Residuals for Model 6", main = "Graph of Standard Residuals for Model 6") # All values are between -3 to 3 + Symmetrical & Bell-shaped => Normality satisfied
qqnorm(SR6) # Approximately Normal (Almost all points lie on QQ line but slight underdispered)
qqline(SR6, col = "red")
plot(model6$fitted.values, SR6, xlab = "Predicted Values", ylab = "Standard Residuals for Model 6") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied

boxplot(SR6~data[c(-69, -87, -239, -668, -328),]$season, xlab = "Season", ylab = "Standard Residuals for Model 6") # Most values are between -3 to 3 + Median is around same for all levels => constant var assumption satisfied
plot(data[c(-69, -87, -239, -668, -328),]$temp, SR6, xlab = "Temperature", ylab = "Standard Residuals for Model 6") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied
plot(data[c(-69, -87, -239, -668, -328),]$hum, SR6, xlab = "Humdity", ylab = "Standard Residuals for Model 6") # Most values are between -3 to 3 + Randomly scattered => constant var assumption satisfied

indexofout = which(SR6>3|SR6<(-3)) # None
C6 = cooks.distance(model6)
influpt = which(C6>1) # None

confint(model6)