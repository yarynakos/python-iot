from models.fridge import Fridge


class WineFridge(Fridge):
    """
     Class that describe WineFridge
    """
    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, set_price,
                 max_numbers_of_bottle, max_capacity_of_bottle):
        """

        :param brand: The brand of the fridge.
        :param model: The model of the fridge.
        :param capacity: The capacity of the fridge.
        :param is_defrosting: Defrost state of the fridge.
        :param energy_efficiency_class:  Energy efficiency of fridge.
        :param max_numbers_of_bottle: Information on the maximum number of bottles.
        :param max_capacity_of_bottle: The maximum permissible volume of the bottle.
        """
        self.max_numbers_of_bottle = max_numbers_of_bottle
        self.max_capacity_of_bottle = max_capacity_of_bottle
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class, set_price)

    def get_max_usable_capacity(self):
        """
        Overriding abstract method
        :return: Returns a list of the maximum useful volume of products that can be contained in the fridges.
        """
        return self.capacity * self.max_numbers_of_bottle

    def __str__(self):
        """
        The method returns a string view of object
        :return: String view of object
        """
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class},' \
               f' max_numbers_of_bottle: {self.max_numbers_of_bottle},' f'max_capacity_of_bottle:' \
               f' {self.max_capacity_of_bottle}'
