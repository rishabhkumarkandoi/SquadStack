"""
Handler for processing the input file having commands. Execution of commands will be fired from here
"""

from parking_handler import ParkingHandler


class FileProcessor:
    CREATE_SLOT = "Create_parking_lot"
    PARK = "Park"
    DRIVER_AGE = "driver_age"
    GET_SLOTS_BY_AGE = "Slot_numbers_for_driver_of_age"
    GET_SLOT_BY_VEHICLE = "Slot_number_for_car_with_number"
    GET_VEHICLES_BY_AGE = "Vehicle_registration_number_for_driver_of_age"
    VACATE = "Leave"

    def __init__(self, file_path):
        self.file_path = file_path
        self.parking_handler = None
        self.invalid_command_error = "Command invalid..!!"
        self.invalid_data_type_error = "Provide correct data type. Driver age and slot number " \
                                       "should be an integer."
        self.file_error = "File error. Please cross check file path provided..!!"
        self.empty_file_error = "No commands found..!!"

    def process_file(self):
        """
        Reads file line by line
        :return: None. Prints message here only
        """
        try:
            with open(self.file_path, "r") as reader:
                if not reader:
                    print(self.empty_file_error)
                else:
                    self.parking_handler = ParkingHandler()
                for command in reader:
                    print(self.process_command(command))
        except IOError:
            print(self.file_error)

    def process_command(self, command):
        """
        For each command given, validate it and link it to correct operation required.
        :param command: Command (string)
        :return: message (string)
        """
        if self.CREATE_SLOT in command:
            total_slots = int(command.split()[-1])
            msg = self.parking_handler.create_slots(total_slots)
        elif self.PARK in command and self.DRIVER_AGE in command:
            split_command = command.split()
            vehicle_reg, age = split_command[1], split_command[-1]
            msg = self.parking_handler.park_vehicle(vehicle_reg, age)
        elif self.VACATE in command:
            slot_num = int(command.split()[-1])
            msg = self.parking_handler.vacate_slot(slot_num)
        elif self.GET_SLOTS_BY_AGE in command:
            age = command.split()[-1]
            msg = self.parking_handler.get_slots_by_age(age)
        elif self.GET_SLOT_BY_VEHICLE in command:
            vehicle_reg = command.split()[-1]
            msg = self.parking_handler.get_slot_by_vehicle_reg(vehicle_reg)
        elif self.GET_VEHICLES_BY_AGE in command:
            age = command.split()[-1]
            msg = self.parking_handler.get_vehicle_reg_by_age(age)
        else:
            msg = self.invalid_command_error
        return msg
