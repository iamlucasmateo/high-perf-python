from typing import Iterable, Dict, List

import matplotlib.pyplot as plt


C_CONSTANT = -0.63772 + 0.42193j
MIN_, MAX_ = -1.6, 1.6
MAX_ITER = 600
SPLITS = 600


def get_complex_coords(min_: float, max_: float, splits: int):
    split_size: float = (max_ - min_) / splits
    coord: float = min_
    coords: List[float] = []
    while coord < max_:
        coords.append(coord)
        coord += split_size 
    
    bi_coords = []
    for xcoord in coords:
        row_coords = []
        for ycoord in coords:
            row_coords.append(complex(xcoord, ycoord))
        bi_coords.append(row_coords)
    
    return bi_coords


def count_iterations(bi_coordinates: Iterable[Iterable[complex]], constant: complex, max_iter: int):
    counts: List[List[int]] = []
    for row in bi_coordinates:
        row_counts = []
        for z in row:
            z_aux = z
            for iteration in range(max_iter):
                if abs(z_aux) < 2 and iteration != max_iter - 1:
                    z_aux: complex = z_aux*z_aux + constant
                else:
                    gray_scale = int((iteration / max_iter) * 255)
                    row_counts.append((gray_scale, gray_scale, gray_scale))
                    break
        counts.append(row_counts)
    
    return counts


def full_run():
    coords = get_complex_coords(MIN_, MAX_, splits = SPLITS)
    iterations = count_iterations(coords, C_CONSTANT, MAX_ITER)
    plt.matshow(iterations)
    plt.savefig("example")


if __name__ == "__main__":
    full_run()