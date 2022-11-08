
import pandas as pd 
import matplotlib.pyplot as plt 
# reading the database 
data = pd.read_csv("data.csv") # Scatter plot 
plt.scatter(data['day'], data['tip']) # Adding Title to the Plot 
plt.title("Scatter Plot") 
# Setting the X and Y labels 
plt.xlabel('Day') 
plt.ylabel('Tip') 
plt.show() 
# Histogram 
plt.hist(data['total_bill']) 
plt.title('Histogram')
plt.show()
