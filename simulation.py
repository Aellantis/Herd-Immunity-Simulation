import random
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initially_vaccinated, mortality_rate, initially_infected=1):
        self.logger = Logger('simulation_log.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initially_infected = initially_infected
        self.initially_vaccinated = initially_vaccinated
        self.mortality_rate = mortality_rate

        self.step_counter = 0
        self.number_of_interactions = 0
        self.number_of_new_infections = 0  # Change to simple counter
        self.fatalities_total = []
        self.total_vaccinations = [initially_vaccinated + initially_infected]
        self.population = self._create_population()

    def _create_population(self):
        population = []
        for i in range(self.pop_size):
            person = Person(i, False)
            population.append(person)
        
        infected_count = 0
        while infected_count < self.initially_infected:
            random_person = random.choice(population)
            if random_person.infection is None:
                random_person.infection = self.virus
                infected_count += 1

        vaccinated_count = 0
        while vaccinated_count < self.initially_vaccinated:
            random_person = random.choice(population)
            if not random_person.is_vaccinated and random_person.is_alive:
                random_person.is_vaccinated = True
                vaccinated_count += 1
        return population

    def _simulation_should_continue(self):
        living_people = [person for person in self.population if person.is_alive]
        living_infected_people = [person for person in living_people if person.infection]
        if len(living_people) == 0:
            return False
        if not living_infected_people:
            return False  # Stop if there are no infected people left to spread the infection
        if all(person.is_vaccinated or person.infection for person in living_people):
            return False

        return True

    def run(self):
        should_continue = True

        self.logger.write_metadata(
            self.pop_size,
            self.virus.name,
            self.initially_infected,
            self.initially_vaccinated,
            self.mortality_rate,
            self.vacc_percentage,
        )
        print(f"Simulation starting with {self.pop_size} people.")

        while should_continue:
            self.step_counter += 1
            print(f"Wave: {self.step_counter}")  # Debugging step counter
            self.time_step()  # Run a full time step
            should_continue = self._simulation_should_continue()
            print(f"Should Continue: {should_continue}")  # Debugging condition

        self.logger.log_infection_survival(
            self.step_counter,
            self.pop_size,
            self.initially_infected,
            self.initially_vaccinated,
            sum(self.total_vaccinations),
            sum(self.fatalities_total),
            self.population
        )

    def time_step(self):
        number_of_interactions = 100
        living_people = [person for person in self.population if person.is_alive]
        living_infected_people = [person for person in living_people if person.infection]

        if not living_infected_people:
            print("No infected people to interact with.")

        for person in living_infected_people:
            completed_interactions = 0
            while completed_interactions < number_of_interactions:
                random_person = random.choice(living_people)
                self.number_of_interactions += 1  
                self.interaction(person, random_person)  # Pass both the infected and random person
                completed_interactions += 1 
        
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        
        # Only interact if the random person is susceptible and hasn't already been infected
        if not random_person.is_vaccinated and random_person.infection is None and random_person.is_alive:
            random_number = random.random()
            if random_number < self.virus.repro_rate:
                random_person.infection = self.virus
                self.number_of_new_infections += 1  # Increment new infections counter
                print(f"Person {random_person._id} got infected!")  # Debugging infection spread
                print(f"New infections: {self.number_of_new_infections}")  # Debugging new infection count

        self.logger.log_interactions(
            self.step_counter,
            self.number_of_interactions,
            self.number_of_new_infections,  # Use the count of new infections directly
        )

    def _infect_newly_infected(self):
        newly_infected = [person for person in self.population if person.infection and person.is_alive]
        print(f"Infected people: {len(newly_infected)}")  # Debugging number of newly infected

        for person in newly_infected:
            if person.did_survive_infection():  # No need to pass mortality_rate here
                self.total_vaccinations.append(1)
                person.is_vaccinated = True
            else:
                self.fatalities_total.append(1)
                person.is_alive = False
                person.infection = None

        # Debugging total infections and resets
        print(f"Total new infections so far: {self.number_of_new_infections}")  # Check if counter is working
        # Reset the number of new infections for the next step
        self.number_of_new_infections = 0

if __name__ == "__main__":
    virus_name = "Flu"
    repro_num = 0.02
    mortality_rate = 0.05
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 10000
    vacc_percentage = 0.7
    initially_vaccinated = int(pop_size * vacc_percentage)
    initially_infected = 785

    sim = Simulation(virus, pop_size, vacc_percentage, initially_vaccinated, mortality_rate, initially_infected)
    sim.run()
    print(f"Simulation complete. Steps: {sim.step_counter}, Fatalities: {sum(sim.fatalities_total)}")
