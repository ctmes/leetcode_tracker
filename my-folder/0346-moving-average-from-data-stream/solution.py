class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.window_sum = 0
        
    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val
        
        # If window size is exceeded, remove oldest element
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.pop(0)
            
        return self.window_sum / min(len(self.queue), self.size)
