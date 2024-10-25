#Module Code: B9DA101 | Module Title: Statistics for Data Analytics | School: DBS
#Lecturer Name: Dr. Muhammad Alli
#To be completed by date: Thursday, 31st October 2024, 11:55 PM
#Student Name: Sandeep Kumar | Student ID: 20049275 | Email: 20049275@mydbs.ie | Git: https://github.com/sandeepkumar-84/DBS.git

#Installing all the necessary packages and importing the libraries.

install.packages('tidyverse')
install.packages("fitdistrplus")
install.packages("ggcorrplot")
install.packages("reshape2")
library('tidyverse')
library(ggplot2)
library(dplyr)
library(fitdistrplus)
library(reshape2)
library(ggcorrplot)

#Load the dataset 

dsVehAll <- read.csv("C:/AssignmentFiles/VehicleDataV3.csv")

#Taking the vehicle data set (downloaded from kaggle).
#dsVeh <- VehicleDataV3[0:20000,]
dsVeh <- dsVehAll[0:20000,]
head(dsVeh)

#Summarizing each column of the dataset
summary(dsVeh)

#Structure of the dataset is determined using 

str(dsVeh)

#Question 1 - (a)	Describe the dataset using appropriate plots/curves/charts,

  #Histogram of the sellingprice column of the dataset.
hist(dsVeh$sellingprice, xlab = "Selling Price", ylab = "Frequency", xlim = c(0,80000), 
     main = "Distribution of Selling Price", col = "blue")

#Plotting of the selling price based on year. Different transmission can be recongnized by distinct colors.
ggplot(data = dsVeh, aes(x = year , y = sellingprice)) +
  geom_point(mapping = aes(x=year, y=sellingprice, color=transmission))

#Seperate plots of the selling prices v/s year based on transmission
ggplot(data = dsVeh, aes(x = year , y = sellingprice)) +
  geom_point(mapping = aes(x=year, y=sellingprice, color=transmission)) +
  facet_wrap(~transmission, nrow=2)

#Bar plotting of the selling price against year
ggplot(data = dsVeh, aes(x = year , y = sellingprice, fill=year)) +
  geom_bar(stat="identity")

#Scatter plot of selling price based on two different transmission.

ggplot(data = dsVeh, aes(x = transmission,  y = sellingprice, color="red")) +
  geom_point()

#Scatter plot of selling price based on different makes.
ggplot(data = dsVeh, aes(x = make,  y = sellingprice)) +
  geom_point()

#Summary Plot of the selling price data against the year variable ofthe data set.
ggplot(data = dsVeh) +
  stat_summary(
    mapping = aes(x = year, y = sellingprice),
    fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )

#Pie Chart distribution of the different transmission in the dataset.
ggplot(dsVeh, aes(x="", y=transmission, fill=transmission)) +
  geom_bar(stat="identity", width=1) + coord_polar("y", start=0)


#Correlation map - visualizing the correlation between the year, mmr, odomoeter and sellinprice. 
# This helps understand the relation between them. 

cor_data <- dsVeh[c('sellingprice', 'mmr', 'odometer', 'year' )]

correlation_matrix <- cor(cor_data)

melted_cormat <- melt(correlation_matrix)

ggplot(data = melted_cormat, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile(color = "white") + 
  scale_fill_gradient2(low = "blue", high = "red", mid = "white",
                       midpoint = 0, limit = c(-1, 1), space = "Lab",
                       name = "Correlation") +
  geom_text(aes(label = round(value, 2)), color = "black", size = 4) + 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1, size = 12),
        axis.text.y = element_text(size = 12),
        plot.title = element_text(hjust = 0.5, face = "bold", size = 16)) +
  labs(title = "Correlation Map", x = "Vehicle Data", y = "Vehicle Data") +
  coord_fixed()

#Question 1 (b)	Consider one of continuous attributes, and compute central and variational measures.

# Considered "sellingprice" column of the Vehicle Dataset for calculation of the Central and variational measures. "sellingprice" can take any value (real) in a given range where range can be infinte.
# 
# "find_mode()" function takes the column data as input parameter and calculate and returns mode of that data.
# 
# "find_central_tendency" takes in column data as input parameter and calculate mean, median and for mode calls "find_mode()" and returns all the results in the form of column to the caller.
# 
# "find_variance" takes in column data as input parameter and calculate variance, standard deviation, range, InterQuantileRange and returns all the results as a column.
# 
# "find_centralTendency_and_variance" internally calls all the above functions to calculate and display the central measures and variance parameters together

find_mode <- function(colData)
{
  tblColData = table(colData)
  mode = names(tblColData)[which(tblColData==max(tblColData))]
  mode
}

find_central_tendency <- function(colData)
{
  mode <- find_mode(colData)
  mean <- mean(colData)
  median <- median(colData)
  return(c(mode, mean, median))
}

find_variance <- function(colData)
{
  varData <- var(colData)
  stndDev <- sd(colData)
  range <- max(colData) - min(colData)
  iqr <- IQR(colData)
  return (c(varData,stndDev,range,iqr))
}

find_centralTendency_and_variance <- function(dataColumn)
{
  print("Mode, Mean & Median of dataset are")
  for (x in find_central_tendency(dataColumn))
  {
    print(x)
  }
  print("Variance, standard deviation, range and IQR of dataset are")
  for (x in find_variance(dataColumn))
  {
    print(x)
  }
}

find_centralTendency_and_variance(dsVeh$sellingprice)

#The central measures and variance parameters are calculated again so that they can be 
#assigned into their respective variables so that they can be utilized in further calculations.

dsVehSp = dsVeh$sellingprice

modeSellingPrice = find_mode(dsVehSp)
print(paste("The mode of the Selling Price Column = ", modeSellingPrice))

dsVehMean = mean(dsVehSp)
print(paste("The mean of the Selling Price Column = ", dsVehMean))

dsVehMedian = median(dsVehSp)
print(paste("The median of the Selling Price Column = ", dsVehMedian))

dsVehRange = max(dsVehSp) - min(dsVehSp)
print(paste("The max of Selling Price Column = ", max(dsVehSp)))
print(paste("The min of the Selling Price Column = ", min(dsVehSp)))
print(paste("The range of the Selling Price Column = ", dsVehRange))

QSellingPrice = quantile(dsVeh$sellingprice)
print("Quantile of the Selling Price column is ")
QSellingPrice

QSellingPrice1 = QSellingPrice[2]
print("First Quantile of the Selling Price column is ")
QSellingPrice1

QSellingPrice3 = QSellingPrice[4]
print("Third Quantile of the Selling Price column is ")
QSellingPrice3

IQRSellingPrice = QSellingPrice3 - QSellingPrice1
print("IQR of the Selling Price column is ")
IQRSellingPrice

dsVehStndDev = sd(dsVehSp)
print("Standard Deviation of the Selling Price column is ")
dsVehStndDev

dsVehVar = var(dsVehSp)
print("Variance of the Selling Price column is ")
dsVehVar

#Question 1 (c)	For a particular variable of the dataset, use Chebyshev's rule, and propose one-sigma interval. 
#Based on your proposed interval, specify the outliers if any.  

# According to Chebyshev''s theorem for any distribution (bell shaped or non bell shaped) at 
# least (1 - 1\k**2) proportion of values lies within k standard deviation for k > 1.
# 
# To find outliers
# Find the lower bound = mean - k * standard dev
# Find the upper bound = mean + k * standard dev
# outliers will be found below the lower bound value and above the upper bound
# outliers within k = 1 ( 1 * standard dev ) will be

k = 1
lowerRange = dsVehMean - k * dsVehStndDev
upperRange = dsVehMean + k * dsVehStndDev
print(paste("Taking k = 1, the lower range of sellingprice = ",round(lowerRange, 2)))
print(paste("Taking k = 1, the upper range of sellingprice = ",round(upperRange, 2)))


outliers = dsVehSp < lowerRange | dsVehSp > upperRange

totalOutliers =  sum(outliers)
print(paste("Total Outliers = ", totalOutliers))

dsVehSellingPriceLowerRange =  filter(dsVeh, sellingprice < lowerRange)
dsVehSellingPriceUpperRange =  filter(dsVeh, sellingprice > upperRange)

print(paste("Lower Range Outliers Count = ", count(dsVehSellingPriceLowerRange)))
print(paste("Upper Range Outliers Count ", count(dsVehSellingPriceUpperRange)))
print(paste("Total Outliers = ", count(dsVehSellingPriceLowerRange) + count(dsVehSellingPriceUpperRange)))


#For k = 1, Mean is shown below in red line, the standard deviation is shown as yellow line.

hist(dsVehSp, xlab = "Vehicle Selling Price", ylab = "Frequency", main="Distribution of Selling Price" , 
     xlim = c(0, 100000))
abline(v = mean(dsVehSp), col='red', lwd = 3)
abline(v = lowerRange, col='yellow', lwd = 3)
abline(v = upperRange, col='yellow', lwd = 3)

k = 2
lowerRangeK2 = dsVehMean - k * dsVehStndDev
upperRangeK2 = dsVehMean + k * dsVehStndDev
print(paste("Taking k = 2, the lower range of sellingprice = ",round(lowerRangeK2, 2)))
print(paste("Taking k = 2, the upper range of sellingprice = ",round(upperRangeK2, 2)))

outliersK2 = dsVehSp < lowerRangeK2 | dsVehSp > upperRangeK2
totalOutliersK2 =  sum(outliersK2)
print(paste("Total Outliers for k=2 = ", totalOutliersK2))

dsVehSellingPriceLowerRangeK2 =  filter(dsVeh, sellingprice < lowerRangeK2)
dsVehSellingPriceUpperRangeK2 =  filter(dsVeh, sellingprice > upperRangeK2)

print(paste("Lower Range Outliers Count for k = 2= ", count(dsVehSellingPriceLowerRangeK2)))
print(paste("Upper Range Outliers Count for k = 2", count(dsVehSellingPriceUpperRangeK2)))
print(paste("Total Outliers for k = 2  ", count(dsVehSellingPriceLowerRangeK2) + 
              count(dsVehSellingPriceUpperRangeK2)))

# For k = 2, Mean is shown below in red line, the standard deviation is shown as yellow line. 
# As per the Chebyshev's rule (1 - 1\k*2) which is 3\4. therfore at least 75% of the total selling price 
# distribution will be withing range of (mean -2 standard dev) and (mean + 2* standard deviation).
# 
# This comes true in our case as 75% of 20000 is 15000 and 716 lies outside the k=2 
# standard deviation range.

hist(dsVehSp, xlab = "Vehicle Selling Price", ylab = "Frequency", main="Distribution of Selling Price" , xlim = c(0, 100000))
abline(v = mean(dsVehSp), col='red', lwd = 3)
abline(v = lowerRangeK2, col='yellow', lwd = 3)
abline(v = upperRangeK2, col='yellow', lwd = 3)

#Question 1 (d)	Explain how the box-plot technique can be used to detect outliers. 
#Apply this technique for one attribute of the dataset

# boxplot is constructed using the min max,median, first and third quantile. A box is drwan between the lower and upper quartiles. A line across the box is the median. The straight lines are connected to min and max which are also known as whiskers. From it we can easily find out
# 
# The lower and upper quartiles, Q1 and Q3
# The interquartile range (IQR), the distance between the lower and upper quartiles
# The most extreme (lowest and highest) values
# The symmetry or asymmetry of the distribution of scores (R.Lyman, 106)

boxplot(dsVehSp, main = "Box Plot of Vehicle Selling Price", ylab = "Selling Price")


q = quantile(dsVehSp, c(0.25, 0.75))
iqr = q[2] - q[1]
upperOutliers = q[2] + 1.5 * iqr
lowerOutliers = q[1] - 1.5 * iqr
print(paste("Upper outliers value = ", upperOutliers))
print(paste("Lower outliers value = ", lowerOutliers))
print(paste("Upper outliers total = ", sum(dsVehSp > upperOutliers)))
print(paste("Lower outliers total= ", sum(dsVehSp > upperOutliers)))
boxplotOutliers = dsVehSp > upperOutliers | dsVehSp < lowerOutliers
sum(boxplotOutliers)

outliersData = dsVehSp[dsVehSp > upperOutliers | dsVehSp < lowerOutliers]
print(outliersData)

#Question 2 (a) - Select four variables of the dataset, and propose an appropriate probability model to quantify uncertainty of each variable.

# 1. MMR - Provides the most accurate wholesale valuations based on vehicle year, make, model and style, among other criteria 
#        - It is a continues variable 
#        - Probability Model for this variable is Normal Distribution. 
#        - The valuation might vary but most of them will be around the mean. 

# 2. State - State of the vehicle
#        - It is a categorical variable (more than 2 categories)
#        - Probability Model for this variable is Multinational Distribution. 
#        - There can be multiple probability outcomes as the state variable has multiple categories.

# 3. Transmission - Provides the car transmission and the current data is categorized into Manual and Automatic 
#        - It is a Binary Variable.  
#        - Probability Model for this variable is Bernoulli Distribution. 
#        - Transmission in the car can be encodes as a binary outcome (yes/no, 1,0 or in other words Automatic\Manual).

# 4. Odometer - Provides Odometer reading of the car. 
#        - It is a continuous variables that possess positive and skewed distributions 
#        - Probability Model for this variable is Gamma Distribution. 
#       

# Selecting variables for probability models
Selected_Data <- dsVeh[, c('mmr', 'state', 'transmission', 'odometer')]
# Previewing the selected data
head(Selected_Data)

#Question 2 (b) For each model in part (a), estimate the parameters of the model.

#1- MMR - Normal Distribution

dsVehMmr=dsVeh$mmr
dsVehMmrMean = mean(dsVehMmr)
dsVehMmrSd = sd(dsVehMmr)

print(paste("Mean MMR = ", dsVehMmrMean, "Standard Deviation=", dsVehMmrSd))
# Simulation a new set of data with N = 1000 with the above mean and standard deviation 
# and calculate its mean. 
sim=rnorm(1000,dsVehMmrMean,dsVehMmrSd)

# Mean of the simulated data 
pred=mean(sim)
print(paste("For random 1000 the pred mean is ", pred))

#This function returns the value of the cumulative density function (cdf) of the normal distribution 
#given a certain random variable q, a population mean μ, and the population standard deviation σ.
# 13342 value is approximated value of the MMr column close to the mean. It will provide us with percentage of vehicles 
# whose MMR is greater than 13342 value. It should approximate to 50%. 
pnorm(13342,dsVehMmrMean,dsVehMmrSd)

#This implies that for the distribution with mean = 13106.3425 and standard deviation of 9638.278, 
# The probability that the randomly selected selling price will be less than 13342 is 0.509. 
# This can also be checked by calculating the 

zvalue = (13342 - dsVehMmrMean)/dsVehMmrSd

print(paste("Z-Value = ",zvalue))

# Using the pnomr function we can calculate the area under the zvalue. 

print(paste("Area under Z value", zvalue, "is ",pnorm(zvalue) * 100))
  

hist(dsVeh$mmr, main = "Normal Distribution - MMR", xlab = "MMR", freq = FALSE, xlim=c(0,100000))
curve(dnorm(x, mean = dsVehMmrMean, sd = dsVehMmrSd), add = TRUE, col = "red")
abline(v = dsVehMmrMean, col='green', lwd = 3)

#2- State - Multinational Distribution

dsVehState=dsVeh$state
tbldsVehState=table(dsVehState);

print("Number of vehicles per state")
tbldsVehState

# Total number of vehicles in all the states. 
sum(tbldsVehState)

dsVehStateMode=names(tbldsVehState)[which(tbldsVehState==max(tbldsVehState))];
print(paste("The Most vehicles belongs to the state", dsVehStateMode))

# Probability of number of vehicles per state. That means number of vehicles per state 
# divided by total number of vehicles. 
probPerState=tbldsVehState/sum(tbldsVehState);
probPerState

barplot(probPerState, main = "Multinomial Distribution - State",
        xlab = "State", ylab = "Outcomes", ylim = c(0, 1))


#3 - Transmission - Bernoulli Distribution.

print("The distribution of the vehicles based on their transmission is ")
transmission = dsVeh$transmission
table(transmission)

# Dividing number of vehicles of a particular transmission by total number of the vehicles 
# gives the individual probability distribution. 
transmission_prob = table(transmission) / nrow(dsVeh)
transmission_prob

print(paste("Result shows that about ", transmission_prob[1] * 100 , "% are 
            Automatic, while rest ", transmission_prob[2] * 100, "% are Manual"))

transmission_manual = transmission_prob[2]
barplot(transmission_prob, main = "Bernoulli Distribution - Transmission", 
        xlab = "transmission", ylab = "Outcomes", ylim = c(0, 1))
abline(h = transmission_manual, col = "blue")

#4 - Odometer - Gamma Distribution. 

# Taking the numeric data from the data set for odometer readings. 
dsVehOdometerNumeric = filter(dsVeh,odometer != '')
dsVehOdometer = dsVehOdometerNumeric$odometer

dsVehOdometerMean=mean(dsVehOdometer);
dsVehOdometerVar=var(dsVehOdometer)

print(paste("Mean = ",dsVehOdometerMean, "Variance = ",dsVehOdometerVar))

# Lambda is mean/variance
lambdaOdometer =dsVehOdometerMean/dsVehOdometerVar
# Alpha is lambda * mean
alphaOdometer=lambdaOdometer*dsVehOdometerMean

print(paste("Lambda = ",lambdaOdometer, "Alpha = ",alphaOdometer))

#Probability of getting odometer reading more than 65000 is P(>65000) = 1-P(X<65000)
print(paste("Probability of getting odometer reading more than 65000 is",
            1-pgamma(65000,alphaOdometer,lambdaOdometer)))


# The fitdistrplus package provides us fitdist function to fit a distribution
#fitdist(dataset, distr = “choice”, method = “method”)
#rgamma(s, α, λ) = s-sample, the parameter counter - rate, gamma- rate
#lambdaOdometer = 2.82, alpha = 2.17 sample size = 100

sampleGamma <- rgamma(100, 2.17, 2.82)

ans <- fitdist(sampleGamma, distr = "gamma", method = "mle")

summary(ans)
plot(ans)

#Question 2 (c) - Express the way in which each model can be used for the predictive analytics, 
#then find the prediction for each attribute. 

#Normal Distribution - Prediction of MMR
dsVehMmrMean
dsVehMmrSd

dsVehMmrProbability = pnorm(dsVehMmr, mean = dsVehMmrMean, sd = dsVehMmrSd)
dsVehMmrProbabilityPrediction = dsVehMmr[which.max(dsVehMmrProbability)]

## prediction
c("The predicted of mmr is", dsVehMmrProbabilityPrediction)

#Multinomial Distribution

# Total number of states  = 34 therefore n = 34
# The states probability looks like 
 probPerState
# total sum of the values in the vector should equals N=34
# let X is a vector displaying the frequency of each result. Assuming that we want to calculate  
# probability of getting combination where 29 vehicles belongs to ca, 1 to fl,hi, pa, tx, va 
# then x will be represented like below vector. 

x=c(0,0,29,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0)

n =34

p = dmultinom(x,n,probPerState)

print(paste("The predicted probality of above combination is :",p))

print(paste("The predicted State is:",dsVehStateMode))

#Bernoulli Distribution

# probability distribution for transmission is 
transmission_prob

# out of two the one with the higher probability is picked up 
trans = transmission_prob
transmission_pred = names(transmission_prob)[which.max(transmission_prob)]

c("The predicted transmission type  is", transmission_pred)


#Gamma Distribution

# 10000 sample is generated through rgama for the alpha and lambda of the current data set Odometer values 
# calculated in 2.b. The mean of the sample is the prediction value. 
rgammadsVehOdometerdata=rgamma(10000,alphaOdometer,lambdaOdometer)
predDsVehOdometerGamma=mean(rgammadsVehOdometerdata)
print(paste("The predicted odometer reading is", predDsVehOdometerGamma))

#Question 3 (a) -Consider two categorical variables of the dataset, develop a binary decision making strategy to check whether two variables are independent at the significant level alpha=0.01. To do so,
# i. State the hypotheses
# ii. Find the statistic and critical values.
# iii. Explain your decision and Interpret results.

# Since the two categorical variables are required to be checked for dependence, 
# two-way or contingency tables method is employed. These tables will provide 
# statistical inference based on data observed. Furthermore, The chi-square test will 
# be used as it provides the best method for testing the association between the row 
# and column variables in a two-way table.
# 
# The chi-square test is based on a test statistic that measures the divergence of the observed data 
# from the values that would be expected under the null hypothesis of no association. 
# This requires calculation of the expected values based on the data. The expected value for 
# each cell in a two-way table is equal to (row total*column total)/n, where n is the total 
# number of observations included in the table.
# 
# A new categorical column (cond_rating) is added in the dataset based on condition column of the 
# dataset. Condition of the vehicle (condition column) is possibly rated on a scale. 
# If you are reading a car review or attending an auction that uses the six category system, 
# it is easily translatable from the 100 point system (nationalmusclecars->Ratings Guide).

# Category 1 would be a 90 + point car
# Category 2 would be a 80 - 89 point car
# Category 3 would be a 70 - 79 point car
# Category 4 would be a 60 - 69 point car
# Category 5 would be a 40 - 59 point car
# Category 6 is any car under a 40 point car

# Step 1: State the hypotheses
# 
# The null hypothesis H0 assumes that there is no association between the variables (in other words, one variable does not vary according to the other variable)
# 
# H0: X1 (Category Ratings) and X2 (Transmission) are independent
# 
# H1: X1 (Category Ratings) and X2 (Transmission) are dependent

# function to create Category ratings based on the conditional ratings of the dataset
condition_new_mult <- function(cond) {
  ifelse(cond >= 90, "Category 1",
         ifelse(cond >= 80 & cond <= 89, "Category 2",
                ifelse(cond >= 70 & cond <= 79, "Category 3",
                       ifelse(cond >= 60 & cond <= 69, "Category 4",
                              ifelse(cond >= 50 & cond <= 59, "Category 5",
                                     ifelse(cond >= 40 & cond <= 49, "Category 6",
                                            ifelse(cond >= 30 & cond <= 39, "Category 7",
                                                   ifelse(cond <= 20, "Category 7", "Category 7"))))))))
}

# Filtering out the rows which has blank conditional ratings
dsVehRatings <- filter(dsVeh, condition != '')
# New vector for categorical ratings is created by calling the function 
dsCol <-condition_new_mult(dsVehRatings$condition) 
# New column is added in the dsVehRatings dataset
dsVehRatings$cond_rating <- dsCol

print("The data set with new column cond_rating")
head(dsVehRatings)

#category Table is created using the cond_rating and transmission columns

X1=dsVehRatings$cond_rating
X2=dsVehRatings$transmission
C_T_table=table(X1,X2)

#Step 2: Setting significance level to 0.01. A matrix (2X2) is created
alpha = 0.01
E=matrix(NA,2,2)
N = nrow(dsVehRatings)
E

#Calculation of the expected values based on the data. The expected value for each cell 
# in a two-way table is equal to (row total*column total)/n, where n is the total number 
# of observations included in the table.
X1=2;X2=2
for(i in 1:X1){
  for(j in 1:X2){
    Ci=sum(C_T_table[i,]);
    Cj=sum(C_T_table[,j])
    E[i,j]=(Ci*Cj)/N
  }
}

print("The original relation table for ratings and transmission is")
C_T_table
print("The Expected relation table for ratings and transmission is") 
E

# Step 3: Test Value : Once the expected values have been computed the chi-square test statistic 
#is computed as
# 
# X**2 = SUM(observed - Expected)POWER2/Expected
# 
# where the square of the differences between the observed and expected values in each cell, 
# divided by the expected value, are added across all of the cells in the table. 
# The distribution of the statistic X2 is chi-square with (r-1)(c-1) degrees of freedom, 
# where r represents the number of rows in the two-way table and c represents the number of columns. 
# The distribution is denoted (df), where df is the number of degrees of freedom.

test.value=sum((C_T_table-E)^2/E)
test.value

# 
# Step 4: C Value: The chi-square test is based on a test statistic that measures the divergence of 
# the observed data from the values that would be expected under the null hypothesis of no association.
# This requires calculation of the expected values based on the data. The expected value for each cell 
# -way table is equal to (row total*column total)/n, where n is the total number of observations 
# included in the table.

df = 1
c.value = qchisq(1-alpha,df)
c.value

#Step 5: Decision Rule

ifelse(test.value < c.value, "H0 is accepted: ie, X1 and X2 are independent", "H0 is rejected: ie, X1 and X2 are dependent")


#Step 6: Make a decision and conclusion

#H0 is accepted: ie, Category Ratings and Transmission are independent. Here the null hypothesis (H0) is satisfied, 
#therefore two categorical variables Conditional Rating and Transmission are independent at the significance level α = 0.01

#3 b) Consider one categorical variable, apply goodness of fit test to evaluate whether a candidate set of probabilities 
#can be appropriate to quantify the uncertainty of class frequency at the significant level alpha=0.05.

#Considering the Transmission as the categorical vehicle for this test

#Step 1: State the hypotheses

#H0: p1=p2=1/2

#H1: Not H0

#Step 2: Set significance level alpha = 0.05

X=dsVeh$transmission

# The Significant level is 0.05
alpha = 0.05

TransTabl=table(X)

print("Original Transmission Table")
TransTabl

ProbabilityTransTable =TransTabl/sum(TransTabl)

print("Probability of the original Transmission Table")
ProbabilityTransTable

P0=rep(1/2,2)

print("Probability table 50 percent")

P0

N=nrow(dsVeh)

print(paste("Expected Probability table 50 percent= Prob * Total Number = ", N))

ExpectedProbTbl=N*P0

ExpectedProbTbl

test.value=sum((TransTabl-ExpectedProbTbl)^2/ExpectedProbTbl)
test.value

#Step 4: Find the c.value
df = N-1
c.value = qchisq(1-alpha, df)
c.value

if (test.value < c.value){
  c("H0 is accepted")
}else{
  c("H0 is rejected")
}

#Step 6: Make a decision and conclusion

#Here c.value less than test.value, therefore the null hypothesis (H0) is rejected and alternate hypothesis H1 is accepted.

#Question 3-(c) Consider one continuous variable in the data set, and apply test of mean for a 
# proposed candidate of μ at the significant level alpha=0.05.

# Step 1: State the hypotheses
# 
# Considering the selling price column as the continues column for this test.
# 
# Selling price of the vehicle in population will be < 11000.00
# 
# Let Mu0 be 11000
# 
# H0: Poulation Mean < 11000
# 
# H1: Poulation Mean >= 11000
# 
# This fits in the "Upper One Sided HT" and as per "Upper One Sided HT"
# 
# H0: µ < µ0 , H1: µ ≥ µ0, if α = 0.05, then
# 
# t.value = (Xbar-Mu0)/StandardDeviation/SquarRoot(N) c.value = qnorm(1- α)
# 
# if test.value ≥ c.value therefore H0 is rejected
# 
# If the condition above is satisfied, the candidate value is at least equal to µ0.


#Step 2: Setting Significance value

alpha = 0.05
print(paste("Significance is set to : ", alpha))

Mu0 = 11000
X=dsVeh$sellingprice
X_bar=mean(X)
SD=sd(X)
N = length(X)

print(paste("Sample Mean: ", X_bar,"Standard Deviation: ", SD,"Sample Size: ", N))

#Step 3: Compute the test.value

test.value=(X_bar-Mu0)/(SD/sqrt(N))
print(paste("Test Value = : ",test.value))

#Step 4: Find the c.value

c.value = qnorm(1-alpha)
print(paste("C Value = : ",c.value))

# Step 5: Specify the decision rule
# 
# If test.value ≥ c.value therefore H0 is rejected

evaluate_results <- function(tval, cval)
{
  if (tval < cval)
  {
    print("H0 is accepted")
  }
  else
  {
    print("H0 is rejected")
  }
}

evaluate_results(test.value,c.value)

# Step 6: Make a decision and conclusion
# 
# If the condition in step 5 is satisfied, the population mean is atleast equal to Mu0.
# 
# Here test.value greater than c.value, therefore the null hypothesis (H0) is rejected and alternate hypothesis H1 is accepted. 
# That means the population mean would be at least 11000.

### End of the Assignment 



