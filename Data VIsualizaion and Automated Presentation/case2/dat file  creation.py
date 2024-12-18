import numpy as np

# Define the number of rows
num_rows = np.random.randint(200, 301)

# Create data for data3.dat with 10 columns
data3 = np.column_stack((
    np.linspace(0, 7, num_rows),
    np.sin(np.linspace(0, 7, num_rows)),
    np.cos(np.linspace(0, 7, num_rows)),
    np.tan(np.linspace(0, 7, num_rows)),
    np.log(np.linspace(1, 8, num_rows)),
    np.exp(np.linspace(0, 2, num_rows)),
    np.random.rand(num_rows) * 3,
    np.random.randn(num_rows) * 1.5,
    np.random.poisson(8, num_rows),
    np.random.binomial(20, 0.6, num_rows)
))
np.savetxt('data3.dat', data3, header='X Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 Y10', comments='')

# Create data for data4.dat with 10 columns
data4 = np.column_stack((
    np.linspace(0, 7, num_rows),
    np.sin(np.linspace(0, 7, num_rows) + np.pi/3),
    np.cos(np.linspace(0, 7, num_rows) + np.pi/3),
    np.tan(np.linspace(0, 7, num_rows) + np.pi/3),
    np.log(np.linspace(1, 8, num_rows) + 0.5),
    np.exp(np.linspace(0, 2, num_rows) + 0.2),
    np.random.rand(num_rows) * 4,
    np.random.randn(num_rows) * 2,
    np.random.poisson(6, num_rows),
    np.random.binomial(25, 0.8, num_rows)
))
np.savetxt('data4.dat', data4, header='X Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 Y10', comments='')

print("Data files created: data3.dat and data4.dat")
