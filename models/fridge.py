class Fridge:
    __instance = None

    def __init__(self, brand='samsung', model='abc', capacity=100, is_defrosting=False, energy_efficiency_class='A'):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        self.model = None

    @staticmethod
    def get_instance():
        return Fridge.__instance

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting: {self.is_defrosting},' \
               f' energy_efficiency_class: {self.energy_efficiency_class}'

