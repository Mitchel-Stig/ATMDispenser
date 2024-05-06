import math


class ATMDispenser:
    def __init__(self):
        self.available_currency = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    # Admin usage to set up currency
    def initialize_currency(self, currency):
        self.available_currency = currency

    # Admin usage to add currency
    def add_currency(self, currency):
        for denomination, count in currency.items():
            self.available_currency[denomination] += count
        print("Total Currency Counts:", self.available_currency)

    # Admin usage to remove currency
    def remove_currency(self, currency):
        for denomination, count in currency.items():
            self.available_currency[denomination] -= count
        print("Total Currency Counts:", self.available_currency)


    def withdraw(self, amount):
        dist = self.calculate_withdraw(amount)
        print("Withdrawing the following currency amounts: ", dist)
        self.remove_currency(dist)

    def calculate_withdraw(self, amount):
        dist = {}
        denoms = dict(sorted(self.available_currency.items(), reverse=True))
        for i in range(0, len(denoms)):
            dist = self.calculate_dist(i, denoms, amount)
            if self.has_funds_available(dist):
                break
        if not self.has_funds_available(dist):
            raise Exception("Not enough Currency in ATM")
        if self.get_distribution_total(dist) != amount:
            raise Exception("Amount not possible with current Denominations")
        return dist

    def calculate_dist(self, position, denoms, amount):
        withdraw_dist = {}
        for iteration in range(0, self.get_total_denom_count()):
            withdraw_dist = {}
            current_amount = amount
            current_iteration = iteration
            for i in range(position, len(denoms)):
                denom_value = list(denoms.keys())[i]
                if denom_value <= current_amount: # or negative?
                    try_denom_count = (current_amount / denom_value) - current_iteration
                    action_denom_count = min(math.floor(try_denom_count), denoms[denom_value])
                    withdraw_dist[denom_value] = action_denom_count
                    current_amount -= denom_value * action_denom_count
                    current_iteration = 0
                    if current_amount == 0:
                        return withdraw_dist

        return withdraw_dist

    def has_funds_available(self, dist):
        for denom in dist.keys():
            if self.available_currency[denom] < dist[denom]:
                return False
        return True

    def get_distribution_total(self, dist):
        total = 0
        for denom in dist:
            total += denom * dist[denom]
        return total

    def report_total_cash_amount(self):
        total = self.get_distribution_total(self.available_currency)
        print("Total Cash Amount:", total)
        return total

    def get_total_denom_count(self):
        total = 0
        for denom in self.available_currency:
            total += self.available_currency[denom]
        return total

