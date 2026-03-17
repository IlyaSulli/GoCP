import datetime

from django import forms
from django.core.validators import ValidationError
from django.forms.models import ModelChoiceIterator
from django.forms.widgets import CheckboxSelectMultiple
from django.template import Context, Template
from django.test import TestCase

from .models import Article, Author, Book, Category, Writer


class ModelChoiceFieldTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c1 = Category.objects.create(name='Entertainment', slug='entertainment', url='entertainment')
        cls.c2 = Category.objects.create(name='A test', slug='test', url='test')
        cls.c3 = Category.objects.create(name='Third', slug='third-test', url='third')

def extendedString(string1, string2) :
INDENT
    x = string1
    y = string2
    z = ""
    if len(x) == len(y) :
    INDENT
        return "".join(i for j in zip(string1, string2) for i in j)
    DEDENT
    elif len(x) < len(y) :
    INDENT
        x = x + x [- 1] * (len(y) - len(x))
        return extendedString(x, y)
    DEDENT
    else :
    INDENT
        y = y + y [- 1] * (len(x) - len(y))
        return extendedString(x, y)
    DEDENT
DEDENT

def split(s, n) :
INDENT
    new_list = []
    for i in range(0, len(s), n) :
    INDENT
        new_list.append(s [i : i + n])
    DEDENT
    return new_list
DEDENT

def findWinner(contestants) :
INDENT
    if (len(contestants) ! = 1) :
    INDENT
        remainingContestants = []
        for i, contestant in enumerate(contestants, 1) :
        INDENT
            if (isEven(i)) :
            INDENT
                remainingContestants.append(contestant)
            DEDENT
        DEDENT
        return findWinner(remainingContestants)
    DEDENT
    return contestants
DEDENT

def emit(self, record) :
INDENT
    try :
    INDENT
        s = self._format_record(record)
        self.send(s)
    DEDENT
    except (KeyboardInterrupt, SystemExit) :
    INDENT
        raise
    DEDENT
    except :
    INDENT
        self.handleError(record)
    DEDENT
DEDENT

    def test_basics(self):
        f = forms.ModelChoiceField(Category.objects.all())
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
            (self.c3.pk, 'Third'),
        ])
        with self.assertRaises(ValidationError):
            f.clean('')
        with self.assertRaises(ValidationError):
            f.clean(None)
        with self.assertRaises(ValidationError):
            f.clean(0)

        # Invalid types that require TypeError to be caught.
        with self.assertRaises(ValidationError):
            f.clean([['fail']])
        with self.assertRaises(ValidationError):
            f.clean([{'foo': 'bar'}])

        self.assertEqual(f.clean(self.c2.id).name, 'A test')
        self.assertEqual(f.clean(self.c3.id).name, 'Third')

        # Add a Category object *after* the ModelChoiceField has already been
        # instantiated. This proves clean() checks the database during clean()
        # rather than caching it at  instantiation time.
        c4 = Category.objects.create(name='Fourth', url='4th')
        self.assertEqual(f.clean(c4.id).name, 'Fourth')

        # Delete a Category object *after* the ModelChoiceField has already been
        # instantiated. This proves clean() checks the database during clean()
        # rather than caching it at instantiation time.
        Category.objects.get(url='4th').delete()
        msg = "['Select a valid choice. That choice is not one of the available choices.']"
        with self.assertRaisesMessage(ValidationError, msg):
            f.clean(c4.id)

def get_or_415(self, ident) :
INDENT
    model_class_name = ''
    try :
    INDENT
        model_class_name = self._mapper_zero().class_.__name__
    DEDENT
    except Exception as e :
    INDENT
        print (e)
    DEDENT
    rv = self.get(ident)
    if rv is None :
    INDENT
        error_message = json.dumps({'message' : model_class_name + ' ' + str(ident) + ' not found'})
        abort(Response(error_message, 415))
    DEDENT
    return rv
DEDENT

def CalcSomething(a) :
INDENT
    if cache.has_key(a) :
    INDENT
        return cache [a]
    DEDENT
    cache [a] = ReallyCalc(a)
    return cache [a]
DEDENT

def __init__(self, action, minute = allMatch, hour = allMatch,
day = allMatch, month = allMatch, daysofweek = allMatch,
args = (), kwargs = {}) :
INDENT
    self.mins = conv_to_set(minute)
    self.hours = conv_to_set(hour)
    self.days = conv_to_set(day)
    self.months = conv_to_set(month)
    self.daysofweek = conv_to_set(daysofweek)
    self.action = action
    self.args = args
    self.kwargs = kwargs
DEDENT

def sierpinski(depth, turtle, size) :
INDENT
    turtle.shapesize(size / CURSOR_SIZE)
    turtle.stamp()
    if depth < 1 :
    INDENT
        return
    DEDENT
    half = size / 2
    circumradius = half * 3 ** 0.5 / 3
    for _ in range(3) :
    INDENT
        turtle.forward(circumradius)
        sierpinski(depth - 1, turtle, half)
        turtle.backward(circumradius)
        turtle.left(120)
    DEDENT
DEDENT

def curry(f) :
INDENT
    @ wraps(f)
    def _(arg) :
    INDENT
        try :
        INDENT
            return f(arg)
        DEDENT
        except TypeError :
        INDENT
            return curry(wraps(f)(partial(f, arg)))
        DEDENT
    DEDENT
    return _
DEDENT

def run_command(command) :
INDENT
    p = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        shell = True)
    for line in iter(p.stdout.readline, b'') :
    INDENT
        if line :
        INDENT
            yield line
        DEDENT
    DEDENT
    while p.poll() is None :
    INDENT
        sleep(.1)
    DEDENT
    err = p.stderr.read()
    if p.returncode ! = 0 :
    INDENT
        print ("Error: " + str(err))
    DEDENT
DEDENT

    def test_clean_model_instance(self):
        f = forms.ModelChoiceField(Category.objects.all())
        self.assertEqual(f.clean(self.c1), self.c1)
        # An instance of incorrect model.
        msg = "['Select a valid choice. That choice is not one of the available choices.']"
        with self.assertRaisesMessage(ValidationError, msg):
            f.clean(Book.objects.create())

def printTable(mylist) :
INDENT
    maxLength = 0
    for item in mylist :
    INDENT
        for i in item :
        INDENT
            if len(i) > maxLength :
            INDENT
                maxLength = len(i)
            DEDENT
            else :
            INDENT
                maxLength = maxLength
            DEDENT
        DEDENT
    DEDENT
    for item in mylist :
    INDENT
        for i in range(len(item)) :
        INDENT
            item [i] = (item [i].rjust(maxLength))
        DEDENT
    DEDENT
    myNewlist = {0 : [], 1 : [], 2 : [], 3 : []}
    for i in range(len(item)) :
    INDENT
        for u in tableData :
        INDENT
            myNewlist [i].append(u [i])
        DEDENT
    DEDENT
    for key, value in myNewlist.items() :
    INDENT
        print (''.join(value))
    DEDENT
DEDENT

def censored(sentence, bad_words = EXCLUDED_WORDS) :
INDENT
    if bad_words :
    INDENT
        for word in bad_words :
        INDENT
            sentence = sentence.replace(word, '*' * len(word))
        DEDENT
    DEDENT
    return sentence
DEDENT

def countSubStringMatchRecursive(target, key, start_index = 0) :
INDENT
    index = target.find(key, start_index)
    if index > = 0 :
    INDENT
        return countSubStringMatchRecursive(target, key, index + len(key)) + 1
    DEDENT
    return 0
DEDENT

def __init__(cls, name, bases, dct) :
INDENT
    def static_attrs() :
    INDENT
        import types
        attrs = {}
        val_set = set()
        filter_names = set(['__doc__', '__init__', '__metaclass__', '__module__', '__main__'])
        for key, value in dct.iteritems() :
        INDENT
            if type(value) ! = types.FunctionType and key not in filter_names :
            INDENT
                if len(value) ! = 2 :
                INDENT
                    raise NotImplementedError('not support for values that is not 2 elements!')
                DEDENT
                if value [0] not in val_set :
                INDENT
                    val_set.add(value [0])
                DEDENT
                else :
                INDENT
                    raise KeyError("%s 's key: %s is duplicated!" % (dict([(key, value)]), value [0]))
                DEDENT
                attrs [key] = value
            DEDENT
        DEDENT
        return attrs, val_set
    DEDENT
    attrs, val_set = static_attrs()
    setattr(cls, 'STATIC_ATTRS', attrs)
    setattr(cls, 'static_val_set', val_set)
    super(ConstMeta, cls).__init__(name, bases, dct)
DEDENT

def insert_sequence(dna1, dna2, number) :
INDENT
    index = 0
    result = ''
    for character in dna1 :
    INDENT
        if index == number :
        INDENT
            result = result + dna2
        DEDENT
        result = result + character
        index += 1
    DEDENT
    print (result)
DEDENT

def md5sum(filename) :
INDENT
    d = hashlib.md5()
    for buf in chunks(filename, 128) :
    INDENT
        d.update(buf)
    DEDENT
    return d.hexdigest()
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

def __init__(self, parent, job) :
INDENT
    self.job = job
    wx.Dialog.__init__(self, parent, - 1, "Progress", size = (350, 200))
    sizeAll = wx.BoxSizer(wx.VERTICAL)
    self.JobStatusText = wx.StaticText(self, - 1, "Starting...")
    sizeAll.Add(self.JobStatusText, 0, wx.EXPAND | wx.ALL, 8)
    self.ProgressBar = wx.Gauge(self, - 1, 10, wx.DefaultPosition, (250, 15))
    sizeAll.Add(self.ProgressBar, 0, wx.EXPAND | wx.ALL, 8)
    sizeRemaining = wx.BoxSizer(wx.HORIZONTAL)
    sizeRemaining.Add((2, 2), 1, wx.EXPAND)
    self.remainingText = wx.StaticText(self, - 1, "???:??")
    sizeRemaining.Add(self.remainingText, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8)
    self.remainingLabel = wx.StaticText(self, - 1, "remaining")
    sizeRemaining.Add(self.remainingLabel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 8)
    sizeAll.Add(sizeRemaining, 1, wx.EXPAND)
    sizeButtons = wx.BoxSizer(wx.HORIZONTAL)
    sizeButtons.Add((2, 2), 1, wx.EXPAND | wx.ADJUST_MINSIZE)
    self.PauseButton = wx.Button(self, - 1, "Pause")
    sizeButtons.Add(self.PauseButton, 0, wx.ALL, 4)
    self.Bind(wx.EVT_BUTTON, self.OnPauseButton, self.PauseButton)
    self.CancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
    sizeButtons.Add(self.CancelButton, 0, wx.ALL, 4)
    self.Bind(wx.EVT_BUTTON, self.OnCancel, self.CancelButton)
    sizeAll.Add(sizeButtons, 0, wx.EXPAND | wx.ALL, 4)
    self.SetSizer(sizeAll)
    sizeAll.SetSizeHints(self)
    self.Bind(EVT_PROGRESS_START, self.OnProgressStart)
    self.Bind(EVT_PROGRESS, self.OnProgress)
    self.Bind(EVT_DONE, self.OnDone)
    self.Layout()
DEDENT

    def test_clean_to_field_name(self):
        f = forms.ModelChoiceField(Category.objects.all(), to_field_name='slug')
        self.assertEqual(f.clean(self.c1.slug), self.c1)
        self.assertEqual(f.clean(self.c1), self.c1)

def window(seq, n = 2) :
INDENT
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n :
    INDENT
        yield result
    DEDENT
    for elem in it :
    INDENT
        result = result [1 :] + (elem,)
        yield result
    DEDENT
DEDENT

def arePermsEqualParity(perm0, perm1) :
INDENT
    transCount = 0
    for loc in range(len(perm0) - 1) :
    INDENT
        if perm0 [loc] ! = perm1 [loc] :
        INDENT
            sloc = perm1.index(perm0 [loc])
            perm1 [loc], perm1 [sloc] = perm1 [sloc], perm1 [loc]
            transCount += 1
        DEDENT
    DEDENT
    if (transCount % 2) == 0 :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
DEDENT

def dataType(str) :
INDENT
    str = str.strip()
    if len(str) == 0 : return 'BLANK'
    try :
    INDENT
        t = ast.literal_eval(str)
    DEDENT
    except ValueError :
    INDENT
        return 'TEXT'
    DEDENT
    except SyntaxError :
    INDENT
        return 'TEXT'
    DEDENT
    else :
    INDENT
        if type(t) in [int, long, float, bool] :
        INDENT
            if t in set((True, False)) :
            INDENT
                return 'BIT'
            DEDENT
            if type(t) is int or type(t) is long :
            INDENT
                return 'INT'
            DEDENT
            if type(t) is float :
            INDENT
                return 'FLOAT'
            DEDENT
        DEDENT
        else :
        INDENT
            return 'TEXT'
        DEDENT
    DEDENT
DEDENT

def enum(clsdef) :
INDENT
    class Enum(object) :
    INDENT
        __slots__ = tuple([var for var in clsdef.__dict__ if isinstance((getattr(clsdef, var)), tuple) and not var.startswith('__')])
        def __new__(cls, * args, ** kwargs) :
        INDENT
            if not '_the_instance' in cls.__dict__ :
            INDENT
                cls._the_instance = object.__new__(cls, * args, ** kwargs)
            DEDENT
            return cls._the_instance
        DEDENT
        def __init__(self) :
        INDENT
            clsdef.values = lambda cls, e = Enum : e.values()
            clsdef.valueOf = lambda cls, n, e = self : e.valueOf(n)
            for ordinal, key in enumerate(self.__class__.__slots__) :
            INDENT
                args = getattr(clsdef, key)
                instance = clsdef(* args)
                instance._name = key
                instance._ordinal = ordinal
                setattr(self, key, instance)
            DEDENT
        DEDENT
        @ classmethod
        def values(cls) :
        INDENT
            if not hasattr(cls, '_values') :
            INDENT
                cls._values = [getattr(cls, name) for name in cls.__slots__]
            DEDENT
            return cls._values
        DEDENT
        def valueOf(self, name) :
        INDENT
            return getattr(self, name)
        DEDENT
        def __repr__(self) :
        INDENT
            return ''.join(['<class Enum (', clsdef.__name__, ') at ', str(hex(id(self))), '>'])
        DEDENT
    DEDENT
    return Enum()
DEDENT

def touch(fname) :
INDENT
    if os.path.exists(fname) :
    INDENT
        os.utime(fname, None)
    DEDENT
    else :
    INDENT
        open(fname, 'a').close()
    DEDENT
DEDENT

    def test_choices(self):
        f = forms.ModelChoiceField(Category.objects.filter(pk=self.c1.id), required=False)
        self.assertIsNone(f.clean(''))
        self.assertEqual(f.clean(str(self.c1.id)).name, 'Entertainment')
        with self.assertRaises(ValidationError):
            f.clean('100')

        # len() can be called on choices.
        self.assertEqual(len(f.choices), 2)

        # queryset can be changed after the field is created.
        f.queryset = Category.objects.exclude(name='Third')
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
        ])
        self.assertEqual(f.clean(self.c2.id).name, 'A test')
        with self.assertRaises(ValidationError):
            f.clean(self.c3.id)

        # Choices can be iterated repeatedly.
        gen_one = list(f.choices)
        gen_two = f.choices
        self.assertEqual(gen_one[2], (self.c2.pk, 'A test'))
        self.assertEqual(list(gen_two), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
        ])

        # Overriding label_from_instance() to print custom labels.
        f.queryset = Category.objects.all()
        f.label_from_instance = lambda obj: 'category ' + str(obj)
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'category Entertainment'),
            (self.c2.pk, 'category A test'),
            (self.c3.pk, 'category Third'),
        ])

def remove_element(value, array) :
INDENT
    shift = 0
    for index in xrange(len(array)) :
    INDENT
        try :
        INDENT
            array [index] = array [index + shift]
            while array [index] == value :
            INDENT
                shift += 1
                array [index] = array [index + shift]
            DEDENT
        DEDENT
        except IndexError :
        INDENT
            array [index] = None
        DEDENT
    DEDENT
DEDENT

def __enter__(self) :
INDENT
    self.interrupted = False
    self.released = False
    for sig in self.signals :
    INDENT
        self.original_handlers [sig] = signal.getsignal(sig)
        signal.signal(sig, self.handler)
    DEDENT
    return self
DEDENT

def update(self, instance, validated_data) :
INDENT
    user_data = validated_data.pop('user', {})
    user_serializer = UserSerializer(instance.user, data = user_data, partial = True)
    user_serializer.is_valid(raise_exception = True)
    user_serializer.update(instance.user, user_data)
    super(ProfileSerializer, self).update(instance, validated_data)
    return instance
DEDENT

def flattenjson(self, mp, delim = "|") :
INDENT
    ret = []
    if isinstance(mp, dict) :
    INDENT
        for k in mp.keys() :
        INDENT
            csvs = self.flattenjson(mp [k], delim)
            for csv in csvs :
            INDENT
                ret.append(k + delim + csv)
            DEDENT
        DEDENT
    DEDENT
    elif isinstance(mp, list) :
    INDENT
        for k in mp :
        INDENT
            csvs = self.flattenjson(k, delim)
            for csv in csvs :
            INDENT
                ret.append(csv)
            DEDENT
        DEDENT
    DEDENT
    else :
    INDENT
        ret.append(mp)
    DEDENT
    return ret
DEDENT

def insert_sequence(dna1, dna2, number) :
INDENT
    '''(str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence
    at the given index. (You can assume that the index is valid.)  
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('TTGC', 'GG', 2)
    'TTGGGC'
    '''
    return dna1 [: number] + dna2 + dna1 [number :]
DEDENT

def convert(items, ID) :
INDENT
    result = {}
    for key, value in items.items() :
    INDENT
        if key in ID.keys() :
        INDENT
            result [ID [key]] = value
        DEDENT
        else :
        INDENT
            result [key] = value
        DEDENT
    DEDENT
    items.clear()
    for key, value in result.items() :
    INDENT
        items [key] = value
    DEDENT
    return items
DEDENT

def touch(fname, mode = 0o666, dir_fd = None, ** kwargs) :
INDENT
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags = flags, mode = mode, dir_fd = dir_fd)) as f :
    INDENT
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
            dir_fd = None if os.supports_fd else dir_fd, ** kwargs)
    DEDENT
DEDENT

def reverse(s) :
INDENT
    t = - 1
    s2 = ''
    while abs(t) < len(s) + 1 :
    INDENT
        s2 = s2 + s [t]
        t = t - 1
    DEDENT
    return s2
DEDENT

    def test_choices_freshness(self):
        f = forms.ModelChoiceField(Category.objects.all())
        self.assertEqual(len(f.choices), 4)
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
            (self.c3.pk, 'Third'),
        ])
        c4 = Category.objects.create(name='Fourth', slug='4th', url='4th')
        self.assertEqual(len(f.choices), 5)
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
            (self.c3.pk, 'Third'),
            (c4.pk, 'Fourth'),
        ])

def __init__(self, pos, * groups) :
INDENT
    super().__init__(groups)
    self.image = pg.Surface((90, 40), pg.SRCALPHA)
    self.image.fill(pg.Color('steelblue2'))
    self.orig_image = self.image
    self.rect = self.image.get_rect(center = pos)
    self.vel = Vector2(0, 0)
    self.pos = Vector2(pos)
    self.angle = 0
    self.children = [Child(self.pos, Vector2(90, 30), * groups)]
DEDENT

def update(self, request, * args, ** kwargs) :
INDENT
    partial = True
    instance = self.get_object()
    serializer = self.get_serializer(instance, data = request.data, partial = partial)
    serializer.is_valid(raise_exception = True)
    self.perform_update(serializer)
    return Response(serializer.data)
DEDENT

def search(request) :
INDENT
    if request.method == "GET" :
    INDENT
        search_terms = request.GET ['title']
        search_filter = Q()
        for term in search_terms.split(',') :
        INDENT
            search_filter |= Q(title__contains = term)
        DEDENT
        jobs = Job.objects.filter(search_filter)
    DEDENT
DEDENT

    def test_choices_bool(self):
        f = forms.ModelChoiceField(Category.objects.all(), empty_label=None)
        self.assertIs(bool(f.choices), True)
        Category.objects.all().delete()
        self.assertIs(bool(f.choices), False)

def is_monotone(heights) :
INDENT
    j = 0
    if len(heights) == 0 :
    INDENT
        return True
    DEDENT
    for i in heights :
    INDENT
        if j + 1 > len(heights) :
        INDENT
            return True
        DEDENT
        if heights [j + 1] > = heights [j] :
        INDENT
            j += 1
            return True
        DEDENT
        return False
    DEDENT
DEDENT

def parse_name(name) :
INDENT
    first_name, last_name = name.split(' ', 1)
    first_initial = re.search("^[A-Z.]+", first_name).group()
    if not first_initial.endswith(".") :
    INDENT
        first_initial += "."
    DEDENT
    return {"FirstName" : first_name,
        "FirstInitial" : first_initial,
        "LastName" : last_name}
DEDENT

def printPascal(n) :
INDENT
    if n == 0 :
    INDENT
        return [[1]]
    DEDENT
    else :
    INDENT
        final_r = printPascal(n - 1)
        last = [0] + final_r [- 1] + [0]
        new_row = [last [k] + last [k - 1] for k in range(1, len(last))]
        return final_r + [new_row]
    DEDENT
DEDENT

def fib(n) :
INDENT
    if n == 0 :
    INDENT
        return [0]
    DEDENT
    elif n == 1 :
    INDENT
        return [0, 1]
    DEDENT
    else :
    INDENT
        lst = fib(n - 1)
        lst.append(lst [- 1] + lst [- 2])
        return lst
    DEDENT
DEDENT

def transform_non_affine(self, a) :
INDENT
    diff = np.zeros(len(a))
    total_shift = 0
    for left, right in self._breaks :
    INDENT
        pos = bisect.bisect_right(a, left - total_shift)
        if pos > = len(diff) :
        INDENT
            break
        DEDENT
        diff [pos] = right - left
        total_shift += right - left
    DEDENT
    return a + diff.cumsum()
DEDENT

def __init__(self, parent, * args, ** kwargs) :
INDENT
    super(MenuBar, self).__init__(* args, ** kwargs)
    file_menu = wx.Menu()
    self.Append(file_menu, '&File')
    quit_menu_item = wx.MenuItem(file_menu, wx.ID_EXIT)
    parent.Bind(wx.EVT_MENU, parent.on_quit_click, id = wx.ID_EXIT)
    file_menu.Append(quit_menu_item)
DEDENT

def emit(self, record) :
INDENT
    try :
    INDENT
        message = self.format(record)
        stream = self.stream
        if not self.is_tty :
        INDENT
            stream.write(message)
        DEDENT
        else :
        INDENT
            message = self._colors [record.levelno] + message + self.RESET
            stream.write(message)
        DEDENT
        stream.write(getattr(self, 'terminator', '\n'))
        self.flush()
    DEDENT
    except (KeyboardInterrupt, SystemExit) :
    INDENT
        raise
    DEDENT
    except :
    INDENT
        self.handleError(record)
    DEDENT
DEDENT

def reverse(string) :
INDENT
    tmp = ""
    for i in range(1, len(string) + 1) :
    INDENT
        tmp += string [len(string) - i]
    DEDENT
    return tmp
DEDENT

    def test_choices_bool_empty_label(self):
        f = forms.ModelChoiceField(Category.objects.all(), empty_label='--------')
        Category.objects.all().delete()
        self.assertIs(bool(f.choices), True)

def synchronized(method) :
INDENT
    def new_method(self, * arg, ** kws) :
    INDENT
        with self.lock :
        INDENT
            return method(self, * arg, ** kws)
        DEDENT
    DEDENT
    return new_method
DEDENT

def window(seq, n = 2) :
INDENT
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen = n)
    yield win
    append = win.append
    for e in it :
    INDENT
        append(e)
        yield win
    DEDENT
DEDENT

def window(seq, n = 2) :
INDENT
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(1)), maxlen = n)
    yield win
    append = win.append
    for e in it :
    INDENT
        append(e)
        yield win
    DEDENT
    for _ in xrange(len(win) - 1) :
    INDENT
        win.popleft()
        yield win
    DEDENT
DEDENT

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

def char_first_index(s, c) :
INDENT
    if len_rec(s) == 0 :
    INDENT
        return None
    DEDENT
    if s [0] == c :
    INDENT
        return 0
    DEDENT
    answer = char_first_index(s [1 :], c)
    if answer is not None :
    INDENT
        return 1 + answer
    DEDENT
    else :
    INDENT
        return answer
    DEDENT
DEDENT

def duplicate(self) :
INDENT
    kwargs = {}
    for field in self._meta.fields :
    INDENT
        kwargs [field.name] = getattr(self, field.name)
    DEDENT
    kwargs.pop('id')
    new_instance = self.__class__(** kwargs)
    new_instance.save()
    fkeys_qs = self.fkeys.all()
    new_fkeys = []
    for fkey in fkey_qs :
    INDENT
        fkey_kwargs = {}
        for field in fkey._meta.fields :
        INDENT
            fkey_kwargs [field.name] = getattr(fkey, field.name)
        DEDENT
        fkey_kwargs.pop('id')
        fkey_kwargs ['foreign_key_field'] = new_instance.id
        new_fkeys.append(fkey_qs.model(** fkey_kwargs))
    DEDENT
    fkeys_qs.model.objects.bulk_create(new_fkeys)
    return new_instance
DEDENT

def family_lineage(familytree, lineage) :
INDENT
    trees = [familytree]
    while trees :
    INDENT
        tree = trees.pop()
        trees.extend(t for t in tree.values() if t)
        for name in lineage :
        INDENT
            if name not in tree :
            INDENT
                break
            DEDENT
            tree = tree [name]
        DEDENT
        else :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def almostIncreasingSequence(sequence) :
INDENT
    j = first_bad_pair(sequence, - 1)
    if j == - 1 :
    INDENT
        return True
    DEDENT
    if first_bad_pair(sequence, j) == - 1 :
    INDENT
        return True
    DEDENT
    if first_bad_pair(sequence, j + 1) == - 1 :
    INDENT
        return True
    DEDENT
    return False
DEDENT

def int_to_roman(a) :
INDENT
    all_roman_digits = []
    digit_lookup_table = [
        "", "0", "00", "000", "01",
        "1", "10", "100", "1000", "02"]
    for i, c in enumerate(reversed(str(a))) :
    INDENT
        roman_digit = ""
        for d in digit_lookup_table [int(c)] :
        INDENT
            roman_digit += ("IVXLCDM" [int(d) + i * 2])
        DEDENT
        all_roman_digits.append(roman_digit)
    DEDENT
    return "".join(reversed(all_roman_digits))
DEDENT

def seq(start, stop, step = 1) :
INDENT
    n = int(round((stop - start) / float(step)))
    if n > 1 :
    INDENT
        return ([start + step * i for i in range(n + 1)])
    DEDENT
    elif n == 1 :
    INDENT
        return ([start])
    DEDENT
    else :
    INDENT
        return ([])
    DEDENT
DEDENT

    def test_deepcopies_widget(self):
        class ModelChoiceForm(forms.Form):
            category = forms.ModelChoiceField(Category.objects.all())

        form1 = ModelChoiceForm()
        field1 = form1.fields['category']
        # To allow the widget to change the queryset of field1.widget.choices
        # without affecting other forms, the following must hold (#11183):
        self.assertIsNot(field1, ModelChoiceForm.base_fields['category'])
        self.assertIs(field1.widget.choices.field, field1)

def compose(* funcs) :
INDENT
    if not funcs :
    INDENT
        return lambda x : x
    DEDENT
    else :
    INDENT
        return lambda x : funcs [0](compose(* funcs [1 :])(x))
    DEDENT
DEDENT

def parse_entities(data) :
INDENT
    results = ''
    for entity_data in data.values() :
    INDENT
        for entity in entity_data :
        INDENT
            if entity ['sentiment'] ! = 'none' :
            INDENT
                results += entity ['name'] + ":" + entity ['sentiment'] + ","
            DEDENT
        DEDENT
    DEDENT
    return results
DEDENT

def fib(n) :
INDENT
    if n == 0 :
    INDENT
        return 0
    DEDENT
    elif n == 1 :
    INDENT
        return 1
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

def micro_world(bacteria, k) :
INDENT
    bacteria = sorted(bacteria, reverse = True)
    i = 0
    result = 0
    while i < len(bacteria) :
    INDENT
        bacterium_size = bacteria [i]
        bigger_bacterium_exists = False
        while i + 1 < len(bacteria) :
        INDENT
            difference = bacterium_size - bacteria [i + 1]
            if difference > k :
            INDENT
                break
            DEDENT
            if difference == 0 and not bigger_bacterium_exists :
            INDENT
                break
            DEDENT
            bacterium_size = bacteria [i + 1]
            i += 1
            bigger_bacterium_exists = True
        DEDENT
        result += 1
        i += 1
    DEDENT
    return result
DEDENT

def update(d, u) :
INDENT
    for k, v in u.iteritems() :
    INDENT
        if isinstance(d, collections.Mapping) :
        INDENT
            if isinstance(v, collections.Mapping) :
            INDENT
                r = update(d.get(k, {}), v)
                d [k] = r
            DEDENT
            else :
            INDENT
                d [k] = u [k]
            DEDENT
        DEDENT
        else :
        INDENT
            d = {k : u [k]}
        DEDENT
    DEDENT
    return d
DEDENT

def prime_factors(n) :
INDENT
    i = 2
    factors = []
    while i * i < = n :
    INDENT
        if n % i :
        INDENT
            i += 1
        DEDENT
        else :
        INDENT
            n //= i
            factors.append(i)
        DEDENT
    DEDENT
    if n > 1 :
    INDENT
        factors.append(n)
    DEDENT
    return factors
DEDENT

def translation_function(quit_flag, language) :
INDENT
    lang = gettext.translation('simple', localedir = 'locale', languages = [language])
    while not quit_flag.is_set() :
    INDENT
        print (lang.gettext("Running translator"), ": %s" % language)
        time.sleep(1.0)
    DEDENT
DEDENT

def _add(node, v) :
INDENT
    new = [v, [], []]
    if node :
    INDENT
        left, right = node [1 :]
        if not left :
        INDENT
            left.extend(new)
        DEDENT
        elif not right :
        INDENT
            right.extend(new)
        DEDENT
        else :
        INDENT
            _add(left, v)
        DEDENT
    DEDENT
    else :
    INDENT
        node.extend(new)
    DEDENT
DEDENT

def all_pairs(lst) :
INDENT
    if len(lst) < 2 :
    INDENT
        yield []
        return
    DEDENT
    if len(lst) % 2 == 1 :
    INDENT
        for i in range(len(lst)) :
        INDENT
            for result in all_pairs(lst [: i] + lst [i + 1 :]) :
            INDENT
                yield result
            DEDENT
        DEDENT
    DEDENT
    else :
    INDENT
        a = lst [0]
        for i in range(1, len(lst)) :
        INDENT
            pair = (a, lst [i])
            for rest in all_pairs(lst [1 : i] + lst [i + 1 :]) :
            INDENT
                yield [pair] + rest
            DEDENT
        DEDENT
    DEDENT
DEDENT

    def test_result_cache_not_shared(self):
        class ModelChoiceForm(forms.Form):
            category = forms.ModelChoiceField(Category.objects.all())

        form1 = ModelChoiceForm()
        self.assertCountEqual(form1.fields['category'].queryset, [self.c1, self.c2, self.c3])
        form2 = ModelChoiceForm()
        self.assertIsNone(form2.fields['category'].queryset._result_cache)

def searchContact() :
INDENT
    number = raw_input("Enter phone number to search data : ")
    obj1 = open("file.txt", "r")
    re = obj1.read()
    print re
    x = re.split("\n")
    matching = [s for s in x if number in s]
    print matching
    obj1.close()
DEDENT

def window(seq, n = 2) :
INDENT
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n :
    INDENT
        yield result
    DEDENT
    for elem in it :
    INDENT
        result = result [1 :] + (elem,)
        yield result
    DEDENT
DEDENT

def get_data(self) :
INDENT
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) :
    INDENT
        return sys.stdin.read(1)
    DEDENT
    return False
DEDENT

def invertSelectionRemoveSelected(self) :
INDENT
    model = self.view.model()
    for i in range(model.rowCount()) :
    INDENT
        for j in range(model.columnCount()) :
        INDENT
            ix = model.index(i, j)
            self.view.selectionModel().select(ix, QItemSelectionModel.Toggle)
        DEDENT
    DEDENT
    for ix in reversed(self.view.selectionModel().selectedRows()) :
    INDENT
        model.removeRow(ix.row())
    DEDENT
DEDENT

def postalValidate(S) :
INDENT
    S = S.upper().replace(" ", "")
    if len(S) == 6 :
    INDENT
        for i in range(len(S)) :
        INDENT
            if i % 2 == 0 :
            INDENT
                if not (S [i].isalpha()) :
                INDENT
                    return False
                DEDENT
            DEDENT
            else :
            INDENT
                if not (S [i].isdigit()) :
                INDENT
                    return False
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    else :
    INDENT
        return False
    DEDENT
    return S
DEDENT

def is_prime(n) :
INDENT
    if n == 2 or n == 3 : return True
    if n < 2 or n % 2 == 0 : return False
    if n < 9 : return True
    if n % 3 == 0 : return False
    r = int(n ** 0.5)
    f = 5
    while f < = r :
    INDENT
        print '\t', f
        if n % f == 0 : return False
        if n % (f + 2) == 0 : return False
        f += 6
    DEDENT
    return True
DEDENT

    def test_queryset_none(self):
        class ModelChoiceForm(forms.Form):
            category = forms.ModelChoiceField(queryset=None)

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['category'].queryset = Category.objects.filter(slug__contains='test')

def readlines(self) :
INDENT
    lines = []
def decrypt(quotedEncodedEncrypted) :
INDENT
    key = 'SecretKey'
    encodedEncrypted = urllib2.unquote(quotedEncodedEncrypted)
    cipher = AES.new(key)
    decrypted = cipher.decrypt(base64.b64decode(encodedEncrypted)) [: 16]
    for i in range(1, len(base64.b64decode(encodedEncrypted)) / 16) :
    INDENT
        cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(encodedEncrypted) [(i - 1) * 16 : i * 16])
        decrypted += cipher.decrypt(base64.b64decode(encodedEncrypted) [i * 16 :]) [: 16]
    DEDENT
    return decrypted.strip()
DEDENT

def __init__(self, data) :
INDENT
    super(MyObject, self).__init__()
    if isinstance(data, self.__class__) :
    INDENT
        self.value = data.value
    DEDENT
    elif isinstance(data, basestring) :
    INDENT
        self.value = float(data)
    DEDENT
    else :
    INDENT
        self.value = data
    DEDENT
DEDENT

    for line in iter(self.readline, '') :
    INDENT
        lines.append(line)
    DEDENT
    return lines
DEDENT

def underscore_to_camelcase(s) :
INDENT
    def camelcase_words(words) :
    INDENT
        first_word_passed = False
        for word in words :
        INDENT
            if not word :
            INDENT
                yield "_"
                continue
            DEDENT
            if first_word_passed :
            INDENT
                yield word.capitalize()
            DEDENT
            else :
            INDENT
                yield word.lower()
            DEDENT
            first_word_passed = True
        DEDENT
    DEDENT
    return ''.join(camelcase_words(s.split('_')))
DEDENT

        form = ModelChoiceForm()
        self.assertCountEqual(form.fields['category'].queryset, [self.c2, self.c3])

def __init__(self, * args, ** kwargs) :
INDENT
    wx.Frame.__init__(self, * args, ** kwargs)
    self.panel = wx.Panel(self)
    self.button = wx.Button(self.panel, label = "Test")
    self.sizer = wx.BoxSizer()
    self.sizer.Add(self.button)
    self.panel.SetSizerAndFit(self.sizer)
    self.Show()
DEDENT

def __init__(self, parent, this_worker) :
INDENT
    self.parent = parent
    self.this_worker = this_worker
    QtGui.QTabWidget.__init__(self, parent)
    self.treeWidget = QtGui.QTreeWidget(self)
    self.properties = QtGui.QTreeWidgetItem(self.treeWidget, ["Properties"])
    self.step = QtGui.QTreeWidgetItem(self.properties, ["Iteration #"])
    self.thread = QtCore.QThread();
    self.this_worker.moveToThread(self.thread);
    self.this_worker.update_signal.connect(self.update_GUI)
    self.this_worker.done_signal.connect(self.thread.quit)
    self.start_comp.connect(self.this_worker.start_computation)
    self.thread.start()
DEDENT

    def test_no_extra_query_when_accessing_attrs(self):
        """
        ModelChoiceField with RadioSelect widget doesn't produce unnecessary
        db queries when accessing its BoundField's attrs.
        """
        class ModelChoiceForm(forms.Form):
            category = forms.ModelChoiceField(Category.objects.all(), widget=forms.RadioSelect)

        form = ModelChoiceForm()
        field = form['category']  # BoundField
        template = Template('{{ field.name }}{{ field }}{{ field.help_text }}')
        with self.assertNumQueries(1):
            template.render(Context({'field': field}))

def run(cmd, timeout_sec) :
INDENT
    proc = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    timeout = {"value" : False}
    timer = Timer(timeout_sec, kill_proc, [proc, timeout])
    timer.start()
    stdout, stderr = proc.communicate()
    timer.cancel()
    return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8"), timeout ["value"]
DEDENT

def run(self) :
INDENT
    self.process = subprocess.Popen(self.cmd, stdout = self.outFile, stderr = self.errFile)
    while (self.process.poll() is None and self.timeout > 0) :
    INDENT
        time.sleep(1)
        self.timeout -= 1
    DEDENT
    if not self.timeout > 0 :
    INDENT
        self.process.terminate()
        self.timed_out = True
    DEDENT
    else :
    INDENT
        self.timed_out = False
    DEDENT
DEDENT

def window(iterable, size) :
INDENT
    iters = tee(iterable, size)
    for i in xrange(1, size) :
    INDENT
        for each in iters [i :] :
        INDENT
            next(each, None)
        DEDENT
    DEDENT
    return izip(* iters)
DEDENT

def factors(n) :
INDENT
    i = 2
    while n > 1 :
    INDENT
        p = 0
        while n > 1 and n % i == 0 :
        INDENT
            p += 1
            n /= i
        DEDENT
        if p :
        INDENT
            yield (i, p)
        DEDENT
        i += 1
    DEDENT
DEDENT

def split_at_first_false(pred, seq) :
INDENT
    if not isinstance(seq, list) :
    INDENT
        seq = list(seq)
    DEDENT
    for i, x in enumerate(seq) :
    INDENT
        if not pred(x) :
        INDENT
            return seq [: i], seq [i :]
        DEDENT
    DEDENT
    return seq, []
DEDENT

def tail(f, nlines) :
INDENT
    buf = ''
    result = []
    for block in rblocks(f) :
    INDENT
        buf = block + buf
        lines = buf.splitlines()
        if lines :
        INDENT
            result.extend(lines [1 :])
            if (len(result) > = nlines) :
            INDENT
                return result [- nlines :]
            DEDENT
            buf = lines [0]
        DEDENT
    DEDENT
    return ([buf] + result) [- nlines :]
DEDENT

def __setattr__(self, key, value) :
INDENT
    setIsOK = False
    for item in self.__List :
    INDENT
        if key == item :
        INDENT
            setIsOK = True
        DEDENT
    DEDENT
    if setIsOK == True :
    INDENT
        object.__setattr__(self, key, value)
    DEDENT
    else :
    INDENT
        raise TypeError("%r has no attributes %r" % (self, key))
    DEDENT
DEDENT

    def test_disabled_modelchoicefield(self):
        class ModelChoiceForm(forms.ModelForm):
            author = forms.ModelChoiceField(Author.objects.all(), disabled=True)

            class Meta:
                model = Book
                fields = ['author']

        book = Book.objects.create(author=Writer.objects.create(name='Test writer'))
        form = ModelChoiceForm({}, instance=book)
        self.assertEqual(
            form.errors['author'],
            ['Select a valid choice. That choice is not one of the available choices.']
        )

def clean_code(self) :
INDENT
    input_code = self.cleaned_data ['code']
    discount_code = self.event.discounts.filter(code = input_code).first()
    if not discount_code :
    INDENT
        raise forms.ValidationError(_("The discount code couldn't be found."),
            code = 'code_exists')
    DEDENT
    if not discount_code.is_active() :
    INDENT
        raise forms.ValidationError(_("This discount code is not available anymore."),
            code = 'code_not_active')
    DEDENT
    return input_code
DEDENT

def nindex(needle, haystack, index = 1) :
INDENT
    parts = haystack.split(needle)
    position = 0
    length = len(needle)
    for i in range(index - 1) :
    INDENT
        position += len(parts [i]) + length
    DEDENT
    return position
DEDENT

def partition(sequence, low, high) :
INDENT
    pivot = sequence [low]
    i = low + 1
    for j in range(low + 1, high + 1) :
    INDENT
        if sequence [j] < pivot :
        INDENT
            sequence [j], sequence [i] = sequence [i], sequence [j]
            i += 1
        DEDENT
    DEDENT
    sequence [i - 1], sequence [low] = sequence [low], sequence [i - 1]
    return i - 1
DEDENT

    def test_disabled_modelchoicefield_has_changed(self):
        field = forms.ModelChoiceField(Author.objects.all(), disabled=True)
        self.assertIs(field.has_changed('x', 'y'), False)

def get_form_instance(self, step) :
INDENT
    if not self.instance :
    INDENT
        if 'project_id' in self.kwargs :
        INDENT
            project_id = self.kwargs ['project_id']
            self.instance = Project.objects.get(id = project_id)
        DEDENT
        else :
        INDENT
            self.instance = Project()
        DEDENT
    DEDENT
    return self.instance
DEDENT

def partition(a_list, low, high) :
INDENT
    pivot = a_list [low]
    while True :
    INDENT
        while a_list [low] < pivot :
        INDENT
            low += 1
        DEDENT
        while a_list [high] > pivot :
        INDENT
            high -= 1
        DEDENT
        if low > = high :
        INDENT
            return high
        DEDENT
        a_list [low], a_list [high] = a_list [high], a_list [low]
        low += 1
        high -= 1
    DEDENT
DEDENT

def main() :
INDENT
    cap = VideoCapture()
    shape = cap.get_size()
    shared_array_base = Array(ctypes.c_uint8, shape [0] * shape [1] * shape [2])
    frame = np.ctypeslib.as_array(shared_array_base.get_obj())
    frame = frame.reshape(shape [0], shape [1], shape [2])
    finished = Value('i', 0)
    video_process = Process(target = stream,
        args = (cap, shared_array_base, finished))
    video_process.start()
    time.sleep(2)
    def terminate() :
    INDENT
        print ("Main: termination")
        finished.value = True
        time.sleep(1)
        video_process.join()
    DEDENT
    while True :
    INDENT
        try :
        INDENT
            cv2.imshow('frame', frame)
            time.sleep(0.1)
            cv2.waitKey(1)
        DEDENT
        except KeyboardInterrupt :
        INDENT
            cv2.destroyAllWindows()
            terminate()
            break
        DEDENT
    DEDENT
DEDENT

    def test_disabled_modelchoicefield_initial_model_instance(self):
        class ModelChoiceForm(forms.Form):
            categories = forms.ModelChoiceField(
                Category.objects.all(),
                disabled=True,
                initial=self.c1,
            )

        self.assertTrue(ModelChoiceForm(data={'categories': self.c1.pk}).is_valid())

def inf_repeat(k) :
INDENT
    for i in it.count(1) :
    INDENT
        for j in [i] * k :
        INDENT
            yield j
        DEDENT
    DEDENT
DEDENT

def flatten(l, a) :
INDENT
    for i in l :
    INDENT
        if isinstance(i, list) :
        INDENT
            flatten(i, a)
        DEDENT
        else :
        INDENT
            a.append(i)
        DEDENT
    DEDENT
    return a
DEDENT

def scan(thewords) :
INDENT
    thewords = thewords.split()
    sentence = []
    for i in thewords :
    INDENT
        if i in directions :
        INDENT
            sentence.append(('direction', i))
        DEDENT
        elif i in verbs :
        INDENT
            sentence.append(('verb', i))
        DEDENT
        elif i in stops :
        INDENT
            sentence.append(('stop', i))
        DEDENT
        elif i in nouns :
        INDENT
            sentence.append(('noun', i))
        DEDENT
        elif i.isdigit() :
        INDENT
            sentence.append(('number', convert_number(i)))
        DEDENT
        else :
        INDENT
            sentence.append(('error', i))
        DEDENT
    DEDENT
    return sentence
DEDENT

def flat_sum(lst) :
INDENT
    if len(lst) == 0 :
    INDENT
        return 0
    DEDENT
    hd, tl = lst [0], lst [1 :]
    if isinstance(hd, list) :
    INDENT
        return flat_sum(hd) + flat_sum(tl)
    DEDENT
    elif isinstance(hd, Number) :
    INDENT
        return hd + flat_sum(tl)
    DEDENT
    else :
    INDENT
        return flat_sum(tl)
    DEDENT
DEDENT

def fire(self) :
INDENT
    for observer in Observer._observers :
    INDENT
        if self.name in observer._observables :
        INDENT
            observer._observables [self.name](self.data)
        DEDENT
    DEDENT
DEDENT

def tail(filename, n) :
INDENT
    size = os.path.getsize(filename)
    with open(filename, "rb") as f :
    INDENT
        fm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        try :
        INDENT
            for i in xrange(size - 1, - 1, - 1) :
            INDENT
                if fm [i] == '\n' :
                INDENT
                    n -= 1
                    if n == - 1 :
                    INDENT
                        break
                    DEDENT
                DEDENT
            DEDENT
            return fm [i + 1 if i else 0 :].splitlines()
        DEDENT
        finally :
        INDENT
            fm.close()
        DEDENT
    DEDENT
DEDENT

def get_size(start_path = '.') :
INDENT
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path) :
    INDENT
        for f in filenames :
        INDENT
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        DEDENT
    DEDENT
    return total_size
DEDENT

    def test_disabled_multiplemodelchoicefield(self):
        class ArticleForm(forms.ModelForm):
            categories = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)

            class Meta:
                model = Article
                fields = ['categories']

        category1 = Category.objects.create(name='cat1')
        category2 = Category.objects.create(name='cat2')
        article = Article.objects.create(
            pub_date=datetime.date(1988, 1, 4),
            writer=Writer.objects.create(name='Test writer'),
        )
        article.categories.set([category1.pk])

        form = ArticleForm(data={'categories': [category2.pk]}, instance=article)
        self.assertEqual(form.errors, {})
        self.assertEqual([x.pk for x in form.cleaned_data['categories']], [category2.pk])
        # Disabled fields use the value from `instance` rather than `data`.
        form = ArticleForm(data={'categories': [category2.pk]}, instance=article)
        form.fields['categories'].disabled = True
        self.assertEqual(form.errors, {})
        self.assertEqual([x.pk for x in form.cleaned_data['categories']], [category1.pk])

def all_pairs(lst) :
INDENT
    N = len(lst)
    choice_indices = itertools.product(* [
            xrange(k) for k in reversed(xrange(1, N, 2))])
    for choice in choice_indices :
    INDENT
        tmp = lst [:]
        result = []
        for index in choice :
        INDENT
            result.append((tmp.pop(0), tmp.pop(index)))
        DEDENT
        yield result
    DEDENT
DEDENT

def runthis(* stringinput) :
INDENT
    for t in stringinput :
    INDENT
        t = t.upper()
        print (t)
    DEDENT
    print ()
DEDENT

    def test_disabled_modelmultiplechoicefield_has_changed(self):
        field = forms.ModelMultipleChoiceField(Author.objects.all(), disabled=True)
        self.assertIs(field.has_changed('x', 'y'), False)

def run(self) :
INDENT
    while True :
    INDENT
        image = self.tasks_q.get()
        time.sleep(1)
        self.results_q.put("text")
    DEDENT
DEDENT

def decode(string, alphabet = BASE62) :
INDENT
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
    for char in string :
    INDENT
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1
    DEDENT
    return num
DEDENT

def underscore_to_camelcase(value) :
INDENT
    def camelcase() :
    INDENT
        yield str.lower
        while True :
        INDENT
            yield str.capitalize
        DEDENT
    DEDENT
    c = camelcase()
    return "".join(c.next()(x) if x else '_' for x in value.split("_"))
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

def transitive_closure(elements) :
INDENT
    elements = set([(x, y) if x < y else (y, x) for x, y in elements])
    relations = {}
    for x, y in elements :
    INDENT
        if x not in relations :
        INDENT
            relations [x] = []
        DEDENT
        relations [x].append(y)
    DEDENT
    closure = set()
    def build_closure(n) :
    INDENT
        def f(k) :
        INDENT
            for y in relations.get(k, []) :
            INDENT
                closure.add((n, y))
                f(y)
            DEDENT
        DEDENT
        f(n)
    DEDENT
    for k in relations.keys() :
    INDENT
        build_closure(k)
    DEDENT
    return closure
DEDENT

def __init__(self, parent, this_worker) :
INDENT
    self.parent = parent
    self.this_worker = this_worker
    QtGui.QTabWidget.__init__(self, parent)
    self.treeWidget = QtGui.QTreeWidget(self)
    self.properties = QtGui.QTreeWidgetItem(self.treeWidget, ["Properties"])
    self.step = QtGui.QTreeWidgetItem(self.properties, ["Iteration #"])
    self.thread = QtCore.QThread();
    self.this_worker.moveToThread(self.thread);
    self.this_worker.update_signal.connect(self.update_GUI)
    self.this_worker.done_signal.connect(self.thread.quit)
    self.start_comp.connect(self.this_worker.start_computation)
    self.thread.start()
DEDENT

    def test_overridable_choice_iterator(self):
        """
        Iterator defaults to ModelChoiceIterator and can be overridden with
        the iterator attribute on a ModelChoiceField subclass.
        """
        field = forms.ModelChoiceField(Category.objects.all())
        self.assertIsInstance(field.choices, ModelChoiceIterator)

        class CustomModelChoiceIterator(ModelChoiceIterator):
            pass

        class CustomModelChoiceField(forms.ModelChoiceField):
            iterator = CustomModelChoiceIterator

        field = CustomModelChoiceField(Category.objects.all())
        self.assertIsInstance(field.choices, CustomModelChoiceIterator)

def is_sorted(lst, key = lambda x : x) :
INDENT
    for i, el in enumerate(lst [1 :]) :
    INDENT
        if key(el) < key(lst [i]) :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def fib(n) :
INDENT
    if n == 1 :
    INDENT
        return (1)
    DEDENT
    elif n == 0 :
    INDENT
        return (0)
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

def flatten(l, ltypes = (list, tuple)) :
INDENT
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l) :
    INDENT
        while isinstance(l [i], ltypes) :
        INDENT
            if not l [i] :
            INDENT
                l.pop(i)
                i -= 1
                break
            DEDENT
            else :
            INDENT
                l [i : i + 1] = l [i]
            DEDENT
        DEDENT
        i += 1
    DEDENT
    return ltype(l)
DEDENT

def __new__(cls, name, value, base = None) :
INDENT
    value = int(value) if base is None else int(value, base)
    if isinstance(value, int) :
    INDENT
        NamedNumber = Named
    DEDENT
    else :
    INDENT
        NamedNumber = cls = NamedLong
    DEDENT
    self = super(NamedNumber, cls).__new__(cls, value)
    super(NamedNumber, self).__setattr__('_name', name)
    return self
DEDENT

def quicksort(a_list) :
INDENT
    def _quicksort(a_list, low, high) :
    INDENT
        if low < high :
        INDENT
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p + 1, high)
        DEDENT
    DEDENT
    def partition(a_list, low, high) :
    INDENT
        pivot = a_list [low]
        while True :
        INDENT
            while a_list [low] < pivot :
            INDENT
                low += 1
            DEDENT
            while a_list [high] > pivot :
            INDENT
                high -= 1
            DEDENT
            if low > = high :
            INDENT
                return high
            DEDENT
            a_list [low], a_list [high] = a_list [high], a_list [low]
            low += 1
            high -= 1
        DEDENT
    DEDENT
    _quicksort(a_list, 0, len(a_list) - 1)
    return a_list
DEDENT

    def test_choice_iterator_passes_model_to_widget(self):
        class CustomModelChoiceValue:
            def __init__(self, value, obj):
                self.value = value
                self.obj = obj

def index(filename, lst) :
INDENT
    infile = open('raven.txt', 'r')
    lines = infile.readlines()
    words = []
    dic = {}
    for line in lines :
    INDENT
        line_words = line.split(' ')
        words.append(line_words)
    DEDENT
    for i in range(len(words)) :
    INDENT
        for j in range(len(words [i])) :
        INDENT
            if words [i] [j] in lst :
            INDENT
                if words [i] [j] not in dic.keys() :
                INDENT
                    dic [words [i] [j]] = set()
                DEDENT
                dic [words [i] [j]].add(i + 1)
            DEDENT
        DEDENT
    DEDENT
    return dic
DEDENT

def __call__(self, parser, args, values, option_string = None) :
INDENT
    if args.verbose == None :
    INDENT
        base = 0
    DEDENT
    else :
    INDENT
        base = args.verbose
    DEDENT
    option_string = option_string.lstrip('-')
    if option_string [0] == 'q' :
    INDENT
        incr = - 1
    DEDENT
    elif option_string [0] == 'v' :
    INDENT
        incr = 1
    DEDENT
    else :
    INDENT
        raise argparse.ArgumentError(self,
            'Option string for verbosity must start with v(erbose) or q(uiet)')
    DEDENT
    if values == None :
    INDENT
        values = base + incr
    DEDENT
    else :
    INDENT
def index(filename, lst) :
INDENT
    infile = open('raven.txt', 'r')
    lines = infile.readlines()
    words = []
    dic = {}
    for line in lines :
    INDENT
        line_words = line.split(' ')
        words.append(line_words)
    DEDENT
    for i in range(len(words)) :
    INDENT
        for j in range(len(words [i])) :
        INDENT
            if words [i] [j] in lst :
            INDENT
                if words [i] [j] not in dic.keys() :
                INDENT
                    dic [words [i] [j]] = set()
                DEDENT
                dic [words [i] [j]].add(i + 1)
            DEDENT
        DEDENT
    DEDENT
    return dic
DEDENT

        try :
        INDENT
            values = int(values)
        DEDENT
        except ValueError :
        INDENT
            values = values.lower()
            if not re.match('^[vq]+$', values) :
            INDENT
                raise argparse.ArgumentError(self,
                    "Option string for -v/-q must contain only further 'v'/'q' letters")
            DEDENT
            values = base + incr + values.count('v') - values.count('q')
        DEDENT
    DEDENT
    setattr(args, self.dest, values)
DEDENT

def test() :
INDENT
    fn = 'users.txt'
    changeuser = 'peterpeter'
    newinfo = 'HeIsTall'
    for line in fileinput.input(fn, inplace = 1) :
    INDENT
        user, oldinfo = line.split(':')
        print '%s:%s' % (user, newinfo if user == changeuser else oldinfo.replace('\n', ''))
    DEDENT
DEDENT

def arePermsEqualParity(perm0, perm1) :
INDENT
    perm1 = list(perm1)
    perm1_map = dict((v, i) for i, v in enumerate(perm1))
    transCount = 0
    for loc, p0 in enumerate(perm0) :
    INDENT
        p1 = perm1 [loc]
        if p0 ! = p1 :
        INDENT
            sloc = perm1_map [p0]
            perm1 [loc], perm1 [sloc] = p0, p1
            perm1_map [p0], perm1_map [p1] = loc, sloc
            transCount += 1
        DEDENT
    DEDENT
    return (transCount % 2) == 0
DEDENT

def curry(x, argc = None) :
INDENT
    if argc is None :
    INDENT
        argc = x.func_code.co_argcount
    DEDENT
    def p(* a) :
    INDENT
        if len(a) == argc :
        INDENT
            return x(* a)
def pdf_view(request) :
INDENT
    with open('/path / to /name.pdf', 'rb') as pdf :
    INDENT
        response = HttpResponse(pdf.read(), content_type = 'application/pdf')
        response ['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    DEDENT
DEDENT

        DEDENT
        def q(* b) :
        INDENT
            return x(* (a + b))
        DEDENT
        return curry(q, argc - len(a))
    DEDENT
    return p
DEDENT

            def __str__(self):
                return str(self.value)

def __init__(self, iterable = {}, ** kwargs) :
INDENT
    super(StrictDict, self).__init__({})
    keys = set(iterable.keys()).union(set(kwargs.keys()))
    if not keys.issuperset(self.required) :
    INDENT
        msg = str(self.__class__.__name__) + " requires: " + str([str(key) for key in self.required])
        raise AttributeError(msg)
    DEDENT
    if len(list(self.at_least_one_required)) and len(list(keys.intersection(self.at_least_one_required))) < 1 :
    INDENT
        msg = str(self.__class__.__name__) + " requires at least one: " + str([str(key) for key in self.at_least_one_required])
        raise AttributeError(msg)
    DEDENT
    for key, val in iterable.iteritems() :
    INDENT
        self.__setitem__(key, val)
    DEDENT
    for key, val in kwargs.iteritems() :
    INDENT
        self.__setitem__(key, val)
    DEDENT
DEDENT

def encrypt(key, plaintext) :
INDENT
    padded_key = key.ljust(KEY_SIZE, '\0')
    padded_text = plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * '\0'
    r = rijndael.rijndael(padded_key, BLOCK_SIZE)
    ciphertext = ''
    for start in range(0, len(padded_text), BLOCK_SIZE) :
    INDENT
        ciphertext += r.encrypt(padded_text [start : start + BLOCK_SIZE])
    DEDENT
    encoded = base64.b64encode(ciphertext)
    return encoded
DEDENT

def __init__(cls, name, bases, dct) :
INDENT
    def static_attrs() :
    INDENT
        import types
        attrs = {}
        val_set = set()
        filter_names = set(['__doc__', '__init__', '__metaclass__', '__module__', '__main__'])
        for key, value in dct.iteritems() :
        INDENT
            if type(value) ! = types.FunctionType and key not in filter_names :
            INDENT
                if len(value) ! = 2 :
                INDENT
                    raise NotImplementedError('not support for values that is not 2 elements!')
                DEDENT
                if value [0] not in val_set :
                INDENT
                    val_set.add(value [0])
                DEDENT
                else :
                INDENT
                    raise KeyError("%s 's key: %s is duplicated!" % (dict([(key, value)]), value [0]))
                DEDENT
                attrs [key] = value
            DEDENT
        DEDENT
        return attrs, val_set
    DEDENT
    attrs, val_set = static_attrs()
    setattr(cls, 'STATIC_ATTRS', attrs)
    setattr(cls, 'static_val_set', val_set)
    super(ConstMeta, cls).__init__(name, bases, dct)
DEDENT

def tail(f, window = 20) :
INDENT
    if window == 0 :
    INDENT
        return []
    DEDENT
    BUFSIZ = 1024
    f.seek(0, 2)
    remaining_bytes = f.tell()
    size = window + 1
    block = - 1
    data = []
    while size > 0 and remaining_bytes > 0 :
    INDENT
        if remaining_bytes - BUFSIZ > 0 :
        INDENT
            f.seek(block * BUFSIZ, 2)
            bunch = f.read(BUFSIZ)
        DEDENT
        else :
        INDENT
            f.seek(0, 0)
            bunch = f.read(remaining_bytes)
        DEDENT
        bunch = bunch.decode('utf-8')
        data.insert(0, bunch)
        size -= bunch.count('\n')
        remaining_bytes -= BUFSIZ
        block -= 1
    DEDENT
    return ''.join(data).splitlines() [- window :]
DEDENT

        class CustomModelChoiceIterator(ModelChoiceIterator):
            def choice(self, obj):
                value, label = super().choice(obj)
                return CustomModelChoiceValue(value, obj), label

def is_palindrome(word) :
INDENT
    if len(word) < = 1 :
    INDENT
        print 'This word is a palindrome'
    DEDENT
    elif first(word) ! = last(word) :
    INDENT
        print 'This word is not a palindrome'
    DEDENT
    else :
    INDENT
        word = middle(word)
        is_palindrome(word)
    DEDENT
DEDENT

def function(argument) :
INDENT
    max_arg = max(argument)
    argument.remove(max_arg)
    for length in range(1, len(argument) + 1) :
    INDENT
        for combo in combinations(argument, length) :
        INDENT
            if sum(combo) == max_arg :
            INDENT
                return "true"
            DEDENT
        DEDENT
    DEDENT
    return "false"
DEDENT

def integer(s) :
INDENT
    for i in s :
    INDENT
        if s in "0123456789" :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def accept(self, mimetype) :
INDENT
    def decorator(func) :
    INDENT
        self.accept_handlers [mimetype] = func
        return func
    DEDENT
    return decorator
DEDENT

def flatten(l, ltypes = (list, tuple)) :
INDENT
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l) :
    INDENT
        while isinstance(l [i], ltypes) :
        INDENT
            if not l [i] :
            INDENT
                l.pop(i)
                i -= 1
                break
            DEDENT
            else :
            INDENT
                l [i : i + 1] = l [i]
            DEDENT
        DEDENT
        i += 1
    DEDENT
    return ltype(l)
DEDENT

def tail(self, lines_2find = 1) :
INDENT
    self.seek(0, 2)
    bytes_in_file = self.tell()
    lines_found, total_bytes_scanned = 0, 0
    while (lines_2find + 1 > lines_found and
        bytes_in_file > total_bytes_scanned) :
    INDENT
        byte_block = min(1024, bytes_in_file - total_bytes_scanned)
        self.seek(- (byte_block + total_bytes_scanned), 2)
        total_bytes_scanned += byte_block
        lines_found += self.read(1024).count('\n')
    DEDENT
    self.seek(- total_bytes_scanned, 2)
    line_list = list(self.readlines())
    return line_list [- lines_2find :]
DEDENT

def tail(f, window = 20) :
INDENT
    if window == 0 :
    INDENT
        return []
    DEDENT
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window + 1
    block = - 1
    data = []
    while size > 0 and bytes > 0 :
    INDENT
        if bytes - BUFSIZ > 0 :
        INDENT
            f.seek(block * BUFSIZ, 2)
            data.insert(0, f.read(BUFSIZ))
        DEDENT
        else :
        INDENT
            f.seek(0, 0)
            data.insert(0, f.read(bytes))
        DEDENT
        linesFound = data [0].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    DEDENT
    return ''.join(data).splitlines() [- window :]
DEDENT

        class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
            def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
                option = super().create_option(name, value, label, selected, index, subindex=None, attrs=None)
                # Modify the HTML based on the object being rendered.
                c = value.obj
                option['attrs']['data-slug'] = c.slug
                return option

def readParag(fileObj) :
INDENT
    while True :
    INDENT
        nextList = [ln.rstrip() for ln in takewhile(lambda line : line ! = "\n", fileObj)]
        if not nextList :
        INDENT
            break
        DEDENT
        yield nextList
    DEDENT
DEDENT

def write(self, data) :
INDENT
    if data [0 : LOG_IDR_LENGTH] == LOG_IDENTIFIER :
    INDENT
        self.fl.write("%s\n" % data [LOG_IDR_LENGTH :])
        self.stdout.write(data [LOG_IDR_LENGTH :])
    DEDENT
    else :
    INDENT
        timestamp = str(datetime.datetime.now())
        if 'Traceback' == data [0 : 9] :
        INDENT
            data = '%s: %s' % (timestamp, data)
            self.fl.write(data)
        DEDENT
        else :
        INDENT
            self.fl.write(data)
        DEDENT
        self.stdout.write(data)
    DEDENT
DEDENT

def records(currentTime = Decimal('1.00')) :
INDENT
    first = True
    previousChunk = ''
    exhaustedInput = False
    while True :
    INDENT
        chunk = sample.read(50)
        if not chunk :
        INDENT
            exhaustedInput = True
            chunk = previousChunk
        DEDENT
        else :
        INDENT
            chunk = (previousChunk + chunk).replace('\n', '')
        DEDENT
        items = chunk.split()
        for number in items [: len(items) if exhaustedInput else - 1] :
        INDENT
            if Decimal(number) == currentTime :
            INDENT
                if first :
                INDENT
                    first = False
                DEDENT
                else :
                INDENT
                    yield record
                DEDENT
                record = [number]
                currentTime += Decimal('0.1')
            DEDENT
            else :
            INDENT
                record.append(number)
            DEDENT
        DEDENT
        if exhaustedInput :
        INDENT
            yield record
            break
        DEDENT
        else :
        INDENT
            previousChunk = chunk.split() [- 1]
        DEDENT
    DEDENT
DEDENT

def merge(arr1, arr2) :
INDENT
    for i in arr1 :
    INDENT
        for j in list(range(len(arr2))) :
        INDENT
            if i < arr2 [j] :
            INDENT
                arr2.append(arr2 [- 1])
                for count in list(range(len(arr2) - 1, j, - 1)) :
                INDENT
                    arr2 [count] = arr2 [count - 1]
                DEDENT
                arr2 [j] = i
                break
            DEDENT
            if j == len(arr2) - 1 :
            INDENT
                arr2.append(i)
            DEDENT
        DEDENT
    DEDENT
    return arr2
DEDENT

def div3() :
INDENT
    divlist = []
    num = range(1, 10)
    for n in num :
    INDENT
        if n % 3 == 0 :
        INDENT
            for _ in xrange(20) :
            INDENT
                divlist.append(random.randint(0, 10))
            DEDENT
        DEDENT
    DEDENT
    print divlist
DEDENT

def roll_die(die_type, roll_times, print_op = False) :
INDENT
    total_roll = 0
    for _ in range(roll_times) :
    INDENT
        roll_result = random.randint(1, die_type)
        total_roll += roll_result
        if print_op :
        INDENT
            print (roll_result)
        DEDENT
    DEDENT
    if print_op :
    INDENT
        print (total_roll)
    DEDENT
    return total_roll
DEDENT

def queryset(self, request, queryset) :
INDENT
    origin_GET = request.GET.copy()
    fake_GET = QueryDict(mutable = True)
    fake_GET.update(self.used_parameters)
    request.GET = fake_GET
    all_params = {}
    for spec in self.get_filters(request, self.used_parameters) :
    INDENT
        if spec and spec.has_output() :
        INDENT
            all_params.update(spec.used_parameters)
        DEDENT
    DEDENT
    try :
    INDENT
        query_params = [Q((key, value)) for key, value in all_params.items()]
        queryset = queryset.filter(reduce(operator.or_, query_params))
    DEDENT
    except TypeError as e :
    INDENT
        pass
    DEDENT
    request.GET = origin_GET
    return queryset
DEDENT

def to_bool(bool_str) :
INDENT
    if isinstance(bool_str, basestring) and bool_str :
    INDENT
        if bool_str.lower() in ['true', 't', '1'] : return True
        elif bool_str.lower() in ['false', 'f', '0'] : return False
    DEDENT
    raise ValueError("%s is no recognized as a boolean value" % bool_str)
DEDENT

def Run(self) :
INDENT
    self.time0 = time.clock()
    self.JobBeginning(self.duration)
def run(self) :
INDENT
    print '>>>> skip body manually by returning flag with context'
    with self.drivercontext(self.driverfactory) as (driver, ok) :
    INDENT
        if ok :
        INDENT
            self.dostuff(driver)
        DEDENT
        else :
        INDENT
            print 'skip because driver not ok'
        DEDENT
    DEDENT
DEDENT

def rec(chk, i) :
INDENT
    global flag
    print (locals())
    i += 1
    chk.append(i)
    if (i == 4) :
    INDENT
        flag = 1
    DEDENT
    if (flag == 1) :
    INDENT
        return
    DEDENT
    else :
    INDENT
        rec(chk [:], i)
    DEDENT
    print (locals())
DEDENT

    try :
    INDENT
        for count in range(0, self.duration) :
        INDENT
            time.sleep(1.0)
            self.JobProgress(count)
            self.PossibleStoppingPoint()
        DEDENT
    DEDENT
    except InterruptedException :
    INDENT
        print "canceled prematurely!"
    DEDENT
    self.JobFinished()
DEDENT

        class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
            iterator = CustomModelChoiceIterator
            widget = CustomCheckboxSelectMultiple

        field = CustomModelMultipleChoiceField(Category.objects.all())
        self.assertHTMLEqual(
            field.widget.render('name', []),
            '''<ul>
<li><label><input type="checkbox" name="name" value="%d" data-slug="entertainment">Entertainment</label></li>
<li><label><input type="checkbox" name="name" value="%d" data-slug="test">A test</label></li>
<li><label><input type="checkbox" name="name" value="%d" data-slug="third-test">Third</label></li>
</ul>''' % (self.c1.pk, self.c2.pk, self.c3.pk),
        )

    def test_choices_not_fetched_when_not_rendering(self):
        with self.assertNumQueries(1):
            field = forms.ModelChoiceField(Category.objects.order_by('-name'))
            self.assertEqual('Entertainment', field.clean(self.c1.pk).name)

def wrapper(* args, ** kwargs) :
INDENT
    assert max_retries > 0
    x = max_retries
    while x :
    INDENT
        try :
        INDENT
            return func(* args, ** kwargs)
        DEDENT
        except ex :
        INDENT
            x -= 1
        DEDENT
    DEDENT
DEDENT

def is_less(a, b) :
INDENT
    for i in range(len(a) - 1, - 1, - 1) :
    INDENT
        if a [i] < b [i] : return True
        elif a [i] > b [i] : return False
    DEDENT
    return False
DEDENT

def twos_complement(value, bitWidth) :
INDENT
    if value > = 2 ** bitWidth :
    INDENT
        raise ValueError("Value: {} out of range of {}-bit value.".format(value, bitWidth))
    DEDENT
    else :
    INDENT
        return value - int((value < < 1) & 2 ** bitWidth)
    DEDENT
DEDENT

def perm(a, k = 0) :
INDENT
    if k == len(a) :
    INDENT
        print a
    DEDENT
    else :
    INDENT
        for i in xrange(k, len(a)) :
        INDENT
            a [k], a [i] = a [i], a [k]
            perm(a, k + 1)
            a [k], a [i] = a [i], a [k]
        DEDENT
    DEDENT
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

def outer() :
INDENT
    d = {'y' : 0}
    def inner() :
    INDENT
        d ['y'] += 1
        return d ['y']
    DEDENT
    return inner
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    wx.Frame.__init__(self, * args, ** kwargs)
    self.panel = wx.Panel(self)
    self.button = wx.Button(self.panel, label = "Test")
    self.sizer = wx.BoxSizer()
    self.sizer.Add(self.button)
    self.panel.SetSizerAndFit(self.sizer)
    self.Show()
DEDENT

def tail(f, lines = 20) :
INDENT
    total_lines_wanted = lines
    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = - 1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0 :
    INDENT
        if (block_end_byte - BLOCK_SIZE > 0) :
        INDENT
            f.seek(block_number * BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        DEDENT
        else :
        INDENT
            f.seek(0, 0)
            blocks.append(f.read(block_end_byte))
        DEDENT
        lines_found = blocks [- 1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    DEDENT
    all_read_text = ''.join(reversed(blocks))
    return '\n'.join(all_read_text.splitlines() [- total_lines_wanted :])
DEDENT

def myfun(my_list, n, par1 = '') :
INDENT
    new_list = ([my_fun2(i, j) for j in range(n)] for i in range(n))
    if par1 ! = '' :
    INDENT
        new_list = filter(eq(par1), new_list)
    DEDENT
    return list(new_list)
DEDENT

def all_pairs(lst) :
INDENT
    N = len(lst)
    choice_indices = itertools.product(* [
            xrange(k) for k in reversed(xrange(1, N, 2))])
    for choice in choice_indices :
    INDENT
        tmp = lst [:]
        result = []
        for index in choice :
        INDENT
            result.append((tmp.pop(0), tmp.pop(index)))
        DEDENT
        yield result
    DEDENT
DEDENT

def combine_word_documents(files) :
INDENT
    merged_document = Document()
    for index, file in enumerate(files) :
    INDENT
        sub_doc = Document(file)
        if index < len(files) - 1 :
        INDENT
            sub_doc.add_page_break()
        DEDENT
        for element in sub_doc.element.body :
        INDENT
            merged_document.element.body.append(element)
        DEDENT
    DEDENT
    merged_document.save('merged.docx')
DEDENT

    def test_queryset_manager(self):
        f = forms.ModelChoiceField(Category.objects)
        self.assertEqual(len(f.choices), 4)
        self.assertEqual(list(f.choices), [
            ('', '---------'),
            (self.c1.pk, 'Entertainment'),
            (self.c2.pk, 'A test'),
            (self.c3.pk, 'Third'),
        ])

def __new__(metacls, cls, bases, clsdict) :
INDENT
    enum_cls = super(LineMakerMeta, metacls).__new__(cls, bases, clsdict)
    canonical_members = [
        member for name, member in enum_cls.__members__.items()
        if name == member.name
        ]
    last_member = None
    for next_member in canonical_members :
    INDENT
        next_member.length = 0
        if last_member is not None :
        INDENT
            last_member.length = next_member.start - last_member.start
        DEDENT
    DEDENT
DEDENT

def __init__(self) :
INDENT
    wx.Frame.__init__(self, None, - 1, "matplotlib pick_event problem")
    self.plotarea = PlotPanel(self)
    self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
    self.mainSizer.Add(self.plotarea, 1, wx.EXPAND)
    self.SetSizer(self.mainSizer)
    self.mainSizer.Fit(self)
DEDENT

    def test_num_queries(self):
        """
        Widgets that render multiple subwidgets shouldn't make more than one
        database query.
        """
        categories = Category.objects.all()

        class CategoriesForm(forms.Form):
            radio = forms.ModelChoiceField(queryset=categories, widget=forms.RadioSelect)
            checkbox = forms.ModelMultipleChoiceField(queryset=categories, widget=forms.CheckboxSelectMultiple)

        template = Template(
            '{% for widget in form.checkbox %}{{ widget }}{% endfor %}'
            '{% for widget in form.radio %}{{ widget }}{% endfor %}'
        )
        with self.assertNumQueries(2):
            template.render(Context({'form': CategoriesForm()}))
def run(self) :
INDENT
    self.process = subprocess.Popen(self.cmd, stdout = self.outFile, stderr = self.errFile)
    while (self.process.poll() is None and self.timeout > 0) :
    INDENT
        time.sleep(1)
        self.timeout -= 1
    DEDENT
    if not self.timeout > 0 :
    INDENT
        self.process.terminate()
        self.timed_out = True
    DEDENT
    else :
    INDENT
        self.timed_out = False
    DEDENT
DEDENT

def __setitem__(self, key, value) :
INDENT
    if value in self.inverse :
    INDENT
        raise BijectionError(value)
    DEDENT
    self.inverse._set_item(value, key)
    self._set_item(key, value)
DEDENT

def makeArchive(fileList, archive, root) :
INDENT
    a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
    for f in fileList :
    INDENT
        print "archiving file %s" % (f)
        a.write(f, os.path.relpath(f, root))
    DEDENT
    a.close()
DEDENT

def ensure_even(* argvars) :
INDENT
    def fdec(func) :
    INDENT
        def f(* args, ** kwargs) :
        INDENT
            for argvar in argvars :
            INDENT
                try :
                INDENT
                    assert (not args [func.func_code.co_varnames.index(argvar)] % 2)
                DEDENT
                except IndexError :
                INDENT
                    assert (not kwargs [argvar] % 2)
                DEDENT
            DEDENT
            return func(* args, ** kwargs)
        DEDENT
        return f
    DEDENT
    return fdec
DEDENT

def extendedString(string1, string2) :
INDENT
    x = string1
    y = string2
    z = ""
    if len(x) == len(y) :
    INDENT
        return "".join(i for j in zip(string1, string2) for i in j)
    DEDENT
    elif len(x) < len(y) :
    INDENT
        x = x + x [- 1] * (len(y) - len(x))
        return extendedString(x, y)
    DEDENT
    else :
    INDENT
        y = y + y [- 1] * (len(x) - len(y))
        return extendedString(x, y)
    DEDENT
DEDENT

def allpaths(source_node, sink_node, memo_dict = None) :
INDENT
    if memo_dict is None :
    INDENT
        memo_dict = dict()
    DEDENT
    if source_node == sink_node :
    INDENT
        return frozenset([(source_node,)])
    DEDENT
    else :
    INDENT
        pair = (source_node, sink_node)
        if pair in memo_dict :
        INDENT
            return memo_dict [pair]
        DEDENT
        else :
        INDENT
            result = set()
            for new_source in source_node.children :
            INDENT
                paths = allpaths(new_source, sink_node, memo_dict)
                for path in paths :
                INDENT
                    path = (source_node,) + path
                    result.add(path)
                DEDENT
            DEDENT
            result = frozenset(result)
            memo_dict [(source_node, sink_node)] = result
            return result
        DEDENT
    DEDENT
DEDENT

def find_neighbors(tess, points) :
INDENT
    neighbors = {}
    for point in range(points.shape [0]) :
    INDENT
        neighbors [point] = []
    DEDENT
    for simplex in tess.simplices :
    INDENT
        neighbors [simplex [0]] += [simplex [1], simplex [2]]
        neighbors [simplex [1]] += [simplex [2], simplex [0]]
        neighbors [simplex [2]] += [simplex [0], simplex [1]]
    DEDENT
    return neighbors
DEDENT

def search(self, st) :
INDENT
    if self.value == st :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        if not self.children :
        INDENT
            return False
        DEDENT
        else :
        INDENT
            return any(child.search(st) for child in self.children)
        DEDENT
    DEDENT
DEDENT

def quicksort(arr) :
INDENT
    if not arr :
    INDENT
        return []
    DEDENT
    pivots = [x for x in arr if x == arr [0]]
    lesser = quicksort([x for x in arr if x < arr [0]])
    greater = quicksort([x for x in arr if x > arr [0]])
    return lesser + pivots + greater
DEDENT

def fib(n) :
INDENT
    if n == 0 or n == 1 :
    INDENT
        return n, 0
    DEDENT
    else :
    INDENT
        f1, count1 = fib(n - 1)
        f2, count2 = fib(n - 2)
        sum_counts = count1 + count2
        if n == 2 :
        INDENT
            sum_counts = 1
        DEDENT
        return f1 + f2, sum_counts
    DEDENT
DEDENT































































































































































