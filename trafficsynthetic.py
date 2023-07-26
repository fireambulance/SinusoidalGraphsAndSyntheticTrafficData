import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of traffic volume (e.g., low, moderate, high)
low_volume = np.random.randint(50, 200, size=300)  # Random values between 50 and 200
moderate_volume = np.random.randint(200, 500, size=300)  # Random values between 200 and 500
high_volume = np.random.randint(500, 1000, size=300)  # Random values between 500 and 1000

# Concatenate the synthetic data to create the overall traffic volume dataset
traffic_volume_data = np.concatenate([low_volume, moderate_volume, high_volume])

# Assume a normal distribution for traffic speed (mean: 60 km/h, standard deviation: 10 km/h)
mean_speed = 60
std_dev_speed = 10
synthetic_speed_data = np.random.normal(loc=mean_speed, scale=std_dev_speed, size=900)  # Changed size to 900

# Assuming a distance of 10 kilometers for the road segment
distance = 10

# Calculate travel time using the formula: travel_time = distance / speed
synthetic_travel_time_data = distance / synthetic_speed_data

# Generate synthetic congestion pattern by adding random variations to traffic volume and speed
peak_hour_traffic_volume = np.random.randint(800, 1200, size=300)  # Random values between 800 and 1200
peak_hour_speed = np.random.normal(loc=40, scale=5, size=300)  # Random speeds around 40 km/h with some variability

# Concatenate the synthetic data for peak hour congestion
congestion_data = np.concatenate([traffic_volume_data[:300], peak_hour_traffic_volume])
speed_data = np.concatenate([synthetic_speed_data[:300], peak_hour_speed])

# Simulate the traffic congestion dynamics over time due to non-linear interactions
def simulate_congestion_evolution(traffic_volume, speed, num_time_steps, distance):
    travel_time = distance / speed
    congestion_evolution = np.zeros((num_time_steps, len(traffic_volume)))

    for i in range(num_time_steps):
        congestion_evolution[i] = traffic_volume * (1 + np.sin(travel_time * i))

    return congestion_evolution

# Simulate congestion dynamics over 100 time steps
num_time_steps = 100
congestion_evolution = simulate_congestion_evolution(congestion_data, speed_data, num_time_steps, distance)

# Calculate travel time using the formula: travel_time = distance / speed
travel_time_data = distance / synthetic_speed_data

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D scatter plot
ax.scatter(synthetic_speed_data, traffic_volume_data, travel_time_data, c=travel_time_data, cmap='viridis')

# Set axis labels
ax.set_xlabel('Speed (km/h)')
ax.set_ylabel('Traffic Volume')
ax.set_zlabel('Travel Time (hours)')

# Set the title
ax.set_title('Speed vs Traffic Volume vs Travel Time')

# Show the plot
plt.show()

# Plot the results
plt.figure(figsize=(10, 6))
for i in range(len(congestion_data)):
    plt.plot(np.linspace(0, num_time_steps, num_time_steps), congestion_evolution[:, i], alpha=0.5)

plt.xlabel('Time Steps')
plt.ylabel('Congestion Level')
plt.title('Traffic Congestion Evolution with Chaos Theory')
plt.show()

# Calculate statistics for traffic volume and speed
volume_mean = np.mean(traffic_volume_data)
volume_std = np.std(traffic_volume_data)
speed_mean = np.mean(synthetic_speed_data)
speed_std = np.std(synthetic_speed_data)

# Calculate statistics for travel time and congestion
time_mean = np.mean(synthetic_travel_time_data)
time_std = np.std(synthetic_travel_time_data)
congestion_mean = np.mean(congestion_data)
congestion_std = np.std(congestion_data)

# Display the statistics
print("Traffic Volume - Mean:", volume_mean, "Standard Deviation:", volume_std)
print("Traffic Speed - Mean:", speed_mean, "Standard Deviation:", speed_std)
print("Travel Time - Mean:", time_mean, "Standard Deviation:", time_std)
print("Congestion Data - Mean:", congestion_mean, "Standard Deviation:", congestion_std)

# Create a scatter plot of traffic volume vs. speed
plt.scatter(traffic_volume_data, synthetic_speed_data, c='blue', alpha=0.5)
plt.xlabel('Traffic Volume')
plt.ylabel('Traffic Speed (km/h)')
plt.title('Traffic Volume vs. Speed')
plt.grid(True)
plt.show()

# Create histograms for travel time and congestion data
plt.subplot(1, 2, 1)
plt.hist(synthetic_travel_time_data, bins=20, edgecolor='black')
plt.xlabel('Travel Time (hours)')
plt.ylabel('Frequency')
plt.title('Distribution of Travel Time')

plt.subplot(1, 2, 2)
plt.hist(congestion_data, bins=20, edgecolor='black')
plt.xlabel('Congestion Data')
plt.ylabel('Frequency')
plt.title('Distribution of Congestion')

plt.tight_layout()
plt.show()

