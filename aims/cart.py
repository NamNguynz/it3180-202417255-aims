from search import search_by_title
MAX_NUMBERS_ORDERED = 20

class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def sort_by_title(self):
        self.items.sort(key=lambda dvd: (dvd.title, -dvd.cost, -dvd.length))
        print("The cart has been sorted by Title.")

    def sort_by_cost(self):
        self.items.sort(key=lambda dvd: (-dvd.cost, dvd.title))
        print("The cart has been sorted by Cost.")