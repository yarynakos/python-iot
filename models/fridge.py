from abc import ABC


class Fridge(ABC):
    """
    That abstract class describe Fridge
    """
    def __init__(self, brand='samsung', model='abc', capacity=100, is_defrosting=False, energy_efficiency_class='A'):
        """
        :param brand: The brand of the fridge.
        :param model: The model of the fridge.
        :param capacity: The capacity of the fridge.
        :param is_defrosting: Defrost state of the fridge.
        :param energy_efficiency_class:  Energy efficiency of fridge.
        """
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosting(self):
        """
        Changes the field of the object to True
        """
        self.is_defrosting = True

    def turn_off_defrosting(self):
        """
        Changes the field of the object to False
        """
        self.is_defrosting = False

    def delete_model_info(self):
        """
        Removes information about the fridge criterion
        """
        self.model = None

    def __str__(self):
        """
        The method returns a string view of object
        :return: String view of object
        """
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class}'

