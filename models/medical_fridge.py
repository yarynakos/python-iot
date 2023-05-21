from models.fridge import Fridge


class MedicalFridge(Fridge):
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class,
                 type_of_doors, type_of_fridge, number_of_doors):
        self.type_of_doors = type_of_doors
        self.type_of_fridge = type_of_fridge
        self.number_of_doors = number_of_doors
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class)

    def get_max_usable_capacity(self):
        return self.capacity() * self.number_of_doors

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class}' \
               f' type_of_doors: {self.type_of_doors}, ' f' type_of_fridge: {self.type_of_fridge}' \
               f' number_of_doors: {self.number_of_doors}'
