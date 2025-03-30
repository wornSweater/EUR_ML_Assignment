import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets


# Define the function to plot the sine wave
def plot_sine_wave(frequency):
    x = np.linspace(0, 2 * np.pi, 1000)  # X-axis range
    y = np.sin(frequency * x)  # Sine wave with variable frequency

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=f'Sine wave with frequency {frequency} Hz')
    plt.xlabel('X')
    plt.ylabel('sin(X)')
    plt.title('Sine Wave with Adjustable Frequency')
    plt.ylim(-1, 1)
    plt.legend()
    plt.show()


# Use ipywidgets' interact function to create a slider
interact(plot_sine_wave, frequency=widgets.FloatSlider(value=1, min=0.1, max=10.0, step=0.1));
