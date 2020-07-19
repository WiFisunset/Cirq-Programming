import strawberryfields as sf
from strawberryfields import ops

# create a 2-mode quantum program
prog = sf.Program(2)

# create a free parameter named 'a'
a = prog.params('a')

# define the program
with prog.context as q:
    # DGate Phase space displacement gate.
    ops.Dgate(a ** 2)    | q[0]  # free parameter
    # MeasureX:
    # Performs a homodyne measurement, measures one quadrature of a mode.
    # Position basis measurement: ϕ=0
    # Momentum basis measurement: ϕ=π/2
    # Measure qumode 0, the result is used in the next operation.
    ops.MeasureX         | q[0]
    # Phase space squeezing gate.
    ops.Sgate(1 - sf.math.sin(q[0].par)) | q[1]  # measured parameter
    ops.MeasureFock()    | q[1]

# intialize the Fock backend
eng = sf.Engine('fock', backend_options={'cutoff_dim': 5})

# run the program, with the free parameter 'a' bound to the value 0.9
result = eng.run(prog, args={'a': 0.9})

# Contains details and methods for manipulation of the final circuit state.
print(result.state)
state = result.state

# Density Matrix
state.dm().shape

# To avoid significant numerical error when working with Fock backends,
# ensure that the trace of your program after simulation remains reasonably close
# to 1, by calling state.trace(). If the trace is much less than 1, you will need to
# increase the cutoff dimension.
# state.trace()
