def module_fuel(mass):
    if mass > 0:
        fuel = mass // 3  - 2
        if fuel > 0:
            return fuel + module_fuel(fuel)
        else:
            return 0
    else:
        return 0
