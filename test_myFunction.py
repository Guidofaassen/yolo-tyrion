import myFunction
import numpy as np

class TestClass:
	def test_answer(self):
	    assert myFunction.add_one(3) == 4

	def test_answer2(self):
	    assert myFunction.add_one(4) == 5

	def test_answer3(self):
	    assert myFunction.add_one(-2) == -1

	# def test_similarity_conditional2(self):
	# 	freqUV = np.asarray([[2,3],[3,4]])
	# 	freqU = np.asarray([2,0])
	# 	u = 0
	# 	v = 1
	# 	assert myFunction.similarity_conditional(freqUV,freqU, u, v) == 0

	def test_similarity_conditional(self):
		freqUV = np.asarray([[2,3],[3,4]])
		freqU = np.asarray([2,0])
		u = 0
		v = 1
		assert myFunction.similarity_conditional(freqUV,freqU, u, v) == 0

	def test_similarity_conditional2(self):
		freqUV = np.asarray([[2,3],[3,4]])
		freqU = np.asarray([2,1])
		u = 0
		v = 1
		assert myFunction.similarity_conditional(freqUV,freqU, u, v) == 1.5

	def test_myDivide(self):
		assert myFunction.myDivide(1,0) == 0