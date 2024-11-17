import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create a scatter plot
plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed data')

# 3. Line of best fit for all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = range(1880, 2051)
plt.plot(years_extended, [slope * year + intercept for year in years_extended], color='red', label='Best fit line (all data)')

# 4. Line of best fit for data from 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(years_extended, [slope_recent * year + intercept_recent for year in years_extended], color='green', label='Best fit line (2000 onwards)')

# 5. Set labels and title
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

# 6. Display the legend
plt.legend()

# 7. Show the plot
plt.tight_layout()
plt.show()

