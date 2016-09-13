# Enter your code for the AdoptionCenter class here
# Be sure to include the __init__, get_name, get_species_count, get_number_of_species, and adopt_pet methods.
import random
class AdoptionCenter(object):
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

# Enter your code for the Adopter class here
class Adopter(object):
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
        
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
        return float(1 * adoption_center.species_types.get(self.desired_species, 0))
        
# Enter your code for the FlexibleAdopter and FearfulAdopter classes here
class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        otherScore = 0
        for x in self.considered_species:
            otherScore += float(0.3 * adoption_center.species_types.get(x, 0))
        return Adopter.get_score(self, adoption_center) + otherScore

class FearfulAdopter(Adopter):
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
# Enter your code for the AllergicAdopter and MedicatedAllergicAdopter classes here
class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    
    def get_score(self, adoption_center):
        for x in self.allergic_species:
            if x in adoption_center.species_types:
                return 0.0
        return Adopter.get_score(self, adoption_center)
        
class MedicatedAllergicAdopter(AllergicAdopter):
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

# Enter your code for the SluggishAdopter class here
import math
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
            
            

# Enter your code for get_ordered_adoption_center_list and get_adopters_for_advertisement
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    scores = [(adopter.get_score(x), x) for x in list_of_adoption_centers]
    return [x[1] for x in sorted(scores, key=lambda x: (-x[0], x[1].get_name()))]
    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    scores = [(x.get_score(adoption_center), x) for x in list_of_adopters]
    return [x[1] for x in sorted(scores, key=lambda x: (-x[0], x[1].get_name()))][:min(n, len(list_of_adopters))]       

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list

                      
# you can print the name and score of each item in the list returned