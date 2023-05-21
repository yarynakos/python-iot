from models.fridge import Fridge


class WineFridge(Fridge):
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class,
                 max_numbers_of_bottle, max_capacity_of_bottle):
        self.max_numbers_of_bottle = max_numbers_of_bottle
        self.max_capacity_of_bottle = max_capacity_of_bottle
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class)

    def get_max_usable_capacity(self):
        return self.capacity() * self.max_numbers_of_bottle

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class},' \
               f' max_numbers_of_bottle: {self.max_numbers_of_bottle},' f'max_capacity_of_bottle:' \
               f' {self.max_capacity_of_bottle}'
