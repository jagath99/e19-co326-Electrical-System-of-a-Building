import numpy as np
import time
import json
import cmath
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
VOLTAGE_AMPLITUDE = 230

def generate_electricity_data(t):
    # Generate random frequency between 50 and 60 Hz
    frequency = np.random.uniform(50, 60)
    
    # Calculate angular frequency
    omega = 2 * np.pi * frequency
    
    # Generate the voltage as a function of time
    voltage = VOLTAGE_AMPLITUDE * np.sin(omega * t)
    
    # Generate random resistance (real part) and reactance (imaginary part)
    resistance = np.random.uniform(10000, 10000)  # Resistance in ohms
    reactance = np.random.uniform(5, 50)  # Reactance in ohms
    
    # Create the complex impedance
    impedance = complex(resistance, reactance)
    
    # Calculate the current using Ohm's Law for AC circuits: I = V / Z
    current = voltage / impedance
    
    # Get the magnitude of the current
    current_magnitude = abs(current)
    
    # Generate the timestamp
    timestamp = time.time()
    
    return {
        "timestamp": timestamp,
        "voltage": voltage,
        "current": current_magnitude,
        "resistance": resistance,
        "reactance": reactance,
        "frequency": frequency
    }

# Set up the plot
fig, (ax1, ax2) = plt.subplots(2, 1)
time_data = []
voltage_data = []
current_data = []

def update_plot(frame):
    t = time.time() - start_time
    data = generate_electricity_data(t)
    
    time_data.append(t)
    voltage_data.append(data['voltage'])
    current_data.append(data['current'])
    
    # Keep the lists at a manageable length
    time_data[:] = time_data[-200:]
    voltage_data[:] = voltage_data[-200:]
    current_data[:] = current_data[-200:]
    
    ax1.clear()
    ax2.clear()
    
    ax1.plot(time_data, voltage_data, label='Voltage (V)')
    ax2.plot(time_data, current_data, label='Current (A)', color='orange')
    
    ax1.set_ylabel('Voltage (V)')
    ax2.set_ylabel('Current (A)')
    ax2.set_xlabel('Time (s)')
    
    ax1.legend()
    ax2.legend()
    
    ax1.set_title('Real-time Voltage and Current Readings')

if __name__ == "__main__":
    start_time = time.time()
    
    ani = animation.FuncAnimation(fig, update_plot, interval=5)  # Update every 5 milliseconds
    plt.tight_layout()
    plt.show()
