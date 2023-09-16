import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

sql_command = 'SELECT Year, CO2, Temperature FROM ClimateData'
cursor.execute(sql_command)
data = cursor.fetchall() # return all rows of a query result as a list

years = []
co2 = []
temp = []

for row in data:
    [year_val, co2_val, temp_val] = row # unpack the tuple into 3 variables
    years.append(year_val)
    co2.append(co2_val)
    temp.append(temp_val)

connection.close()  # close the database connection

# plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.savefig("co2_temp_1.png") 
plt.show() 
