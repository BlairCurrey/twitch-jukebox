import unittest
from tests import t_cmus_controller

if __name__=="__main__":
    test_sets = [
        t_cmus_controller.TestSet()
    ]
    for t in test_sets:
        unittest.main(t,verbosity=2)