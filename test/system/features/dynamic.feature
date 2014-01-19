Feature: Dynamic data extraction

    @function_calls
    Scenario: identify function calls
        Given my program calls functions main, aa_func, ab_func, ba_func, bb_func
        When I run dissect on it
        Then the function calls main, aa_func, ab_func, ba_func, bb_func are identified as such

    @threads
    Scenario: identify threads
        Given my program runs in the MainThread and more other threads
        When I run dissect on it
        Then the MainThread and four other threads are identified as such
