class SingleWire:

    def __init__(self, material_number, description):
        self.material_number = material_number
        self.description = description
        self.components = {'Wire': '', 'Left Terminal': '', 'Right Terminal': '',
                           'Left Seal': '', 'Right Seal': '', 'KS': ''}
        self.length = 0
        self.close_materials = {}
        self.rework = {}

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError('Wire length cannot be less than zero!')
        self.__length = value

    def add_wire(self, wire_number):
        self.components['Wire'] = wire_number

    def add_left_terminal(self, terminal_number):
        self.components['Left Terminal'] = terminal_number

    def add_right_terminal(self, terminal_number):
        self.components['Right Terminal'] = terminal_number

    def add_left_seal(self, seal_number):
        self.components['Left Seal'] = seal_number

    def add_right_seal(self, seal_number):
        self.components['Right Seal'] = seal_number

    def add_ks_code(self, ks_code):
        self.components['KS'] = ks_code

    def compare_components(self, other):
        current_material = set(self.components.items())
        other_material = set(other.components.items())
        return current_material ^ other_material

    @staticmethod
    def tolerance(length):
        mapper = {
            range(0, 100): 5,
            range(100, 1000): 10,
            range(1000, 2000): 20,
            range(2000, 5000): 50,
        }
        for difference_range, value in mapper.items():
            if length in difference_range:
                return value
        return 0

    def compare_length(self, other):
        difference = self.length - other.length
        tolerance = self.tolerance(self.length)
        if 0 <= difference <= tolerance:
            return difference
        return False

class TwistedWire(SingleWire):

    def __init__(self, material_number, description):
        super().__init__(material_number, description)
        self.wires = []  # SingleWire objects
        self.spot_tape = ''

    def add_single_wire(self, single_wire):
        self.wires.append(single_wire)

    def define_protective_cover(self, protective_cover_number):
        self.spot_tape = protective_cover_number

    def compare_wires(self, other):
        result = [self.spot_tape == other.spot_tape, len(self.wires) == len(other.wires)]
        for wire in self.wires:
            for other_wire in other.wires:
                result.append(other_wire in wire.close_materials)
        if False in result:
            return False
        return True
