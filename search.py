#Imports
import os
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
 

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve("DIRECT")
phc.Show_Best()
