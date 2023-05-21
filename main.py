from models.freezer import Freezer
from models.fridge_camera import FridgeCamera
from models.wine_fridge import WineFridge
from models.medical_fridge import MedicalFridge
import fridge_manager

if __name__ == "main":
    fridge_manager = fridge_manager.FridgeManager()
    fridge_list = [
        fridge_manager.add_fridge(FridgeCamera("cold", "abc1", 50.0, False, "B", 4, "електрична", 6.0, 150.0)),
        fridge_manager.add_fridge(FridgeCamera("frozen", "abc6", 45.0, True, "D", 3, "механічна", 7.0, 200.0)),
        fridge_manager.add_fridge(WineFridge("Tefcold", "abc4", 15.0, True, "A", 20, 1.0)),
        fridge_manager.add_fridge(WineFridge("Klarstein", "adc", 20.0, True, "B", 15, 0.75)),
        fridge_manager.add_fridge(Freezer("Tefal", "acb1", 32.5, False, "C", -30.0, 3)),
        fridge_manager.add_fridge(Freezer("Samsung", "acb2", 29.7, True, "D", -10.0, 5)),
        fridge_manager.add_fridge(MedicalFridge("inetmed", "adc2", 25.0, True, "C", "скляні", "вертикальний", 1)),
        fridge_manager.add_fridge(MedicalFridge("Meling", "adc3", 40.0, False, "A", "глухі", "горизонтальний", 3))]

    print(len(fridge_manager.fridge_list))
    for fridge in fridge_manager.fridge_list:
        print(fridge)

    print("\n" + "All fridges with big capasity: ")
    for fridge in fridge_manager.find_all_fridges_bigger_than(30):
        print(f"{fridge.brand} {fridge.capacity}")

    print("\n" + "All fridges which is defrosting: ")
    for fridge in fridge_manager.find_all_fridges_is_defrosing(True):
        print(f"{fridge.brand} {fridge.model}")
