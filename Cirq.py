import cirq

n = 5
a = [1, 1, 1, 1, 0]

#preparing qubits
qubits = cirq.LineQubit.range(n)
ancilla = cirq.LineQubit(n)

circuit = cirq.Circuit()

#first hadamard
for q in qubits:
    circuit.append(cirq.H(q))
circuit.append(cirq.X(ancilla))
circuit.append(cirq.H(ancilla))

#oracle
for i in range (n):
    if(a[i] == 1):
        circuit.append(cirq.CNOT(qubits[i], ancilla))

#second hadamard
for q in qubits:
    circuit.append(cirq.H(q))

#measurement
circuit.append(cirq.measure(qubits))

print(circuit)

sim = cirq.Simulator()

result = sim.run(circuit, repetitions=3)

print(result)   