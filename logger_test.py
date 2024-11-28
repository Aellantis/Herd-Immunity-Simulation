from logger import Logger 

# Test 1
def test_write_metadata():
    # Prepare a Logger instance
    logger = Logger("test_log.txt")

    logger.write_metadata(10000, "Flu", 500, 7000, 0.05, 0.7)

    with open("test_log.txt", "r") as file:
        content = file.read()

    assert "Population Size: 10000" in content
    assert "Virus Name: Flu" in content
    assert "Mortality Rate: 0.05" in content
    assert "Vaccination Percentage: 0.7" in content
    assert "Initially Infected: 500" in content
    assert "Initially Vaccinated: 7000" in content

    print("Test 1: write_metadata() passed!")


# Test 2:
def test_log_interactions():
    logger = Logger("test_log.txt")
    logger.log_interactions(1, 200, 50)
    with open("test_log.txt", "r") as file:
        content = file.read()

    assert "Wave: 1" in content
    assert "Number of Interactions: 200" in content
    assert "Number of New Infections: 50" in content
    print("Test 2: log_interactions() passed!")


# Test 3
def test_log_infection_survival():
    class Person:
        def __init__(self, is_alive, is_vaccinated):
            self.is_alive = is_alive
            self.is_vaccinated = is_vaccinated

    logger = Logger("test_log.txt")
    population = [Person(True, False), Person(False, False), Person(True, True)]
    logger.log_infection_survival(1, 10000, 500, 7000, 2000, 10, population)

    with open("test_log.txt", "r") as file:
        content = file.read()

    assert "Wave: 1" in content
    assert "Population Size: 10000" in content
    assert "Living People: 2" in content 
    assert "Vaccinated People: 1" in content 
    assert "Initially Infected: 500" in content
    assert "Total Fatalities: 10" in content

    print("Test 3: log_infection_survival() passed!")


# Run the tests
if __name__ == "__main__":
    test_write_metadata()
    test_log_interactions()
    test_log_infection_survival()
