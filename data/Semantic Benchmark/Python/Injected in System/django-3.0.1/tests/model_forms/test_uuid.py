from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import UUIDPK


class UUIDPKForm(forms.ModelForm):
    class Meta:
        model = UUIDPK
        fields = '__all__'


class ModelFormBaseTest(TestCase):
    def test_create_save_error(self):
        form = UUIDPKForm({})
        self.assertFalse(form.is_valid())
        msg = "The UUIDPK could not be created because the data didn't validate."
        with self.assertRaisesMessage(ValueError, msg):
            form.save()

def is_monotone(heights) :
INDENT
    if len(heights) == 0 :
    INDENT
        return True
    DEDENT
    for j in range(len(heights) - 1) :
    INDENT
        if heights [j + 1] > = heights [j] :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def json_scan(json_obj, key) :
INDENT
    for element in json_obj :
    INDENT
        if str(element) == key :
        INDENT
            result = json_obj [element]
            return result
        DEDENT
        else :
        INDENT
            if type(json_obj [element]) == DictType :
            INDENT
                json_scan(json_obj [element], key)
            DEDENT
            elif type(json_obj [element]) == ListType :
            INDENT
                json_scan(element, key)
            DEDENT
        DEDENT
    DEDENT
    return None
DEDENT

def fib(n) :
INDENT
    x, r = (1, 0), (0, 1)
    while n :
    INDENT
        if n & 1 : r = mul(r, x)
        x = mul(x, x)
        n >>= 1
    DEDENT
    return r [0]
DEDENT

def evaluate(tokens, ops, precedence) :
INDENT
    for prec in precedence :
    INDENT
        index = find_op(tokens, prec)
        while index > = 0 :
        INDENT
            tokens = reduce_binary_infix(tokens, index, ops)
            index = find_op(tokens, prec)
        DEDENT
    DEDENT
    return tokens
DEDENT

def tail(file, n = 1, bs = 1024) :
INDENT
    f = open(file)
    f.seek(- 1, 2)
    l = 1 - f.read(1).count('\n')
    B = f.tell()
    while n > = l and B > 0 :
    INDENT
        block = min(bs, B)
        B -= block
        f.seek(B, 0)
        l += f.read(block).count('\n')
    DEDENT
    f.seek(B, 0)
    l = min(l, n)
    lines = f.readlines() [- l :]
    f.close()
    return lines
DEDENT

def same_structure(a, b) :
INDENT
    if not is_list(a) and not is_list(b) :
    INDENT
        return True
    DEDENT
    elif (is_list(a) and is_list(b)) and (len(a) == len(b)) :
    INDENT
        return all(map(same_structure, a, b))
    DEDENT
    return False
DEDENT

    def test_update_save_error(self):
        obj = UUIDPK.objects.create(name='foo')
        form = UUIDPKForm({}, instance=obj)
        self.assertFalse(form.is_valid())
        msg = "The UUIDPK could not be changed because the data didn't validate."
        with self.assertRaisesMessage(ValueError, msg):
            form.save()

def tone(self, frequency, length = 1000, play = False, ** kwargs) :
INDENT
    number_of_frames = int(self.bitrate * length / 1000.)
    record = False
    x = 0
    y = 0
    while 1 :
    INDENT
        x += 1
        v = math.sin(x / ((self.bitrate / float(frequency)) / math.pi))
        if round(v, 3) == + 1 :
        INDENT
            record = True
        DEDENT
        if record :
        INDENT
            self._queue.append(chr(int(v * 127 + 128)))
            y += 1
            if y > number_of_frames and round(v, 3) == + 1 :
            INDENT
                break
            DEDENT
        DEDENT
    DEDENT
DEDENT

def __init__(self, parent = None) :
INDENT
    super(Main, self).__init__(parent)
    self.addButton = QtGui.QPushButton('button to add other widgets')
    self.addButton.clicked.connect(self.addWidget)
    self.scrollLayout = QtGui.QFormLayout()
    self.scrollWidget = QtGui.QWidget()
    self.scrollWidget.setLayout(self.scrollLayout)
    self.scrollArea = QtGui.QScrollArea()
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setWidget(self.scrollWidget)
    self.mainLayout = QtGui.QVBoxLayout()
    self.mainLayout.addWidget(self.addButton)
    self.mainLayout.addWidget(self.scrollArea)
    self.centralWidget = QtGui.QWidget()
    self.centralWidget.setLayout(self.mainLayout)
    self.setCentralWidget(self.centralWidget)
DEDENT

def after_request(response) :
INDENT
    diff = time.time() - g.start
    if ((response.response) and
        (200 < = response.status_code < 300) and
        (response.content_type.startswith('text/html'))) :
    INDENT
        response.set_data(response.get_data().replace(
                b'__EXECUTION_TIME__', bytes(str(diff), 'utf-8')))
    DEDENT
    return response
DEDENT

def enum(* names) :
INDENT
    assert names, 'Empty enums are not supported'
    assert len([i for i in names if not isinstance(i, types.StringTypes) and not isinstance(i, unicode)]) == 0, 'Enum values must be string or unicode'
    assert len([i for i in names if i.startswith("__")]) == 0, 'Enum values beginning with __ are not supported'
    assert names == uniquify(names), 'Enums must not repeat values'
    class EnumClass(object) :
    INDENT
        """ See parent function for explanation """
        __slots__ = names
        def __iter__(self) :
        INDENT
            return iter(constants)
        DEDENT
        def __len__(self) :
        INDENT
            return len(constants)
        DEDENT
        def __getitem__(self, i) :
        INDENT
            if isinstance(i, types.StringTypes) :
            INDENT
                i = names.index(i)
            DEDENT
            return constants [i]
        DEDENT
        def __repr__(self) :
        INDENT
            return 'enum' + str(names)
        DEDENT
        def __str__(self) :
        INDENT
            return 'enum ' + str(constants)
        DEDENT
        def index(self, i) :
        INDENT
            return names.index(i)
        DEDENT
    DEDENT
    class EnumValue(object) :
    INDENT
        """ See parent function for explanation """
        __slots__ = ('__value')
        def __init__(self, value) :
        INDENT
            self.__value = value
        DEDENT
        value = property(lambda self : self.__value)
        enumtype = property(lambda self : enumtype)
        def __hash__(self) :
        INDENT
            return hash(self.__value)
        DEDENT
        def __cmp__(self, other) :
        INDENT
            assert self.enumtype is other.enumtype, 'Only values from the same enum are comparable'
            return cmp(self.value, other.value)
        DEDENT
        def __invert__(self) :
        INDENT
            return constants [maximum - self.value]
        DEDENT
        def __nonzero__(self) :
        INDENT
            return True
        DEDENT
        def __repr__(self) :
        INDENT
            return str(names [self.value])
        DEDENT
    DEDENT
    maximum = len(names) - 1
    constants = [None] * len(names)
    for i, each in enumerate(names) :
    INDENT
        val = EnumValue(i)
        setattr(EnumClass, each, val)
        constants [i] = val
    DEDENT
    constants = tuple(constants)
    enumtype = EnumClass()
    return enumtype
DEDENT

def deprecated(reason) :
INDENT
    if isinstance(reason, string_types) :
    INDENT
        def decorator(func1) :
        INDENT
            if inspect.isclass(func1) :
            INDENT
                fmt1 = "Call to deprecated class {name} ({reason})."
            DEDENT
            else :
            INDENT
                fmt1 = "Call to deprecated function {name} ({reason})."
            DEDENT
            @ functools.wraps(func1)
            def new_func1(* args, ** kwargs) :
            INDENT
                warnings.simplefilter('always', DeprecationWarning)
                warnings.warn(
                    fmt1.format(name = func1.__name__, reason = reason),
                    category = DeprecationWarning,
                    stacklevel = 2)
                warnings.simplefilter('default', DeprecationWarning)
                return func1(* args, ** kwargs)
            DEDENT
            return new_func1
        DEDENT
        return decorator
    DEDENT
    elif inspect.isclass(reason) or inspect.isfunction(reason) :
    INDENT
        func2 = reason
        if inspect.isclass(func2) :
        INDENT
            fmt2 = "Call to deprecated class {name}."
        DEDENT
        else :
        INDENT
            fmt2 = "Call to deprecated function {name}."
        DEDENT
        @ functools.wraps(func2)
        def new_func2(* args, ** kwargs) :
        INDENT
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(
                fmt2.format(name = func2.__name__),
                category = DeprecationWarning,
                stacklevel = 2)
            warnings.simplefilter('default', DeprecationWarning)
            return func2(* args, ** kwargs)
        DEDENT
        return new_func2
    DEDENT
    else :
    INDENT
        raise TypeError(repr(type(reason)))
    DEDENT
DEDENT

def wrapper(* args, ** kwargs) :
INDENT
    time_diff = time.time() - last_time [0]
    if time_diff < 1 :
    INDENT
        print ("Too fast...")
        time.sleep(1 - time_diff)
        last_time [0] = time.time()
        return f(* args, ** kwargs)
    DEDENT
DEDENT

def transitive_closure(elements) :
INDENT
    edges = defaultdict(set)
    for x, y in elements : edges [x].add(y)
    for _ in range(len(elements) - 1) :
    INDENT
        edges = defaultdict(set, (
                (k, v.union(* (edges [i] for i in v))) for (k, v) in edges.items()
                ))
    DEDENT
    return set((k, i) for (k, v) in edges.items() for i in v)
DEDENT

    def test_model_multiple_choice_field_uuid_pk(self):
        f = forms.ModelMultipleChoiceField(UUIDPK.objects.all())
        with self.assertRaisesMessage(ValidationError, 'â€œinvalid_uuidâ€? is not a valid UUID.'):
            f.clean(['invalid_uuid'])
def __eq__(self, other) :
INDENT
    if set(self.__slots__) ! = set(other.__slots__) : return False
    for slot in self.__slots__ :
    INDENT
        if getattr(self, slot) ! = getattr(other, slot) :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def dfs(row, col) :
INDENT
    global suc
    if suc == 1 :
    INDENT
        return
    DEDENT
    matrix [row] [col] = "2"
    if (row, col) == (numrows - 1, numcols - 1) :
    INDENT
        print ("Success")
        suc = 1
    DEDENT
    if col + 1 < numcols and matrix [row] [col + 1] == "0" :
    INDENT
        dfs(row, col + 1)
    DEDENT
    if row + 1 < numrows and matrix [row + 1] [col] == "0" :
    INDENT
        dfs(row + 1, col)
    DEDENT
    if 0 < = col - 1 and matrix [row] [col - 1] == "0" :
    INDENT
        dfs(row, col - 1)
    DEDENT
    if 0 < = row - 1 and matrix [row - 1] [col] == "0" :
    INDENT
        dfs(row - 1, col)
    DEDENT
DEDENT

def __getitem__(self, item) :
INDENT
    if type(item) in [tuple, list] :
    INDENT
        item = list(item)
        ret = self
        while True :
        INDENT
            try :
            INDENT
                ret = ret [item.pop(0)]
            DEDENT
            except IndexError :
            INDENT
                break
            DEDENT
        DEDENT
        return ret
    DEDENT
    else :
    INDENT
        return super(ListAccess, self).__getitem__(item)
    DEDENT
DEDENT

def wrapper(arg1) :
INDENT
    try :
    INDENT
        return func(arg1)
    DEDENT
    except MyException as e :
    INDENT
        print "Error:", e.args
    DEDENT
DEDENT


















