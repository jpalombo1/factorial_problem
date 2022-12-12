import math
import time
from functools import partial
from itertools import product
from typing import Dict, List, Tuple


def check_digits(digits: Tuple[int, ...]) -> bool:
    """For sequence of n digits, check if d1! + d2! + ... dn! = d1d2..dn base 10.
    Fact is sum of factorial of each digit. Concat is sum of digit times place which
    is 10 ^ (len(digits) - 1 - curr_place) since inverse.
    """
    fact = sum(math.factorial(digit) for digit in digits)
    concat_places = len(digits)
    concat = sum(
        digit * 10 ** (concat_places - curr_place - 1)
        for curr_place, digit in enumerate(digits)
    )
    return fact == concat


def int_to_tuple(num: int) -> Tuple[int, ...]:
    """Take integer and return tuple of integer one for each digit.

    e.g 123 would return (1,2,3)
    """
    str_int = str(num)
    return tuple(int(digit) for digit in str_int)


def concat_fact_brute() -> List[Tuple[int, int, int]]:
    """Function to test values of a! + b! + c! = abc base 10 using brute force triple loop.

    Return list of tuples of digits that satisfy equation.
    """
    nums = range(10)
    val_list = []
    for a in nums:
        for b in nums:
            for c in nums:
                concat = a * 100 + b * 10 + c
                fact = math.factorial(a) + math.factorial(b) + math.factorial(c)
                if concat == fact:
                    val_list.append((a, b, c))
    return val_list


def concat_fact_comp() -> List[Tuple[int, int, int]]:
    """Function to test values of a! + b! + c! = abc base 10 by doing in line list comprehension of values computed.

    Return list of tuples of digits that satisfy equation. Only usable 3 digit numbers.
    """
    nums = range(10)
    return [
        (a, b, c)
        for a in nums
        for b in nums
        for c in nums
        if math.factorial(a) + math.factorial(b) + math.factorial(c)
        == a * 100 + b * 10 + c
    ]


def concat_fact_strtuple(num_places: int = 5) -> List[Tuple[int, ...]]:
    """Function to test values of a! + b! + c! + d! + ... = abcd... base 10 by using range.

    Finding n place numbers same as finding range(10^n) e.g. n=4 abcd range(10**4) = range(1000) = 0,1,...9999
    Make these numbers into a,b,c,d... tuples (0,),(1,),....(9,9,9,9)

    Since this creates tuples of size of integer (no leading 0s, will gets ABC...=A!+B!+C!+... where A != 0)
    and num_places = N will captures num_places=0,1,2,...N-1 cases as well.

    Call check_digits function for more general use where digits configurable.
    """
    tup_nums = [int_to_tuple(num) for num in range(10**num_places)]
    return [tup_num for tup_num in tup_nums if check_digits(tup_num)]


def concat_fact_itertools(num_places: int = 5) -> List[Tuple[int, ...]]:
    """Function to test values of a! + b! + c! + d! + ... = abcd... base 10 by using product chain.

    Num_tuples construction of product 1..10 N times make by product(*[range(10) for _ in range(N)]), which is
    product(*[range(10), range(10), ... N TIMES ..., range(10)]) = product(range(10), range(10),...range(10)) =
    (0,0,...0), (0,0,...1),... (9,9,....9), N digits all possible tuples to avert N nested loops.

    Since this creates tuples of size of num_places which can have leading 0s can get sequences where A=0, B=0, etc.
    e.g num_plaecs = 5, 00125 = 0! + 0! + 1! + 2! + 5!

    Call check_digits function for more general use where digits configurable.
    """
    nums = range(10)
    num_tuples = product(*[list(nums) for _ in range(num_places)])
    return [nums for nums in num_tuples if check_digits(nums)]


def get_values(values: List[Tuple[int, ...]]) -> None:
    """Function to print out results of equation friendly format."""
    for value in values:
        concat_str = "".join(str(digit) for digit in value)
        fact_str = "! + ".join(str(digit) for digit in value)
        print(f"{concat_str} = {fact_str}!")


def main() -> None:
    """Main function."""
    NUM_PLACES = 5
    funcs: Dict[str, partial] = {
        "brute": partial(concat_fact_brute),
        "comprehension": partial(concat_fact_comp),
        "itertools": partial(concat_fact_itertools, NUM_PLACES),
        "range": partial(concat_fact_strtuple, NUM_PLACES),
    }
    for func_name, func in funcs.items():
        t0 = time.time()
        vals = func()
        total_time = time.time() - t0
        get_values(vals)
        print(f"Func {func_name} Time Loops: {round((total_time * 1000), 3)} ms")


if __name__ == "__main__":
    main()
