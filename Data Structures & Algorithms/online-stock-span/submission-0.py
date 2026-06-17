class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.span=0
    def next(self, price: int) -> int:
        temp_stack=[]

        if not self.stack:
            self.span=1
            self.stack.append(price)
            return self.span

        self.span=1
        while self.stack and self.stack[-1]<=price:
            self.span+=1
            temp_stack.append(self.stack.pop())
        
        while temp_stack:
            self.stack.append(temp_stack.pop())
        
        self.stack.append(price)

        return self.span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)