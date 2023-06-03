from models.fridge import Fridge


class MedicalFridge(Fridge):
    """
     Class that describe MedicalFridge
    """
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, set_price,
                 type_of_doors, type_of_fridge, number_of_doors):
        """

        :param brand: The brand of the fridge.
        :param model: The model of the fridge.
        :param capacity: The capacity of the fridge.
        :param is_defrosting: Defrost state of the fridge.
        :param energy_efficiency_class:  Energy efficiency of fridge.
        :param type_of_doors: Which type of doors has fridge.
        :param type_of_fridge: Type of fridge.
        :param number_of_doors: How many doors has fridge.
        """
        self.type_of_doors = type_of_doors
        self.type_of_fridge = type_of_fridge
        self.number_of_doors = number_of_doors
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class, set_price)

    def get_max_usable_capacity(self):
        """
        Overriding abstract method
        :return: Returns a list of the maximum useful volume of products that can be contained in the fridges.
        """
        return self.capacity * self.number_of_doors

    def __str__(self):
        """
        The method returns a string view of object
        return: String view of object
        """
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class}' \
               f' type_of_doors: {self.type_of_doors}, ' f' type_of_fridge: {self.type_of_fridge}' \
               f' number_of_doors: {self.number_of_doors}'
