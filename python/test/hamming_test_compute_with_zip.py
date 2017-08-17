import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_zip('A', 'A'))

    def test_long_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_zip('GGACTGA', 'GGACTGA'))

    def test_complete_compute_with_zip_in_single_nucleotide_strands(self):
        self.assertEqual(1, hamming.compute_with_zip('A', 'G'))

    def test_complete_compute_with_zip_in_small_strands(self):
        self.assertEqual(2, hamming.compute_with_zip('AG', 'CT'))

    def test_small_compute_with_zip_in_small_strands(self):
        self.assertEqual(1, hamming.compute_with_zip('AT', 'CT'))

    def test_small_compute_with_zip(self):
        self.assertEqual(1, hamming.compute_with_zip('GGACG', 'GGTCG'))

    def test_small_compute_with_zip_in_long_strands(self):
        self.assertEqual(2, hamming.compute_with_zip('ACCAGGG', 'ACTATGG'))

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(1, hamming.compute_with_zip('AGA', 'AGG'))

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(1, hamming.compute_with_zip('AGG', 'AGA'))

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(2, hamming.compute_with_zip('TAG', 'GAT'))

    def test_large_compute_with_zip(self):
        self.assertEqual(4, hamming.compute_with_zip('GATACA', 'GCATAA'))

    def test_large_compute_with_zip_in_off_by_one_strand(self):
        self.assertEqual(9, hamming.compute_with_zip('GGACGGATTCTG', 'AGGACGGATTCT'))

    def test_very_large_compute_with_zip(self):
        self.assertEqual(0, hamming.compute_with_zip('CAT' * 5000, 'CAT' * 5000))

    def test_empty_strands(self):
        self.assertEqual(0, hamming.compute_with_zip('', ''))

    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_zip('AATG', 'AAA')

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_zip('ATA', 'AGTG')


if __name__ == '__main__':
    unittest.main()
