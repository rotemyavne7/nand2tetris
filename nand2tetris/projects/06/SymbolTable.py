class SymbolTable(object):
    def __init__(self):
        self.sym_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576,
        }
        self.var_address = 16

    def get_variable(self, symbol):
        if symbol not in self.sym_table:
            self.sym_table[symbol] = self.var_address
            self.var_address += 1
        return self.sym_table[symbol]
    
    def add_label(self, symbol, value):
        self.sym_table[symbol] = value
        return value