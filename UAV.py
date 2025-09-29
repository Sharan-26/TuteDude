import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from IPython.display import HTML
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ✅ 1. Sample Data Definition (No Drive Mounting)
mission_data = {
    "primary": {
        "id": "Primary",
        "waypoints": [
            {"position": [10, 10], "time": 1},
            {"position": [20, 20], "time": 2},
            {"position": [30, 30], "time": 3}
        ]
    },
    "simulated": [
        {
            "id": "Drone_1",
            "waypoints": [
                {"position": [12, 12], "time": 1},
                {"position": [22, 22], "time": 2},
                {"position": [35, 35], "time": 4}
            ]
        },
        {
            "id": "Drone_2",
            "waypoints": [
                {"position": [50, 50], "time": 2},
                {"position": [60, 60], "time": 3},
                {"position": [70, 70], "time": 4}
            ]
        }
    ]
}

primary_drone = mission_data['primary']
simulated_drones = mission_data['simulated']

# ✅ 2. Helper: Euclidean distance (2D or 3D)
def euclidean(p1, p2):
    return np.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# ✅ 3. Conflict Checking Function
def check_conflict(primary, others, spatial_thresh=10, time_tolerance=0):
    conflicts = []
    for wp1 in primary['waypoints']:
        for drone in others:
            for wp2 in drone['waypoints']:
                dist = euclidean(wp1['position'], wp2['position'])
                time_diff = abs(wp1['time'] - wp2['time'])
                if dist <= spatial_thresh and time_diff <= time_tolerance:
                    conflicts.append({
                        'conflict_with': drone['id'],
                        'location': wp1['position'],
                        'time': wp1['time']
                    })
    return conflicts

# ✅ 4. Run Conflict Check
conflict_report = check_conflict(primary_drone, simulated_drones)

# ✅ 5. Output Result
if conflict_report:
    print("[!] Conflict Detected")
    for c in conflict_report:
        print(f"Conflict with {c['conflict_with']} at {c['location']} at time {c['time']}")
else:
    print("✅ Mission is Clear")

# ✅ 6. Visualization (2D Static Plot)
def plot_mission(primary, others, conflicts):
    plt.figure(figsize=(10, 8))
    px, py = zip(*[tuple(wp['position'][:2]) for wp in primary['waypoints']])
    plt.plot(px, py, 'bo-', label='Primary Drone')
    
    for sim in others:
        sx, sy = zip(*[tuple(wp['position'][:2]) for wp in sim['waypoints']])
        plt.plot(sx, sy, '--', label=f"{sim['id']}")

    for c in conflicts:
        cx, cy = c['location'][:2]
        plt.plot(cx, cy, 'rx', markersize=12, label='Conflict')

    plt.title("UAV Deconfliction Map")
    plt.legend()
    plt.grid(True)
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.show()

plot_mission(primary_drone, simulated_drones, conflict_report)

# ✅ 7. Animated 4D Visualization (X, Y, optional Z + time)
def animate_mission(primary, others):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title('4D UAV Mission Simulation')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    primary_line, = ax.plot([], [], 'bo-', label='Primary Drone')
    other_lines = [ax.plot([], [], '--', label=d['id'])[0] for d in others]

    def init():
        primary_line.set_data([], [])
        for line in other_lines:
            line.set_data([], [])
        return [primary_line] + other_lines

    def update(frame):
        if frame == 0:
            return init()
        px_py = [wp['position'][:2] for wp in primary['waypoints'][:frame]]
        if px_py:
            px, py = zip(*px_py)
            primary_line.set_data(px, py)

        for i, d in enumerate(others):
            ox_oy = [wp['position'][:2] for wp in d['waypoints'][:frame]]
            if ox_oy:
                ox, oy = zip(*ox_oy)
                other_lines[i].set_data(ox, oy)

        return [primary_line] + other_lines

    ani = animation.FuncAnimation(fig, update, frames=len(primary['waypoints']) + 1,
                                  init_func=init, blit=True, repeat=False)
    plt.legend()
    plt.close()
    return HTML(ani.to_jshtml())

animate_mission(primary_drone, simulated_drones)