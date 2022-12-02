from sfode import equations_to_cfunc_string

stiff_equation = ['dy/dt = z + t',
                  'dz/dt = -100 * y * t']

funcstr, funch = equations_to_cfunc_string(stiff_equation)

print("Function str: ", funcstr)
print("Head str: ", funch)


lorenz_equation_strs = ['dx/dt = sigma * (y - x)',
                        'dy/dt = rho * x - y - x * z',
                        'dz/dt = x * y - beta * z']

lorenz_constants = ['sigma = 10e0',
                    'rho = 28e0',
                    'beta = 8e0 / 3e0']
