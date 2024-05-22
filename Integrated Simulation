import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_cell_health = 50  # Initial health of a cell, scaled 0-100
time_steps = st.slider("Time Steps (years)", 1, 100, 50)

# Define hypothetical intervention parameters
telomere_extension_effect = st.slider("Telomere Extension Effectiveness (%)", 0, 100, 50)
protein_folding_correction = st.slider("Protein Folding Correction Effectiveness (%)", 0, 100, 50)
epigenetic_reprogramming_effect = st.slider("Epigenetic Reprogramming Effectiveness (%)", 0, 100, 50)
aging_rate = st.slider("Aging Rate (%)", 0, 10, 5)

# Simulate cellular health over time with interventions
def simulate_aging_interventions(initial_health, telomere_extension, protein_folding, epigenetic_reprogramming, aging_rate, time_steps):
    health = initial_health
    health_over_time = []
    for t in range(time_steps):
        health -= aging_rate
        health += (telomere_extension / 100) * (100 - health)
        health += (protein_folding / 100) * (100 - health)
        health += (epigenetic_reprogramming / 100) * (100 - health)
        health_over_time.append(max(min(health, 100), 0))
    return health_over_time

# Run the simulation
health_over_time = simulate_aging_interventions(initial_cell_health, telomere_extension_effect, protein_folding_correction, epigenetic_reprogramming_effect, aging_rate, time_steps)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(time_steps), health_over_time, label="Cellular Health")
plt.xlabel("Time (years)")
plt.ylabel("Cellular Health")
plt.title("Simulated Effect of Interventions on Cellular Aging")
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Display the results
st.write(f"Initial Cell Health: {initial_cell_health}")
st.write(f"Telomere Extension Effectiveness: {telomere_extension_effect}%")
st.write(f"Protein Folding Correction Effectiveness: {protein_folding_correction}%")
st.write(f"Epigenetic Reprogramming Effectiveness: {epigenetic_reprogramming_effect}%")
st.write(f"Aging Rate: {aging_rate}% per year")
st.write(f"Simulated Time: {time_steps} years")
