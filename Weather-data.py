#!/usr/bin/env python3


import numpy as np

# Simulated average daily temperatures (in degrees Celsius) for a month
temperatures = np.linspace(start=25.0, stop=40, num=100) + np.random.normal(loc=0, scale=0.2, size=100)

print(temperatures)