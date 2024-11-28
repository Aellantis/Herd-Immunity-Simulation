from simulation import Simulation
from virus import Virus

# Test 1: Test initialization of the simulation
def test_simulation_initialization():
    virus = Virus("Flu", 0.02, 0.05)
    pop_size = 10000
    vacc_percentage = 0.7
    initially_vaccinated = int(pop_size * vacc_percentage)
    initially_infected = 785
    
    # Create a simulation instance
    sim = Simulation(virus, pop_size, vacc_percentage, initially_vaccinated, 0.05, initially_infected)

    # Check initialization
    assert sim.pop_size == pop_size
    assert sim.vacc_percentage == vacc_percentage
    assert sim.initially_infected == initially_infected
    assert sim.initially_vaccinated == initially_vaccinated
    assert sim.mortality_rate == 0.05
    assert len(sim.population) == pop_size
    print("Test 1: Simulation initialization passed!")

# Test 2
def test_infection_survival():
    virus = Virus("Flu", 0.02, 0.05)
    pop_size = 100
    vacc_percentage = 0.7
    initially_vaccinated = int(pop_size * vacc_percentage)
    initially_infected = 10

    # Create a simulation instance
    sim = Simulation(virus, pop_size, vacc_percentage, initially_vaccinated, 0.05, initially_infected)
    
    # Ensure the population is freshly created
    infected_person = sim.population[0]
    
    # Reset the infection and survival process for the test
    infected_person.infection = virus  # Infected again for the test
    infected_person.is_alive = True  # Reset to alive before infection
    
    # Simulate infection survival
    infected_person.did_survive_infection()
    
    # After survival, the person should be vaccinated
    assert infected_person.is_vaccinated == True
    assert infected_person.is_alive == True
    print("Test 2: Infection survival passed!")


# Run all tests
if __name__ == "__main__":
    test_simulation_initialization()
    test_infection_survival()
