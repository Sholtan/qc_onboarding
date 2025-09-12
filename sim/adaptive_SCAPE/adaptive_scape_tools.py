import netsquid as ns
from enum import Enum, auto

class Basis(Enum):
    X = auto()
    Y = auto()
    Z = auto()
operators = {
    Basis.X: ns.qubits.operators.X,
    Basis.Y: ns.qubits.operators.Y,
    Basis.Z: ns.qubits.operators.Z
}
kets = {
    Basis.X: (ns.h0, ns.h1),
    Basis.Y: (ns.y0, ns.y1),
    Basis.Z: (ns.s0, ns.s1)
}

def simulate_chunk(msg_chunk, params_chunk, basis):
    qubes = ns.qubits.create_qubits(len(msg_chunk), no_state=True)
    k0, k1 = kets[basis]
    op = operators[basis]

    results = []
    for bit, pauli_params, q in zip(msg_chunk, params_chunk, qubes):
        ns.qubits.assign_qstate(q, k1 if bit else k0)
        ns.qubits.apply_pauli_noise(q, p_weights=list(pauli_params))
        results.append(ns.qubits.measure(q, observable=op)[0])
    return results