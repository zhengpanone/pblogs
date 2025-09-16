class ReprMixin:

    def __repr__(self):
        s = self.__class__.__name__ + '('

        for k, v in self.__dict__.items():
            if not k.startwith("_"):
                s += '{}={}, '.format(k, v)

        s = s.rstrip(', ') + ')'
        return s