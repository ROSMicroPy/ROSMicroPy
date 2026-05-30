from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class BatteryState(Message):
    _TYPE_NAME = 'BatteryState'
    _TYPE_DEF = _TYPE_DEFS['BatteryState']
    _fields_and_field_types = {'header': 'Header', 'voltage': 'float32', 'temperature': 'float32', 'current': 'float32', 'charge': 'float32', 'capacity': 'float32', 'design_capacity': 'float32', 'percentage': 'float32', 'power_supply_status': 'uint8', 'power_supply_health': 'uint8', 'power_supply_technology': 'uint8', 'present': 'bool', 'cell_voltage': 'float32', 'cell_temperature': 'float32', 'location': 'string', 'serial_number': 'string'}
    POWER_SUPPLY_STATUS_UNKNOWN = 0
    POWER_SUPPLY_STATUS_CHARGING = 1
    POWER_SUPPLY_STATUS_DISCHARGING = 2
    POWER_SUPPLY_STATUS_NOT_CHARGING = 3
    POWER_SUPPLY_STATUS_FULL = 4
    POWER_SUPPLY_HEALTH_UNKNOWN = 0
    POWER_SUPPLY_HEALTH_GOOD = 1
    POWER_SUPPLY_HEALTH_OVERHEAT = 2
    POWER_SUPPLY_HEALTH_DEAD = 3
    POWER_SUPPLY_HEALTH_OVERVOLTAGE = 4
    POWER_SUPPLY_HEALTH_UNSPEC_FAILURE = 5
    POWER_SUPPLY_HEALTH_COLD = 6
    POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE = 7
    POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE = 8
    POWER_SUPPLY_TECHNOLOGY_UNKNOWN = 0
    POWER_SUPPLY_TECHNOLOGY_NIMH = 1
    POWER_SUPPLY_TECHNOLOGY_LION = 2
    POWER_SUPPLY_TECHNOLOGY_LIPO = 3
    POWER_SUPPLY_TECHNOLOGY_LIFE = 4
    POWER_SUPPLY_TECHNOLOGY_NICD = 5
    POWER_SUPPLY_TECHNOLOGY_LIMN = 6
    POWER_SUPPLY_TECHNOLOGY_TERNARY = 7
    POWER_SUPPLY_TECHNOLOGY_VRLA = 8

    def __init__(self, header=None, voltage=None, temperature=None, current=None, charge=None, capacity=None, design_capacity=None, percentage=None, power_supply_status=None, power_supply_health=None, power_supply_technology=None, present=None, cell_voltage=None, cell_temperature=None, location=None, serial_number=None):
        self['header'] = {} if header is None else header
        self['voltage'] = 0.0 if voltage is None else voltage
        self['temperature'] = 0.0 if temperature is None else temperature
        self['current'] = 0.0 if current is None else current
        self['charge'] = 0.0 if charge is None else charge
        self['capacity'] = 0.0 if capacity is None else capacity
        self['design_capacity'] = 0.0 if design_capacity is None else design_capacity
        self['percentage'] = 0.0 if percentage is None else percentage
        self['power_supply_status'] = 0 if power_supply_status is None else power_supply_status
        self['power_supply_health'] = 0 if power_supply_health is None else power_supply_health
        self['power_supply_technology'] = 0 if power_supply_technology is None else power_supply_technology
        self['present'] = False if present is None else present
        self['cell_voltage'] = [] if cell_voltage is None else cell_voltage
        self['cell_temperature'] = [] if cell_temperature is None else cell_temperature
        self['location'] = '' if location is None else location
        self['serial_number'] = '' if serial_number is None else serial_number

dataMap = BatteryState.get_data_map()
