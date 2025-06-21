from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt

def random_single_qubit_rotation(qc, qubit):
    """Apply random single-qubit rotations to approximate a Haar-random unitary."""
    qc.rx(np.random.uniform(0, 2*np.pi), qubit)
    qc.ry(np.random.uniform(0, 2*np.pi), qubit)
    qc.rz(np.random.uniform(0, 2*np.pi), qubit)

def generate_approx_2_design_circuit(n_qubits=5, depth=3, entangle='nearest'):
    """
    Generate an approximate 2-design quantum circuit.
    
    Args:
        n_qubits: Number of qubits in the circuit
        depth: Number of layers (repetitions of the pattern)
        entangle: Entanglement pattern ('nearest' or 'random')
    
    Returns:
        QuantumCircuit: The generated circuit
    """
    qc = QuantumCircuit(n_qubits)
    
    for d in range(depth):
        # Apply random single-qubit unitaries
        for q in range(n_qubits):
            random_single_qubit_rotation(qc, q)
        
        # Apply entangling CNOT gates
        if entangle == 'nearest':
            for q in range(n_qubits - 1):
                qc.cx(q, q+1)
        elif entangle == 'random':
            for _ in range(n_qubits):
                q1, q2 = np.random.choice(n_qubits, 2, replace=False)
                qc.cx(q1, q2)
    
    return qc

# Set random seed for reproducible results
np.random.seed(42)

# Generate the circuit
print("Generating approximate 2-design circuit...")
qc = generate_approx_2_design_circuit(n_qubits=5, depth=3, entangle='nearest')

# Create the circuit diagram
print("Creating circuit diagram...")
fig = qc.draw('mpl', style='iqp')

# Save as PNG
output_filename = '2design_circuit.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
print(f"Circuit diagram saved as: {output_filename}")

# Display circuit info
print(f"\nCircuit Information:")
print(f"Number of qubits: {qc.num_qubits}")
print(f"Circuit depth: {qc.depth()}")
print(f"Number of gates: {len(qc.data)}")

plt.show() 