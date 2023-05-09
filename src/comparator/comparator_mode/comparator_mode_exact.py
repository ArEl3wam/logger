"""!
It contains ComparatorModeExact class.
"""
from src.comparator.comparator_mode.comparator_mode import ComparatorMode


class ComparatorModeExact(ComparatorMode):
    """!
    Class ComparatorModeExact is used for exact comparison of two objects.
    """
    def get_comparator_options(self):
        """!
        @brief Method returns comparator options.
        @return: Comparator options.
        """
        return {
            'ignore_numeric_type_changes': True,
            'ignore_string_case': True,
        }
