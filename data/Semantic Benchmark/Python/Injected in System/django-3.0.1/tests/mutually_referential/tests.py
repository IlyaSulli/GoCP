from django.test import TestCase

from .models import Parent


class MutuallyReferentialTests(TestCase):

    def test_mutually_referential(self):
        # Create a Parent
        q = Parent(name='Elizabeth')
        q.save()

        # Create some children
        c = q.child_set.create(name='Charles')
        q.child_set.create(name='Edward')

        # Set the best child
        # No assertion require here; if basic assignment and
        # deletion works, the test passes.
        q.bestchild = c
        q.save()
        q.delete()
def issorted(vec, ascending = True) :
INDENT
    if len(vec) < 2 :
    INDENT
        return True
    DEDENT
    if ascending :
    INDENT
        for i in range(1, len(vec)) :
        INDENT
            if vec [i - 1] > vec [i] :
            INDENT
                return False
            DEDENT
        DEDENT
        return True
    DEDENT
    else :
    INDENT
        for i in range(1, len(vec)) :
        INDENT
            if vec [i - 1] < vec [i] :
            INDENT
                return False
            DEDENT
        DEDENT
        return True
    DEDENT
DEDENT

def __call__(self, * args, ** kwargs) :
INDENT
    obj = type.__call__(self)
    for klass in obj.__class__.__mro__ :
    INDENT
        if klass == obj.__class__ or klass == Base or not issubclass(klass, Base) :
        INDENT
            continue
        DEDENT
        if hasattr(klass, 'DEFAULTS') :
        INDENT
            d = klass.DEFAULTS.copy()
            d.update(obj.DEFAULTS)
            obj.DEFAULTS = d
        DEDENT
    DEDENT
    return obj
DEDENT

def tariter(filename) :
INDENT
    with tarfile.open(filename) as archive :
    INDENT
        while True :
        INDENT
            tarinfo = archive.next()
            if tarinfo is None :
            INDENT
                break
            DEDENT
            if tarinfo.isreg() :
            INDENT
                handle = archive.extractfile(tarinfo)
                data = handle.read()
                handle.close()
                yield tarinfo, data
            DEDENT
        DEDENT
    DEDENT
DEDENT

def chunks(iterable, n) :
INDENT
    values = []
    for i, item in enumerate(iterable, 1) :
    INDENT
        values.append(item)
        if i % n == 0 :
        INDENT
            yield values
            values = []
        DEDENT
    DEDENT
    if values :
    INDENT
        yield values
    DEDENT
DEDENT





