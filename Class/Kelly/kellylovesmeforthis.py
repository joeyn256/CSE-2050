class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.total_cost = []
    def print_item_cost(self):
        i = self.item_quantity * self.item_price
        self.total_cost.append(i)
        return i
    