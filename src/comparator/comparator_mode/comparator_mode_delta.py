"""!
It contains ComparatorModeDelta class.
"""
from src.comparator.comparator_mode.comparator_mode import ComparatorMode


class ComparatorModeDelta(ComparatorMode):
    """!
    Class ComparatorModeDelta is used for comparison of two objects with a maximum difference.
    """
    def __init__(self, delta):
        """!
        @brief Constructor of ComparatorModeDelta class.
        @param delta: Maximum difference between two objects.
        """
        self.delta = delta

    def get_comparator_options(self):
        """!
        @brief Method returns comparator options.
        @return: Comparator options.
        """
        return {
            'ignore_string_case': True,
            'math_epsilon': self.delta,
            'ignore_numeric_type_changes': True,
        }
