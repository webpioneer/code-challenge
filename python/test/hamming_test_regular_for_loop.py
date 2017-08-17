import unittest

import hamming


class HammingTest(unittest.TestCase):

    def test_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_for_loop('A', 'A'))

    def test_long_identical_strands(self):
        self.assertEqual(0, hamming.compute_with_for_loop('GGACTGA', 'GGACTGA'))

    def test_complete_compute_with_for_loop_in_single_nucleotide_strands(self):
        self.assertEqual(1, hamming.compute_with_for_loop('A', 'G'))

    def test_complete_compute_with_for_loop_in_small_strands(self):
        self.assertEqual(2, hamming.compute_with_for_loop('AG', 'CT'))

    def test_small_compute_with_for_loop_in_small_strands(self):
        self.assertEqual(1, hamming.compute_with_for_loop('AT', 'CT'))

    def test_small_compute_with_for_loop(self):
        self.assertEqual(1, hamming.compute_with_for_loop('GGACG', 'GGTCG'))

    def test_small_compute_with_for_loop_in_long_strands(self):
        self.assertEqual(2, hamming.compute_with_for_loop('ACCAGGG', 'ACTATGG'))

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(1, hamming.compute_with_for_loop('AGA', 'AGG'))

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(1, hamming.compute_with_for_loop('AGG', 'AGA'))

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(2, hamming.compute_with_for_loop('TAG', 'GAT'))

    def test_large_compute_with_for_loop(self):
        self.assertEqual(4, hamming.compute_with_for_loop('GATACA', 'GCATAA'))

    def test_large_compute_with_for_loop_in_off_by_one_strand(self):
        self.assertEqual(9, hamming.compute_with_for_loop('GGACGGATTCTG', 'AGGACGGATTCT'))

    def test_very_large_compute_with_for_loop(self):
        self.assertEqual(0, hamming.compute_with_for_loop('CAT' * 5000, 'CAT' * 5000))

    def test_empty_strands(self):
        self.assertEqual(0, hamming.compute_with_for_loop('', ''))

    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_for_loop('AATG', 'AAA')

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.compute_with_for_loop('ATA', 'AGTG')


if __name__ == '__main__':
    unittest.main()
