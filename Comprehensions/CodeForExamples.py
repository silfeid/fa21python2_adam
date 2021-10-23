# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:47:19 2021

@author: brode
"""

#EXAMPLE 1

#This has us write a new list which is comprised of all combinations of the elements of the two (or more) old lists. I'm frankly not sure why you would realistically want to do this, but it does allow us to map out the probability space of the combinations in a statistical sense.

bird_chances = []
for bird1 in ['Bluejay', 'Robin', 'Sparrow']:
    for bird2 in ['Osprey', 'Buzzard', 'Steller\'s Sea Eagle']:
           bird_chances.append((bird1, bird2))
print(bird_chances)

#EXAMPLE 2

#And here we achieve the same exact thing as in example 1, but using a much more efficient comprehension.

bird_chances = [(bird1, bird2) for bird1 in ['Bluejay', 'Robin', 'Sparrow'] for bird2 in ['Osprey', 'Buzzard', 'Steller\'s Sea Eagle']]
print(bird_chances)

#EXAMPLE 3

#We can make a new list using a comprehension which simply mathematically alters each value in the old list; this obviously could be done using a for loop, but the comprehension is more efficient and in fact  easier to write, once you're aware of the possibility.  Obviously almost any mathematical permutation of the list elements is possible.

bird_pops = [12.2, 45.3, 0.6, 4.1, 89.2, 11.3, 3.4]
print([pop*1000 for pop in bird_pops])

#Example 4

#We can also use built-in functions to modify the elements of our old list before adding them to our new list via the comprehension.

bird_pops = [12.2, 45.3, 0.6, 4.1, 89.2, 11.3, 3.4]
print([round(pop) for pop in bird_pops])


#EXAMPLE 5

#And we can modify the elements of the old list via a function that we've created ourselves - here, a simple one that will first round the numbers in bird_pops, then multiply them by one thousand.

def round_and_multiply(number):
    number = int(number)
    number = round(number)
    number = number*1000
    return number

bird_pops = [12.2, 45.3, 0.6, 4.1, 89.2, 11.3, 3.4]

print([round_and_multiply(pop) for pop in bird_pops])

#EXAMPLE 5 - FLATTEN LIST

#If we have a list of lists, we can "flatten" the list and combine all of the items of the individual sublists into one big, uniform list. I found this to the hardest syntax to really get my head around, but the utility is pretty clear.

bird_pops = [[12.2, 45.3, 0.6], [4.1, 89.2], [11.3, 3.4]]
print([pop for item in bird_pops for pop in item])

#EXAMPLE 6

#And all of the transformations used in our comprehensions above can be applied analogously to lists of strings.

birdies = ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon']

better_birdies = ['A '+ bird +' is a fine bird' for bird in birdies if bird[0] == 'P' or bird[0] == 'G']

print(better_birdies)

#EXAMPLE 7

#Here, we use a built-in string method, again, analogously to the example with round() above.

birdies = ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon']
worse_birdies = [bird.lstrip('P') for bird in birdies]
print(worse_birdies)

#EXAMPLE 8

#The rest of the examples deal with transposing the rows and columns of a matrix - would have been useful for our icon project, right?  This example shows how to use a nested list comprehension - one list comprehension written inside another - to do that.

bird_matrix = [
     ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon'],
     ['Y', 'Y', 'N', 'N', 'N'],
     [1, 3, 7, 4, 2],
]

print([[row[item] for row in bird_matrix] for item in range(5)])

#EXAMPLE 9

bird_matrix = [
     ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon'],
     ['Y', 'Y', 'N', 'N', 'N'],
     [1, 3, 7, 4, 2],
]

transposed_bird_matrix = []
for item in range(5):
    transposed_bird_matrix.append([row[item] for row in bird_matrix])
print(transposed_bird_matrix)

#EXAMPLE 10

bird_matrix = [
     ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon'],
     ['Y', 'Y', 'N', 'N', 'N'],
     [1, 3, 7, 4, 2],
]

transposed_bird_matrix = []
for item in range(5):
     # the following 3 lines implement the nested listcomp
     transposed_row = []
     for row in bird_matrix:
         transposed_row.append(row[item])
     transposed_bird_matrix.append(transposed_row)
print(transposed_bird_matrix)

#EXAMPLE 11

bird_matrix = [
     ['Peacock', 'Penguin', 'Snipe', 'Great Auk', 'Gyrfalcon'],
     ['Y', 'Y', 'N', 'N', 'N'],
     [1, 3, 7, 4, 2],
]

new_bird_matrix_zip = zip(*bird_matrix))
New_bird_matrix_zip_list = list(new_bird_matrix_zip)
print(new_bird_matrix_zip_list)

