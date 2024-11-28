class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, virus_name, initially_infected, initially_vaccinated, mortality_rate, vacc_percentage):
        formatted_string = f""" 
        ---------------
            Population Size: {pop_size}
            Virus Name: {virus_name}
            Mortality Rate: {mortality_rate}
            Vaccination Percentage: {vacc_percentage}
            Initially Infected: {initially_infected}
            Initially Vaccinated: {initially_vaccinated}
        ---------------
        """
        with open(self.file_name, "w") as f:
            f.write(formatted_string) 

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        formatted_string = f""" 
        ---------------
            Wave: {step_number}
            Number of Interactions: {number_of_interactions}
            Number of New Infections: {number_of_new_infections}
        ---------------
        """

        with open(self.file_name, "a") as f:
            f.write(formatted_string) 

    def log_infection_survival(self, step_number, pop_size, initially_infected, initially_vaccinated, total_vaccinations, fatalities_total, population):
        living_people = len([person for person in population if person.is_alive])
        vaccinated_people = sum(1 for person in population if person.is_vaccinated)

        formatted_string = f""" 
        ---------------
            Wave: {step_number}
            Population Size: {pop_size}
            Living People: {living_people}
            Vaccinated People: {vaccinated_people}
            Initially Infected: {initially_infected}
            Initially Vaccinated: {initially_vaccinated}
            Total Fatalities: {fatalities_total}
            Total Vaccinations: {total_vaccinations}
        ---------------
        """
        with open(self.file_name, "a") as f:
            f.write(formatted_string) 
