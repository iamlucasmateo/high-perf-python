from line_profiler import LineProfiler

from julia import count_iterations, count_iterations_alt, get_complex_coords, MIN_, MAX_, SPLITS, C_CONSTANT, MAX_ITER


coords = get_complex_coords(MIN_, MAX_, splits = SPLITS)
lp = LineProfiler()
lp_wrapper = lp(count_iterations)
lp_wrapper(coords, C_CONSTANT, MAX_ITER)
lp.print_stats()
lp.dump_stats("count_iterations.lprof")

