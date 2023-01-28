import matplotlib.pyplot as plt
with open(r'./experimental_circuit_qasm.txt', 'r') as f:
    circuit_qasm = ''.join(f.readlines())

import qiskit

circuit = qiskit.QuantumCircuit.from_qasm_str(circuit_qasm)
circuit.draw('mpl', fold=-1, scale=0.5, idle_wires=False)

plt.savefig(r'./experimental_circuit.pdf',
            dpi=None,
            facecolor='w',
            edgecolor='w',
            orientation='portrait',
            format="pdf",
            bbox_inches='tight')
