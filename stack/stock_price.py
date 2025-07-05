class Stockspan:
    def __init__(self):
        self.stack = []
    
    def calculate_span(self, prices):
        spans = [0] * len(prices)
        for i, price in enumerate(prices):
            span = 1
            while self.stack and self.stack[-1][0] <=price:
                span += self.stack.pop()[1]
            
            self.stack.append((price, span))
            spans[i] = span
        return spans
    
spanner = Stockspan()
prices = [100, 80, 60, 70, 60, 75, 85]
print(spanner.calculate_span(prices))