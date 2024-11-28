import random
from virus import Virus

class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection=None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        """This method checks if a person survived an infection."""
        if self.infection is not None:
            # Person has an infection, check if they survive or die based on mortality rate
            if random.random() < self.infection.mortality_rate:
                self.is_alive = False  # Person dies
                self.infection = None  # They are no longer infected after death
            else:
                self.is_vaccinated = True  # Person survives and becomes vaccinated
                self.infection = None  # Infection is cleared after survival
        return self.is_alive  # Returns True if the person survived, False if they died

if __name__ == "__main__":
    # Testing the Person class
    # Create a Virus object
    virus = Virus("Dysentery", 0.7, 0.2)  

    # Create a vaccinated person
    vaccinated_person = Person(1, True)
    print(f"Vaccinated person - ID: {vaccinated_person._id}, Alive: {vaccinated_person.is_alive}, Vaccinated: {vaccinated_person.is_vaccinated}, Infection: {vaccinated_person.infection}")

    # Create an unvaccinated person
    unvaccinated_person = Person(2, False)
    print(f"Unvaccinated person - ID: {unvaccinated_person._id}, Alive: {unvaccinated_person.is_alive}, Vaccinated: {unvaccinated_person.is_vaccinated}, Infection: {unvaccinated_person.infection}\n")

    # Create an infected person
    infected_person = Person(3, False, virus)
    print(f"Infected person - ID: {infected_person._id}, Alive: {infected_person.is_alive}, Vaccinated: {infected_person.is_vaccinated}, Infection: {infected_person.infection}")

    # Simulate survival or death for a group of 100 people
    people = [Person(i, False, virus) for i in range(1, 101)]

    did_survive = 0
    did_not_survive = 0

    # Simulate survival/death based on mortality rate
    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"People who survived: {did_survive}")
    print(f"People who did not survive: {did_not_survive}")
    print(f"Expected Mortality rate: {int(virus.mortality_rate * 100)}%")

    # Test 2
    person.did_survive_infection()
    assert person.is_alive == True 
    print("Person survival test passed!")

    # Test 3:
    high_mortality_virus = Virus("FatalVirus", 0.5, 0.8)
    person = Person(2, False, high_mortality_virus)
    person.did_survive_infection()
    assert person.is_alive == False
    print("Person mortality test (high mortality rate) passed!")



    # Stretch challenge: Simulate infection spread among uninfected people
    uninfected_people = [Person(i, False) for i in range(1, 101)]
    became_infected = 0
    became_vaccinated = 0

    for person in uninfected_people:
        if random.random() < virus.repro_rate:  # Infection rate check
            person.infection = virus
            became_infected += 1
        else:
            became_vaccinated += 1

    print(f"People who became infected: {became_infected}")
    print(f"Virus infection rate: {int(virus.repro_rate * 100)}%")
    print(f"People who remained uninfected and vaccinated: {became_vaccinated}")
