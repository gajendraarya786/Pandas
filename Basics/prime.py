import pandas as pd

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5.0/9.0

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9.0/5.0) + 32

# Generate temperature data
fahrenheit_temps = list(range(0, 101, 10))  # Fahrenheit temperatures from 0 to 100
celsius_temps = [fahrenheit_to_celsius(f) for f in fahrenheit_temps]
celsius_temps2 = list(range(-10, 41, 10))  # Celsius temperatures from -10 to 40
fahrenheit_temps2 = [celsius_to_fahrenheit(c) for c in celsius_temps2]

# Create DataFrames
df_f_to_c = pd.DataFrame({
    'Fahrenheit': fahrenheit_temps,
    'Celsius': celsius_temps
})

df_c_to_f = pd.DataFrame({
    'Celsius': celsius_temps2,
    'Fahrenheit': fahrenheit_temps2
})

# Save DataFrames to CSV
df_f_to_c.to_csv('fahrenheit_to_celsius_dataset.csv', index=False)
df_c_to_f.to_csv('celsius_to_fahrenheit_dataset.csv', index=False)

print("Temperature conversion datasets created and saved as 'fahrenheit_to_celsius_dataset.csv' and 'celsius_to_fahrenheit_dataset.csv'")
