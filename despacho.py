#!/usr/bin/env python3

import sys
import logging

# Create a logger that outputs to the console
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def add_debug_log(logger):
    class LevelFilter(object):
        def __init__(self, level):
            self.level = level

        def filter(self, record):
            return record.levelno != self.level

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    handler.addFilter(LevelFilter(logging.INFO))

    logger.addHandler(handler)

# add_debug_log(logger)

def add_output_log(logger):
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

add_output_log(logger)

# Read the stdin.
# The first line is the amount of months that need to be processed.
# The second line is a list of the monthly demands
# The third line is a list of the monthly tributaries
# The fourth line is the v_ini, v_min, v_max, and k
# The fifth line is t_max and ct
# The sixth line is the ca

logger.debug('Opening stdin...')

input_lines = sys.stdin.readlines()

# Get the amount of months.
months = int(input_lines[0])

# Get the monthly demands.
d_is = input_lines[1].split(' ')
d_is = [float(x.rstrip()) for x in d_is]


# Get the monthly tributaries.
y_is = input_lines[2].split(' ')
y_is = [float(x.rstrip()) for x in y_is]

# Get the v_ini, v_min, v_max, and k.
v_ini, v_min, v_max, k = input_lines[3].split(' ')
v_ini = float(v_ini)
v_min = float(v_min)
v_max = float(v_max)
k = float(k)

# Get the t_max and ct.
t_max, ct = input_lines[4].split(' ')
t_max = float(t_max)
ct = float(ct)

# Get the ca.
ca = float(input_lines[5])

# Debug log all the read variables to the console.
logger.debug('months: %s', months)
logger.debug('d_is: %s', d_is)
logger.debug('y_is: %s', y_is)
logger.debug('v_ini: %s', v_ini)
logger.debug('v_min: %s', v_min)
logger.debug('v_max: %s', v_max)
logger.debug('k: %s', k)
logger.debug('t_max: %s', t_max)
logger.debug('ct: %s', ct)
logger.debug('ca: %s', ca)

# objetivo: minimizar o custo
# min ∑(ci)

def get_months(): 
    return range(1, months + 1)

# Print the minimization
logger.info(f"min: { ' + '.join(['c_' + str(i) for i in get_months()]) };")

for i in get_months():
    # - Todas devem ser maior ou igual a 0
    #     - `p_t_i, p_h_i, v_i, c_t_i, c_h_i, p_i ≥ 0`
    logger.info(f"p_t_{i} >= 0;")
    logger.info(f"p_h_{i} >= 0;")
    logger.info(f"v_{i} >= 0;")
    logger.info(f"c_t_{i} >= 0;")
    logger.info(f"c_h_{i} >= 0;")
    logger.info(f"p_{i} >= 0;")

    # - Produção total é da termo + hidro
    #     - `p_i = p_t_i + p_h_i`
    logger.info(f"p_{i} - p_t_{i} - p_h_{i} = 0;")

    # - Custo da termo é a produção vezes o CT
    #     - `c_t_i = p_t_i * CT`
    logger.info(f"c_t_{i} - {ct}p_t_{i} = 0;")

    # - Custo da hidro é a diferença de volume
    #     - `c_h_i = |dv_i| * CA`
    #     - `c_h_i - CA*|dv_i| = 0`
    logger.info(f"c_h_{i} - {ca}dv_P{i} - {ca}dv_N{i} = 0;")

    # - Diferença de volume é volume de um mês menos do outro
    #     - `dv_i = v_i - v_i_1`
    #     - `dv_i - v_i + v_i_1 = 0`
    #     - `dv_Pi - dv_Ni - v_i + v_i_1 = 0`
    logger.info(f"dv_P{i} - dv_N{i} - v_{i} + v_{i-1} = 0;")

    # - Produção da hidro em um mês deve ser menor que o máximo
    #     - `p_h_i < t_max`
    logger.info(f"p_h_{i} < {t_max};")

    # - Volume em um mês i nunca deve ser maior que o máximo
    #     - `v_i ≤ v_max`
    logger.info(f"v_{i} <= {v_max};")

    # - Volume em um mês i nunca deve ser menor que o mínimo
    #     - `v_i ≥ v_min`
    logger.info(f"v_{i} >= {v_min};")

    # - Volume do mês i é o volume do mês anterior + a afluência do mês atual - a quantidade de água usada para a produção
    #     - `v_i = v_i_1 + y_1 - w_p_i`
    logger.info(f"v_{i} - v_{i-1} + w_p_{i} = {y_is[i-1]};")

    # - Água usada para a produção da hidro em um mês i deve ser, no máximo, o volume resultante do mês anterior + a afluência do mês atual
    #     - `w_p_i ≤ v_i_1 + y_1`
    logger.info(f"w_p_{i} - v_{i-1} <= {y_is[i-1]};")

    # - Produção da hidro em um mês i é a água usada vezes a constante
    #     - `p_h_i = w_p_i * k`
    logger.info(f"p_h_{i} - {k}w_p_{i} = 0;")

    # - Produção de um mês i deve atender a demanda
    #     - `p_i ≥ d_i`
    logger.info(f"p_{i} - {d_is[i-1]} >= 0;")

    # - Custo do mês i é igual a soma dos custos
    #     - `c_i = c_t_i + c_h_i`
    logger.info(f"c_{i} - c_t_{i} - c_h_{i} = 0;")

# - v_0 é o volume inicial
#     - `v_0 = v_ini
logger.info(f"v_0 - {v_ini} = 0;")


