import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data from .dat files
data1 = pd.read_csv('data1.dat', delim_whitespace=True)
data2 = pd.read_csv('data2.dat', delim_whitespace=True)

# Create directory to save plots
import os
if not os.path.exists('plots'):
    os.makedirs('plots')

# Function to save plot
def save_plot(filename):
    plt.savefig(f'plots/{filename}.png')
    plt.close()

# 1. Simple Line Plot
plt.figure()
plt.plot(data1['X'], data1['Y1'], label='Data1 Y1')
plt.plot(data2['X'], data2['Y1'], label='Data2 Y1', linestyle='--')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('line_plot_simple')

# 2. Line Plot with Different Markers
plt.figure()
plt.plot(data1['X'], data1['Y2'], 'o-', label='Data1 Y2')
plt.plot(data2['X'], data2['Y2'], 'x--', label='Data2 Y2')
plt.title('Line Plot with Different Markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('line_plot_markers')

# 3. Line Plot with Grid
plt.figure()
plt.plot(data1['X'], data1['Y3'], label='Data1 Y3')
plt.plot(data2['X'], data2['Y3'], linestyle='--', label='Data2 Y3')
plt.title('Line Plot with Grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
save_plot('line_plot_grid')

# 4. Line Plot with Error Bars
errors1 = np.random.normal(0.1, 0.02, size=len(data1))
errors2 = np.random.normal(0.1, 0.02, size=len(data2))
plt.figure()
plt.errorbar(data1['X'], data1['Y4'], yerr=errors1, label='Data1 Y4', linestyle='-', marker='o', capsize=3)
plt.errorbar(data2['X'], data2['Y4'], yerr=errors2, label='Data2 Y4', linestyle='--', marker='x', capsize=3)
plt.title('Line Plot with Error Bars')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('line_plot_error_bars')

# 5. Line Plot with Shaded Region
plt.figure()
plt.plot(data1['X'], data1['Y5'], label='Data1 Y5', linestyle='-', marker='o')
plt.plot(data2['X'], data2['Y5'], label='Data2 Y5', linestyle='--', marker='x')
plt.fill_between(data1['X'], data1['Y5'] - errors1, data1['Y5'] + errors1, alpha=0.2)
plt.fill_between(data2['X'], data2['Y5'] - errors2, data2['Y5'] + errors2, alpha=0.2)
plt.title('Line Plot with Shaded Region')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('line_plot_shaded')

# 6. Scatter Plot
plt.figure()
plt.scatter(data1['X'], data1['Y6'], label='Data1 Y6')
plt.scatter(data2['X'], data2['Y6'], label='Data2 Y6')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('scatter_plot')

# 7. Scatter Plot with Different Markers
plt.figure()
plt.scatter(data1['X'], data1['Y7'], marker='o', label='Data1 Y7')
plt.scatter(data2['X'], data2['Y7'], marker='x', label='Data2 Y7')
plt.title('Scatter Plot with Different Markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('scatter_plot_markers')

# 8. Bar Plot
plt.figure()
plt.bar(data1['X'][::10], data1['Y8'][::10], width=0.4, label='Data1 Y8')
plt.bar(data2['X'][::10] + 0.4, data2['Y8'][::10], width=0.4, label='Data2 Y8')
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('bar_plot')

# 9. Histogram
plt.figure()
plt.hist(data1['Y9'], bins=30, alpha=0.5, label='Data1 Y9')
plt.hist(data2['Y9'], bins=30, alpha=0.5, label='Data2 Y9')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
save_plot('histogram')

# 10. Box Plot
plt.figure()
plt.boxplot([data1['Y10'], data2['Y10']], labels=['Data1 Y10', 'Data2 Y10'])
plt.title('Box Plot')
plt.xlabel('Dataset')
plt.ylabel('Value')
save_plot('box_plot')

# 11. Pie Chart
plt.figure()
plt.pie(data1['Y1'][:5], labels=data1['X'][:5], autopct='%1.1f%%')
plt.title('Pie Chart (Data1 Y1)')
save_plot('pie_chart_data1')

# 12. Pie Chart (Data2)
plt.figure()
plt.pie(data2['Y1'][:5], labels=data2['X'][:5], autopct='%1.1f%%')
plt.title('Pie Chart (Data2 Y1)')
save_plot('pie_chart_data2')

# 13. Line Plot (Subplots)
fig, axs = plt.subplots(2, 2)
fig.suptitle('Line Plot (Subplots)')
axs[0, 0].plot(data1['X'], data1['Y1'], label='Data1 Y1')
axs[0, 1].plot(data1['X'], data1['Y2'], 'tab:orange', label='Data1 Y2')
axs[1, 0].plot(data1['X'], data1['Y3'], 'tab:green', label='Data1 Y3')
axs[1, 1].plot(data1['X'], data1['Y4'], 'tab:red', label='Data1 Y4')
for ax in axs.flat:
    ax.legend()
    ax.set(xlabel='X-axis', ylabel='Y-axis')
for ax in axs.flat:
    ax.label_outer()
save_plot('line_plot_subplots')

#14.Violin Plot
plt.figure()
plt.violinplot([data1['Y8'], data2['Y8']], showmedians=True)
plt.xticks([1, 2], ['Data1 Y8', 'Data2 Y8'])
plt.title('Violin Plot')
plt.ylabel('Value')
save_plot('violin_plot')


#15. Area Plot
plt.figure()
plt.stackplot(data1['X'], data1['Y9'], data2['Y9'], labels=['Data1 Y9', 'Data2 Y9'])
plt.title('Stacked Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
save_plot('area_plot')


#16. Hexbin Plot
plt.figure()
plt.hexbin(data1['X'], data1['Y10'], gridsize=20, cmap='Blues')
plt.hexbin(data2['X'], data2['Y10'], gridsize=20, cmap='Oranges')
plt.colorbar(label='count')
plt.title('Hexbin Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
save_plot('hexbin_plot')


#17. Polar Plot
plt.figure()
theta = np.linspace(0, 2*np.pi, len(data1))
plt.polar(theta, data1['Y1'], label='Data1 Y1')
plt.polar(theta, data2['Y1'], label='Data2 Y1')
plt.title('Polar Plot')
plt.legend()
save_plot('polar_plot')





