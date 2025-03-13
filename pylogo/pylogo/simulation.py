import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import warnings

class Simulation:
    def __init__(self, model, time, **kwargs) -> None:
        self.model = model
        self.time = time

    def run(self,
            property_name,
            type,
            plot_dict,
            animation_dict,
            **kwargs):
        if not animation_dict:
            warnings.warn("Animation dictionary is empty. Using default values.")
            animation_dict = {'frames': 100, 'interval': 100}
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig,
                                      self._animation_hook,
                                      fargs=(ax, property_name, type, plot_dict),
                                      frames=animation_dict['frames'],
                                      interval=animation_dict['interval'],
                                      repeat=kwargs.get('repeat', False))
        # save the animation
        ani.save('animation.gif', writer='pillow')

    def init(self, ax, plot_dict):
        if len(plot_dict.keys()) == 0:
            plot_dict = {'xlabel': 'X', 'ylabel': 'Y', 'title': 'Title', 'xlim': (0, 100), 'ylim': (0, 100)}
        ax.set_xlabel(plot_dict['xlabel'])
        ax.set_ylabel(plot_dict['ylabel'])
        ax.set_title(plot_dict['title'])
        ax.set_xlim(plot_dict['xlim'])
        ax.set_ylim(plot_dict['ylim'])
        return ax

    def _animation_hook(self, i, ax, property_name, type, plot_dict, **kwargs):
        self.model.step()
        ax.clear()
        self.init(ax, plot_dict)
        if type == 'histogram':
            ax.hist([turtle.__dict__[property_name] for turtle in self.model.agent_dict.turtle_dict.values()],
                    bins=int(2*np.log(self.model.agent_dict.numbers)))
        else:
            pass