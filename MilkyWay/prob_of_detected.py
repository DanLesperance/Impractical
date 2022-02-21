from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000 # num of locations in which civs are placed
MAX_CIVS = 5000 # max num of advanced civs
TRIALS = 1000 # number of times to model
CIV_STEP_SIZE = 100 # civs count step size

x = []
y = []
for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = [] # equivalent volumes containing a civilization
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        #print(overlap_count) # using these print statements to understand output
        overlap_rollup = Counter(overlap_count.values())
        #print(overlap_rollup) # Same as above comment, using for understanding
        #
        num_single_civs += overlap_rollup[1]

prob = 1 - (num_single_civs / (num_civs * TRIALS))

# print ratio of civs-per-vol vs. probability of 2+ civs in one location
print("{:.4f} {:.4f}".format(civs_per_vol,prob))
x.append(civs_per_vol)
y.append(prob)




