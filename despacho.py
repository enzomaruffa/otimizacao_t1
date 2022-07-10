#!/usr/bin/env python3

import sys
import logging

# Create a logger that outputs to the console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Read the stdin.
# The first line is the amount of months that need to be processed.
# The second line is a list of the monthly demands
# The third line is a list of the monthly tributaries
# The fourth line is the v_ini, v_min, v_max, and k
# The fifth line is t_max and termo_cost
# The sixth line is the ambiental_cost

logger.info('Opening stdin...')

input_lines = sys.stdin.readlines()

# Get the amount of months.
months = int(input_lines[0])

# Get the monthly demands.
monthly_demands = input_lines[1].split(' ')
monthly_demands = [float(x.rstrip()) for x in monthly_demands]


# Get the monthly tributaries.
monthly_water_input = input_lines[2].split(' ')
monthly_water_input = [float(x.rstrip()) for x in monthly_water_input]

# Get the v_ini, v_min, v_max, and k.
v_ini, v_min, v_max, k = input_lines[3].split(' ')
v_ini = float(v_ini)
v_min = float(v_min)
v_max = float(v_max)
k = float(k)

# Get the t_max and termo_cost.
t_max, termo_cost = input_lines[4].split(' ')
t_max = float(t_max)
termo_cost = float(termo_cost)

# Get the ambiental_cost.
ambiental_cost = float(input_lines[5])

# Debug log all the read variables to the console.
logger.debug('months: %s', months)
logger.debug('monthly_demands: %s', monthly_demands)
logger.debug('monthly_water_input: %s', monthly_water_input)
logger.debug('v_ini: %s', v_ini)
logger.debug('v_min: %s', v_min)
logger.debug('v_max: %s', v_max)
logger.debug('k: %s', k)
logger.debug('t_max: %s', t_max)
logger.debug('termo_cost: %s', termo_cost)
logger.debug('ambiental_cost: %s', ambiental_cost)
