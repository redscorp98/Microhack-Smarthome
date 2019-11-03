
runtime = 6

applicances = [{"Appliance": "Fridge", "Fuel": "Electricity", "Rate": 5, "Status": True},
               {"Appliance": "Kettle", "Fuel": "Electricity",
                   "Rate": 100, "Status": True},
               {"Appliance": "Oven", "Fuel": "Gas", "Rate": 3, "Status": True},
               {"Appliance": "Boiler", "Fuel": "Gas", "Rate": 10, "Status": True}]


class ApplianceGenerator:
    def generate_appliance(self, *args):
        self.appliance = args[0]
        self.fuel = args[1]
        self.rate = args[2]
        self.state = True
        return self


class Appliance(ApplianceGenerator):
    def create_appliance(self, type):
        if type == "Fridge":
            return self.generate_appliance("Fridge", "Electricity", 5)
        if type == "Kettle":
            return self.generate_appliance("Kettle", "Electricity", 100)


class SmartHome:
    def __init__(self):
        print("Initialised")

    def run(self):
        print("Starting simulation, running for ", runtime, " hours")
        total_consumption = {"Electricity": 0, "Gas": 0}
        for hour in range(runtime):
          #  input("Press enter to continue...\n")
            print("Hour: ", hour)
            for applicance in applicances:
                if applicance["Status"]:
                    total_consumption[applicance["Fuel"]
                                      ] += applicance["Rate"]
            print(total_consumption)


if __name__ == "__main__":
    home = SmartHome()
    home.run()
