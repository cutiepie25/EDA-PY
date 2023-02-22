
import random
import stddraw

class Dataset:

    def generateClusters(self, n: int, d: int):
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


if __name__ == "__main__":
    ds = Dataset()
    ds.generateClusters(20,2)
    ds.plot_points()

