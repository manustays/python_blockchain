from time import time

from transaction import Transaction

class Block:

	def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
		self.index = index
		self.previous_hash = previous_hash
		self.transactions = transactions
		self.proof = proof
		self.timestamp = time() if timestamp is None else timestamp


	def __repr__(self):
		# return str(self.__dict__)
		return '{{"index":{},"previous_hash":"{}","proof":{},"timestamp":{},"transactions":{}}}'.format(
			self.index,
			self.previous_hash,
			self.proof,
			self.timestamp,
			self.transactions
			# str([str(tx) for tx in self.transactions])
		)


	@classmethod
	def from_dict(cls, block):
		"""Factory function to return a Block object from a block dictionary

		Arguments:
			:block: A block dictionary to convert into object
		"""
		return cls(block['index'],
			block['previous_hash'],
			[Transaction.from_dict(tx) for tx in block['transactions']],
			block['proof'],
			block['timestamp'])


	def to_dict(self):
		"""Returns a copy of the block in the dict format"""
		block =  self.__dict__.copy()
		block['transactions'] = [tx.to_dict() for tx in block['transactions']]
		return block


	def to_hashable_dict(self):
		"""Returns a copy of the block as a dict with the transactions as OrderedDict"""
		hashable_block = self.__dict__.copy()
		hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]

