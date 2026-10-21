# Data visualization using NumPy, Pandas, and Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data using NumPy
months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
sales = np.array([100, 150, 120, 180, 200])

# Create a DataFrame using Pandas
data = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print("Sales Data:")
print(data)

print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))

# Plot a line graph
plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()