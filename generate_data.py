import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic CPU load (%)
cpu_load = np.random.uniform(10, 95, 500)

# Generate RAM usage (%) correlated with CPU load
ram_usage = cpu_load * 0.8 + np.random.normal(5, 3, 500)
ram_usage = np.clip(ram_usage, 15, 98)

# Calculate Server Temperature (°C) based on CPU load
temperature = 28 + (cpu_load * 0.35) + np.random.normal(0, 1.5, 500)

# Calculate Power Draw (Watts) based on CPU load and temperature
power_draw = 120 + (cpu_load * 2.8) + (temperature * 0.5) + np.random.normal(0, 5, 500)

df = pd.DataFrame({
    'cpu_load': np.round(cpu_load, 2),
    'ram_usage': np.round(ram_usage, 2),
    'temperature': np.round(temperature, 2),
    'power_draw': np.round(power_draw, 2)
})

df.to_csv('dummy_telemetry.csv', index=False)
print("✅ Created dummy_telemetry.csv with 500 telemetry records.")