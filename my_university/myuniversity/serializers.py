import pickle


class PickleSerializer:
    def dumps(self, obj):
        return pickle.dumps(obj)

    def loads(self, data):
        return pickle.loads(data)
