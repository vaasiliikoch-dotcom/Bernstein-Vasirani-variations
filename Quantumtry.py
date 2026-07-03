from qiskit import QuantumCircuit
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
#preparing qubits
qc = QuantumCircuit(n + 1, n + 1)

#first hadamard
for i in range(n):
    qc.h(i)
qc.x(n)
qc.h(n)

#oracle
for i in range(n):
    if a[i] == 1:
        qc.cx(i, n)

#second hadamard
for i in range(n):
    qc.h(i)

#result
for i in range(n):
    qc.measure(i, i)

print(qc.draw())

#stimulation
from qiskit_aer import AerSimulator
sim = AerSimulator()

from qiskit import transpile
compiled = transpile(qc, sim)
job = sim.run(compiled, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)