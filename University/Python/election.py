%run -i ../m269_util

from collections import Counter

def winner(votes: list) -> str:
    """
    Return the most frequent string in votes, a list of strings
    or return 'round 2' if two or more strings are equally frequent the counter value is greater than 1
    """
    votes_counter = Counter(votes)
    # a Counter method that sorts counter values in descending order
    sorted_counter = votes_counter.most_common()
    
    for k,v in sorted_counter:
        # count the number of times the counter value appears 
        times_drawn_count = list(votes_counter.values()).count(v)
        # if the counter value appears more than once and it is greater than 1
        if (times_drawn_count > 1) and (v > 1): return "round 2"
        # else if we are down to counter values of 1
        elif v == 1: return sorted_counter[0][0]
        # else continue on with loop 
        else: continue
            

winner_tests = [
    # case,         votes,                              name
    ['2 of 2 tied', ['Alice', 'Bob', 'Bob', 'Alice'],   'round 2'],
    ['1 of 2 wins', ['Alice', 'Bob', 'Alice', 'Alice'], 'Alice'  ],
    ['1 of 3 wins', ['Bob', 'Chan', 'Chan', 'Alice'],   'Chan'   ],
    # new tests:
]

test(winner, winner_tests)
