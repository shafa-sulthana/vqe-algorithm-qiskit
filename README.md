# Variational Quantum Eigensolver (VQE) using Qiskit

## Overview

This project implements the Variational Quantum Eigensolver (VQE), a hybrid quantum-classical algorithm used to estimate the ground-state energy of a quantum system.

A simple one-qubit Hamiltonian, H = Z, is used to demonstrate the VQE workflow.

## Objective

To implement VQE using Python and Qiskit and find the minimum energy of a quantum system using a parameterized quantum circuit and classical optimization.

## VQE Workflow

1. Define the Hamiltonian.
2. Prepare a parameterized quantum circuit.
3. Calculate the expectation value of the Hamiltonian.
4. Use a classical optimizer to update the circuit parameter.
5. Repeat the process until the energy is minimized.
6. Obtain the approximate ground-state energy.

## Quantum Circuit

The variational ansatz is:

Ry(θ)

The parameter θ is optimized by the classical optimizer.

## Hamiltonian

The Hamiltonian used is:

H = Z

```text
H = [[1, 0],
     [0, -1]]