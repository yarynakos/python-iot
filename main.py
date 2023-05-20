import models.fridge as fridge

arr = []
fridge1 = fridge.Fridge("LG", "air", 12, True, "A")
fridge2 = fridge.Fridge()
arr.append(fridge1)
arr.append(fridge2)
print(fridge1.__str__())
print(fridge2.__str__())
fridge1.turn_on_defrosting()
print(fridge1.__str__())
fridge1.turn_off_defrosting()
print(fridge1.__str__())
fridge1.delete_model_info()
print(fridge1.__str__())
print(fridge1.__str__())
print(fridge2.__str__())
