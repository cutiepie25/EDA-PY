
import random
import stddraw

class Dataset:

    def generateClusters2D(self, n: int):
        self.points = []
        self.labels = []
        sigma = 0.5
        for i in range(n):
            if random.randint(0,1):
                mu = 1
                self.labels.append(1)
            else:
                mu = -1
                self.labels.append(0)
            punto = ( random.gauss(mu,sigma), random.gauss(mu,sigma) ) 
            self.points.append(punto)


    def gaussianPoint(centroid: list[float], sigma: float) -> list[float]:
        point = [ random.gauss(centroid[i],sigma) for i in range(len(centroid)) ]
        return point


    def generateClusters(self, n: int, dim: int, labels: int):
        assert labels<=2**dim, "Number of labels must be <= 2**dim"
        self.points = []
        self.labels = []
        centroids = Dataset.hypercube(dim)
        sigma = 0.5
        for i in range(n):
            label = random.randint(0,labels-1)
            # print(label, centroids[label])
            self.labels.append(label)
            self.points.append(Dataset.gaussianPoint(centroids[label],sigma))


    def get_points(self):
        return self.points

    def get_labels(self):
        return self.labels

    def plot_points(self):
        stddraw.setXscale(-5,5)
        stddraw.setYscale(-5,5)
        colors = [ stddraw.RED, stddraw.BLUE ]
        for (point,label) in zip(self.points, self.labels):
            stddraw.setPenColor(colors[label])
            stddraw.setPenRadius(0.01)
            stddraw.point(point[0], point[1])
        stddraw.show()

    def hypercube(d: int) -> list[list[int]]:
        powers = [ 2**i for i in range(d) ]
        vertices = []
        val = lambda i,d: 1 if i & powers[d] else -1
        for i in range(2**d):
            vertices.append([ val(i,j) for j in range(d) ])
        return vertices
    

if __name__ == "__main__":
    n = 20

    # Generar un dataset de n puntos en 3D
    ds = Dataset()
    ds.generateClusters(n, 3, 8)
    print(ds.get_points())

    # Generar un dataset de n puntos en 2D
    ds = Dataset()
    ds.generateClusters2D(n)
    ds.plot_points()



