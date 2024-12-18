import numpy as np

# Define the number of rows
num_rows = np.random.randint(200, 301)

# Create data for data1.dat with 10 columns
data1 = np.column_stack((
    np.linspace(0, 10, num_rows),
    np.sin(np.linspace(0, 10, num_rows)),
    np.cos(np.linspace(0, 10, num_rows)),
    np.tan(np.linspace(0, 10, num_rows)),
    np.log(np.linspace(1, 10, num_rows)),
    np.exp(np.linspace(0, 1, num_rows)),
    np.random.rand(num_rows),
    np.random.randn(num_rows),
    np.random.poisson(5, num_rows),
    np.random.binomial(10, 0.5, num_rows)
))
np.savetxt('data1.dat', data1, header='X Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 Y10', comments='')

# Create data for data2.dat with 10 columns
data2 = np.column_stack((
    np.linspace(0, 10, num_rows),
    np.sin(np.linspace(0, 10, num_rows) + np.pi/4),
    np.cos(np.linspace(0, 10, num_rows) + np.pi/4),
    np.tan(np.linspace(0, 10, num_rows) + np.pi/4),
    np.log(np.linspace(1, 10, num_rows) + 1),
    np.exp(np.linspace(0, 1, num_rows) + 0.1),
    np.random.rand(num_rows) * 2,
    np.random.randn(num_rows) * 2,
    np.random.poisson(7, num_rows),
    np.random.binomial(15, 0.7, num_rows)
))
np.savetxt('data2.dat', data2, header='X Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 Y10', comments='')

print("Data files created: data1.dat and data2.dat")
