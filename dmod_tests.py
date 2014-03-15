import unittest
import numpy as np
import dmod

class TestPSK(unittest.TestCase):
	def setUp(self):
		self.epsilon = 1e-10

	def test_qpsk(self):
		modulated = dmod.qpsk_mod([0,1,2,3])
		truth = np.array([1+0j, 0 + 1j, -1 + 0j, 0 - 1j])
		error = np.sum(np.square(truth - np.array(list(modulated))))
		self.assertTrue(error < self.epsilon)

	def test_bpsk(self):
		modulated = dmod.qpsk_mod([0,1,0,1])
		truth = np.array([1,-1,1,-1])
		error = np.sum(np.square(truth - np.array(list(modulated))))
		self.assertTrue(error < self.epsilon)

	def test_differential(self):
		modulated = dmod.dpsk_mod([0,1,1,0], 4)
		truth = np.array([1, 1, 1j, -1, -1])
		error = np.sum(np.square(truth - np.array(list(modulated))))
		self.assertTrue(error < self.epsilon)

	def test_bad_symbols(self):
		with self.assertRaises(IndexError):
			list(dmod.qpsk_mod([0,1,2,3,4]))

	def test_bad_mapping(self):
		with self.assertRaises(ValueError):
			list(dmod.mpsk_mod([0,1,2,3], 4, True, 0, [0,1,1,2]))

if __name__ == '__main__':
	unittest.main()
