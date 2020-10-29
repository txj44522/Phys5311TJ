'''
This code is an example use of the weasel function found in weaselprog_2_. This code explores the degrees of
freedom in the weasel function. Here the number of generations it takes for the parent to match the target
is averaged over 5 runs and is plotted as a function of mutation rate, number of offsprings, and target phrases.

Author: Tre'Shunda James
'''
# Import the necessary module for the weasel function
import weaselprog_2_
# Import the plotting module
import matplotlib.pyplot as plt

# Define list of input values for mutation rate
rate = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]
# Define list of input values for number of offsprings
num_offspring = [10,20,30,40,50,60,70,80,90,100]
# Define list of input phrases for target
target = ['H',"Hell","Hello","Hello there"]

# Empty list to store the number of generations until convergence for varying rate
gen_list_1 = []
# Empty list to store the number of generations until convergence for varying number of offspring
gen_list_2 = []
# Empty list to store the number of generations until convergence for varying target phrases
gen_list_3 = []

# Perform the for-loop for each value given in rate
for i in rate:
    # Empty list to store the generation from each rate
    gen_i = []
    # Perform the for-loop 5 times
    for k in range(5):
        # Use the weasel function with 100 offsprings,  i as the rate, and 'methings IT IS A WEASEL' as the
        # target phrase and return the iterations until convergence and store it as generation.
        generation = weaselprog_2_.weasel(100, i)
        # Add the generation to the gen_i list
        gen_i.append(generation)
    #print(gen_i) # For debugging
    # Calculate the average of the list of 5 values for generation
    avg_gen = sum(gen_i)/len(gen_i)
    #print(avg_gen) # For debugging
    # Add the average of the generation list to gen_list_1
    gen_list_1.append(avg_gen)
print(gen_list_1) # For debugging

# Perform the for-loop for each value given in num_offspring
for j in num_offspring:
    # Empty list to store the generation from each rate
    gen_j = []
    # Perform the for-loop 5 times
    for k in range(5):
        # Use the weasel function with j offsprings,  0.04 as the rate, and 'methings IT IS A WEASEL' as the
        # target phrase and return the iterations until convergence and store it as generation.
        generation = weaselprog_2_.weasel(j, 0.04)
        # Add the generation to the gen_i list
        gen_j.append(generation)
    #print(gen_j)# For debugging
    # Calculate the average of the list of 5 values for generation
    avg_gen_2 = sum(gen_j)/len(gen_j)
    #print(avg_gen_2)# For debugging
    # Add the average of the generation list to gen_list_1
    gen_list_2.append(avg_gen_2)
print(gen_list_2)# For debugging

# Perform the for-loop for each phrase given in target
for l in target:
    # Empty list to store the generation from each rate
    gen_l = []
    # Perform the for-loop 5 times
    for k in range(5):
        # Use the weasel function with 100 offsprings,  0.04 as the rate, and l as the
        # target phrase and return the iterations until convergence and store it as generation.
        generation = weaselprog_2_.weasel(100, 0.04,l)
        # Add the generation to the gen_i list
        gen_l.append(generation)
    #print(gen_l)# For debugging
    # Calculate the average of the list of 5 values for generation
    avg_gen_3 = sum(gen_l) / len(gen_l)
    #print(avg_gen_3)# For debugging
    # Add the average of the generation list to gen_list_1
    gen_list_3.append(avg_gen_3)
print(gen_list_3)# For debugging




# Create figure 1
plt.figure(1)
# Plot Generations vs Rate
plt.plot(rate,gen_list_1)
# Create title
plt.title('Average Generations vs Rate')
# Name x axis
plt.xlabel('Rate')
# Name y axis
plt.ylabel('Average Generations')



# Create figure 2
plt.figure(2)
# Plot Generations vs Number of Offsprings
plt.plot(num_offspring, gen_list_2)
# Create title
plt.title('Average Generations vs Number of Offsprings')
# Name x axis
plt.xlabel('Number of Offsprings')
# Name y axis
plt.ylabel('Average Generations')



# Create figure 3
plt.figure(3)
# Plot Generations vs Target Phrase
plt.plot(target, gen_list_3)
# Create title
plt.title('Average Generations vs Target Phrase')
# Name x axis
plt.xlabel('Target Phrase')
# Name y axis
plt.ylabel('Average Generations')

# Show all three figures
plt.show()




