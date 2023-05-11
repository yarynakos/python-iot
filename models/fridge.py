class Fridge:
    __brand = 'samsung'
    __model = 'abc'
    __capacity = 100
    __is_defrosting = False
    __energy_efficiency_class = 'A'
    instance = None

    def __init__(self, brand='samsung', model='abc', capacity=100, is_defrosting=False, energy_efficiency_class='A'):
        self.__brand = brand
        self.__model = model
        self.__capacity = capacity
        self.__is_defrosting = is_defrosting
        self.__energy_efficiency_class = energy_efficiency_class

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_is_defrosting(self):
        return self.__is_defrosting

    def get_energy_efficiency_class(self):
        return self.__energy_efficiency_class

    def set_brand(self, value):
        self.__brand = value

    def set_model(self, value):
        self.__model = value

    def set_capacity(self, value):
        self.__capacity = value

    def set_is_defrosting(self, value):
        self.__is_defrosting = value

    def set_energy_efficiency_class(self, value):
        self.__energy_efficiency_class = value

    def turn_on_defrosting(self):
        self.__is_defrosting = True

    def turn_off_defrosting(self):
        self.__is_defrosting = False

    def delete_model_info(self):
        self.__model = None

    @staticmethod
    def get_instance():
        return Fridge.instance

    def __str__(self):
        return f'brand: {self.__brand}, model: {self.__model}, capacity: {self.__capacity}, is_defrosting: {self.__is_defrosting},' \
               f' energy_efficiency_class: {self.__energy_efficiency_class}'
