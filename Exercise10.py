class Elevator:
    def __init__(self, go_to_floor: int, current_floor, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor
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
result = Elevator(floor, 0, -3, 5)
print(f'Current floor is {result.current_floor}')
while True:
    floor = int(input("Enter the floor you want to reach."))
    result = Elevator(floor, result.current_floor, -3, 5)
    print(f'Current floor is {result.current_floor}')
