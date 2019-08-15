import numpy as np
import matplotlib.pyplot as plt


class GraphFunction():

    @staticmethod
    def graph_sequence(_list):
        y_pos = np.arange(len(_list))
        plt.bar(np.arange(len(_list)), _list, align='center')
        plt.xticks(y_pos, _list)
        plt.ylabel('P(Class = N)')
        plt.title('Amazon Review!')
        return plt.show()
