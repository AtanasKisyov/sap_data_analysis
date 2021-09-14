class SingleWire:

    def __init__(self, material_number, description):
        self.material_number = material_number
        self.description = description
        self.components = {"Wire": "", "Left Terminal": "", "Right Terminal": "", "Left Seal": "", "Right Seal": ""}
        self.length = 0
        self.close_materials = {}
        self.rework = {}

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Wire length cannot be less than zero!")
        self.__length = value

    def add_wire(self, wire_number):
        self.components["Wire"] = wire_number

    def add_left_terminal(self, terminal_number):
        self.components["Left Terminal"] = terminal_number

    def add_right_terminal(self, terminal_number):
        self.components["Right Terminal"] = terminal_number

    def add_left_seal(self, seal_number):
        self.components["Left Seal"] = seal_number

    def add_right_seal(self, seal_number):
        self.components["Right Seal"] = seal_number

    def compare_components(self, other):
        if self.components['Wire'] == other.components['Wire']:
            first_material = set(self.components.values())
            second_material = set(other.components.values())
            return first_material.difference(second_material)
        return "Wire difference"

    def compare_length(self, other):
        difference = self.length - other.length
        if 0 <= difference <= 50:
            return difference
        return False


class TwistedWire(SingleWire):

    def __init__(self, material_number, description):
        super().__init__(material_number, description)
        self.wires = []  # SingleWire objects


class Splice(SingleWire):

    def __init__(self, material_number, description):
        super().__init__(material_number, description)
        self.wires = []  # SingleWire objects
