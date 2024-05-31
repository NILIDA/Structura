def calculate_pressure_drop(flow_rate, height, density, pressure, previous_pressure=None):
    def pressure_drop_equation(q, h, ro, p):
        return (9.81 * ro * q * h) / (p * 1000)

    def pressure_drop_with_previous_pressure(q, h, ro, p, p_n, f1):
        print("Pressure drop with previous pressure\n")
        return (9.81 * ro * q * h) / (p_n * 1000 * f1(q, h, ro, p))

    def pressure_drop_calculation(q, h, ro, p, p_n):
        if p_n is None:
            return pressure_drop_equation(q, h, ro, p)
        else:
            return pressure_drop_with_previous_pressure(q, h, ro, p, p_n, pressure_drop_equation)

    return pressure_drop_calculation(flow_rate, height, density, pressure, previous_pressure)


print(calculate_pressure_drop(12, 12, 3, 5, 12))