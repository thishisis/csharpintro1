class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -1*amount, "description": description})
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        #why duble check funds?
        if self.check_funds(amount) and self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.balance
    
    def __str__(self):
        answer = f"{self.name:*^30}\n"
        for entry in self.ledger:
            answer += f"{entry['description'][:23]:<23}{entry['amount']:>7.2f}\n"
        answer += f"Total: {self.balance:.2f}"
        return answer

def create_spend_chart(categories):
    pass