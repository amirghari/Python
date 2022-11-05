
class Building:
    def __init__(self, elevators_no, bottom_floor, top_floor):
        self.elevators_no = elevators_no
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(self.elevators_no):
            elevator = [i+1, self.bottom_floor, self.top_floor]
            self.elevators.append(elevator)



    def run_elevator(self, elev_num, floor):
        for i in range(self.elevators_no):
            if elev_num == self.elevators[i][0]:
                bottom = self.elevators[i][1]
                top = self.elevators[i][2]
                elev_travel = Elevator(floor, bottom, bottom, top)
                print(f'You are in Elevator number {i+1} and the current floor is {elev_travel.current_floor}')




class Elevator:
    def __init__(self, go_to_floor: int, current_floor, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        if bottom_floor <= go_to_floor < current_floor:
            for i in range(-(go_to_floor - current_floor)):
                self.go_down()
        elif top_floor >= go_to_floor > current_floor:
            for i in range(go_to_floor - current_floor):
                self.go_up()
        else:
            print("This floor doesn't exist.")

    def go_down(self):
        print("one floor down!")
        self.current_floor -= 1
        return self.current_floor

    def go_up(self):
        print("one floor up!")
        self.current_floor += 1
        return self.current_floor





elevator_no = int(input("Enter the Number of elevator you want to use."))
floor = int(input("Enter the floor you want to reach."))
# result = Elevator(floor, 0, 0, 5)
# print(f'Current floor is {result.current_floor}')
a_building = Building(3, 0, 10)
a_building.run_elevator(elevator_no, floor)
