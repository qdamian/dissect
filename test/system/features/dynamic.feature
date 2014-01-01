Feature: Dynamic data extraction

    Scenario: identify function calls
        Given my program calls functions aa_func, ab_func, ba_func, bb_func
        When I run dissect on it
        Then the function calls aa_func, ab_func, ba_func, bb_func are identified as such
