import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('honey.csv')

# --- Step 1: Data cleaning ---
print("Before cleaning:")
print(df['Value'])

# Remove commas and convert to numeric
df['Value'] = df['Value'].str.replace(',', '', regex=False)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Drop rows where Value is NaN
df.dropna(subset=['Value'], inplace=True)

print("\nAfter cleaning:")
print(df['Value'])

# --- Step 2: Group by state and sum ---
unique_states = df['State'].unique()
all_honey = []
all_states = []

for state in unique_states:
    state_data = df[df['State'] == state]
    honey_grouped = state_data.groupby('Year')['Value'].sum()
    
    print(f"{state}:\n{honey_grouped}\n")
    
    all_honey.append(honey_grouped)
    all_states.append(state)

# --- Step 3: Plot honey production per state ---
plt.figure(figsize=(12, 6))
for i in range(len(all_honey)):
    honey = all_honey[i]
    state = all_states[i]
    
    # Handle single-year data
    if isinstance(honey, pd.Series):
        years = honey.index
        values = honey.values
    else:
        years = [1997]  # default year if single number
        values = [honey]
    
    plt.plot(years, values, label=state)

plt.xlabel("Year")
plt.ylabel("Honey Production (lbs)")
plt.title("Honey Production by State Over Years")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Step 4: Categorize states by total production ---
total_honey_per_state = [h.sum() for h in all_honey]

large_threshold = 500000
medium_threshold = 200000

large_states, large_honey_list = [], []
medium_states, medium_honey_list = [], []
small_states, small_honey_list = [], []

for i in range(len(all_states)):
    total = total_honey_per_state[i]
    if total > large_threshold:
        large_states.append(all_states[i])
        large_honey_list.append(all_honey[i])
    elif total > medium_threshold:
        medium_states.append(all_states[i])
        medium_honey_list.append(all_honey[i])
    else:
        small_states.append(all_states[i])
        small_honey_list.append(all_honey[i])

# --- Step 5: Function to plot groups ---
def plot_group(states_list, honey_list, group_name):
    plt.figure(figsize=(10, 6))
    for i in range(len(states_list)):
        honey = honey_list[i]
        if isinstance(honey, pd.Series):
            years = honey.index
            values = honey.values
        else:
            years = [1997]
            values = [honey]
        plt.plot(years, values, label=states_list[i])
    plt.xlabel("Year")
    plt.ylabel("Honey Production (lbs)")
    plt.title(f"Honey Production for {group_name} Producers")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_group(large_states, large_honey_list, "Large")
plot_group(medium_states, medium_honey_list, "Medium")
plot_group(small_states, small_honey_list, "Small")

# --- Step 6: Average honey per state ---
avg_honey_per_state = []
for state in unique_states:
    honey_avg = df[df['State'] == state].groupby('Year')['Value'].mean()
    avg_honey_per_state.append(honey_avg)

plt.figure(figsize=(10,6))
for honey_avg in avg_honey_per_state:
    plt.plot(honey_avg.index, honey_avg.values, linestyle='--', marker='o')
plt.xlabel("Year")
plt.ylabel("Average Honey Production (lbs)")
plt.title("Average Honey Production per State Over Years")
plt.show()

# --- Step 7: Total honey per year across all states ---
unique_years = df['Year'].unique()
yearly_totals = []

for year in sorted(unique_years):
    totals = df[df['Year'] == year].groupby('Year')['Value'].sum()
    yearly_totals.append(totals.values[0])

plt.figure(figsize=(8,5))
plt.bar(sorted(unique_years), yearly_totals, color='gold', edgecolor='brown')
plt.xlabel("Year")
plt.ylabel("Total Honey Production (lbs)")
plt.title("Total Honey Production Across All States by Year")
plt.show()

# --- Step 8: Customize averages plot with line styles and legend ---
plt.figure(figsize=(10,6))
line_styles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'd', '*']
for i, honey_avg in enumerate(avg_honey_per_state):
    style = line_styles[i % len(line_styles)]
    marker = markers[i % len(markers)]
    plt.plot(honey_avg.index, honey_avg.values, linestyle=style, marker=marker)
plt.xlabel("Year")
plt.ylabel("Average Honey Production (lbs)")
plt.title("Average Honey Production per State Over Years")
plt.legend(unique_states, loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()