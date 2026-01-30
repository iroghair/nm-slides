class IdealGas:
    def __init__(self, name, n=1, R=8.314):
        """Create an ideal gas of n moles (using default R J/K/mol)"""
        self.name = name
        self.R = R
        self.n = n
        
    def compute_pressure(self,V,T):
        """Compute the pressure using P=nRT/V"""
        P = (self.n * self.R * T) / V
        return P
    
H2 = IdealGas("Hydrogen", 1.0)
N2 = IdealGas("Nitrogen", 2.5)
O2 = IdealGas("Oxygen", 1.333)

for gas in [H2,N2,O2]:
    pres = gas.compute_pressure(0.1,373)
    print(f'{gas.name} has a pressure of {pres:4.2f} Pa')
    
