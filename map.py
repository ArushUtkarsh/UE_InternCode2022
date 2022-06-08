# Import the class
import kmapper as km

# Some sample data
from sklearn import datasets
data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.3)

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
projected_data = mapper.fit_transform(data, projection=[0,1]) # X-Y axis

# Create a cover with 10 elements
cover = km.Cover(n_cubes=10)

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, cover=cover)

# Visualize it
mapper.visualize(graph, path_html="make_circles_keplermapper_output.sif",
                 title="make_circles(n_samples=5000, noise=0.03, factor=0.3)")
                 
import matplotlib.pyplot as plt               
plt.figure(figsize=(6, 6))
plt.subplot(111)
plt.scatter(data[labels == 0, 0], data[labels == 0, 1], color='navy')
plt.scatter(data[labels == 1, 0], data[labels == 1, 1], color='c')
plt.show()
