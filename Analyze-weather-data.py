import numpy as np
import matplotlib.pyplot as plt


# Simulated average daily temperatures (in degrees Celsius) for a month
temperatures = np.linspace(start=25.0, stop=40, num=100) + np.random.normal(loc=0, scale=0.2, size=100)

#Basic statics
#Mean
temp_mean = np.mean(temperatures)
print(f'Mean of Given temperatures is : {temp_mean:.2f}')

#Median
temp_median = np.median(temperatures)
print(f'Median of given temperatures is : {temp_median:.2f}')

#Standard Deviation
temp_std = np.std(temperatures)
print(f'Standard Deviation of Given temperatures is : {temp_std:.2f}')

#------------------------------------------------------------------------------

#Analyze Temperatures Fluctuations
#day-to-day temperatures differences
temperature_difference = np.diff(temperatures)
print(f'Temperature differences : {temperature_difference}')

#Average day-to-day temperature differences
temp_avg = np.mean(temperature_difference)
print(f'Average day to day temperature difference is : {temp_avg:.2f}')

#------------------------------------------------------------------------------

#Visualize Data using matplotlib library

#days
days = np.arange(1,101)

#thresolds
hot_thresold = 37
cold_thresold = 30

#hot and cold days
hot_days = np.where(temperatures > hot_thresold)[0]
cold_days = np.where(temperatures < cold_thresold)[0]
normal_days = np.setdiff1d(np.arange(len(temperatures)), np.concatenate((hot_days, cold_days)))

#plot temperature trend
plt.figure(figsize=(12,6),num="Daily Temperature Analysis")
plt.scatter(days[normal_days], temperatures[normal_days], color='gray', s=30, alpha=0.7, label='Normal Days')

#highlight hot days in red
plt.scatter(days[hot_days], temperatures[hot_days], color='red', label='hot days (>37°C)',s=30,alpha=0.7)

#highlight cold days in blue
plt.scatter(days[cold_days], temperatures[cold_days], color='blue', label='cold days (<30°C)',s=30,alpha=0.7)

#Labels and title
plt.xlabel('Days')
plt.ylabel('Temperatures in °C')
plt.xticks(np.arange(0,101,10))
plt.title('Daily temperatures of given days')

#legend and grid
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)

#show plot
plt.show()
