import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_numpy('A', 'A'))

    def test_long_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_numpy('GGACTGA', 'GGACTGA'))

    def test_complete_compute_with_numpy_in_single_nucleotide_strands(self):
        self.assertEqual(1, hamming.compute_with_numpy('A', 'G'))

    def test_complete_compute_with_numpy_in_small_strands(self):
        self.assertEqual(2, hamming.compute_with_numpy('AG', 'CT'))

    def test_small_compute_with_numpy_in_small_strands(self):
        self.assertEqual(1, hamming.compute_with_numpy('AT', 'CT'))

    def test_small_compute_with_numpy(self):
        self.assertEqual(1, hamming.compute_with_numpy('GGACG', 'GGTCG'))

    def test_small_compute_with_numpy_in_long_strands(self):
        self.assertEqual(2, hamming.compute_with_numpy('ACCAGGG', 'ACTATGG'))

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(1, hamming.compute_with_numpy('AGA', 'AGG'))

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(1, hamming.compute_with_numpy('AGG', 'AGA'))

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(2, hamming.compute_with_numpy('TAG', 'GAT'))

    def test_large_compute_with_numpy(self):
        self.assertEqual(4, hamming.compute_with_numpy('GATACA', 'GCATAA'))

    def test_large_compute_with_numpy_in_off_by_one_strand(self):
        self.assertEqual(9, hamming.compute_with_numpy('GGACGGATTCTG', 'AGGACGGATTCT'))

    def test_very_large_compute_with_numpy(self):
        self.assertEqual(0, hamming.compute_with_numpy('CAT' * 5000, 'CAT' * 5000))

    def test_empty_strands(self):
        self.assertEqual(0, hamming.compute_with_numpy('', ''))

    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_numpy('AATG', 'AAA')

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_numpy('ATA', 'AGTG')


if __name__ == '__main__':
    unittest.main()
