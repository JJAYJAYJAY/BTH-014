import pickle
import hashlib


class D:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getstate__(self):
        
        return {'data': self.data}


def test_dict():

    d = D()
    s_data1 = pickle.dumps(d)
    s_data2 = pickle.dumps(d)
    assert hashlib.sha256(s_data1).hexdigest() == hashlib.sha256(s_data2).hexdigest()
