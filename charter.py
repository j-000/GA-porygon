from matplotlib import pyplot


class SimulationChart:

    def __init__(self):
        self.x_data = []
        self.y_fittest = []
        self.y_mean = []
        self.y_std_dev = []

    def main(self):
        fig, axs = pyplot.subplots(1, 3, figsize=(9, 3))
        axs[0].plot(self.x_data, self.y_fittest)
        axs[0].set_title('Fittest score')
        axs[1].plot(self.x_data, self.y_mean)
        axs[1].set_title('Mean score')
        axs[2].plot(self.x_data, self.y_std_dev)
        axs[2].set_title('Std. Dev. score')

        pyplot.show()
