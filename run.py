from simulation import BasicSimulation
from charter import SimulationChart


chart_manager = SimulationChart()
sim = BasicSimulation(
    target='Can you find me in this house',
    pop_max=1000,
    mutation_rate=0.015,
    charter=chart_manager,
)
sim.run()
sim.display_charts()

