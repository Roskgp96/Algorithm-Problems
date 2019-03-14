"""Function to solve the unique cap to each person problem.
   For Problem statement visit https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person/
   The solution doesn't involve any bit-masking and instead uses python dictionary and a recursive Function.
   Memoizartion can be introduced to increase speed"""

   
import copy

def unique_ways(person_to_caps):
    """Function to count number of unique ways to distribute caps so that each person wears a unique cap.

    Args:
        person_to_caps (Dict): The dictionary containing caps owned by each person.(Persons are numbered from 0 to n-1 and
                               caps are numbered from 0 to N-1)


    Returns:
        no_of_ways (int): Number of unique ways to distribute caps so that each person wears a unique cap
    """


    min_person = min(person_to_caps.keys())
    no_of_ways = 0

    if len(person_to_caps.keys()) == 1:
        no_of_ways = len(person_to_caps[min_person])

    else:
        for item in person_to_caps[min_person]:
            x = copy.deepcopy(person_to_caps)
            del x[min_person]
            for k,v in x.items():
                if item in v:
                    v.remove(item)
            no_of_ways += unique_ways(x)

    return no_of_ways

if __name__ == "__main__":
    input = {0:[5,35,99,0],1:[2,17,76],2:[5,99,55]}
    print(unique_ways(input))
