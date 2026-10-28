"""some useful formulas in information theory"""
import math

unit_of_info: int
probability_of_info: float

def self_information(probability_of_info ,unit_of_info=2) -> float:
	return -1 * math.log(probability_of_info, unit_of_info)

def entrophy():
	pass
