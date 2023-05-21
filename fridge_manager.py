class FridgeManager:
    def __int__(self):
        self.fridge_list = []

    def add_fridge(self, fridge):
        self.fridge_list.append(fridge)

    def find_all_fridges_bigger_than(self, value):
        return [fridge for fridge in self.fridge_list if fridge.capacity > value]

    def find_all_fridges_is_defrosing(self, value2):
        return [fridge for fridge in self.fridge_list if fridge.is_defrosting is value2]

