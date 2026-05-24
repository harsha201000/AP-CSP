# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and clean data
def load_and_clean(filename):
    # Load csv file
    df = pd.read_csv(filename)
    
    # Rename columns
    df.columns = ['Neighborhood', 'Id', 'Value', 'Margin_of_Error']
    
    # Remove rows where value is missing
    df = df[df['Value'] != '-']
    
    # Convert Value column to numeric
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    
    # Drop any remaining NaN values
    df.dropna(subset=['Value'], inplace=True)
    
    print("Data cleaned successfully.\n")
    return df

# Function to calculate statistics
def calculate_statistics(df):
    max_value = df['Value'].max()
    min_value = df['Value'].min()
    avg_value = df['Value'].mean()
    
    print("Statistics:")
    print("Maximum Income: {}".format(max_value))
    print("Minimum Income: {}".format(min_value))
    print("Average Income: {}".format(avg_value))
    print()
    
    return max_value, min_value, avg_value

# Function to categorize neighborhoods
def categorize_income(df):
    categories = []
    
    # Iteration with conditional logic
    for value in df['Value']:
        if value < 50000000:
            categories.append("Low")
        elif value < 150000000:
            categories.append("Medium")
        else:
            categories.append("High")
            
    df['Income_Category'] = categories
    return df

# Function to plot data
def plot_income_categories(df):
    category_counts = df['Income_Category'].value_counts()
    
    plt.figure()
    plt.bar(category_counts.index, category_counts.values)
    plt.title("Neighborhood Income Categories")
    plt.xlabel("Income Categories")
    plt.ylabel("Number of Neighborhoods")
    plt.show()
    
# Program
filename = "income_data.csv" # CSV File
# Load and clean data
df = load_and_clean(filename)
# Calculate Statistics
calculate_statistics(df)
# Categorize Data
df = categorize_income(df)
# Plot Results
plot_income_categories(df)
