import numpy as np
"""
Phase Shift Keying
"""
def mpsk_mod(syms, m, differential = False, phase_offset = 0, symbol_mapping = 'binary'):
	"""
	Modulates the symbols in an m-ary phase shift keying.

	Arguments
	syms -- an iterator of symbols that are in the range [0,m-1]
	m -- the number of constellation points
	differential -- whether or not to do differential encoding
	phase_offset -- the offset, in radians, of the first symbol
	symbol_mapping -- The mapping of symbol to constellation place. The default is
	binary, but a user supplied list of length m can be used to define a custom 
	mapping, where symbol_mapping[i] == j indicates symbol i is mapped to the jth 
	constellation point
	
	Outputs
	A generator of complex points, with the number of points equal to len(syms) if
	non-differential, or equal to len(syms)+1 if differential
	"""


	def check_mapping(mp):
		return (max(mp) < m) and (min(mp) > 0) and (len(np.unique(mp)) == m)

	if symbol_mapping == 'binary':
		mapping = np.arange(m)
	elif check_mapping(symbol_mapping):
		mapping = symbol_mapping
	else:
		raise ValueError("Badly formatted symbol mapping")

	rotations_rads = 2 * np.pi * np.arange(m) / m
	points = np.exp(1j * rotations_rads + phase_offset)

	last_point = np.exp(1j * phase_offset)
	if differential:
		yield last_point
	for s in syms:
		if s > m-1 or s < 0:
			raise IndexError("Symbol " + str(s) + " out of range [0,m-1]")

		if differential:
			last_point = last_point * np.exp(1j * rotations_rads[mapping[s]])
			yield last_point
		else:
			yield points[mapping[s]]

def qpsk_mod(syms, differential = False, phase_offset=0, symbol_mapping = 'binary'):
	"""
	Equivalent to mpsk_mod with m = 4
	"""
	return mpsk_mod(syms, 4, differential, phase_offset, symbol_mapping)

def bpsk_mod(syms, differential = False, phase_offset=0, symbol_mapping = 'binary'):
	"""
	Equivalent to mpsk_mod with m = 2
	"""
	return mpsk_mod(syms, 2, differential, phase_offset, symbol_mapping)


def dpsk_mod(syms, m, phase_offset = 0, symbol_mapping = 'binary'):
	return mpsk_mod(syms, m, True, phase_offset, symbol_mapping)

def opsk_mod(syms, m, phase_offset = 0, symbol_mapping = 'binary'):
	raise NotImplementedError

"""
Frequency Shift Keying
"""

def fsk_mod():
	raise NotImplementedError

def discontinuous_bfsk_modulate(bits, h, samplesperbit):
	#these are in fractions of fs, not in Hz.
	#it's a bit weird, but it allows us to be agnostic to
	#the actual sampling frequency
	fh = (h / 2.0) / samplesperbit
	fl = -(h / 2.0) / samplesperbit

	t = np.arange(len(bits) * samplesperbit)
	sl = np.exp(1j * 2 * np.pi * fl * t)
	sh = np.exp(1j * 2 * np.pi * fh * t)

	bits = [1 if a > 0 else 0 for a in bits]
	bits = np.repeat(bits,samplesperbit)
	notbits = [0 if a else 1 for a in bits]
	return sh * bits + sl * notbits

"""
Amplitude Shift Keying
"""

def qam_mod():
	raise NotImplementedError

