from unittest import TestCase
from main import createTest

# add the 9 entries for "now" at the index of the center of the jump and that should give us the vector
# we are after.

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

    def retimed_value(self, row):
        return (int) (row * 104/120)

    def testak1_09(self):
        filename = "example_ak1_09.txt"
        # this has been retimed.
        beg = self.retimed_value(2690) # 2729
        end = self.retimed_value(2805)  # 2805
        # ... 135 entries.  should be aggr. using max value.  window size 150, sampling interval 5.
        # 150 / 5 = 30  270 / 30 = 9  and there's 9 reaings per sample.
        # actualy have 279 entries in vector, so that's 31 readings.
        expected = 2  # it's a flip.
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_10(self):
        filename = "example_ak1_10.txt"
        beg = self.retimed_value(3620)  # 3647
        end = self.retimed_value(3750)  # 3724
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_13(self):
        filename = "example_ak1_13.txt"
        beg = self.retimed_value(75)  # 89
        end = self.retimed_value(170)  # 151
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_14(self):
        filename = "example_ak1_14.txt"
        beg = self.retimed_value(2500)  # 2523
        end = self.retimed_value(2600)  # 2594
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_15(self):
        filename = "example_ak1_15.txt"
        beg = self.retimed_value(1800)  # 1813
        end = self.retimed_value(1900)  # 1867
        expected = 4
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testak1_17(self):
        filename = "example_ak1_17.txt"
        beg = self.retimed_value(2200)  # 2390
        end = self.retimed_value(2500)  # 2459
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testal1_02(self):
        filename = "example_al1_02.txt"
        beg = self.retimed_value(1960)  # 1994
        end = self.retimed_value(2080)  # 2047
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_05(self):
        filename = "example_cnp_05.txt"
        beg = self.retimed_value(1390)  # 1406
        end = self.retimed_value(1500)  # 1482
        expected = 3
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_20(self):
        filename = "example_cnp_20.txt"
        beg = self.retimed_value(610)  # 621
        end = self.retimed_value(710)  # 698
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)
