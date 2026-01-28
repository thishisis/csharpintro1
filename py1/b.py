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
    answer = "Percentage spent by category\n"
    spent_amounts = []
    total_spent = 0
    for i in range(len(categories)):
        spent = sum(-1*entry['amount'] for entry in categories[i].ledger if entry['amount'] < 0)
        spent_amounts.append(spent)
        total_spent += spent
    spent_percentages = [int((spent / total_spent) * 10) * 10 for spent in spent_amounts]
    for i in range(100, -1, -10):
        answer += f"{i:>3}| "
        for j in range(len(spent_percentages)):
            if spent_percentages[j] >= i:
                answer += "o  "
            else:
                answer += "   "
        answer += "\n"
    answer += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        answer += "     "
        for category in categories:
            if i < len(category.name):
                answer += category.name[i] + "  "
            else:
                answer += "   "
        if i < max_length - 1:
            answer += "\n"
    return answer

if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    food.deposit(900, "deposit")
    food.withdraw(105.55, "groceries")
    food.withdraw(33.40, "restaurant and more food for dessert")

    entertainment.deposit(900, "deposit")
    entertainment.withdraw(33.40, "movie ticket")
    
    business.deposit(900, "deposit")
    business.withdraw(10.99, "office supplies")

    print(create_spend_chart([business, food, entertainment]))