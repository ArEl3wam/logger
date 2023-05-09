"""!
It contains Comparator class.
"""
from deepdiff import DeepDiff
from .comparator_mode.comparator_mode_delta import ComparatorModeDelta
from .comparator_mode.comparator_mode_exact import ComparatorModeExact


class Comparator:
    """!
    Class Comparator is used for comparing two objects.
    """

    def __init__(self, comparator_mode=None):
        """!
        @brief Constructor of Comparator class.
        @param comparator_mode: Mode of the comparator.
        """
        if comparator_mode is None:
            comparator_mode = ComparatorModeExact()
        self.comparator_options = comparator_mode.get_comparator_options()

    def compare(self, data1, data2):
        """!
        @brief Method compares two objects.
        @param data1: First object to compare.
        @param data2: Second object to compare.
        @return: Difference between two objects.
        """
        return DeepDiff(data1, data2, **self.comparator_options)

    @classmethod
    def compare_dict(cls, row_content):
        """!
        @brief Method takes any dict with "expected, actual, tolerance" keys and returns new dict with status, difference keys
        @return: new dict with expected, actual, tolerance, status and difference keys
        """
        keys_list = list(row_content.keys())
        if "expected" in keys_list:
            expected = row_content["expected"]
            actual = row_content["actual"]
            tolerance = row_content["tolerance"]
            if tolerance > 0:
                result = Comparator(ComparatorModeDelta(tolerance)).compare(expected, actual)
            else:
                result = Comparator(ComparatorModeExact()).compare(expected, actual)
            if result:
                return {
                    "expected": expected,
                    "actual": actual,
                    "tolerance": tolerance,
                    "status": "fail",
                }
            else:
                return {
                    "expected": expected,
                    "actual": actual,
                    "tolerance": tolerance,
                    "status": "pass",
                }
        else:
            return_dict = {}
            for key in keys_list:
                result = cls.compare_dict(row_content[key])
                return_dict[key] = result
            return return_dict
