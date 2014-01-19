Feature: Static data extraction

    Scenario: identify modules
        Given my program has modules main, aa, ab, ba, bb
        When I run dissect on it
        Then the modules main, aa, ab, ba, bb are identified as such

    Scenario: identify function
        Given my program has functions main, aa_func, ab_func, ba_func, bb_func
        When I run dissect on it
        Then the functions main, aa_func, ab_func, ba_func, bb_func are identified as such
