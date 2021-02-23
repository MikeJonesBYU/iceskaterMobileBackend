from unittest import TestCase
from main import createTest

class TestCreateTest(TestCase):
    #     #Jump Types:
    #     #"axel" = 0;
    #     #"toe" = 1;
    #     #"flip" = 2;
    #     #"lutz" = 3;
    #     #"loop" = 4;
    #     #"sal" = 5;
    #     #"half-loop" = 6;
    #     #"waltz" = 7;

    def testak1_09(self):
        filename = "example_ak1_09.txt"
        # todo: make the windows 150 samples wit hte jump in there.
        # this has been retimed.
        beg = 2690  # 2729
        end = 2805  # 2805
        # ... 135 entries.  should be aggr. using max value.  window size 150, sampling interval 5.
        # What is Orion's thing doing?  we are using Orion's code.
        # window size is maybe 155?
        # 150 / 5 = 30  270 / 30 = 9  and there's 9 reaings per sample.
        # actualy have 279 entries in vector, so that's 31 readings.
        expected = 2  # it's a flip.
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_10(self):
        filename = "example_ak1_10.txt"
        beg = 3620  # 3647
        end = 3750  # 3724
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_13(self):
        filename = "example_ak1_13.txt"
        beg = 75  # 89
        end = 170  # 151
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_14(self):
        filename = "example_ak1_14.txt"
        beg = 2500  # 2523
        end = 2600  # 2594
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_15(self):
        filename = "example_ak1_15.txt"
        beg = 1800  # 1813
        end = 1900  # 1867
        expected = 4
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_17(self):
        filename = "example_ak1_17.txt"
        beg = 1800  # 2390
        end = 1900  # 2459
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testal1_02(self):
        filename = "example_al1_02.txt"
        beg = 1960  # 1994
        end = 2080  # 2047
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_05(self):
        filename = "example_cnp_05.txt"
        beg = 1390  # 1406
        end = 1500  # 1482
        expected = 3
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_20(self):
        filename = "example_cnp_20.txt"
        beg = 610  # 621
        end = 710  # 698
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)
