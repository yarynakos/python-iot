from models.fridge import Fridge


class Freezer(Fridge):
    """
      Class that describe Freezer
    """
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, set_price,
                 min_temperature, number_of_boxes):
        """
        Initializes a Freezer object
        :param brand: The brand of the fridge.
        :param model: The model of the fridge.
        :param capacity: The capacity of the fridge.
        :param is_defrosting: Defrost state of the fridge.
        :param energy_efficiency_class: Energy efficiency of fridge.
        :param min_temperature: Minimum freezing temperature.
        :param number_of_boxes: Number of boxes in fridges.
        """
        self.min_temperature = min_temperature
        self.number_of_boxes = number_of_boxes
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class, set_price)

    def get_max_usable_capacity(self):
        """
         Overriding abstract method
        :return: Returns a list of the maximum useful volume of products that can be contained in the fridges.
        """
        return self.capacity * self.number_of_boxes

    def __str__(self):
        """
        The method returns a string view of object
        :return: String view of object
        """
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class},' \
               f'min_temperature: {self.min_temperature},' f'number_of_boxes: {self.number_of_boxes}'
