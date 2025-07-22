import pandas as pd
import matplotlib.pyplot as plt

# ---------- Load Datasets ----------
# Load carbon sequestration-related dataset
carbon_df = pd.read_csv('GlobalTemperatures.csv')

# Load renewable energy dataset
renewable_df = pd.read_csv('climate_dataset.csv')

# ---------- Carbon Sequestration Estimation Function ----------
def estimate_carbon_sequestration(land_areas, rate):
    return [area * rate for area in land_areas]

# Sample values for carbon sequestration
land_areas = [1000, 1500, 2000, 2500, 3000, 3500, 4000]
avg_sequestration_rate = 4.5  # tons CO2/ha/year
carbon_sequestered = estimate_carbon_sequestration(land_areas, avg_sequestration_rate)

# ---------- Renewable Energy Adoption Simulation Function ----------
def simulate_renewable_energy(initial, growth, years):
    usage = [initial]
    for _ in range(years):
        usage.append(usage[-1] + usage[-1] * growth)
    return usage

# Sample values for renewable energy simulation
initial_usage = 0.15  # 15%
growth_rate = 0.05    # 5% annual growth
years = 20
renewable_usage = simulate_renewable_energy(initial_usage, growth_rate, years)

# ---------- Combined Visualization ----------
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Carbon Sequestration
axs[0].plot(land_areas, carbon_sequestered, marker='o', color='green')
axs[0].set_title('Carbon Sequestration vs Land Area')
axs[0].set_xlabel('Land Area (hectares)')
axs[0].set_ylabel('CO2 Sequestered (tons/year)')
axs[0].grid(True)

# Plot 2: Renewable Energy Adoption
axs[1].plot(range(years + 1), renewable_usage, marker='o', color='blue')
axs[1].set_title('Renewable Energy Adoption Over Time')
axs[1].set_xlabel('Years')
axs[1].set_ylabel('Renewable Usage (%)')
axs[1].grid(True)

plt.tight_layout()
plt.show()
