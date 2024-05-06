class ATMDispenser:
    def __init__(self):
        self.available_currency = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    # Admin usage to add currency
    def add_currency(self, currency):
        for denomination, count in currency.items():
            self.available_currency[denomination] += count

    # Admin usage to remove currency
    def remove_currency(self, currency):
        for denomination, count in currency.items():
            self.available_currency[denomination] -= count

    def report_available_currency(self):
        return self.available_currency

    def dispense_cash(self, amount):
        remaining_amount = amount
        dispensed_currency = {}

        all_denominations = sorted(self.available_currency.keys(), reverse=True)

        for denomination in all_denominations:
            if remaining_amount <= 0:
                break

            if denomination <= remaining_amount and self.available_currency[denomination] > 0:
                num_units = min(remaining_amount // denomination, self.available_currency[denomination])
                dispensed_currency[denomination] = num_units
                remaining_amount -= num_units * denomination

        if remaining_amount == 0:
            self.remove_currency(dispensed_currency)
            return dispensed_currency
        else:
            return "Error: Unable to dispense requested amount"
