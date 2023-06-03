from models.fridge import Fridge


class FridgeCamera(Fridge):
    """
     Class that describe FridgeCamera
     :param VOLUME_PER_KILOGRAM: describes the volume of 1 kilogram of sausage.
    """
    VOLUME_PER_KILOGRAM = 1.5

    def __init__(self, brand, model, capacity, is_defrosting, energy_efficiency_class, set_price,
                 number_of_entries, type_of_tape, speed_of_tape, max_weight):
        """
        Initializes a FridgeCamera object
        :param brand: The brand of the fridge.
        :param model: The model of the fridge.
        :param capacity: The capacity of the fridge.
        :param is_defrosting: Defrost state of the fridge.
        :param energy_efficiency_class: Energy efficiency of fridge.
        :param number_of_entries: Number of entries to the sausage fridge.
        :param type_of_tape: Type of belt drive for hanging and moving sausage products
        :param speed_of_tape: Belt speed.
        :param max_weight: The maximum weight of sausages that the tape can withstand.
        """
        self.number_of_entries = number_of_entries
        self.type_of_tape = type_of_tape
        self.speed_of_tape = speed_of_tape
        self.max_weight = max_weight
        super().__init__(brand, model, capacity, is_defrosting, energy_efficiency_class, set_price)

    def get_max_usable_capacity(self):
        """
        Overriding abstract method
        :return: Returns a list of the maximum useful volume of products that can be contained in the fridges.
        """
        return self.capacity * self.number_of_entries

    def __str__(self):
        """
        The method returns a string view of object
        :return: String view of object
        """
        return f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}, is_defrosting:' \
               f' {self.is_defrosting},'  f' energy_efficiency_class: {self.energy_efficiency_class,}' \
               f' number_of_entries: {self.number_of_entries},' f'type_of_tape: {self.type_of_tape},' \
               f'speed_of_tape: {self.speed_of_tape},' f'max_weight: {self.max_weight},' f' VOLUME_PER_KILOGRAM' \
               f' {self.VOLUME_PER_KILOGRAM}'
