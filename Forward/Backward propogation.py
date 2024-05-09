class MultiplyGate(object):
    def forward(self, x, y):
        z = x * y
        self.x = x
        self.y = y
        return z

    def backward(self, dz):
        dx = self.y * dz
        dy = self.x * dz
        return [dx, dy]
