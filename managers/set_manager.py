class SetManager:
    def __init__(self, fridge_manager):
        self.fridge_manager = fridge_manager

    def __len__(self):
        length = 0
        for fridge in self.fridge_manager.__iter__():
            length += len(fridge.set_price)
        return length

    def __iter__(self):
        new_set = set()
        for fridge in self.fridge_manager.__iter__():
            new_set.update(fridge.set_price)
        return iter(new_set)

    def __getitem__(self, key):
        for fridge in self.fridge_manager.__iter__():
            return fridge[key]

    def __next__(self):
        for fridge in self.fridge_manager.__iter__():
            return next(fridge)
