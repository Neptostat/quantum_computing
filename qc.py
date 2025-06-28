from qiskit import QuantumCircuit, Aer, execute

def quantum_random_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)  # put qubit into superposition
    qc.measure(0, 0)

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    return list(counts.keys())[0]  # '0' or '1'

# Generate a 16-bit random number
random_number = ''.join([quantum_random_bit() for _ in range(16)])
print("Quantum Random Number (binary):", random_number)
print("As Integer:", int(random_number, 2))
