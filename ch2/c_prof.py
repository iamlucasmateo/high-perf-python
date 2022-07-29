import cProfile
from pstats import Stats

from julia import full_run

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    full_run()

    pr.disable()
    pr.dump_stats("ch2/julia.profile")
    stats = Stats(pr)
    # can also do Stats("folder/file")
    first_n_lines = 10
    sort_by = "tottime"
    stats.sort_stats('tottime').print_stats(first_n_lines)
    print("")
    # stats.print_callers(10)
    # stats.print_callees(10)