"link: https://www.w3schools.com/python/scipy/scipy_intro.php"


from scipy import constants

class about_scipy:

    def scipy_intro(self):
        # SciPy stands for Scientific Python.
        # It provides more utility functions for optimization, stats and signal processing.

        print(dir(constants))
        print(constants.liter)
        print(constants.pi)


scientific= about_scipy()
scientific.scipy_intro()
