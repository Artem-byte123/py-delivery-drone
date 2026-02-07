class BaseRobot:
    def __init__(self, name: str, weight: int,  coords=None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step=1) -> None:
        self.coords[1] += step

    def go_back(self, step=1) -> None:
        self.coords[1] -= step

    def go_right(self, step=1) -> None:
        self.coords[0] += step

    def go_left(self, step=1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

class FlyingRobot(BaseRobot):
    def __init__(self, weight: int, name: str, coords=None) -> None:
        if coords is None:
            coords = [0, 0, 0]

        super().__init__(name, weight, coords)

    def go_up(self, step=1) -> None:
            self.coords[2] += step

    def go_down(self, step=1) -> None:
        self.coords[2] -= step




# write your code here
