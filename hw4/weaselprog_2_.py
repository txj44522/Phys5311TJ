'''
A function is defined to recreate Richard Dawkins' weasel program.
:Usage:
To use, put this file in a place where Python can find it.  To see Python's
search path, type this in the python terminal:
#>>>from sys import path
#>>>print(path)

Next, import the module:
#>>> import weaselprog_2_

Author: Tre'Shunda James
'''


# Define function
def weasel(num_offspring, rate,target = 'methinks IT IS LIKE A WEASEL'):
    '''
    :param:
    num_offspring: int
    target: str
    rate: float
    :return: the number of generations
    :Usage:
    #>>> generation = weaselprog_2_.weasel(100, 0.04,'methinks IT IS LIKE A WEASEL')
    #>>> generation
    ------------------------------------------------------------------------------------------------------------------
    This function takes three input parameters: number of offsprings as an int,  mutation rate as a float and target as
    a string. The function converts target from a string into a list of characters. The default target phrase is
    'methinks IT IS LIKE A WEASEL'. Then, generates a list of random characters, that is limited to letters and spaces,
    that is the length of the target list and stores it as a variable named 'parent'.
    Then mutates the 'parent' list a given number of times as specified by num_offsprings at a given mutation rate,
    in the range 0.0-0.1, where each mutation is called an 'offspring'.
    Next, the function takes the fittest or most similar offspring to the target and sets that as the new
    'parent' and repeats until the most similar offspring matches the target. The function returns the number
    of iterations (or generations) it takes for the randomly generated 'parent' to become the target.
    '''
    # Import the necessary module to use random.
    import random
    # List of acceptable characters.
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    # For given target, make all letters in target uppercase. The code will not converge with lowercase letters in
    # target.
    target = target.upper()
    # Take the string target and store it as a list.
    target_list = list(target)
    # Raise ValueError message if rate is not given as a decimal between 0 and 1.
    if rate >= 0.1 or rate <= 0.0:
        raise ValueError("Rate must be in range (0.0,0.1). Examples: 0.01,0.02,0.03,...0.09")
    # Raise TypeError message if num_offspring is not an integer.
    if type(num_offspring) != int:
        raise TypeError("Number of offsprings must be an integer. Examples: 1,20,200")

    # Empty array to store the most-similar offspring
    fittest = []

    # Create a parent list that is composed of as many randomly selected characters as the length of the target
    parent = random.choices(characters, k=len(target_list))

    # Empty array to store offsprings
    offsprings = []

    # Now count the number of generations to arrive at target
    # Initialize generation as the integer 0
    generation = 0
    # While loop to continue iterations until the fittest offspring matches the target
    while fittest != target_list:
        # For each loop add 1 to generation. This keeps track of what generation the code is on.
        generation = generation + 1
        # produce num_offspring with each letter able to mutate at given rate
        for i in range(num_offspring):
            # copy the parent list and store it as offspring
            offspring = parent[:]
            # print(offspring); for debugging
            # print(len(offspring)); for debugging
            # Now, for mutating offspring, let each letter in offspring mutate at the given rate.
            for l in range(len(offspring)):
                # If larger than given mutation rate, would indicate that a certain letter should be changed.
                if random.random() < rate:
                    # Copy the characters list and store it as new_characters.
                    new_characters = characters[:]
                    # Removes the mutating letter from the characters list and store the new list as new_characters.
                    new_characters.remove(parent[l])
                    # print(parent[l]); for debugging
                    # Replace the letter up for mutation with a random letter from new_character.
                    offspring[l] = random.choice(new_characters)
                    # print(new_characters); for debugging
            # Add offspring to the list offsprings.
            offsprings.append(offspring)
        # print(offsprings); for debugging

        # Now, find most similar offspring.
        # The minimal difference is initialized as the length of the target phrase + 1 to ensure it will always be
        # larger than the difference between the letters in the offspring and the target.
        min_difference = len(target_list) + 1
        # Take each offspring in the list offsprings.
        for offspring in offsprings:
            # Initialize the difference as integer 0, so that the count increases.
            difference = 0
            # For-loop over each letter in target_list.
            for k in range(len(target_list)):
                # If a letter in the same position of offspring and target_list and not equal to one another, add 1 to
                #the difference count.
                if offspring[k] != target_list[k]:
                    # Increase difference count by 1.
                    difference = difference + 1
            # Keep the offspring with the minimal difference.
            # If the difference for an offspring is smaller than the minal difference, store that number as
            # min_difference.
            if difference < min_difference:
                min_difference = difference
                # Store offspring with minimal difference as fittest.
                fittest = offspring
        # Now, use fittest as the parent offspring in next iteration.
        parent = fittest
        #print(generation)#; to print to screen the generation number at the end of each iteration.
        #print(''.join(parent))#; to print to screen the parent phrase at the end of each iteration.
    return (generation)

