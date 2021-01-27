import matplotlib.pyplot as plt
import numpy as np
from covid19_data import JHU
fig = plt.figure(figsize=(5.00, 3.75))
ax = fig.add_axes([0,0,1,1])
total_confirmed = JHU.Total.confirmed
total_death = JHU.Total.deaths
total_recovered = JHU.Total.recovered
label = ["Confirmed", "Death", "Recovered"]
# label = [f"Confirmed ({total_confirmed})", f"Death ({total_death})", f"Recovered ({total_recovered})"]
ax.bar(f"Confirmed\n({total_confirmed})", total_confirmed, color='b', width=0.8)
ax.bar(f"Death\n({total_death})", total_death, color='r', width=0.8)
ax.bar(f"Recovered\n({total_recovered})", total_recovered, color='g', width=0.8)
# ax.bar(f"Confirmed", total_confirmed, color='b', width=0.8)
# ax.bar(f"Death", total_death, color='r', width=0.8)
# ax.bar(f"Recovered", total_recovered, color='g', width=0.8)
ax.legend(labels=label)
plt.title("COVID-19 Visualization (World)")
plt.show()