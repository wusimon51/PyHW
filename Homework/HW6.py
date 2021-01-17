# WARNING: Iterative solutions will not be considered correct.

def digit_sum(num):
    """
    Recursively compute the sum of the digits in a given number.

    Hint: First cast num to a string.

    :param num: the number
    :type num: int
    :return: the sum of the digits of {num}
    :rtype: int
    """
    pass


def hanoi(rings):
    """
    The Tower of Hanoi is a classic mathematical toy. You are given three rods.
    Upon the first rod are a number of discs in ascending order (largest on the bottom, smallest on top).
    Your objective is to move the entire stack of discs onto another rod (any other rod),
    obeying the following rules:
    1. Only one disc can be moved at a time.
    2. You can only move the topmost disc from any rod to another rod.
    3. You cannot move a larger disc on top of a smaller disc.

    Recursively find the minimum number of moves required with a given number of rings.

    Hint: Try it yourself.
    Hint: To move the bottom disc, you will have to move the entire stack on top of it to another rod first.

    :param rings: the number of rings the puzzle starts with
    :type rings: int
    :return: the minimum number of moves to solve a Tower of Hanoi with {rings} discs
    :rtype: int
    """
    pass


def subset_sum(nums, target):
    """
    Recursively determine whether some subset of a given list of numbers sums to a target value.
    Negative values are allowed, both as the target and in the list of numbers.
    If the list is empty, this is vacuously False.

    Hint: Consider what happens if you subtract one of the numbers from the target.
    Hint: Alternatively, generate all subsets of the given list.

    :param nums: the list of numbers
    :type nums: list[int]
    :param target: the target number
    :type target: int
    :return: True if {target} is the sum of a subset of {nums}; else False
    :rtype: bool
    """
    pass


def permute(array):
    """
    Recursively generate all permutations of a given list.

    Hint: nPn = n! = n(n-1)!. But why?
    Hint: To rearrange a list of items, you must rearrange a subset of those items.
    Hint: Perhaps everything but the first item?

    :param array:
    :type array: list
    :return:
    :rtype: list[list]
    """
    pass