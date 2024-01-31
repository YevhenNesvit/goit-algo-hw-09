import timeit

from coins_count import find_coins_greedy, find_min_coins


small_amount = 146
medium_amount = 1946
big_amount = 19469

time_small_greedy = timeit.timeit(lambda: find_coins_greedy(small_amount),
                                  number=11)
time_small_dynamic = timeit.timeit(lambda: find_min_coins(small_amount),
                                   number=11)

time_medium_greedy = timeit.timeit(lambda: find_coins_greedy(medium_amount),
                                   number=11)
time_medium_dynamic = timeit.timeit(lambda: find_min_coins(medium_amount),
                                    number=11)

time_big_greedy = timeit.timeit(lambda: find_coins_greedy(big_amount),
                                number=11)
time_big_dynamic = timeit.timeit(lambda: find_min_coins(big_amount), number=11)

print(f"{'| Algorithm': <10} | {'Time small amount': <17} | {'Time medium amount': <17} | {'Time big amount': <16}|")
print(f"| {'-'*9} | {'-'*17} | {'-'*18} | {'-'*15} |")
print(f"{'| Greedy': <11} | {time_small_greedy:<17.5f} | {time_medium_greedy:<18.5f} | {time_big_greedy:<16.5f}|")
print(f"{'| Dynamic': <11} | {time_small_dynamic:<17.5f} | {time_medium_dynamic:<18.5f} | {time_big_dynamic:<16.5f}|")
print(f"| {'-'*9} | {'-'*17} | {'-'*18} | {'-'*15} |")
