# Data load and downcast

## Variables

### Pressure and Temperature Variables
- `p` (mbar)
    - Atmospheric pressure
    - Unit: Millibars (mbar)
    - Description: The force per unit area exerted by the atmosphere

- `T` (degC)
    - Air temperature
    - Unit: Degrees Celsius (°C)
    - Description: Ambient air temperature measured at standard height

- `Tpot` (K)
    - Potential temperature
    - Unit: Kelvin (K)
    - Description: Temperature a parcel of air would have if brought adiabatically to standard pressure (1000 mbar)

- `Tdew` (degC)
    - Dew point temperature
    - Unit: Degrees Celsius (°C)
    - Description: Temperature at which water vapor begins to condense

### Humidity Variables
- `rh` (%)
    - Relative humidity
    - Unit: Percentage (%)
    - Description: Amount of water vapor in the air relative to maximum possible at current temperature

- `VPmax` (mbar)
    - Maximum vapor pressure
    - Unit: Millibars (mbar)
    - Description: Maximum possible water vapor pressure at current temperature

- `VPact` (mbar)
    - Actual vapor pressure
    - Unit: Millibars (mbar)
    - Description: Current water vapor pressure in the air

- `VPdef` (mbar)
    - Vapor pressure deficit
    - Unit: Millibars (mbar)
    - Description: Difference between maximum and actual vapor pressure (VPmax - VPact)

### Water Content Variables
- `sh` (g/kg)
    - Specific humidity
    - Unit: Grams per kilogram (g/kg)
    - Description: Mass of water vapor per kilogram of moist air

- `H2OC` (mmol/mol)
    - Water vapor concentration
    - Unit: Millimoles per mole (mmol/mol)
    - Description: Molar ratio of water vapor to air

### Air Density
- `rho` (g/m³)
    - Air density
    - Unit: Grams per cubic meter (g/m³)
    - Description: Mass of air per unit volume

### Wind Variables
- `wv` (m/s)
    - Wind velocity
    - Unit: Meters per second (m/s)
    - Description: Current wind speed

- `max. wv` (m/s)
    - Maximum wind velocity
    - Unit: Meters per second (m/s)
    - Description: Maximum wind speed recorded during the measurement period

- `wd` (deg)
    - Wind direction
    - Unit: Degrees (°)
    - Description: Direction from which the wind is blowing, measured clockwise from true north (0° = North, 90° = East, etc.)