import numpy as np

bar_length_cm = 10.0
num_nodes = 5
space_grid = np.linspace(0.0, bar_length_cm, num_nodes)

time_steps = np.arange(0, 7, 2)

num_rows = len(time_steps)
num_cols = len(space_grid)
temp_matrix = np.zeros((num_rows, num_cols))

initial_temperatures = np.array([100.0, 25.0, 25.0, 25.0, 25.0])
temp_matrix[0, :] = initial_temperatures

thermal_conductivity = 0.25

for t in range(1, num_rows):
    temp_matrix[t, :] = temp_matrix[t - 1, :]
    
    for i in range(1, num_cols - 1):
        conduction = thermal_conductivity * (temp_matrix[t-1, i-1] - 2 * temp_matrix[t-1, i] + temp_matrix[t-1, i+1])
        temp_matrix[t, i] = temp_matrix[t-1, i] + conduction

print(f"\n{temp_matrix}\n")