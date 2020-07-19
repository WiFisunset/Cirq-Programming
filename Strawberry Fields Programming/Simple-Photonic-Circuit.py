import strawberryfields as sf
from strawberryfields import ops

# create a 3-mode quantum program
prog = sf.Program(3)

with prog.context as q:
    # Squeezing Gates
    ops.Sgate(0.54) | q[0]
    ops.Sgate(0.54) | q[1]
    ops.Sgate(0.54) | q[2]

    # Beamsplitter Gates: A 50% or 50-50 beamsplitter has θ=π/4 and ϕ=0.
    ops.BSgate(0.43, 0.1) | (q[0], q[2])
    ops.BSgate(0.43, 0.1) | (q[1], q[2])

    # Photon counting is a non-Gaussian projective measurement given by|ni⟩⟨ni|.
    ops.MeasureFock() | q

# Intialize the fock backend with a Fock cutoff dimension (truncation) of 5.
eng = sf.Engine("fock", backend_options={"cutoff_dim": 5})

result = eng.run(prog)

# Contains details and methods for manipulation of the final circuit state.
print(result.state)
state = result.state

# Density Matrix
state.dm().shape
