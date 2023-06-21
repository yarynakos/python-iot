from models.freezer import Freezer
from models.fridge_camera import FridgeCamera
from models.wine_fridge import WineFridge
from models.medical_fridge import MedicalFridge
from managers.fridge_manager import FridgeManager

if __name__ == "__main__":
    fridge_manager = FridgeManager()
    fridge_manager.add_fridge(FridgeCamera("cold", "abc1", 50.0, False, "B", {0}, 4, "електрична", 6.0, 150.0))
    fridge_manager.add_fridge(FridgeCamera("frozen", "abc6", 45.0, True, "D", {0}, 3, "механічна", 7.0, 200.0))
    fridge_manager.add_fridge(WineFridge("Tefcold", "abc4", 15.0, True, "A", {0}, 20, 1.0))
    fridge_manager.add_fridge(WineFridge("Klarstein", "adc", 20.0, True, "B", {0}, 15, 0.75))
    fridge_manager.add_fridge(Freezer("Tefal", "acb1", 32.5, False, "C", {0}, -30.0, 3))
    fridge_manager.add_fridge(Freezer("Samsung", "acb2", 29.7, True, "D", {0}, -10.0, 5))
    fridge_manager.add_fridge(MedicalFridge("inetmed", "adc2", 25.0, True, "C", {0}, "скляні", "вертикальний", 1))
    fridge_manager.add_fridge(MedicalFridge("Meling", "adc3", 40.0, False, "A", {0}, "глухі", "горизонтальний", 3))

for fridge in fridge_manager.fridge_list:
    print(fridge)

print("\n" + "All fridges with big capasity: ")
for fridge in fridge_manager.find_all_fridges_bigger_than(30):
    print(f"{fridge.brand} {fridge.capacity}")

print("\n" + "All fridges which is defrosting: ")
for fridge in fridge_manager.find_all_fridges_is_defrosing(True):
    print(f"{fridge.brand} {fridge.model}")
fridge_manager.get_list_of_max_capacity()
print(fridge_manager.get_zip_of_fridges())
fridge_manager[0].turn_off_defrosting()