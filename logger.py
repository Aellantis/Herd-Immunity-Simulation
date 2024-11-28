class Logger('simulation_log.txt'):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, virus_name, initially_infected, initially_vaccinated, mortality_rate, vacc_percentage):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
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
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        formatted_string = f""" 
        ---------------
            Step Number: {step_number}
            Number of Interactions: {number_of_interactions}
            Number of New Infections: {number_of_new_infections}
        ---------------
        """
        with open(self.file_name, "a") as f:
            f.write(formatted_string)

    def log_infection_survival(self, step_number, pop_size, number_of_new_fatalities, initially_infected, initially_vaccinated, total_vaccinations):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        formatted_string = f""" 
        ---------------
            Step Number: {step_number}
            Population Size: {pop_size}
            Initially Infected: {initially_infected}
            Initially Vaccinated: {initially_vaccinated}
            Number of New Fatalities: {number_of_new_fatalities}
            Total Vaccinations: {total_vaccinations}
        ---------------
        """
        with open(self.file_name, "a") as f:
            f.write(formatted_string)
    
        print(formatted_string)
