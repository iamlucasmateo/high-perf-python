from pyinstrument import Profiler

# from julia import count_iterations, count_iterations_alt, get_complex_coords, MIN_, MAX_, SPLITS, C_CONSTANT, MAX_ITER
from julia import full_run

profiler = Profiler()
profiler.start()

full_run()

profiler.stop()
profiler.print()
profiler.dump_stats("py_instrument.prof")