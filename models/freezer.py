from models.fridge import Fridge


class Freezer(Fridge):
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class,
                 min_temperature, number_of_boxes):
        self.min_temperature = min_temperature
        self.number_of_boxes = number_of_boxes
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class)

    def get_max_usable_capacity(self):
        return self.capacity() * self.number_of_boxes

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class},' \
               f'min_temperature: {self.min_temperature},' f'number_of_boxes: {self.number_of_boxes}'
