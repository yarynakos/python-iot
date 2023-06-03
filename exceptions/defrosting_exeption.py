class DefrostingExceptions(Exception):
    message = 'Fridge can not be turn off'

    def __init__(self, defrosting_status, message='Fridge can not be turn off'):
        self.defrosting_status = defrosting_status
        self.message = message
        super().__init__(self.message)
