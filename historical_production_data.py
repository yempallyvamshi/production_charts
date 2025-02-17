import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file = r"C:\Users\Vamshi Yempally\Downloads\xlsx\timestampdata.xlsx"

df = pd.read_excel(file)

df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%d-%m-%Y %H:%M')

# Extract month and day from TimeStamp
df['Month'] = df['TimeStamp'].dt.month
df['Day'] = df['TimeStamp'].dt.day

# Map month numbers to month names
month_names = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

# Create a figure with 12 subplots (one for each month)
fig, axes = plt.subplots(4, 3, figsize=(18, 16))  # 4 rows, 3 columns for 12 months
fig.suptitle('Monthly Production by Level', fontsize=16)

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Plot data for each month
for month in range(1, 13):  # Iterate through months 1 to 12
    ax = axes[month - 1]  # Get the corresponding subplot
    monthly_data = df[df['Month'] == month]  # Filter data for the current month

    # Plot each level separately
    for level, level_data in monthly_data.groupby('Level'):
        ax.plot(level_data['Day'], level_data['Production'], label=f'{level}', marker='o')

    # Formatting
    ax.set_title(month_names[month], fontsize=10)  # Use month names instead of numbers
    ax.set_xlabel(' ')
    ax.set_ylabel('Production')
    ax.legend(title='Level')
    #ax.grid(True)

    # Set x-ticks to avoid overlapping
    if not monthly_data.empty:  # Check if there is data for the month
        ax.set_xticks(monthly_data['Day'].unique())  # Unique days to avoid duplicates
        ax.set_xticklabels(monthly_data['Day'].unique(), fontsize=7)  # Rotate labels for better readability

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust spacing to prevent overlap
plt.show()