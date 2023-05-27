from  decorators.decorators import check_duration_time


class FridgeManager:
    """
    This is class to manage fridges
    """
    fridge_list = []

    def __init__(self):
        """
        Initializes a FridgeManager object.
        """
        self.fridge_list = []

    def add_fridge(self, fridge):
        """
        Adds a fridge to the list of fridges.
        :param fridge: The fridge object to be added.
        """
        self.fridge_list.append(fridge)

    def find_all_fridges_bigger_than(self, value):
        """
        Finds all fridges with a capacity greater than the specified value.
        :param value: Capacity value for comparison
        :return: List of fridges
        """
        return list(filter(lambda fridge: fridge.capacity > value, self.fridge_list))

    def find_all_fridges_is_defrosing(self, value2):
        """
        Finds fridges by their defrosting status
        :param value2: Value for comparison
        :return: List of fridges
        """
        return list(filter(lambda fridge: fridge.is_defrosting is value2, self.fridge_list))

    @check_duration_time
    def get_list_of_max_capacity(self):
        return [fridge.get_max_usable_capacity() for fridge in self.fridge_list]

    def get_list_of_elements_with_index(self):
        return [f'{index}, {fridge}' for fridge, index in enumerate(self.fridge_list)]

    def get_zip_of_fridges(self):
        return [zip(fridge, fridge.get_max_usable_capacity()) for fridge in self.fridge_list]

    def conditions_dictionary(self):
        return {'all': all(fridge.capacity > 30 for fridge in self.fridge_list), 'any': any(fridge.capacity > 30 for
                                                                                            fridge in self.fridge_list)}

    def __len__(self):
        return len(self.fridge_list)

    def __getitem__(self, index):
        return self.fridge_list[index]

    def __iter__(self):
        return iter(self.fridge_list)
