""" compare costs of fuel for running cars ICE and BEV """

from typing import NamedTuple

def cost(distance, fuel_cost_per_unit, units_per_mile):
    units = distance / units_per_mile
    total_cost = fuel_cost_per_unit / 100 * units
    return units, total_cost

class Fuel(NamedTuple):
    fuel: str
    ppu: float

class Performance(NamedTuple):
    distance: int  # distance travelled in miles
    fuel: str      # petrol, diesel, InstVolt, econ7 nigh, econ7 day
    unit: str      # kHw, mpg, etc
    mpu: int       # miles per unit
    ppu: float     # price per unit
    units: int     # number of units
    cost: float    # total cost

    def __str__(self):
        return (
                f'{self.distance:6} | '
                f'{self.fuel:11}  | {self. unit:8} | '
                f'{self.mpu:5.2f} | {self.ppu:6.2f} | '
                f'{self.units:6.2f} | {self.cost:6.2f}'
        )

def report(costs):
    print('\n\n')
    header = " Miles | Fuel         | unit     |  mpu  |   ppu  | units  | £cost "
    print(f'{header}\n{"-" * len(header)}')
    for record in costs:
        print(record)
    print(f'{"-" * len(header)}')
    print('mpu: miles per unit')
    print('ppu: pence per unit')


journey = 500  # length of journey in miles
costs = []

# Electricity
mpk = 3.88  # miles per kWh
rates = (Fuel('InstaVolt', 66), Fuel('econ7 night', 17.939), Fuel('econ7 day', 40.487))

for rate in rates:
    kWh, total_elec = cost(journey, rate.ppu, mpk)
    costs.append(Performance(journey, rate.fuel, 'kWh', mpk, rate.ppu, kWh, total_elec ))

# petrol cost using national average
ppl = 165.16 # pence per litre (unleaded petrol, average cost)
GALLONS = 4.54553160571567 # this many litres per gallon
ppg = ppl * GALLONS # pence per gallon (unleaded petrol, average cost from RAC)
mpg1 = 41  # average miles per gallon of car for comparison
mpg2 = 45
gallons, total_petrol = cost(journey, ppg, mpg1)
costs.append(Performance(journey, 'unleaded', 'gallon', mpg1, ppg, gallons, total_petrol ))
gallons, total_petrol = cost(journey, ppg, mpg2)
costs.append(Performance(journey, 'unleaded', 'gallon', mpg2, ppg, gallons, total_petrol ))


report(costs)
