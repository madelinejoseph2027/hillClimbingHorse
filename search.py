#Importsimport osimport numpy as npimport matplotlib.pyplot as pltimport constants as cfrom parallelHillClimber import PARALLEL_HILL_CLIMBER phc = PARALLEL_HILL_CLIMBER()phc.Evolve("DIRECT")phc.Show_Best()bestIndividuals = phc.Graph_Best()#plt.plot(np.arange(0, c.numberOfGenerations), bestIndividuals1, color = 'red', label = 'Seed 1')#plt.plot(np.arange(0, c.numberOfGenerations), bestIndividuals2, color = 'orange', label = 'Seed 2')#plt.plot(np.arange(0, c.numberOfGenerations), bestIndividuals3, color = 'yellow', label = 'Seed 3')#plt.plot(np.arange(0, c.numberOfGenerations), bestIndividuals4, color = 'green', label = 'Seed 4')#plt.plot(np.arange(0, c.numberOfGenerations), bestIndividuals5, color = 'blue', label = 'Seed 5')#plt.legend()#plt.show()