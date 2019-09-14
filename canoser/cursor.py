import pdb

class Cursor:
    def __init__(self, buffer, offset=0):
        self.buffer = buffer
        self.offset = offset

    def read_bytes(self, size):
    	end, total = self.offset + size, len(self.buffer)
    	if end > total:
    		raise IOError("{} exceed buffer size: {}".format(end, total))
    	#pdb.set_trace()
    	ret = self.buffer[self.offset : end]
    	self.offset = end
    	return ret

    def peek_bytes(self, size):
    	end, total = self.offset + size, len(self.buffer)
    	if end > total:
    		raise IOError("{} exceed buffer size: {}".format(end, total))
    	return self.buffer[self.offset : end]

    def is_finished(self):
        return self.offset == len(self.buffer)