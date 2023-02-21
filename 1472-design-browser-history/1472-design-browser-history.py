class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.step = 1
    def visit(self, url: str) -> None:
        while(len(self.history) != self.step):
                self.history.pop()
        self.history.append(url)
        self.step += 1

    def back(self, steps: int) -> str:
        if(self.step - steps > 0):
            self.step -= steps
        else:
            self.step = 1
        return self.history[self.step - 1]
    def forward(self, steps: int) -> str:
        if(self.step + steps > len(self.history)):
            self.step = len(self.history)
        else:
            self.step += steps
        return self.history[self.step - 1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)