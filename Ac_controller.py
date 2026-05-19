class ACRemote:

    def __init__(self):
        self.power = False
        self.temperature = 24
        self.mode = "Cool"
        self.fan_speed = "Medium"
        self.swing = False

    def power_toggle(self):
        self.power = not self.power
        print("AC turned ON" if self.power else "AC turned OFF")

    def increase_temp(self):
        if self.power:
            if self.temperature < 30:
                self.temperature += 1
                print("Temperature:", self.temperature)
            else:
                print("Maximum temperature reached")
        else:
            print("Turn AC ON first")

    def decrease_temp(self):
        if self.power:
            if self.temperature > 16:
                self.temperature -= 1
                print("Temperature:", self.temperature)
            else:
                print("Minimum temperature reached")
        else:
            print("Turn AC ON first")

    def display_status(self):
        print("\n----- AC STATUS -----")
        print("Power:", "ON" if self.power else "OFF")
        print("Temperature:", self.temperature)
        print("---------------------")


remote = ACRemote()

while True:
    print("\nAC REMOTE")
    print("1. Power ON/OFF")
    print("2. Increase Temperature")
    print("3. Decrease Temperature")
    print("4. Show Status")
    print("5. Exit")

    choice = input("Press button: ")

    if choice == "1":
        remote.power_toggle()

    elif choice == "2":
        remote.increase_temp()

    elif choice == "3":
        remote.decrease_temp()

    elif choice == "4":
        remote.display_status()

    elif choice == "5":
        print("Remote turned off")
        break

    else:
        print("Invalid button")