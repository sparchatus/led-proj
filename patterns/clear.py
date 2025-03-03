from pattern import Pattern1D
import util
import numpy as np

class Pattern(Pattern1D):

    def __init__(self, n):
        super().__init__(n)
        self.colors = np.zeros((n, 3), dtype=np.int)

    def draw(self, t):
        self.should_finish = True
        return self.colors
