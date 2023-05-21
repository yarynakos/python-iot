from models.fridge import Fridge


class FridgeCamera(Fridge):
    VOLUME_PER_KILOGRAM = 1.5

    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class,
                 number_of_entries, type_of_tape, speed_of_tape, max_weight):
        self.number_of_entries = number_of_entries
        self.type_of_tape = type_of_tape
        self.speed_of_tape = speed_of_tape
        self.max_weight = max_weight
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class)

    def get_max_usable_capacity(self):
        return self.capacity() * self.number_of_entries

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class,}' \
               f' number_of_entries: {self.number_of_entries},' f'type_of_tape: {self.type_of_tape},' \
               f'speed_of_tape: {self.speed_of_tape},' f'max_weight: {self.max_weight},' f' VOLUME_PER_KILOGRAM' \
               f' {self.VOLUME_PER_KILOGRAM}'
