# AICP Week 1 Tasks

#Task 1
class Pupil:
    def __init__(self, name, first_day_weight):
        self.name = name
        self.first_day_weight = first_day_weight
        self.last_day_weight = None

    def set_last_day_weight(self, last_day_weight):
        self.last_day_weight = last_day_weight

    def calculate_weight_difference(self):
        return self.last_day_weight - self.first_day_weight


class WeightTracker:
    def __init__(self, num_pupils=30):
        self.num_pupils = num_pupils
        self.pupils = []

    @staticmethod
    def validate_weight(weight):
        try:
            weight = float(weight)
            if not (0 < weight <= 300):  # Arbitrary weight limits
                return False
            return True
        except ValueError:
            return False
        
    def input_pupil_data(self):
        print("Enter the names and weights of pupils (in kilograms)!")
        for i in range(self.num_pupils):
            name = input(f"Enter name of pupil {i + 1}: ")
            weight_valid = False
            while not weight_valid:
                weight = input(f"Enter weight of {name}: ")
                if self.validate_weight(weight):
                    weight_valid = True
                    pupil = Pupil(name, float(weight))
                    self.pupils.append(pupil)
                else:
                    print("Invalid weight! Please enter a valid weight.")
    #Task 2
    def input_last_day_weights(self):
        print("\nEnter the weights of pupils on the last day:")
        for pupil in self.pupils:
            weight_valid = False
            while not weight_valid:
                weight = input(f"Enter weight of {pupil.name} on last day: ")
                if self.validate_weight(weight):
                    weight_valid = True
                    pupil.set_last_day_weight(float(weight))
                else:
                    print("Invalid weight! Please enter a valid weight.")
    #Task 3
    def output_pupil_details(self):
        print("\nPupil details:")
        for pupil in self.pupils:
            print(f"Name: {pupil.name}, "
                  f"First Day Weight: {pupil.first_day_weight} kg, "
                  f"Last Day Weight: {pupil.last_day_weight} kg, "
                  f"Weight Difference: {pupil.calculate_weight_difference()} kg")

    def output_weight_changes(self):
        print("\nWeight Changes:")
        for pupil in self.pupils:
            weight_difference = pupil.calculate_weight_difference()
            if abs(weight_difference) > 2.5:
                change_type = "rise" if weight_difference > 0 else "fall"
                print(f"{pupil.name} has a {change_type} in weight "
                      f"by {abs(weight_difference)} kg.")


def main():
    #Task 1
    tracker = WeightTracker()
    tracker.input_pupil_data()
    #Task 2
    tracker.input_last_day_weights()
    #Task 3
    tracker.output_pupil_details()
    tracker.output_weight_changes()


if __name__ == "__main__":
    main()


