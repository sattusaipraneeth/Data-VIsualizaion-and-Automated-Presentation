import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pptx import Presentation
from pptx.util import Inches

# Read data from .dat files
data1 = pd.read_csv('data3.dat', delim_whitespace=True)
data2 = pd.read_csv('data4.dat', delim_whitespace=True)

# Function to save plot
def save_plot(filename):
    plt.savefig(f'plots_png/{filename}.png')
    plt.close()

# Create directory to save plots
import os
if not os.path.exists('plots_png'):
    os.makedirs('plots_png')

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

# Create a PowerPoint presentation
if not os.path.exists('presentations'):
    os.makedirs('presentations')

presentation = Presentation()

# Function to add slide with image
def add_slide_with_image(prs, img_path, title=None):
    slide_layout = prs.slide_layouts[5]  # Title and Content layout
    slide = prs.slides.add_slide(slide_layout)
    
    if title:
        slide.shapes.title.text = title
    
    left = Inches(0.5)
    top = Inches(1.5)
    width = Inches(9)
    height = Inches(6)
    
    slide.shapes.add_picture(img_path, left, top, width=width, height=height)

# Add slides with plots
add_slide_with_image(presentation, 'plots_png/line_plot_simple.png', title='Simple Line Plot')
add_slide_with_image(presentation, 'plots_png/line_plot_markers.png', title='Line Plot with Different Markers')
add_slide_with_image(presentation, 'plots_png/line_plot_grid.png', title='Line Plot with Grid')
add_slide_with_image(presentation, 'plots_png/line_plot_error_bars.png', title='Line Plot with Error Bars')
add_slide_with_image(presentation, 'plots_png/line_plot_shaded.png', title='Line Plot with Shaded Region')
add_slide_with_image(presentation, 'plots_png/scatter_plot.png', title='Scatter Plot')
add_slide_with_image(presentation, 'plots_png/scatter_plot_markers.png', title='Scatter Plot with Different Markers')
add_slide_with_image(presentation, 'plots_png/bar_plot.png', title='Bar Plot')
add_slide_with_image(presentation, 'plots_png/histogram.png', title='Histogram')
add_slide_with_image(presentation, 'plots_png/box_plot.png', title='Box Plot')

# Save presentation
presentation.save('presentations/presentation_data1_data2.pptx')

print("Presentation created successfully.")