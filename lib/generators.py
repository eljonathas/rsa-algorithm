from typing import Tuple
from lib.math import eucext
from math import floor
from random import random

def n_num_gen(max_number: int) -> Tuple[int, int]:
  range_list = list(range(max_number + 1))
  prime_list = []

  for number in range_list:
      if number > 1:
          for i in range(2, number):
              if (number % i) == 0:
                  break
          else:
              prime_list.append(number)

  prime_number        = prime_list[len(prime_list) - 1]
  second_prime_number = prime_list[len(prime_list) - 2]
  n_number            = second_prime_number * prime_number
  fi_n_number         = (second_prime_number - 1) * (prime_number - 1)

  return [n_number, fi_n_number]

def e_num_gen(fi_n_number: int) -> int:
  random_value = floor(random() * fi_n_number)
  g, x, y = eucext(random_value, fi_n_number)

  if g == 1:
    return random_value
  else:
    return eucext(fi_n_number)