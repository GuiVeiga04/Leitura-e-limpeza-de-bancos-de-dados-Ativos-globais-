import pip as pp
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (replace "bcatv.csv" with your actual filename)
at_rel_invest_dir = pd.read_csv("bcatv.csv", sep=';', quotechar='"')

# Convert 'data' to datetime and 'valor' to numeric (adjust format if needed)
at_rel_invest_dir["data"] = pd.to_datetime(at_rel_invest_dir["data"], format='%d/%m/%Y')
at_rel_invest_dir["valor"] = pd.to_numeric(at_rel_invest_dir["valor"], errors='coerce')

data_day = at_rel_invest_dir.iloc[1:89]  # Using original slicing for now

# Check what data_day looks like
print(data_day)

# Plot the data
plt.plot(data_day['data'], data_day['valor'])
plt.xlabel("Date")  # Clarified label
plt.ylabel("Valor (Em milhões de dólares)")
plt.title("Ativo - Investimento direto no exterior")
plt.xticks(rotation=45)  # Fixed typo
plt.tight_layout()
plt.xlim(min(data_day['data']), max(data_day['data']))  # Set x-axis limits if needed
plt.ylim(min(data_day['valor']), max(data_day['valor']))  # Set y-axis limits if needed
plt.show()