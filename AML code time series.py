import pandas as pd

# Creating a time series DataFrame
data = {'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'value': [10, 15, 12, 18, 20]}
df = pd.DataFrame(data)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set 'date' column as the index
df.set_index('date', inplace=True)

# Display the DataFrame
print("Time Series Data:")
print(df)

# Accessing specific time periods
print("\nAccessing Specific Time Periods:")
print("Value on January 3, 2024:", df.loc['2024-01-03'])
print("Value between January 2 and January 4, 2024:")
print(df.loc['2024-01-02':'2024-01-04'])

# Resampling (e.g., converting daily data to monthly)
monthly_data = df.resample('M').sum()
print("\nMonthly Data:")
print(monthly_data)

# Plotting
import matplotlib.pyplot as plt

df.plot(figsize=(10, 6))
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
