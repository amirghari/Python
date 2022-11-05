
class Building:
    def __init__(self, elevators_no, bottom_floor, top_floor):
        self.elevators_no = elevators_no
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor



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






floor = int(input("Enter the floor you want to reach."))
result = Elevator(floor, 0, 0, 5)
print(f'Current floor is {result.current_floor}')

