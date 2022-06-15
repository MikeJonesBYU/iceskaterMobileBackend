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
        end = self.retimed_value(2805) # 2805
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

    def testcnp_04(self):
        filename = "example_cnp_04.txt"
        beg = self.retimed_value(450)  # 472
        end = self.retimed_value(600)  # 543
        expected = 1
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_04lutz(self):
        filename = "example_cnp_04.txt"
        beg = self.retimed_value(2900)  # 2919
        end = self.retimed_value(3000)  # 2986
        expected = 3
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testman_05(self):
        filename = "example_man_05.txt"
        beg = self.retimed_value(3400)  # 3410
        end = self.retimed_value(3500)  # 3475
        expected = 5
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testman_05_toe(self):
        filename = "example_man_05.txt"
        beg = self.retimed_value(3500)  # 3589
        end = self.retimed_value(3700)  # 3652
        expected = 1
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testgaf_06(self):
        filename = "example_gaf_06.txt"
        beg = self.retimed_value(1500)  # 1565
        end = self.retimed_value(1610)  # 1598
        expected = 5
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testgaf_06_sal(self):
        filename = "example_gaf_06.txt"
        beg = self.retimed_value(4630)  # 4634
        end = self.retimed_value(4700)  # 4665
        expected = 5
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testgaf_06_sal_2(self):
        filename = "example_gaf_06.txt"
        beg = self.retimed_value(7900)  # 7907
        end = self.retimed_value(7941)  # 7939
        expected = 5
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testjrd_04_loop(self):
        filename = "example_jrd_04.txt"
        beg = self.retimed_value(750)  # 753
        end = self.retimed_value(810)  # 801
        expected = 4
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testjrd_04_loop_2(self):
        filename = "example_jrd_04.txt"
        beg = self.retimed_value(1850)  # 1876
        end = self.retimed_value(1930)  # 1926
        expected = 4
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testal1_04_flip(self):
        filename = "example_al1_04.txt"
        beg = self.retimed_value(300)  # 315
        end = self.retimed_value(400)  # 372
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testal1_04_flip_2(self):
        filename = "example_al1_04.txt"
        beg = self.retimed_value(2500)  # 2527
        end = self.retimed_value(2600)  # 2585
        expected = 2
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)


    def testcnp_24(self):
        filename = "example_cnp_24.txt"
        beg = self.retimed_value(150)  # 192
        end = self.retimed_value(300)  # 261
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

    def testcnp_24(self):
        filename = "example_cnp_24.txt"
        beg = self.retimed_value(4975)  # 4985
        end = self.retimed_value(5060)  # 5050
        expected = 0
        prediction = createTest(filename, beg, end, expected)
        self.assertEqual(expected, prediction)

