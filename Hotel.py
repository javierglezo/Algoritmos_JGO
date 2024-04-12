from Room import Room
from Employee import Employee
class Hotel(Room, Employee):
    """
    Python class to implement a comprehensive hotel management system.

    This class encompasses functionalities for managing hotel rooms, employees, and guest reservations, 
    providing a foundational system for hotel operations.

    Syntax
    ------
    obj = Hotel(name)

    Parameters
    ----------
    [in] name : str
        The name of the hotel.

    Returns
    -------
    obj : Hotel
        An instance of the Hotel class, representing a single hotel with its management capabilities.

    Attributes
    ----------
    name : str
        The name of the hotel.
    rooms : list
        A list of Room instances representing the rooms available in the hotel.
    employees : list
        A list of Employee instances representing the employees working at the hotel.
    reservations : dict
        A dictionary mapping room numbers to guest names, representing current reservations.
    """
    #Here you start your code.
    def __init__(self, name, rooms, employees, reservations):
        #Room.__init__(self, room_type, room_number, room_state, room_price)
        #Employee.__init__(self, emp_id, name, position, salary)
        self._name = name
        self._rooms = []
        self._employees = []
        self._reservations = []


    def add_room(self, room):
        self._rooms.append(room)  
    def remove_room(self, room_number):
        for room in self._rooms:
            if room.get_room_number() == room_number:
                self._rooms.remove(room)
                print("Habitación {} eliminada del hotel.".format(room_number))
                return
        print("No se encontró la habitación {} en el hotel.".format(room_number))
    def add_employee(self, employee):
        self._employees.append(employee)
    def remove_employee(self, emp_id):
        for employee in self._employees:
            if employee.get_emp_id() == emp_id:
                self._employees.remove(employee)
                print("Empleado {} eliminado del hotel.".format(emp_id))
                return
        print("No se encontró el empleado {} en el hotel.".format(emp_id))

    def check_in(self, room_number, guest_name):
        for reservation in self._reservations:
            if reservation["reservation_number"] == guest_name:
                room_number = reservation["room_number"]
                for room in self._rooms:
                    if room.get_room_number() == room_number:
                        room.check_in()
                        print("Check-in realizado con éxito para la reserva número {}.".format(guest_name))
                        return
        print("No se encontró la reserva número {}.".format(guest_name))
    def check_out(self, room_number):
        for reservation in self._reservations:
            if reservation["reservation_number"] == room_number:
                room_number = reservation["room_number"]
                for room in self._rooms:
                    if room.get_room_number() == room_number:
                        room.check_out()
                        self._reservations.remove(reservation)
                        print("Check-out realizado con éxito para la reserva número {}.".format(room_number))
                        return
        print("No se encontró la reserva número {}.".format(room_number))
    def find_room(self, room_number):
        pass
     



    


def main():
# TESTING
    print("=================================================================")
    print("Test Case 1: Create a Hotel.")
    print("=================================================================")
    hotel = Hotel("Grand Hotel")
    if hotel.name == "Grand Hotel":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Add a Room to the Hotel.")
    print("=================================================================")

    room1 = Room("Doble", 101, "Desocupada", 150)
    hotel.add_room(room1)

    if hotel.rooms[0] == room1:
        print("Test PASS. Room has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_room().")

    print("=================================================================")
    print("Test Case 3: Remove a Room from the Hotel.")
    print("=================================================================")

    hotel.remove_room(101)
    if len(hotel.rooms) == 0:
        print("Test PASS. Room has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_room().")

    print("=================================================================")
    print("Test Case 4: Add an Employee to the Hotel.")
    print("=================================================================")

    emp1 = Employee(1, "John Doe", "Receptionist", 30000)
    hotel.add_employee(emp1)

    if hotel.employees[0] == emp1:
        print("Test PASS. Employee has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_employee().")

    print("=================================================================")
    print("Test Case 5: Remove an Employee from the Hotel.")
    print("=================================================================")

    hotel.remove_employee(1)
    if len(hotel.employees) == 0:
        print("Test PASS. Employee has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_employee().")

    print("=================================================================")
    print("Test Case 6: Check-in a Guest.")
    print("=================================================================")

    room2 = Room("Suite", 102, "Desocupada", 300)
    hotel.add_room(room2)
    check_in_result = hotel.check_in(102, "Alice")

    if check_in_result == "Check-in successful for Alice in room 102." and room2.room_state == "Ocupada":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

    print("=================================================================")
    print("Test Case 7: Check-out a Guest.")
    print("=================================================================")

    check_out_result = hotel.check_out(102)

    if check_out_result == "Check-out successful for Alice from room 102." and room2.room_state == "Desocupada":
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")

    print("=================================================================")
    print("Test Case 8: Attempt Check-in on an Occupied Room.")
    print("=================================================================")

    check_in_result = hotel.check_in(102, "Bob")
    if check_in_result == "Room not available or already occupied.":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

if __name__ == "__main__":
    main()