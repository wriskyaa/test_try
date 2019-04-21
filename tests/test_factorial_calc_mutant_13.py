import time
from random import Random
from unittest.mock import patch

from factorial_calc import factorial_calc as original
from factorial_calc_mutant_13 import factorial_calc as mutated


def rand_runner(rand_min, rand_max):
    random = Random()
    f_measure = 0
    while True:
        n = random.randint(rand_min, rand_max)
        with patch('builtins.print') as mocked_print:
            # expected = original(10)
            mutated(n)
            original(n)
            if mocked_print.call_args_list[0] != mocked_print.call_args_list[1]:
                return f_measure
        f_measure = f_measure + 1


def main():
    total_f_measures = 0
    simulation_iterations = 3000
    start_time = time.time()
    for i in range(simulation_iterations + 1):
        f_measure = rand_runner(-1, 1000)
        print('F-measure: ', format(f_measure))
        total_f_measures = total_f_measures + f_measure

    avg_f_measure = total_f_measures / 3000
    print("average_f_measure", format(avg_f_measure))
    print("--- %s seconds ---" % (time.time() - start_time))

main()
