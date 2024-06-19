# pylint:disable=too-few-public-methods
"""Holds Utilities."""


class Utilities:
    """Helper functions for get_data_feed.py"""
    @staticmethod
    def american_to_probability(odds):
        """Helper function that converts american odds into implied probability."""
        if odds < 0:
            odds = odds * -1
            probability = round((odds/(odds+100))*100, 2)
        else:
            probability = round((100/(odds+100))*100, 2)
        return probability
