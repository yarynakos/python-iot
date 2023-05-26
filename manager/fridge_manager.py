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
