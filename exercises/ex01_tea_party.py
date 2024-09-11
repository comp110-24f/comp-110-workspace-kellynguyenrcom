"""Exercise 01 Tea Party"""

__author__: str = "730477537"


def main_planner(guests: int) -> None:
    """main"""
    print(f"A Cozy Tea Party for {guests} People!")
    tea_bags_needed: int = tea_bags(guests)
    print(f"Tea Bags: {tea_bags_needed}")
    treats_needed: int = treats(guests)
    print(f"Treats: {treats_needed}")
    total_cost: float = cost(tea_bags_needed, treats_needed)
    print(f"Cost: ${total_cost}")
    # variales are needed to fill in whats in brackets, careful will determinging what goes in it, what are you looking for


def tea_bags(people: int) -> int:
    """the numnber of people attending tea party and tea bags"""
    return people * 2


def treats(people: int) -> int:
    """the number of guests attending the tea party and treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
