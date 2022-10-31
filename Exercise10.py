

class Elevator:
    def __init__(self, go_to_floor):
        self.current_floor = 0
        if go_to_floor < 0:
            for i in range(-go_to_floor):
                self.go_down()
        else:
            for i in range(go_to_floor):
                self.go_up()

    def go_down(self):
        print("one floor down!")
        self.current_floor -= 1
        return self.current_floor

    def go_up(self):
        print("one floor up!")
        self.current_floor += 1
        return self.current_floor




floor = int(input("Enter the floor you want to reach."))
result = Elevator(floor)
print(f'Current floor is {result.current_floor}')
