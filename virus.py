class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        # TODO Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
    def __repr__(self):
        return f"Virus(name={self.name}, repro_rate={self.repro_rate}, mortality_rate={self.mortality_rate})"


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    print(virus.name)
    print(virus.repro_rate)
    print(virus.mortality_rate)

    another_virus = Virus("Flu", 0.5, 0.1)
    assert another_virus.name == "Flu"
    assert another_virus.repro_rate == 0.5
    assert another_virus.mortality_rate == 0.1
    print(another_virus.name)
    print(another_virus.repro_rate)
    print(another_virus.mortality_rate)
    print("Second virus test passed!")

    assert repr(virus) == "Virus(name=HIV, repro_rate=0.8, mortality_rate=0.3)"
    print("Virus repr test passed!")
