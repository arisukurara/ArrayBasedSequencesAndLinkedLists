from split_evens_odds import *

def main():
    s = SplitEvensOdds()
    s.build_forward_list([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])
    s.display()
    evens, odds = s.split_evens_odds()
    evens.display()
    odds.display()
    s.display()

if __name__ == "__main__":
    main()
