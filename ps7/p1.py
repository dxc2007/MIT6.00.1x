'''
Introduction

In this problem set, you will help some people find their forever friends! You have been tasked with creating a representation of both pet adoption centers and the pet adopters. By creating python classes to model both elements, you will be able to assign a score to each adopter relative to a certain adoption center. A higher score means a specific adopter is more likely to adopt a pet from a specific adoption center.

OBJECTIVES

The goal of this problem will be to learn classes, methods, and class inheritance. There are a lot of references on Python classes available (look for classes in the readings listed in the Reference Links section of the webpage); here is the official Python tutorial on classes, sections 9.1-9.7 (excepting 9.5.1) will be useful for this Problem Set.

You will learn many facets of object-oriented programming, specifically:

Implementing new classes and their attributes.
Understanding class methods.
Understanding inheritance.
Telling the difference between a class and an instance of that class - recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.

'''

import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]), float(location[1]))
    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_number_of_species(self, species_name):
        return self.species_types.get(species_name, 0)

    def adopt_pet(self, species_name):
        self.species_types[species_name] -= 1
        if self.species_types[species_name] == 0:
            self.species_types.pop(species_name, None)


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        return float(1 * adoption_center.species_types.get(self.desired_species, 0))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        otherScore = 0
        for x in self.considered_species:
            otherScore += float(0.3 * adoption_center.species_types.get(x, 0))
        return Adopter.get_score(self, adoption_center) + otherScore

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        fearScore = float(0.3 * adoption_center.species_types.get(self.feared_species, 0))
        totalScore = Adopter.get_score(self, adoption_center) - fearScore
        if totalScore < 0.0:
            return 0.0
        else:
            return totalScore


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for x in self.allergic_species:
            if x in adoption_center.species_types:
                return 0.0
        return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        positive = []
        for x in self.allergic_species:
            if x in adoption_center.species_types:
                positive.append(x)
        temp = 1.0
        for i in positive:
            if self.medicine_effectiveness[i] < temp:
                temp = self.medicine_effectiveness[i]
        return temp * Adopter.get_score(self, adoption_center)


class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    import math
    import random
    class SluggishAdopter(Adopter):
        def __init__(self, name, desired_species, location):
            Adopter.__init__(self, name, desired_species)
            self.location = location

        def get_linear_distance(self, to_location):
            return math.sqrt((self.location[0]-to_location[0])**2+(self.location[1]-to_location[1])**2)

        def get_score(self, adoption_center):
            dist = self.get_linear_distance(adoption_center.get_location())
            if dist < 1:
                return 1 * Adopter.get_score(self, adoption_center)
            elif dist < 3 and dist >= 1:
                return random.uniform(0.7, 0.9) * Adopter.get_score(self, adoption_center)
            elif dist < 5 and dist >= 3:
                return random.uniform(0.5, 0.7) * Adopter.get_score(self, adoption_center)
            else:
                return random.uniform(0.1, 0.5) * Adopter.get_score(self, adoption_center)




def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    scores = [(adopter.get_score(x), x) for x in list_of_adoption_centers]
    return [x[1] for x in sorted(scores, key=lambda x: (-x[0], x[1].get_name()))]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    scores = [(x.get_score(adoption_center), x) for x in list_of_adopters]
    return [x[1] for x in sorted(scores, key=lambda x: (-x[0], x[1].get_name()))][:min(n, len(list_of_adopters))]
