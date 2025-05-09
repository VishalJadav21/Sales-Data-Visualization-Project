import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the path to the CSV file
file_path = 'C:\\Users\\VISHAL JADAV\\OneDrive\\Desktop\\Projects\\Resume Detection\\sales_data_sample.csv'

# Load the dataset
# Try to read with 'latin1' encoding if 'utf-8' fails, as this dataset is known to sometimes use it.
try:
    sales_df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    sales_df = pd.read_csv(file_path, encoding='latin1')

# --- Initial Data Exploration ---
print("First 5 rows of the dataset:")
print(sales_df.head())
print("\n")

print("Dataset Information:")
sales_df.info()
print("\n")

print("Basic Statistical Summary:")
print(sales_df.describe())
print("\n")

# --- Data Cleaning (Example: Convert ORDERDATE to datetime) ---
# Ensure 'ORDERDATE' column exists before trying to convert
if 'ORDERDATE' in sales_df.columns:
    sales_df['ORDERDATE'] = pd.to_datetime(sales_df['ORDERDATE'])
    print("Converted 'ORDERDATE' to datetime objects.\n")
else:
    print("'ORDERDATE' column not found. Please check the CSV file column names.\n")

# --- Example Visualization: Sales per Product Line ---
if 'PRODUCTLINE' in sales_df.columns and 'SALES' in sales_df.columns:
    plt.figure(figsize=(12, 6))
    productline_sales = sales_df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
    sns.barplot(x=productline_sales.index, y=productline_sales.values, palette='viridis')
    plt.title('Total Sales per Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    print("Displayed bar chart for 'Total Sales per Product Line'.")
else:
    print("Could not generate 'Sales per Product Line' chart. Missing 'PRODUCTLINE' or 'SALES' column.\n")

# --- Example Visualization: Sales Over Time (Monthly) ---
if 'ORDERDATE' in sales_df.columns and 'SALES' in sales_df.columns and pd.api.types.is_datetime64_any_dtype(sales_df['ORDERDATE']):
    sales_df['ORDERMONTH'] = sales_df['ORDERDATE'].dt.to_period('M')
    monthly_sales = sales_df.groupby('ORDERMONTH')['SALES'].sum()
    
    plt.figure(figsize=(14, 7))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Total Sales Over Time (Monthly)')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    print("Displayed line chart for 'Total Sales Over Time (Monthly)'.")
elif not 'ORDERDATE' in sales_df.columns or not pd.api.types.is_datetime64_any_dtype(sales_df['ORDERDATE']):
     print("Could not generate 'Sales Over Time' chart. 'ORDERDATE' column is missing or not in datetime format.\n")
else:
    print("Could not generate 'Sales Over Time' chart. Missing 'SALES' column.\n")

print("\n--- Script Finished ---")
