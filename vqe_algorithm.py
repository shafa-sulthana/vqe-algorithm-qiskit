

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scipy.optimize import minimize


# Define Hamiltonian H = Z
H = np.array([
    [1, 0],
    [0, -1]
])


# Calculate energy
def calculate_energy(theta):
    qc = QuantumCircuit(1)

    # Variational ansatz
    qc.ry(theta, 0)

    # Get quantum state
    state = Statevector.from_instruction(qc)

    # Expectation value <ψ|H|ψ>
    energy = np.real(
        np.vdot(state.data, H @ state.data)
    )

    return energy


# Function for classical optimizer
def energy_for_optimizer(x):
    return calculate_energy(x[0])


# Initial parameter
initial_theta = [0.5]


# Classical optimization
result = minimize(
    energy_for_optimizer,
    initial_theta,
    method="COBYLA"
)


# Optimal result
optimal_theta = result.x[0]
minimum_energy = result.fun

print("VQE Results")
print("----------------------")
print("Optimal theta:", optimal_theta)
print("Minimum energy:", minimum_energy)


# Energy landscape
theta_values = np.linspace(0, 2 * np.pi, 100)

energy_values = [
    calculate_energy(theta)
    for theta in theta_values
]


# Plot
plt.figure(figsize=(7, 5))

plt.plot(theta_values, energy_values)

plt.scatter(
    optimal_theta,
    minimum_energy,
    s=100,
    label=f"Minimum Energy = {minimum_energy:.4f}"
)

plt.xlabel("Theta (θ)")
plt.ylabel("Energy")
plt.title("VQE Energy Landscape")
plt.legend()
plt.grid()

plt.savefig(
    "vqe_energy_landscape.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()