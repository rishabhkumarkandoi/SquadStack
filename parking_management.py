"""
Manages parking of vehicles in the parking slots. Decoupled so that it can be scaled independently.
"""


class ManageParking(object):
    VEHICLES = "vehicles"
    SLOTS = "slots"
    AGE = "age"
    VEHICLE_REG = "vehicle_registration_num"

    def __init__(self):
        self.slots = [-1]
        self.age_data = {}
        self.vehicle_data = {}
        self.slot_data = {}
        self.slot_allotted_msg = "Created parking of %s slots"
        self.vehicle_parked_msg = 'Car with vehicle registration number "%s" has been parked at ' \
                                  'slot number %s'
        self.slot_vacated_msg = 'Slot number %s vacated, the car with registration number "%s" ' \
                                'left the space, the driver of the car was of age %s'
        self.parking_full_error = "Parking lot is full..!!"
        self.vacate_slot_error = "Slot is already empty, so cannot be vacated again..!!"
        self.age_error = "No driver present in age of %s..!!"
        self.vehicle_reg_error = "No car in parking lot with registration number of %s..!!"

    def create_slots(self, total_slots):
        """
        Creates slots for parking vehicles
        :param total_slots: Number of slots to be created (integer)
        :return: slot created message (string)
        """
        list(map(lambda slot_num: self.slots.append(1), range(total_slots)))
        return self.slot_allotted_msg % total_slots

    def park_vehicle(self, vehicle_reg, driver_age):
        """
        Allocates slot of the incoming vehicle
        :param vehicle_reg: Vehicle Registration Number (string)
        :param driver_age: Age of the driver (integer)
        :return: vehicle parked message (string)
        """
        try:
            empty_slot_index = self.slots.index(1)
            self.slots[empty_slot_index] = 0
            empty_slot_index = str(empty_slot_index)
            self.insert_slot_data(empty_slot_index, vehicle_reg, driver_age)
            self.insert_age_data(empty_slot_index, driver_age, vehicle_reg)
            self.insert_vehicle_data(empty_slot_index, vehicle_reg)
            return self.vehicle_parked_msg % (vehicle_reg, empty_slot_index)
        except ValueError:
            return self.parking_full_error

    def insert_slot_data(self, slot_num, vehicle_reg, age):
        """
        Inserts slot data in a dictionary in format:
        {<slot_num_1>: {'age': <>, 'vehicle_registration_num': <>}, ...}
        :param slot_num: Slot number which is being allotted (integer)
        :param vehicle_reg: Vehicle Registration number (string)
        :param age: Driver Age (integer)
        :return: Null
        """
        self.slot_data[slot_num] = {self.AGE: age, self.VEHICLE_REG: vehicle_reg}

    def insert_age_data(self, slot_num, age, vehicle_reg):
        """
        Inserts age data in a dictionary in format:
        {<age_1>: {'vehicles': [], 'slots': []}, ...}
        :param slot_num: Slot number which is being allotted (integer)
        :param age: Driver Age (integer)
        :param vehicle_reg: Vehicle Registration number (string)
        :return: Null
        """
        if age not in self.age_data:
            self.age_data[age] = {self.VEHICLES: [vehicle_reg], self.SLOTS: [slot_num]}
        else:
            self.age_data[age][self.VEHICLES].append(vehicle_reg)
            self.age_data[age][self.SLOTS].append(slot_num)

    def insert_vehicle_data(self, slot_num, vehicle_reg):
        """
        Inserts vehicle data in a dictionary in format:
        {<vehicle_registration_num_1>: <slot_num_1>, ...}
        :param slot_num: Slot number which is being allotted (integer)
        :param vehicle_reg: Vehicle Registration number (string)
        :return: Null
        """
        self.vehicle_data[vehicle_reg] = slot_num

    def vacate_slot(self, slot_num):
        """
        Vacate the parking slot of given slot number. Also clear the data related to it.
        Make the slot again available for parking another vehicle.
        :param slot_num: Slot number which needs to be vacated
        :return: slot vacated message or error message (string)
        """
        if self.slots[slot_num] == 0:
            return self.vacate_slot_error
        self.slots[slot_num] = 0
        slot_data = self.slot_data.pop(slot_num)
        self.age_data[slot_data[self.AGE]][self.SLOTS].remove(slot_num)
        self.age_data[slot_data[self.AGE]][self.VEHICLES].remove(slot_data[self.VEHICLE_REG])
        return self.slot_vacated_msg % (slot_num+1, slot_data[self.VEHICLE_REG], slot_data[self.AGE])
