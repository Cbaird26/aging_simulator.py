import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant
initial_cell_health = 100  # Initial health of a cell
time_steps = st.slider("Time Steps (years)", 1, 100, 50)

# Define hypothetical intervention parameters
intervention_effectiveness = st.slider("Intervention Effectiveness (%)", 0, 100, 50)
aging_rate = st.slider("Aging Rate (%)", 0, 10, 5)

# Simulate cellular health over time with intervention
def simulate_aging(initial_health, effectiveness, aging_rate, time_steps):
    health = initial_health
    health_over_time = []
    for t in range(time_steps):
        health -= aging_rate
        health += (effectiveness / 100) * (initial_health - health)
        health_over_time.append(max(health, 0))
    return health_over_time

# Run the simulation
health_over_time = simulate_aging(initial_cell_health, intervention_effectiveness, aging_rate, time_steps)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(time_steps), health_over_time, label="Cellular Health")
plt.xlabel("Time (years)")
plt.ylabel("Cellular Health")
plt.title("Simulated Effect of Intervention on Cellular Aging")
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Display the results
st.write(f"Initial Cell Health: {initial_cell_health}")
st.write(f"Intervention Effectiveness: {intervention_effectiveness}%")
st.write(f"Aging Rate: {aging_rate}% per year")
st.write(f"Simulated Time: {time_steps} years")
