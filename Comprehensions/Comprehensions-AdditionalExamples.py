# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:09:49 2021

@author: brode
"""
#Some completely fake lists

bird_species = ['Bluejay', 'Robin', 'Egret', 'Great Auk', 'Puffin', 'Condor', 'Junco']
#List of bird species, off the top of my head
bird_presence = ['Y', 'Y', 'N', 'N', 'N', 'N', 'Y']
#Are they found in Western PA?
bird_pops = [12, 45, 0, 4, 89, 11, 3]
#Pretend population numbers - we'll interpret this list in two ways, one, as assuming that each number corresponds to each bird, and two, assuming that each number corresponds to the population of a given bird (say, Bluejays) at a number of different locations.

#We can zip two different lists together pretty darn easily. The thing to bear in mind is that the zip object created can't be printed or otherwise manipulated the same as a list; you need to transform it into a list using list(zip_object).  Pretty easily done.

species_presence = list(zip(bird_species, bird_presence))
print(species_presence)

#And we get a list which we could convert into a dictionary pretty readily, listing each species and whether or not it's found in Western PA.

#Next we can zip all three together; just a matter of listing all three of them in our parentheses.

species_presence_pops = list(zip(bird_species, bird_presence, bird_pops))
print(species_presence_pops)

#Lastly, we could iterate over each of our lists using the method described on Python.org and in my tutorial previously, but the results would essentially be gibberish, just a list of every possible combination of elements of the three lists. I really struggled, personally, to see why I would want to combine lists in that fashion *ever*; the best I could come up with in the context of today's avian avidity was to write a list comprehension which would allow us to map a single species onto ALL of the values of another list.  This is where we pretent that the 'bird_pops' list above refers to the populations of a single species at multiple locations; what we're doing here is creating a new list that indicates the population of a given species at those various locations.

bluejay_pops = [(bird, pop) for bird in bird_species[0:1]  for pop in bird_pops]

print(bluejay_pops)
