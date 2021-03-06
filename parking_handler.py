"""
Single class to handle all parking system.
"""

from parking_management import ManageParking


class ParkingHandler(ManageParking):
    def __init__(self):
        super(ParkingHandler, self).__init__()

    def get_slots_by_age(self, age):
        """
        Get all slots allotted to all drivers of the given age
        :param age: Driver Age (integer)
        :return: comma separated slot numbers or error message (string)
        """
        if age not in self.age_data:
            return self.age_error % age
        return ",".join(self.age_data[age][self.SLOTS])

    def get_vehicle_reg_by_age(self, age):
        """
        Get all vehicle registration numbers belonging to all drivers of the given age
        :param age: Driver Age (integer)
        :return: comma separated vehicle registration numbers or error message (string)
        """
        if age not in self.age_data:
            return self.age_error % age
        return ",".join(self.age_data[age][self.VEHICLES])

    def get_slot_by_vehicle_reg(self, vehicle_reg):
        """
        Get the slot allotted to the car with given given registration number
        :param vehicle_reg: Vehicle Registration number (string)
        :return: slot occupied by car with given registration number or error message (string)
        """
        return self.vehicle_data.get(vehicle_reg, self.vehicle_reg_error % vehicle_reg)
