import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("elec_access_data.csv", header=0)

unique_countries = df['Entity'].unique()

# -------- CONTINENT COUNTRY LISTS --------
americas = ['United States', 'Canada', 'Brazil', 'Argentina', 'Mexico', 'Peru']
europe = ['Germany', 'France', 'United Kingdom', 'Italy', 'Spain', 'Norway']
asia = ['India', 'China', 'Japan', 'Indonesia', 'Pakistan', 'Bangladesh']
africa = ['Nigeria', 'Kenya', 'South Africa', 'Ethiopia', 'Egypt', 'Ghana']

markers = ['o', 's', '^', 'x', '*', 'D']
linestyles = ['-', '--', ':', '-.', '-', '--']

# -------- FUNCTION TO PLOT --------
def plot_graph(country_list, title):
    i = 0
    for c in unique_countries:
        if c in country_list:
            years = df[df['Entity'] == c]['Year']
            sum_elec = df[df['Entity'] == c]['Access']

            plt.plot(years, sum_elec,
                     label=c,
                     marker=markers[i],
                     linestyle=linestyles[i])
            i += 1

    plt.ylabel('Percentage of Country Population')
    plt.xlabel('Year')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# -------- GENERATE 4 GRAPHS --------

plot_graph(americas, 'Electricity Access in the Americas')
plot_graph(europe, 'Electricity Access in Europe')
plot_graph(asia, 'Electricity Access in Asia')
plot_graph(africa, 'Electricity Access in Africa')