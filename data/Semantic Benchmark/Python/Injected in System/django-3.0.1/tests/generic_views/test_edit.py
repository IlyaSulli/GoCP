from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.test import SimpleTestCase, TestCase, override_settings
from django.test.client import RequestFactory
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormMixin, ModelFormMixin

from . import views
from .forms import AuthorForm
from .models import Artist, Author


class FormMixinTests(SimpleTestCase):
    request_factory = RequestFactory()

    def test_initial_data(self):
        """ Test instance independence of initial data dict (see #16138) """
        initial_1 = FormMixin().get_initial()
        initial_1['foo'] = 'bar'
        initial_2 = FormMixin().get_initial()
        self.assertNotEqual(initial_1, initial_2)

def draw(self) :
INDENT
    number = random.randint(0, 2 ** 32)
    while number in self.usedNumbers :
    INDENT
        number = random.randint(0, 2 ** 32)
    DEDENT
    self.usedNumbers.append(number)
    return number
DEDENT

def is_sorted(stuff) :
INDENT
    for i in range(1, len(stuff)) :
    INDENT
        if stuff [i - 1] > stuff [i] :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def paren(left, right = None) :
INDENT
    if right is None :
    INDENT
        right = left
    DEDENT
    if left == right == 0 :
    INDENT
        yield ""
    DEDENT
    else :
    INDENT
        if left > 0 :
        INDENT
            for p in paren(left - 1, right) :
            INDENT
                yield "(" + p
            DEDENT
        DEDENT
        if right > left :
        INDENT
            for p in paren(left, right - 1) :
            INDENT
                yield ")" + p
            DEDENT
        DEDENT
    DEDENT
DEDENT

def get_target_path(pth, mtx) :
INDENT
    for level in pth :
    INDENT
        mtx = mtx.get(level, None)
        if mtx is None :
        INDENT
            break
        DEDENT
    DEDENT
    return mtx
DEDENT

    def test_get_prefix(self):
        """ Test prefix can be set (see #18872) """
        test_string = 'test'

        get_request = self.request_factory.get('/')

        class TestFormMixin(FormMixin):
            request = get_request

        default_kwargs = TestFormMixin().get_form_kwargs()
        self.assertIsNone(default_kwargs.get('prefix'))

        set_mixin = TestFormMixin()
        set_mixin.prefix = test_string
        set_kwargs = set_mixin.get_form_kwargs()
        self.assertEqual(test_string, set_kwargs.get('prefix'))

def divisor_function(n) :
INDENT
    "Returns the sum of divisors of n"
    factors = prime_factors(n)
    sum_of_divisors = 1
    count = 0; prev = 0;
    for x in factors :
    INDENT
        if x == prev :
        INDENT
            count += 1
        DEDENT
        else :
        INDENT
            if prev : sum_of_divisors *= (prev ** (count + 1) - 1) / / (prev - 1)
            count = 1; prev = x;
        DEDENT
    DEDENT
    if prev : sum_of_divisors *= (prev ** (count + 1) - 1) / / (prev - 1)
    return sum_of_divisors
DEDENT

    def test_get_form(self):
        class TestFormMixin(FormMixin):
            request = self.request_factory.get('/')

        self.assertIsInstance(
            TestFormMixin().get_form(forms.Form), forms.Form,
            'get_form() should use provided form class.'
        )

        class FormClassTestFormMixin(TestFormMixin):
            form_class = forms.Form

        self.assertIsInstance(
            FormClassTestFormMixin().get_form(), forms.Form,
            'get_form() should fallback to get_form_class() if none is provided.'
        )

def __setitem__(self, key, value) :
INDENT
    if key in self :
    INDENT
        del self [key]
    DEDENT
    if value in self :
    INDENT
        del self [value]
    DEDENT
    dict.__setitem__(self, key, value)
    dict.__setitem__(self, value, key)
DEDENT

def sum67(nums) :
INDENT
    i = 0
    sum = 0
    n = len(nums)
    while i < n :
    INDENT
        if nums [i] == 6 :
        INDENT
            i = nums.index(7, i)
        DEDENT
        else :
        INDENT
            sum += nums [i]
        DEDENT
        i += 1
    DEDENT
    return sum
DEDENT

def nested_sum(a) :
INDENT
    total = 0
    for item in a :
    INDENT
        try :
        INDENT
            total += item
        DEDENT
        except TypeError :
        INDENT
            total += nested_sum(item)
        DEDENT
    DEDENT
    return total
DEDENT

def __init__(self) :
INDENT
    super(Dialog, self).__init__()
    layoutMain = QtGui.QVBoxLayout(self)
    listWidget = QtGui.QListWidget(self)
    gripper = QtGui.QSizeGrip(listWidget)
    l = QtGui.QHBoxLayout(listWidget)
    l.setContentsMargins(0, 0, 0, 0)
    l.addWidget(gripper, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
    layoutMain.addWidget(listWidget)
    layoutMain.addWidget(QtGui.QLabel("Test", self))
    self.setGeometry(200, 500, 200, 500)
DEDENT

def __init__(self, x, y, direction, speed) :
INDENT
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((16, 16))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.direction = math.radians(direction)
    self.speed = speed
DEDENT

def transitive_closure(a) :
INDENT
    closure = set()
    for x, _ in a :
    INDENT
        closure |= set((x, y) for y in dfs(x, a))
    DEDENT
    return closure
DEDENT

    def test_get_context_data(self):
        class FormContext(FormMixin):
            request = self.request_factory.get('/')
            form_class = forms.Form

        self.assertIsInstance(FormContext().get_context_data()['form'], forms.Form)


def sum67(xs) :
INDENT
    xs = iter(xs)
    s = 0
    for x in xs :
    INDENT
        if x == 6 :
        INDENT
            while x ! = 7 :
            INDENT
                x = xs.next()
            DEDENT
        DEDENT
        else :
        INDENT
            s += x
        DEDENT
    DEDENT
    return s
DEDENT

def do_loop(self) :
INDENT
    while true :
    INDENT
        conn = copy(connections [0])
        for line in conn.iter_lines() :
        INDENT
            print line
            if conn ! = connections [0] :
            INDENT
                break
            DEDENT
        DEDENT
    DEDENT
DEDENT

def underscore_to_camelcase(value) :
INDENT
    capitalized_words = [w.capitalize() if w else '_' for w in value.split('_')]
    for i, word in enumerate(capitalized_words) :
    INDENT
        if word ! = '_' :
        INDENT
            capitalized_words [i] = word.lower()
            break
        DEDENT
    DEDENT
    return "".join(capitalized_words)
DEDENT

def tail(f, lines = 1, _buffer = 4098) :
INDENT
    lines_found = []
    block_counter = - 1
    while len(lines_found) < lines :
    INDENT
        try :
        INDENT
            f.seek(block_counter * _buffer, os.SEEK_END)
        DEDENT
        except IOError :
        INDENT
            f.seek(0)
            lines_found = f.readlines()
            break
        DEDENT
        lines_found = f.readlines()
        block_counter -= 1
    DEDENT
    return lines_found [- lines :]
DEDENT

def obj_get(self, request = None, ** kwargs) :
INDENT
    try :
    INDENT
        base_object_list = self.get_object_list(request).filter(** kwargs)
        object_list = self.apply_authorization_limits(request, base_object_list)
        stringified_kwargs = ', '.join(["%s=%s" % (k, v) for k, v in kwargs.items()])
        if len(object_list) < = 0 :
        INDENT
            raise self._meta.object_class.DoesNotExist("Couldn't find an instance of '%s' which matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))
        DEDENT
        elif len(object_list) > 1 :
        INDENT
            raise MultipleObjectsReturned("More than '%s' matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))
        DEDENT
        return object_list [0]
    DEDENT
    except ValueError :
    INDENT
        raise NotFound("Invalid resource lookup data provided (mismatched type).")
    DEDENT
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class BasicFormTests(TestCase):

    def test_post_data(self):
        res = self.client.post('/contact/', {'name': "Me", 'message': "Hello"})
        self.assertRedirects(res, '/list/authors/')

def get_most_ooo_word(words) :
INDENT
    words = words [0].split()
    most = [words [0]]
    for word in words [1 :] :
    INDENT
        if word.count('o') > most [0].count('o') :
        INDENT
            most = [word]
        DEDENT
        elif word.count('o') == most [0].count('o') :
        INDENT
            most.append(word)
        DEDENT
    DEDENT
    return most
DEDENT

def swap(s) :
INDENT
    dct = dict(table)
    dct.update((y, x) for x, y in table)
    return re.sub(
        '|'.join(r'(?:\b%s\b)' % x for x in dct),
        lambda m : dct [m.group(0)],
        s)
DEDENT

def almostIncreasingSequence(sequence) :
INDENT
    for i, x in enumerate(sequence) :
    INDENT
        ret = False
        s = sequence [: i] + sequence [i + 1 :]
        for j, y in enumerate(s [1 :]) :
        INDENT
            if s [j + 1] < = s [j] :
            INDENT
                ret = True
                break
            DEDENT
            if ret :
            INDENT
                break
            DEDENT
        DEDENT
        if not ret :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
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

def __setattr__(self, name, value) :
INDENT
    if name not in self._allowed_attrs :
    INDENT
        raise AttributeError(
            "Cannot set attribute {!r} on type {}".format(
                name, self.__class__.__name__))
    DEDENT
    super(RestrictedAttributesObject, self).__setattr__(name, value)
DEDENT

def chunks(iterable, chunk_size) :
INDENT
    i = 0;
    while i < len(iterable) :
    INDENT
        yield iterable [i : i + chunk_size]
        i += chunk_size
    DEDENT
DEDENT

    def test_late_form_validation(self):
        """
        A form can be marked invalid in the form_valid() method (#25548).
        """
        res = self.client.post('/late-validation/', {'name': "Me", 'message': "Hello"})
        self.assertFalse(res.context['form'].is_valid())


def json_scan(json_obj, key) :
INDENT
    d = json.loads(json_obj)
    def _(dictobj, lookup) :
    INDENT
        if lookup in dictobj.keys() :
        INDENT
            return dictobj [lookup]
        DEDENT
        else :
        INDENT
            for sub_dictobj in [d for d in dictobj.values() if type(d) == DictType] :
            INDENT
                result = _(sub_dictobj, lookup)
                if result :
                INDENT
                    return result
                DEDENT
            DEDENT
            for listobject in [l for l in dictobj.values() if type(d) == list] :
            INDENT
                for sub_dictobj in [d for d in listobject if type(d) == DictType] :
                INDENT
                    result = _(sub_dictobj, lookup)
                    if result :
                    INDENT
                        return result
                    DEDENT
                DEDENT
            DEDENT
            return None
        DEDENT
    DEDENT
    return _(d, key)
DEDENT

def __new__(mcs, name, bases, dict) :
INDENT
    def add_op(op) :
    INDENT
        if op in dict :
        INDENT
            return
        DEDENT
        fn = lambda self, * args : self.__op__(op, args)
        fn.__name__ = op
        dict [op] = fn
    DEDENT
    for op in mcs.__ops :
    INDENT
        add_op(op)
    DEDENT
    return type.__new__(mcs, name, bases, dict)
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

def enum(typename, field_names) :
INDENT
    "Create a new enumeration type"
    if isinstance(field_names, str) :
    INDENT
        field_names = field_names.replace(',', ' ').split()
    DEDENT
    d = dict((reversed(nv) for nv in enumerate(field_names)), __slots__ = ())
    return type(typename, (object,), d)()
DEDENT

def enum(typename, field_names) :
INDENT
    "Create a new enumeration type"
    if isinstance(field_names, str) :
    INDENT
        field_names = field_names.replace(',', ' ').split()
    DEDENT
    d = dict((reversed(nv) for nv in enumerate(field_names)), __slots__ = ())
    return type(typename, (object,), d)()
DEDENT

def remove_adjacent(nums) :
INDENT
    result = []
    if len(nums) > 0 :
    INDENT
        result = [nums [0]]
        for i in range(len(nums) - 1) :
        INDENT
            if nums [i] ! = nums [i + 1] :
            INDENT
                result.append(nums [i + 1])
            DEDENT
        DEDENT
    DEDENT
    return result
DEDENT

def emit(self, record) :
INDENT
    stream = self.stream
    try :
    INDENT
        msg = self.format(record, stream.isatty())
        stream.write(msg)
        stream.write(self.terminator)
        self.flush()
    DEDENT
    except Exception :
    INDENT
        self.handleError(record)
    DEDENT
DEDENT

class ModelFormMixinTests(SimpleTestCase):
    def test_get_form(self):
        form_class = views.AuthorGetQuerySetFormView().get_form_class()
        self.assertEqual(form_class._meta.model, Author)

def get_most_ooo_word(lines) :
INDENT
    k = - 1
    most_o = []
    for line in lines :
    INDENT
        phrase_words = line.split()
        for word in phrase_words :
        INDENT
            c = word.count('o')
            if c > k :
            INDENT
                k = c
                most_o = [word]
            DEDENT
            elif c == k :
            INDENT
                most_o.append(word)
            DEDENT
        DEDENT
    DEDENT
    return most_o
DEDENT

def rep_str(s, x, y) :
INDENT
    while x in s :
    INDENT
        s = s [: s.index(x)] + y + s [s.index(x) + len(x) :]
    DEDENT
    return s
DEDENT

def urls() :
INDENT
    urls = []
    titles = []
    counts = []
    last = []
    conn = sqlite3.connect('C:\Users\username\Desktop\History.sql')
    cursor = conn.execute("SELECT url, title, visit_count, last_visit_time from urls")
    for row in cursor :
    INDENT
        urls.append(row [0])
        titles.append(row [1])
        counts.append(row [2])
        last.append(row [3])
    DEDENT
    df = pandas.DataFrame({'URL' : urls,
            'Title' : titles,
            'Visit Count' : counts,
            'Last visit Time' : last})
    df.to_csv('historyulrs.csv', encoding = 'utf-8', index = False)
    conn.close()
DEDENT

def merge_lists(h1, h2) :
INDENT
    if h1 is None :
    INDENT
        return h2
    DEDENT
    if h2 is None :
    INDENT
        return h1
    DEDENT
    if (h1.value < h2.value) :
    INDENT
        h1.next = merge_lists(h1.next, h2)
        return h1
    DEDENT
    else :
    INDENT
        h2.next = merge_lists(h2.next, h1)
        return h2
    DEDENT
DEDENT

def __init__(self) :
INDENT
    self.secondsRemaining = 10.0
    self.lastTick = 0
    self.isPaused = False
    self.isRunning = False
    self.keepGoing = True
DEDENT

    def test_get_form_checks_for_object(self):
        mixin = ModelFormMixin()
        mixin.request = RequestFactory().get('/')
        self.assertEqual({'initial': {}, 'prefix': None},
                         mixin.get_form_kwargs())


def tone(self, frequency, length = 1000, play = False, ** kwargs) :
INDENT
    number_of_frames = int(self.bitrate * length / 1000.)
    phInc = 2 * math.pi * frequency / self.bitrate
    for x in xrange(number_of_frames) :
    INDENT
        y = math.sin(self._phase)
        _phase += phaseInc;
        self._queue.append(chr(int(y)))
    DEDENT
DEDENT

def extendedString(string1, string2) :
INDENT
    if len(string1) == len(string2) :
    INDENT
        return "".join(i for j in zip(string1, string2) for i in j)
    DEDENT
    else :
    INDENT
        longer, shorter = (string1, string2) if len(string1) > len(string2) else (string2, string1)
        shorter = shorter + shorter [- 1] * (len(longer) - len(shorter))
        return "".join(i for j in zip(shorter, longer) for i in j)
    DEDENT
DEDENT

def permutations(orig_list) :
INDENT
    if not isinstance(orig_list, list) :
    INDENT
        orig_list = list(orig_list)
    DEDENT
    yield orig_list
    if len(orig_list) == 1 :
    INDENT
        return
    DEDENT
    for n in sorted(orig_list) :
    INDENT
        new_list = orig_list [:]
        pos = new_list.index(n)
        del (new_list [pos])
        new_list.insert(0, n)
        for resto in permutations(new_list [1 :]) :
        INDENT
            if new_list [: 1] + resto < > orig_list :
            INDENT
                yield new_list [: 1] + resto
            DEDENT
        DEDENT
    DEDENT
DEDENT

def fib(n) :
INDENT
    if n == 1 :
    INDENT
        return 1
    DEDENT
    elif n == 0 :
    INDENT
        return 0
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

def run(self) :
INDENT
    print '>>>> abuse generator as context manager'
    for driver in self.drivergenerator(self.driverfactory) :
    INDENT
        self.dostuff(driver)
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

def checkLen() :
INDENT
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if "Monday" in days :
    INDENT
        print "found"
        print days.index("Monday")
    DEDENT
DEDENT

def access(obj, indexes) :
INDENT
    def _get_item(subobj, index) :
    INDENT
        if isinstance(subobj, list) and index < len(subobj) :
        INDENT
            return subobj [index]
        DEDENT
        return None
    DEDENT
    return reduce(_get_item, indexes, obj)
DEDENT

def execute(cmdArray, workingDir) :
INDENT
    stdout = ''
    stderr = ''
    try :
    INDENT
        try :
        INDENT
            process = subprocess.Popen(cmdArray, cwd = workingDir, stdout = subprocess.PIPE, stderr = subprocess.PIPE, bufsize = 1)
        DEDENT
        except OSError :
        INDENT
            return [False, '', 'ERROR : command(' + ' '.join(cmdArray) + ') could not get executed!']
        DEDENT
        for line in iter(process.stdout.readline, b'') :
        INDENT
            try :
            INDENT
                echoLine = line.decode("utf-8")
            DEDENT
            except :
            INDENT
                echoLine = str(line)
            DEDENT
            stdout += echoLine
        DEDENT
        for line in iter(process.stderr.readline, b'') :
        INDENT
            try :
            INDENT
                echoLine = line.decode("utf-8")
            DEDENT
            except :
            INDENT
                echoLine = str(line)
            DEDENT
            stderr += echoLine
        DEDENT
    DEDENT
    except (KeyboardInterrupt, SystemExit) as err :
    INDENT
        return [False, '', str(err)]
    DEDENT
    process.stdout.close()
    returnCode = process.wait()
    if returnCode ! = 0 or stderr ! = '' :
    INDENT
        return [False, stdout, stderr]
    DEDENT
    else :
    INDENT
        return [True, stdout, stderr]
    DEDENT
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class CreateViewTests(TestCase):

    def test_create(self):
        res = self.client.get('/edit/authors/create/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['form'], forms.ModelForm)
        self.assertIsInstance(res.context['view'], View)
        self.assertNotIn('object', res.context)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/author_form.html')

        res = self.client.post('/edit/authors/create/', {'name': 'Randall Munroe', 'slug': 'randall-munroe'})
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe>'])

def __init__(self, a = None, b = None, e = None, f = None) :
INDENT
    if [a, b, e, f].count(None) > 2 :
    INDENT
        raise Exception('Not enough parameters to make an ellipse')
    DEDENT
    self.a, self.b, self.e, self.f = a, b, e, f
    self.calculate_a()
    for parameter in 'b', 'e', 'f' :
    INDENT
        if self.__dict__ [parameter] is None :
        INDENT
            Ellipse.__dict__ ['calculate_' + parameter](self)
        DEDENT
    DEDENT
DEDENT

def merge(* sortedlists) :
INDENT
    iterlist = [[i, i.next()] for i in [iter(j) for j in sortedlists]]
    iterlist.sort(key = lambda x : x [1])
    def reorder(iterlist, i) :
    INDENT
        if i == len(iterlist) or iterlist [0] [1] < iterlist [i] [1] :
        INDENT
            iterlist.insert(i - 1, iterlist.pop(0))
        DEDENT
        else :
        INDENT
            reorder(iterlist, i + 1)
        DEDENT
    DEDENT
    while True :
    INDENT
        if len(iterlist) :
        INDENT
            if len(iterlist) > 1 and iterlist [0] [1] > iterlist [1] [1] :
            INDENT
                reorder(iterlist, 1)
            DEDENT
            yield iterlist [0] [1]
            try :
            INDENT
                iterlist [0] [1] = iterlist [0] [0].next()
            DEDENT
            except StopIteration :
            INDENT
                del iterlist [0]
            DEDENT
        DEDENT
        else :
        INDENT
            break
        DEDENT
    DEDENT
DEDENT

def __init__(self, guide, * args, ** kwargs) :
INDENT
    self.guide = guide
    super(ChecklistForm, self).__init__(* args, ** kwargs)
    new_fields = OrderedDict()
    for tier, tasks in guide.tiers().items() :
    INDENT
        questions = [(t ['task'], t ['question']) for t in tasks if 'question' in t]
        new_fields [tier.lower()] = forms.MultipleChoiceField(
            label = tier,
            widget = forms.CheckboxSelectMultiple(),
            choices = questions,
            help_text = 'desired set of site features')
    DEDENT
    new_fields ['name'] = self.fields ['name']
    new_fields ['email'] = self.fields ['email']
    new_fields ['website'] = self.fields ['website']
    self.fields = new_fields
DEDENT

def __init__(self, action, min = allMatch, hour = allMatch,
day = allMatch, month = allMatch, dow = allMatch,
args = (), kwargs = {}) :
INDENT
    self.mins = conv_to_set(min)
    self.hours = conv_to_set(hour)
    self.days = conv_to_set(day)
    self.months = conv_to_set(month)
    self.dow = conv_to_set(dow)
    self.action = action
    self.args = args
    self.kwargs = kwargs
DEDENT

def tail(f, lines = 1, _buffer = 4098) :
INDENT
    lines_found = []
    block_counter = - 1
    while len(lines_found) < lines :
    INDENT
        try :
        INDENT
            f.seek(block_counter * _buffer, os.SEEK_END)
        DEDENT
        except IOError :
        INDENT
            f.seek(0)
            lines_found = f.readlines()
            break
        DEDENT
        lines_found = f.readlines()
        block_counter -= 1
    DEDENT
    return lines_found [- lines :]
DEDENT

def decorator_factory(value) :
INDENT
    def msg_decorator(f) :
    INDENT
        def inner_dec(* args, ** kwargs) :
        INDENT
            res = f(value, * args, ** kwargs)
            return res
        DEDENT
        inner_dec.__name__ = f.__name__
        inner_dec.__doc__ = f.__doc__
        return inner_dec
    DEDENT
    return msg_decorator
DEDENT

def emit(self, record) :
INDENT
    if record.exc_info :
    INDENT
        record.exc_text = self.formatException(record.exc_info)
        record.exc_info = None
    DEDENT
    self.queue.put(record)
DEDENT

    def test_create_invalid(self):
        res = self.client.post('/edit/authors/create/', {'name': 'A' * 101, 'slug': 'randall-munroe'})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_form.html')
        self.assertEqual(len(res.context['form'].errors), 1)
        self.assertEqual(Author.objects.count(), 0)

def compare(A, B) :
INDENT
    same = True
    for i, (a, b) in enumerate(zip(A, B)) :
    INDENT
        if same and a ! = b :
        INDENT
            same = False
            n = i
            firstval = a
        DEDENT
        elif (not same) and (a == b or b == firstval) :
        INDENT
            m = i
            break
        DEDENT
    DEDENT
    origin = A [n : m]
    if n == 0 :
    INDENT
        dest = A [- m :]
        B_expect = dest + A [m : - m] + origin
    DEDENT
    else :
    INDENT
        dest = A [- m : - n]
        B_expect = A [: n] + dest + A [m : - m] + origin + A [- n :]
    DEDENT
    return bool(B_expect == B)
DEDENT

def __init__(self, t) :
INDENT
    self.i = Tkinter.PhotoImage(width = 100, height = 100)
    colors = [[random.randint(0, 255) for i in range(0, 3)] for j in range(0, 10000)]
    row = 0; col = 0
    for color in colors :
    INDENT
        self.i.put('#%02x%02x%02x' % tuple(color), (row, col))
        col += 1
        if col == 100 :
        INDENT
            row += 1; col = 0
        DEDENT
    DEDENT
    c = Tkinter.Canvas(t, width = 100, height = 100); c.pack()
    c.create_image(0, 0, image = self.i, anchor = Tkinter.NW)
DEDENT

def run(self) :
INDENT
    app = QtGui.QApplication([])
    window = QtGui.QWidget()
    layout = QtGui.QVBoxLayout(window)
    button = QtGui.QPushButton('Test')
    button.clicked.connect(self.print_something)
    layout.addWidget(button)
    window.show()
    t = Thread(target = self.listen, args = (app,))
    t.start()
    app.exec_()
DEDENT

def transpose(matrix) :
INDENT
    li = []
    for i in range(len(matrix)) :
    INDENT
        inner_li = []
        for sets in matrix :
        INDENT
            inner_li.append(sets [i])
        DEDENT
        li.append(inner_li)
    DEDENT
    return li
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

def fib() :
INDENT
    a, b = 1, 1
    num = eval(input("Please input what Fib number you want to be calculated: "))
    num_int = int(num - 2)
    for i in range(num_int) :
    INDENT
        a, b = b, a + b
    DEDENT
    print (b)
DEDENT

def __init__(self) :
INDENT
    QMainWindow.__init__(self)
    self.toolBar = self.addToolBar("Toolbar")
    self.toolBar.addAction(QAction('Add Task', self, triggered = self.addTask))
    self.table = QTableWidget()
    self.table.verticalHeader().hide()
    self.table.setColumnCount(2)
    self.setCentralWidget(self.table)
    self.queue = multiprocessing.Queue()
    self.pool = multiprocessing.Pool(processes = 4, initializer = pool_init, initargs = (self.queue,))
    self.timer = QTimer()
    self.timer.timeout.connect(self.updateProgress)
    self.timer.start(2000)
DEDENT

    def test_create_with_object_url(self):
        res = self.client.post('/edit/artists/create/', {'name': 'Rene Magritte'})
        self.assertEqual(res.status_code, 302)
        artist = Artist.objects.get(name='Rene Magritte')
        self.assertRedirects(res, '/detail/artist/%d/' % artist.pk)
        self.assertQuerysetEqual(Artist.objects.all(), ['<Artist: Rene Magritte>'])

def __init__(self, * args, ** kw) :
INDENT
    wx.Frame.__init__(self, * args, ** kw)
    self.list = wx.ListCtrl(self, style = wx.LC_REPORT)
    items = ['A', 'b', 'something really REALLY long']
    self.list.InsertColumn(0, "AAAAAAAAAAAAAAAAAAAAAAAA")
    for item in items :
    INDENT
        self.list.InsertStringItem(0, item)
    DEDENT
    self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
    a = self.list.GetColumnWidth(0)
    print "a " + str(a)
    self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
    b = self.list.GetColumnWidth(0)
    print "b " + str(b)
    if a > b :
    INDENT
        print "a is bigger"
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
    DEDENT
DEDENT

def spiral(inp) :
INDENT
    width = int(ceil(sqrt(len(inp))))
    result = square(width)
    x = width / / 2
    y = width / / 2
    for value, movement in izip(inp, spiral_movements()) :
    INDENT
        result [y] [x] = value
        dx, dy = movement
        x += dx
        y += dy
    DEDENT
    return result
DEDENT

def factorial(n) :
INDENT
    if n == 0 :
    INDENT
        return 1
    DEDENT
    else :
    INDENT
        return n * factorial(n - 1)
    DEDENT
DEDENT

def reverse(text) :
INDENT
    reversed_text = ""
    for n in range(len(text)) :
    INDENT
        reversed_text += text [- 1 - n]
    DEDENT
    return reversed_text
DEDENT

    def test_create_with_redirect(self):
        res = self.client.post('/edit/authors/create/redirect/', {'name': 'Randall Munroe', 'slug': 'randall-munroe'})
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/edit/authors/create/')
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe>'])

def setup(self) :
INDENT
    import os
    self.fixture_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        "/fixtures/")
    assert os.access(self.fixture_dir, os.F_OK), "Oops! the fixture dir should be here: '%s'" % self.fixture_dir
    assert os.access(os.path.join(self.fixture_dir,
            "profiles-source1.csv"), os.F_OK)
DEDENT

def wrapper(* args, ** kwargs) :
INDENT
    saved_stdout = sys.stdout
    sys.stdout = cStringIO.StringIO()
    try :
    INDENT
        out = func(* args, ** kwargs)
        if returns_output :
        INDENT
            out = sys.stdout.getvalue().strip().split()
        DEDENT
    DEDENT
    finally :
    INDENT
        sys.stdout = saved_stdout
    DEDENT
    return out
DEDENT

def get_data(self) :
INDENT
    k = ''
    while True :
    INDENT
        c = timeout_call(sys.stdin.read, args = [1], timeout_duration = 0.05)
        if c is None :
        INDENT
            break
        DEDENT
        k += c
    DEDENT
    return k if k else False
DEDENT

def formatTime(self, record, datefmt = None) :
INDENT
    arrow_time = Arrow.fromtimestamp(record.created)
    if datefmt :
    INDENT
        arrow_time = arrow_time.format(datefmt)
    DEDENT
    return str(arrow_time)
DEDENT

def __next__(self) :
INDENT
    try :
    INDENT
        return next(self.__iter)
    DEDENT
    except StopIteration :
    INDENT
        self.__iter = None
        raise
    DEDENT
DEDENT

def merge(dict1, dict2) :
INDENT
    for k in dict1.keys() - dict2.keys() :
    INDENT
        yield (k, dict1 [k])
    DEDENT
    for k in dict2.keys() - dict1.keys() :
    INDENT
        yield (k, dict2 [k])
    DEDENT
    for k in dict1.keys() & dict2.keys() :
    INDENT
        yield (k, dict(merge(dict1 [k], dict2 [k])))
    DEDENT
DEDENT

def format(self, record) :
INDENT
    levelname = record.levelname
    if self.use_color and levelname in COLORS :
    INDENT
        levelname_color = COLOR_SEQ % (30 + COLORS [levelname]) + levelname + RESET_SEQ
        record.levelname = levelname_color
    DEDENT
    return logging.Formatter.format(self, record)
DEDENT

def foo(s) :
INDENT
    def foo_helper(level = 0) :
    INDENT
        try :
        INDENT
            token = next(tokens)
        DEDENT
        except StopIteration :
        INDENT
            if level ! = 0 :
            INDENT
                raise Exception('missing closing paren')
            DEDENT
            else :
            INDENT
                return []
            DEDENT
        DEDENT
        if token == ')' :
        INDENT
            if level == 0 :
            INDENT
                raise Exception('missing opening paren')
            DEDENT
            else :
            INDENT
                return []
            DEDENT
        DEDENT
        elif token == '(' :
        INDENT
            return [foo_helper(level + 1)] + foo_helper(level)
        DEDENT
        else :
        INDENT
            return [token] + foo_helper(level)
        DEDENT
    DEDENT
    tokens = iter(s)
    return foo_helper()
DEDENT

    def test_create_with_interpolated_redirect(self):
        res = self.client.post(
            '/edit/authors/create/interpolate_redirect/',
            {'name': 'Randall Munroe', 'slug': 'randall-munroe'}
        )
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe>'])
        self.assertEqual(res.status_code, 302)
        pk = Author.objects.first().pk
        self.assertRedirects(res, '/edit/author/%d/update/' % pk)
        # Also test with escaped chars in URL
        res = self.client.post(
            '/edit/authors/create/interpolate_redirect_nonascii/',
            {'name': 'John Doe', 'slug': 'john-doe'}
        )
        self.assertEqual(res.status_code, 302)
        pk = Author.objects.get(name='John Doe').pk
        self.assertRedirects(res, '/%C3%A9dit/author/{}/update/'.format(pk))

def chunks(l, n) :
INDENT
    newn = int(1.0 * len(l) / n + 0.5)
    for i in xrange(0, n - 1) :
    INDENT
        yield l [i * newn : i * newn + newn]
    DEDENT
    yield l [n * newn - newn :]
DEDENT

def num_input(prompt, error) :
INDENT
    s = raw_input(prompt)
    for t in (int, float, complex) :
    INDENT
        try : return t(s)
        except ValueError : pass
    DEDENT
    print error
    return num_input(prompt, error)
DEDENT

def parse(self, response) :
INDENT
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//div[@id="col_3"]//div[@id="module3_1"]//div[@id="moduleData4952"]')
    items = []
    for site in sites :
    INDENT
        item = MlboddsItem()
        item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
        item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c4"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c6"]//text()').extract()
        items.append(item)
    DEDENT
    return items
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

    def test_create_with_special_properties(self):
        res = self.client.get('/edit/authors/create/special/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['form'], views.AuthorForm)
        self.assertNotIn('object', res.context)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/form.html')

        res = self.client.post('/edit/authors/create/special/', {'name': 'Randall Munroe', 'slug': 'randall-munroe'})
        self.assertEqual(res.status_code, 302)
        obj = Author.objects.get(slug='randall-munroe')
        self.assertRedirects(res, reverse('author_detail', kwargs={'pk': obj.pk}))
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe>'])

def num_input(prompt, error) :
INDENT
    while True :
    INDENT
        result = raw_input(prompt)
        for candidate in (int, float) :
        INDENT
            try : return candidate(result)
            except ValueError : pass
        DEDENT
        print error
    DEDENT
DEDENT

def nindex(haystack, needle, nrep = 1, _memo = {}) :
INDENT
    if nrep < 1 :
    INDENT
        raise ValueError('%r < 1' % (nrep,))
    DEDENT
    k = needle, haystack
    if k in _memo :
    INDENT
        where = _memo [k]
    DEDENT
    else :
    INDENT
        where = _memo [k] = [- 1]
    DEDENT
    while len(where) < = nrep :
    INDENT
        if where [- 1] is None :
        INDENT
            return - 1
        DEDENT
        w = haystack.find(needle, where [- 1] + 1)
        if w < 0 :
        INDENT
            where.append(None)
            return - 1
        DEDENT
        where.append(w)
    DEDENT
    return where [nrep]
DEDENT

def pop(self, ind = - 1) :
INDENT
    try :
    INDENT
        obj = list.__getitem__(self, ind)
    DEDENT
    except (IndexError, TypeError) :
    INDENT
        obj = self._index [ind]
        ind = list.index(self, obj)
    DEDENT
    self._delindex(obj)
    return list.pop(self, ind)
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

    def test_create_without_redirect(self):
        msg = (
            'No URL to redirect to.  Either provide a url or define a '
            'get_absolute_url method on the Model.'
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.post('/edit/authors/create/naive/', {'name': 'Randall Munroe', 'slug': 'randall-munroe'})

def countSubStringMatchRecursive(target, key) :
INDENT
    def countit(target, key, count) :
    INDENT
        index = find(target, key)
        if index > = 0 :
        INDENT
            target = target [index + len(key) :]
            count += countit(target, key, count) + 1
        DEDENT
        return count
    DEDENT
    return "No. of instances of", key, 'in', target, 'is', countit(target, key, 0)
DEDENT

    def test_create_restricted(self):
        res = self.client.post(
            '/edit/authors/create/restricted/',
            {'name': 'Randall Munroe', 'slug': 'randall-munroe'}
        )
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/accounts/login/?next=/edit/authors/create/restricted/')

def fib(k) :
INDENT
    a1, b1 = rootipower(1, 1, 5, k)
    a2, b2 = rootipower(1, - 1, 5, k)
    a = a1 - a2
    b = b1 - b2
    a, b = rootiply(0, 1, a, b, 5)
    assert b == 0
    return a / 2 ** k / 5
DEDENT

def permute(xs, low = 0) :
INDENT
    if low + 1 > = len(xs) :
    INDENT
        yield xs
    DEDENT
    else :
    INDENT
        for p in permute(xs, low + 1) :
        INDENT
            yield p
        DEDENT
        for i in range(low + 1, len(xs)) :
        INDENT
            xs [low], xs [i] = xs [i], xs [low]
            for p in permute(xs, low + 1) :
            INDENT
                yield p
            DEDENT
            xs [low], xs [i] = xs [i], xs [low]
        DEDENT
    DEDENT
DEDENT

    def test_create_view_with_restricted_fields(self):

        class MyCreateView(CreateView):
            model = Author
            fields = ['name']

        self.assertEqual(list(MyCreateView().get_form_class().base_fields), ['name'])

def pairsum_n(list1, value) :
INDENT
    result = set()
    for n in combinations(list1, 2) :
    INDENT
        if sum(n) == value :
        INDENT
            result.add((min(n), max(n)))
        DEDENT
    DEDENT
    return list(result)
DEDENT

    def test_create_view_all_fields(self):
        class MyCreateView(CreateView):
            model = Author
            fields = '__all__'

        self.assertEqual(list(MyCreateView().get_form_class().base_fields), ['name', 'slug'])

def __init__(self, parent = None) :
INDENT
    super(Test, self).__init__(parent)
    self.pushButton = QtGui.QPushButton('I am in Test widget')
    layout = QtGui.QHBoxLayout()
    layout.addWidget(self.pushButton)
    self.setLayout(layout)
DEDENT

def backwalk(predecessor_map, start, origin) :
INDENT
    def deffered_output() :
    INDENT
        for i in output :
        INDENT
            yield i
        DEDENT
    DEDENT
    result, a = tee(deffered_output())
    b = imap(predecessor_map.get, a)
    output = takewhile(lambda x : x ! = origin, chain([start], b))
    return result
DEDENT

    def test_create_view_without_explicit_fields(self):
        class MyCreateView(CreateView):
            model = Author

        message = (
            "Using ModelFormMixin (base class of MyCreateView) without the "
            "'fields' attribute is prohibited."
        )
        with self.assertRaisesMessage(ImproperlyConfigured, message):
            MyCreateView().get_form_class()

def getdetails(p) :
INDENT
    req_val = identifiers.get(p)
    if not req_val :
    INDENT
        for key, value in identifiers.items() :
        INDENT
            req_val = value ['subid'].get(p)
        DEDENT
    DEDENT
    return req_val
DEDENT

def update_url(self) :
INDENT
    for url in self :
    INDENT
        url_obj = url._get_url()
        url_obj.write({
                'name' : url.url1,
                'url_seniat' : url.url2,
                'url_seniat2' : url.url3})
    DEDENT
    return {}
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

def cartesian_product(* X) :
INDENT
    if len(X) == 1 :
    INDENT
        return [(x0,) for x0 in X [0]]
    DEDENT
    else :
    INDENT
        return [(x0,) + t1 for x0 in X [0] for t1 in cartesian_product(* X [1 :])]
    DEDENT
DEDENT

def convert(X, Y) :
INDENT
    new_dict = {}
    for x_key, x_value in X.items() :
    INDENT
        for y_key, y_value in Y.items() :
        INDENT
            if x_key == y_key :
            INDENT
                new_dict [y_value] = x_value
            DEDENT
        DEDENT
    DEDENT
    return new_dict
DEDENT

    def test_define_both_fields_and_form_class(self):
        class MyCreateView(CreateView):
            model = Author
            form_class = AuthorForm
            fields = ['name']

        message = "Specifying both 'fields' and 'form_class' is not permitted."
        with self.assertRaisesMessage(ImproperlyConfigured, message):
            MyCreateView().get_form_class()


def Activer(request, produit_id) :
INDENT
    produit = Produit.objects.get(pk = produit_id)
    if produit.user.id == request.user.id :
    INDENT
        produit.etat = "active"
        produit.save()
        return JsonResponse({'success' : True})
    DEDENT
    else :
    INDENT
        return JsonResponse({'error' : 'You are not allowed to edit this product.'})
    DEDENT
DEDENT

def change_keys(obj, convert) :
INDENT
    if isinstance(obj, (str, int, float)) :
    INDENT
        return obj
    DEDENT
    if isinstance(obj, dict) :
    INDENT
        new = obj.__class__()
        for k, v in obj.items() :
        INDENT
            new [convert(k)] = change_keys(v, convert)
        DEDENT
    DEDENT
    elif isinstance(obj, (list, set, tuple)) :
    INDENT
        new = obj.__class__(change_keys(v, convert) for v in obj)
    DEDENT
    else :
    INDENT
        return obj
    DEDENT
    return new
DEDENT

def brute_force() :
INDENT
    for length in range(min_length, max_length + 1) :
    INDENT
        for p in product(chars, repeat = length) :
        INDENT
            guess = ''.join(p)
            if guess == password :
            INDENT
                return guess
            DEDENT
        DEDENT
    DEDENT
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class UpdateViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            pk=1,  # Required for OneAuthorUpdate.
            name='Randall Munroe',
            slug='randall-munroe',
        )

def __init__(self) :
INDENT
    wx.Frame.__init__(self, None, - 1, "Test", size = (500, 270))
    panel = wx.Panel(self, - 1)
    self.buttonStart = wx.Button(panel, - 1, label = "Start timer", pos = (0, 0))
    self.buttonChange = wx.Button(panel, - 1, label = "Change var", pos = (0, 30))
    panel.Bind(wx.EVT_BUTTON, self.startTimer, id = self.buttonStart.GetId())
    panel.Bind(wx.EVT_BUTTON, self.changeVar, id = self.buttonChange.GetId())
    self.value = 1
    self.timer = wx.Timer(self)
    self.Bind(wx.EVT_TIMER, self.printer, self.timer)
DEDENT

def find_neighbors(pindex, triang) :
INDENT
    neighbors = list()
    for simplex in triang.vertices :
    INDENT
        if pindex in simplex :
        INDENT
            neighbors.extend([simplex [i] for i in range(len(simplex)) if simplex [i] ! = pindex])
            '''
            this is a one liner for if a simplex contains the point we`re interested in,
            extend the neighbors list by appending all the *other* point indices in the simplex
            '''
        DEDENT
    DEDENT
    return list(set(neighbors))
DEDENT

def reverseParentheses(s) :
INDENT
    assert '(' in s and ')' in s
    while '(' in s :
    INDENT
        reverseParentheses(s)
    DEDENT
    return s
DEDENT

    def test_update_post(self):
        res = self.client.get('/edit/author/%d/update/' % self.author.pk)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['form'], forms.ModelForm)
        self.assertEqual(res.context['object'], self.author)
        self.assertEqual(res.context['author'], self.author)
        self.assertTemplateUsed(res, 'generic_views/author_form.html')
        self.assertEqual(res.context['view'].get_form_called_count, 1)

        # Modification with both POST and PUT (browser compatible)
        res = self.client.post(
            '/edit/author/%d/update/' % self.author.pk,
            {'name': 'Randall Munroe (xkcd)', 'slug': 'randall-munroe'}
        )
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe (xkcd)>'])

def seriesrun(x, n) :
INDENT
    power = 0
    s = 0
    while power < n :
    INDENT
        s += (- x) ** power
        power += 1
    DEDENT
    return s
DEDENT

def run(self) :
INDENT
    while True :
    INDENT
        events = self.__poll.poll(self.__to)
        for fd, ev in events :
        INDENT
            if (ev & self.__evt) ! = self.__evt :
            INDENT
                continue
            DEDENT
            try :
            INDENT
                self.__fds [fd].run()
            DEDENT
            except Exception, e :
            INDENT
                print e
            DEDENT
        DEDENT
    DEDENT
DEDENT

def mail(to, subject, text, attach) :
INDENT
    msg = MIMEMultipart()
    msg ['From'] = gmail_user
    msg ['To'] = ", ".join(recipients)
    msg ['Subject'] = subject
    msg.attach(MIMEText(text))
    for file in filenames :
    INDENT
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
        msg.attach(part)
    DEDENT
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()
DEDENT

def __getitem__(self, item) :
INDENT
    if isinstance(item, slice) :
    INDENT
        if item.step is None :
        INDENT
            return list(range(item.start, item.stop))
        DEDENT
        return list(range(item.start, item.stop, item.step))
    DEDENT
DEDENT

    def test_update_invalid(self):
        res = self.client.post(
            '/edit/author/%d/update/' % self.author.pk,
            {'name': 'A' * 101, 'slug': 'randall-munroe'}
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_form.html')
        self.assertEqual(len(res.context['form'].errors), 1)
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe>'])
        self.assertEqual(res.context['view'].get_form_called_count, 1)

def insertionSort(L, reverse = False) :
INDENT
    lt = operator.gt if reverse else operator.lt
    for j in xrange(1, len(L)) :
    INDENT
        valToInsert = L [j]
        i = j - 1
        while 0 < = i and lt(valToInsert, L [i]) :
        INDENT
            L [i + 1] = L [i]
            i -= 1
        DEDENT
        L [i + 1] = valToInsert
    DEDENT
    return L
DEDENT

def access(obj, indexes) :
INDENT
    a = obj
    for i in indexes :
    INDENT
        try :
        INDENT
            a = a [i]
        DEDENT
        except IndexError :
        INDENT
            return None
        DEDENT
    DEDENT
    return a
DEDENT

    def test_update_with_object_url(self):
        a = Artist.objects.create(name='Rene Magritte')
        res = self.client.post('/edit/artists/%d/update/' % a.pk, {'name': 'Rene Magritte'})
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/detail/artist/%d/' % a.pk)
        self.assertQuerysetEqual(Artist.objects.all(), ['<Artist: Rene Magritte>'])

def __init__(self, parent) :
INDENT
    super(AppRemovalPage, self).__init__(parent)
    self.setTitle('Apps to Remove')
    self.setSubTitle('Listview')
    self.list_view = QListView(self)
    self.list_view.setMinimumSize(465, 200)
    self.isWritten = False
    loo = "/home/test1/file.txt"
    self.model = QtGui.QStandardItemModel(self.list_view)
    for line in ('a', 'b', 'c', 'd', 'e') :
    INDENT
        self.item = QtGui.QStandardItem(line)
        self.item.setCheckable(True)
        self.item.setCheckState(QtCore.Qt.Unchecked)
        self.model.appendRow(self.item)
    DEDENT
    self.list_view.setModel(self.model)
    self.list_view.show()
DEDENT

def __init__(cls, name, bases, atts) :
INDENT
    classVars = vars(cls)
    enums = classVars.get('__enumerables__', None)
    nextIter = getattr(cls, '__nextitr__', itertools.count)()
    reverseLookup = {}
    values = {}
    if enums is not None :
    INDENT
        for item in enums :
        INDENT
            if isinstance(item, (tuple, list)) :
            INDENT
                items = list(item)
                value = items.pop()
                EnumMeta.__addToReverseLookup(reverseLookup, value, tuple(map(str, items)), nextIter)
            DEDENT
            else :
            INDENT
                value = nextIter.next()
                value = EnumMeta.__addToReverseLookup(reverseLookup, value, (str(item),), nextIter, False)
            DEDENT
        DEDENT
        for value, fkeys in reverseLookup.iteritems() :
        INDENT
            f, keys = fkeys
            for key in keys :
            INDENT
                enum = EnumValue(key, value, cls)
                setattr(cls, key, enum)
                values [key] = enum
            DEDENT
            reverseLookup [value] = tuple(val for val in values.itervalues() if val.Value == value)
        DEDENT
    DEDENT
    setattr(cls, '__reverseLookup__', reverseLookup)
    setattr(cls, '__enumerables__', values)
    setattr(cls, '_Max', max([key for key in reverseLookup] or [0]))
    return super(EnumMeta, cls).__init__(name, bases, atts)
DEDENT

def sameSet(a, b) :
INDENT
    l1, l2 = (a, b) if len(a) > len(b) else (b, a)
    for val in l1 :
    INDENT
        if val not in l2 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def add(self, val) :
INDENT
    if (self.root == None) :
    INDENT
        self.root = Node(val)
    DEDENT
    else :
    INDENT
        self._add(val, self.root)
    DEDENT
DEDENT

def unique(x) :
INDENT
    output = []
    y = {}
    for item in x :
    INDENT
        y [item] = ""
    DEDENT
    for item in x :
    INDENT
        if item in y :
        INDENT
            output.append(item)
        DEDENT
    DEDENT
    return output
DEDENT

def frange(start, stop = None, step = 1) :
INDENT
    if stop is None :
    INDENT
        for x in _xrange(int(ceil(start))) :
        INDENT
            yield x
        DEDENT
    DEDENT
    else :
    INDENT
        indices = (i for i in _xrange(0, int((stop - start) / step)))
        for i in indices :
        INDENT
            yield start + step * i
        DEDENT
    DEDENT
DEDENT

    def test_update_with_redirect(self):
        res = self.client.post(
            '/edit/author/%d/update/redirect/' % self.author.pk,
            {'name': 'Randall Munroe (author of xkcd)', 'slug': 'randall-munroe'}
        )
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/edit/authors/create/')
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe (author of xkcd)>'])

def foo(thing = None, thing_seq = None) :
INDENT
    if thing_seq is not None :
    INDENT
        for _thing in thing_seq :
        INDENT
            foo(thing = _thing)
        DEDENT
    DEDENT
    if thing is not None :
    INDENT
        print "did foo with", thing
    DEDENT
DEDENT

def increase_by_one(d) :
INDENT
    for key in d :
    INDENT
        if type(d [key]) == dict :
        INDENT
            d [key] = increase_by_one(d [key])
        DEDENT
        else :
        INDENT
            d [key] += 1
        DEDENT
    DEDENT
    return d
DEDENT

def searchWordlist() :
INDENT
    path = str(raw_input(PATH))
    word = str(raw_input(WORD))
    with open(path) as f :
    INDENT
        if any(word in line for line in f) :
        INDENT
            print ('Word found')
        DEDENT
        else :
        INDENT
            print ('Word not found')
        DEDENT
    DEDENT
DEDENT

def folder_size(path) :
INDENT
    parent = {}
    folder_size = {}
    folder = os.path.realpath(path)
    for root, _, filenames in os.walk(folder) :
    INDENT
        if root == folder :
        INDENT
            parent [root] = - 1
            folder_size [root] = 0.0
        DEDENT
        elif root not in parent :
        INDENT
            immediate_parent_path = os.path.dirname(root)
            parent [root] = immediate_parent_path
            folder_size [root] = 0.0
        DEDENT
        total_size = 0
        for filename in filenames :
        INDENT
            filepath = os.path.join(root, filename)
            total_size += os.stat(filepath).st_size
        DEDENT
        folder_size [root] = total_size
        temp_path = root
        while parent [temp_path] ! = - 1 :
        INDENT
            folder_size [parent [temp_path]] += total_size
            temp_path = parent [temp_path]
        DEDENT
    DEDENT
    return folder_size [folder] / 1000000.0
DEDENT

    def test_update_with_interpolated_redirect(self):
        res = self.client.post(
            '/edit/author/%d/update/interpolate_redirect/' % self.author.pk,
            {'name': 'Randall Munroe (author of xkcd)', 'slug': 'randall-munroe'}
        )
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe (author of xkcd)>'])
        self.assertEqual(res.status_code, 302)
        pk = Author.objects.first().pk
        self.assertRedirects(res, '/edit/author/%d/update/' % pk)
        # Also test with escaped chars in URL
        res = self.client.post(
            '/edit/author/%d/update/interpolate_redirect_nonascii/' % self.author.pk,
            {'name': 'John Doe', 'slug': 'john-doe'}
        )
        self.assertEqual(res.status_code, 302)
        pk = Author.objects.get(name='John Doe').pk
        self.assertRedirects(res, '/%C3%A9dit/author/{}/update/'.format(pk))

def extendedString(string1, string2) :
INDENT
    x = string1
    y = string2
    if len(x) < len(y) :
    INDENT
        x = x + x [- 1] * (len(y) - len(x))
    DEDENT
    elif len(x) > len(y) :
    INDENT
        y = y + y [- 1] * (len(x) - len(y))
    DEDENT
    return "".join(i for j in zip(x, y) for i in j)
DEDENT

def __setattr__(self, a, v) :
INDENT
    propobj = getattr(self.__class__, a, None)
    if isinstance(propobj, property) :
    INDENT
        print "setting attr %s using property's fset" % a
        if propobj.fset is None :
        INDENT
            raise AttributeError("can't set attribute")
        DEDENT
        propobj.fset(self, v)
    DEDENT
    else :
    INDENT
        print "setting attr %s" % a
        super(Test, self).__setattr__(a, v)
    DEDENT
DEDENT

def has_add_permission(self, request) :
INDENT
    count = MyModel.objects.all().count()
    if count == 0 :
    INDENT
        return True
    DEDENT
    return False
DEDENT

def reverse(text) :
INDENT
    answer = ""
    while text :
    INDENT
        answer = text [0] + answer
        text = text [1 :]
    DEDENT
    return answer
DEDENT

    def test_update_with_special_properties(self):
        res = self.client.get('/edit/author/%d/update/special/' % self.author.pk)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['form'], views.AuthorForm)
        self.assertEqual(res.context['object'], self.author)
        self.assertEqual(res.context['thingy'], self.author)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/form.html')

        res = self.client.post(
            '/edit/author/%d/update/special/' % self.author.pk,
            {'name': 'Randall Munroe (author of xkcd)', 'slug': 'randall-munroe'}
        )
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/detail/author/%d/' % self.author.pk)
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe (author of xkcd)>'])

def minimum(lst) :
INDENT
    if len(lst) == 1 :
    INDENT
        return lst [0]
    DEDENT
    first = lst [0]
    rest = lst [1 :]
    min_of_rest = minimum(rest)
    if first < min_of_rest :
    INDENT
        return first
    DEDENT
    else :
    INDENT
        return min_of_rest
    DEDENT
DEDENT

def __call__(self, f) :
INDENT
    def new_f() :
    INDENT
        print ("Entering", f.__name__)
        print ("p1=", self.p1)
        f()
        print ("Leaving", f.__name__)
    DEDENT
    return new_f
DEDENT

def __getitem__(self, ind) :
INDENT
    try :
    INDENT
        return self._index [ind]
    DEDENT
    except KeyError :
    INDENT
        return list.__getitem__(self, ind)
    DEDENT
DEDENT

def matched(s) :
INDENT
    p_list = []
    for i in range(0, len(s)) :
    INDENT
        if s [i] == '(' :
        INDENT
            p_list.append('(')
        DEDENT
        elif s [i] == ')' :
        INDENT
            if not p_list :
            INDENT
                return False
            DEDENT
            else :
            INDENT
                p_list.pop()
            DEDENT
        DEDENT
    DEDENT
    if not p_list :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
DEDENT

def insert_sequence(dna1, dna2, number) :
INDENT
    result = '';
    for ind, x in enumerate(dna1) :
    INDENT
        if ind == number :
        INDENT
            result = result + dna2 + x
        DEDENT
        else :
        INDENT
            result = result + x
        DEDENT
    DEDENT
    print (result)
DEDENT

def quicksort(sequence, low, high) :
INDENT
    if low < high :
    INDENT
        pivot = partition(sequence, low, high)
        quicksort(sequence, low, pivot - 1)
        quicksort(sequence, pivot + 1, high)
    DEDENT
DEDENT

def qsort(l, fst, lst) :
INDENT
    if fst > = lst : return
    i, j = fst, lst
    pivot = l [random.randint(fst, lst)]
    while i < = j :
    INDENT
        while l [i] < pivot : i += 1
        while l [j] > pivot : j -= 1
        if i < = j :
        INDENT
            l [i], l [j] = l [j], l [i]
            i, j = i + 1, j - 1
        DEDENT
    DEDENT
    qsort(l, fst, j)
    qsort(l, i, lst)
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

    def test_update_without_redirect(self):
        msg = (
            'No URL to redirect to.  Either provide a url or define a '
            'get_absolute_url method on the Model.'
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.post(
                '/edit/author/%d/update/naive/' % self.author.pk,
                {'name': 'Randall Munroe (author of xkcd)', 'slug': 'randall-munroe'}
            )

def __init__(self, host, user, port, key, remote_port) :
INDENT
    self.host = host
    self.user = user
    self.port = port
    self.key = key
    self.remote_port = remote_port
    tmpfile = tempfile.NamedTemporaryFile()
    tmpfile.close()
    self.socket = tmpfile.name
    self.local_port = random.randint(10000, 65535)
    self.local_host = '127.0.0.1'
    self.open = False
DEDENT

def fib(n) :
INDENT
    if n in (0, 1) :
    INDENT
        return 1
    DEDENT
    if n & 1 :
    INDENT
        return fib((n + 1) / / 2 - 1) * (2 * fib((n + 1) / / 2) - fib((n + 1) / / 2 - 1))
    DEDENT
    a, b = fib(n / / 2 - 1), fib(n / / 2)
    return a ** 2 + b ** 2
DEDENT

    def test_update_get_object(self):
        res = self.client.get('/edit/author/update/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['form'], forms.ModelForm)
        self.assertIsInstance(res.context['view'], View)
        self.assertEqual(res.context['object'], self.author)
        self.assertEqual(res.context['author'], self.author)
        self.assertTemplateUsed(res, 'generic_views/author_form.html')

        # Modification with both POST and PUT (browser compatible)
        res = self.client.post('/edit/author/update/', {'name': 'Randall Munroe (xkcd)', 'slug': 'randall-munroe'})
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), ['<Author: Randall Munroe (xkcd)>'])


def get_images(query, start) :
INDENT
    screen_width = 1920
    screen_height = 1080
    params = {
        "q" : query,
        "sa" : "X",
        "biw" : screen_width,
        "bih" : screen_height,
        "tbm" : "isch",
        "ijn" : start / 100,
        "start" : start,
        }
    request = s.get(URL, params = params)
    bs = BeautifulSoup(request.text)
    for img in bs.findAll("div", {"class" : "rg_di"}) :
    INDENT
        images.append(img.find("img").attrs ['data-src'])
    DEDENT
DEDENT

def main() :
INDENT
    for line in open('Magic Square Input.txt') :
    INDENT
        square = [int(n) for n in line.split()]
        if len(set(square)) ! = len(square) :
        INDENT
            print ('Invalid: Duplicates')
        DEDENT
        else :
        INDENT
            for idx in indexes :
            INDENT
                if sum(square [i] for i in idx) ! = 15 :
                INDENT
                    print ('Invalid: Sum')
                    break
                DEDENT
            DEDENT
            else :
            INDENT
                print ('Valid')
            DEDENT
        DEDENT
    DEDENT
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

@override_settings(ROOT_URLCONF='generic_views.urls')
class DeleteViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            name='Randall Munroe',
            slug='randall-munroe',
        )

def outer() :
INDENT
    global mylist
    mylist = []
    def inner() :
    INDENT
        global mylist
        mylist += [1]
    DEDENT
    inner()
DEDENT

def meta_redirect(content) :
INDENT
    soup = BeautifulSoup.BeautifulSoup(content)
    result = soup.find("meta", attrs = {"http-equiv" : "Refresh"})
    if result :
    INDENT
        wait, text = result ["content"].split(";")
        if text.strip().lower().startswith("url=") :
        INDENT
            url = text [4 :]
            return url
        DEDENT
    DEDENT
    return None
DEDENT

def __init__(cls, name, bases, atts) :
INDENT
    classVars = vars(cls)
    enums = classVars.get('__enumerables__', None)
    nextIter = getattr(cls, '__nextitr__', itertools.count)()
    reverseLookup = {}
    values = {}
    if enums is not None :
    INDENT
        for item in enums :
        INDENT
            if isinstance(item, (tuple, list)) :
            INDENT
                items = list(item)
                value = items.pop()
                EnumMeta.__addToReverseLookup(reverseLookup, value, tuple(map(str, items)), nextIter)
            DEDENT
            else :
            INDENT
                value = nextIter.next()
                value = EnumMeta.__addToReverseLookup(reverseLookup, value, (str(item),), nextIter, False)
            DEDENT
        DEDENT
        for value, fkeys in reverseLookup.iteritems() :
        INDENT
            f, keys = fkeys
            for key in keys :
            INDENT
                enum = EnumValue(key, value, cls)
                setattr(cls, key, enum)
                values [key] = enum
            DEDENT
            reverseLookup [value] = tuple(val for val in values.itervalues() if val.Value == value)
        DEDENT
    DEDENT
    setattr(cls, '__reverseLookup__', reverseLookup)
    setattr(cls, '__enumerables__', values)
    setattr(cls, '_Max', max([key for key in reverseLookup] or [0]))
    return super(EnumMeta, cls).__init__(name, bases, atts)
DEDENT

def evaluate(exp) :
INDENT
    for oplist in precedence :
    INDENT
        idx = 0
        while idx < len(exp) :
        INDENT
            op = exp [idx]
            if op in oplist :
            INDENT
                result = ops [op](exp [idx - 1], exp [idx + 1])
                exp [idx - 1 : idx + 2] = [result]
                idx -= 1
            DEDENT
            else :
            INDENT
                idx += 1
            DEDENT
        DEDENT
    DEDENT
    return exp [0]
DEDENT

def func() :
INDENT
    sql = "select some rows"
    dbconn = connect_and_open_database()
    cursor = dbconn.cursor()
    cursor.execute(sql)
    yield cursor_iter(cursor)
    dbclose()
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

def rev(test) :
INDENT
    test = list(test)
    i = len(test) - 1
    result = []
    print test
    while i > = 0 :
    INDENT
        result.append(test.pop(i))
        i -= 1
    DEDENT
    return "".join(result)
DEDENT

    def test_delete_by_post(self):
        res = self.client.get('/edit/author/%d/delete/' % self.author.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author)
        self.assertEqual(res.context['author'], self.author)
        self.assertTemplateUsed(res, 'generic_views/author_confirm_delete.html')

        # Deletion with POST
        res = self.client.post('/edit/author/%d/delete/' % self.author.pk)
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), [])

def combinations(iterable, r) :
INDENT
    pool = tuple(iterable)
    n = len(pool)
    if r > n :
    INDENT
        return
    DEDENT
    indices = range(r)
    yield tuple(pool [i] for i in indices)
    while True :
    INDENT
        for i in reversed(range(r)) :
        INDENT
            if indices [i] ! = i + n - r :
            INDENT
                break
            DEDENT
        DEDENT
        else :
        INDENT
            return
        DEDENT
        indices [i] += 1
        for j in range(i + 1, r) :
        INDENT
            indices [j] = indices [j - 1] + 1
        DEDENT
        yield tuple(pool [i] for i in indices)
    DEDENT
DEDENT

def find_values(id, json_repr) :
INDENT
    results = []
    def _decode_dict(a_dict) :
    INDENT
        try : results.append(a_dict [id])
        except KeyError : pass
        return a_dict
    DEDENT
    json.loads(json_repr, object_hook = _decode_dict)
    return results
DEDENT

def repeat(string, times, lines_left = None) :
INDENT
    print (string * times)
    if (lines_left is None) :
    INDENT
        lines_left = times
    DEDENT
    lines_left = lines_left - 1
    if (lines_left > 0) :
    INDENT
        repeat(string, times, lines_left)
    DEDENT
DEDENT

def create_random(cls, level) :
INDENT
    if level == 0 :
    INDENT
        is_op = True
    DEDENT
    elif level == max_levels :
    INDENT
        is_op = False
    DEDENT
    else :
    INDENT
        is_op = random.random() < = 1.0 - pow(level / max_levels, 2.0)
    DEDENT
    if is_op :
    INDENT
        return binary_expression.create_random(level)
    DEDENT
    else :
    INDENT
        return integer_expression.create_random(level)
    DEDENT
DEDENT

def validate_ip(s) :
INDENT
    a = s.split('.')
    if len(a) ! = 4 :
    INDENT
        return False
    DEDENT
    for x in a :
    INDENT
        if not x.isdigit() :
        INDENT
            return False
        DEDENT
        i = int(x)
        if i < 0 or i > 255 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def is_member(x) :
INDENT
    a = [1, 5, 3, 9, 4, 100]
    for i in range(len(a)) :
    INDENT
        if x == a [i] :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def some_function(eggs) :
INDENT
    if eggs not in [1, 2, 3] :
    INDENT
        do_error()
        return
    DEDENT
    if eggs == 1 :
    INDENT
        do_something_1()
    DEDENT
    elif eggs == 2 :
    INDENT
        do_something_2()
    DEDENT
    elif eggs == 3 :
    INDENT
        do_something_3()
    DEDENT
    else :
    INDENT
        assert False
    DEDENT
    do_something_4()
    do_something_5()
    do_something_6()
DEDENT

    def test_delete_by_delete(self):
        # Deletion with browser compatible DELETE method
        res = self.client.delete('/edit/author/%d/delete/' % self.author.pk)
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), [])

def fib(n) :
INDENT
    if n in fibs : return fibs [n]
    if n % 2 == 0 :
    INDENT
        fibs [n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs [n]
    DEDENT
    else :
    INDENT
        fibs [n] = (fib((n - 1) / 2) ** 2) + (fib((n + 1) / 2) ** 2)
        return fibs [n]
    DEDENT
DEDENT

def lone_sum(* args) :
INDENT
    d = defaultdict(int)
    for x in args :
    INDENT
        d [x] += 1
    DEDENT
    return sum(val for val, apps in d.iteritems() if apps == 1)
DEDENT

def is_binary(filename) :
INDENT
    with open(filename, 'rb') as f :
    INDENT
        for block in f :
        INDENT
            if b'\0' in block :
            INDENT
                return True
            DEDENT
        DEDENT
    DEDENT
    return False
DEDENT

def CardsAssignment() :
INDENT
    global Cards
    while True :
    INDENT
        Cards += 1
        print (Cards)
        yield not time_to_quit
    DEDENT
DEDENT

def run(self) :
INDENT
    while 1 :
    INDENT
        t = datetime.now()
        for e in self.events :
        INDENT
            e.check(t)
        DEDENT
        time.sleep(60 - t.second - t.microsecond / 1000000.0)
    DEDENT
DEDENT

def __new__(mcs, name, bases, dict) :
INDENT
    def gen_test(a, b) :
    INDENT
        def test(self) :
        INDENT
            self.assertEqual(a, b)
        DEDENT
        return test
    DEDENT
    for tname, a, b in l :
    INDENT
        test_name = "test_%s" % tname
        dict [test_name] = gen_test(a, b)
    DEDENT
    return type.__new__(mcs, name, bases, dict)
DEDENT

def foo(s) :
INDENT
    def foo_helper(level = 0) :
    INDENT
        try :
        INDENT
            token = next(tokens)
        DEDENT
        except StopIteration :
        INDENT
            if level ! = 0 :
            INDENT
                raise Exception('missing closing paren')
            DEDENT
            else :
            INDENT
                return []
            DEDENT
        DEDENT
        if token == ')' :
        INDENT
            if level == 0 :
            INDENT
                raise Exception('missing opening paren')
            DEDENT
            else :
            INDENT
                return []
            DEDENT
        DEDENT
        elif token == '(' :
        INDENT
            return [foo_helper(level + 1)] + foo_helper(level)
        DEDENT
        else :
        INDENT
            return [token] + foo_helper(level)
        DEDENT
    DEDENT
    tokens = iter(s)
    return foo_helper()
DEDENT

    def test_delete_with_redirect(self):
        res = self.client.post('/edit/author/%d/delete/redirect/' % self.author.pk)
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/edit/authors/create/')
        self.assertQuerysetEqual(Author.objects.all(), [])

def minimum(lst) :
INDENT
    if len(lst) == 1 :
    INDENT
        return lst [0]
    DEDENT
    if lst [0] < lst [1] :
    INDENT
        return minimum(lst [0 : 1] + lst [2 :])
    DEDENT
    else :
    INDENT
        return minimum(lst [1 :])
    DEDENT
DEDENT

def readlines(self) :
INDENT
    lines = []
    while True :
    INDENT
        line = self.readline()
        if not line :
        INDENT
            break
        DEDENT
        lines.append(line)
    DEDENT
    return lines
DEDENT

    def test_delete_with_interpolated_redirect(self):
        res = self.client.post('/edit/author/%d/delete/interpolate_redirect/' % self.author.pk)
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/edit/authors/create/?deleted=%d' % self.author.pk)
        self.assertQuerysetEqual(Author.objects.all(), [])
        # Also test with escaped chars in URL
        a = Author.objects.create(**{'name': 'Randall Munroe', 'slug': 'randall-munroe'})
        res = self.client.post('/edit/author/{}/delete/interpolate_redirect_nonascii/'.format(a.pk))
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/%C3%A9dit/authors/create/?deleted={}'.format(a.pk))

def turns(NumOfTries, w, score) :
INDENT
    UI = str(raw_input('Guess a letter (caps only): '))
    j = 0
    for i in w :
    INDENT
        if UI == i :
        INDENT
            score.append('Yes')
            UserGuesses [j] = UI
        DEDENT
        j = j + 1
    DEDENT
    print UserGuesses
    while NumOfTries > 0 :
    INDENT
        turns(NumOfTries - 1, w, score)
        break
    DEDENT
DEDENT

def group() :
INDENT
    import numpy as np
    values = np.array(np.random.randint(0, 3298, size = 35000000), dtype = 'u4')
    values.sort()
    dif = np.ones(values.shape, values.dtype)
    dif [1 :] = np.diff(values)
    idx = np.where(dif > 0)
    vals = values [idx]
    count = np.diff(idx)
DEDENT

def setUp(self) :
INDENT
    logging.getLogger().setLevel(logging.DEBUG)
    tb = testbed.Testbed()
    tb.setup_env(current_version_id = 'testbed.version')
    tb.activate()
    tb.init_all_stubs()
    self.testbed = tb
DEDENT

def find_random_pattern(theme) :
INDENT
    found_lines = []
    pattern = open('poempatterns.txt', 'r')
    for line in pattern :
    INDENT
        found = re.findall(".*theme=%s.*" % theme, line.strip())
        for match in found :
        INDENT
            found_lines.append(line)
        DEDENT
    DEDENT
    selectedline = random.choice(found_lines)
    return selectedline
DEDENT

def check_names(name, full_name_list) :
INDENT
    for full_name in full_name_list :
    INDENT
        if name in full_name :
        INDENT
            yield full_name
        DEDENT
    DEDENT
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

    def test_delete_with_special_properties(self):
        res = self.client.get('/edit/author/%d/delete/special/' % self.author.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author)
        self.assertEqual(res.context['thingy'], self.author)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/confirm_delete.html')

        res = self.client.post('/edit/author/%d/delete/special/' % self.author.pk)
        self.assertEqual(res.status_code, 302)
        self.assertRedirects(res, '/list/authors/')
        self.assertQuerysetEqual(Author.objects.all(), [])

def count_occurrences(p, letter) :
INDENT
    count = 0
    for elem in p :
    INDENT
        try :
        INDENT
            if elem [0] == letter :
            INDENT
                count = count + 1
            DEDENT
        DEDENT
        except Exception, ex :
        INDENT
            print ex.message
        DEDENT
    DEDENT
    return count
DEDENT

def insert(self, val) :
INDENT
    if self.val is not None :
    INDENT
        if val < self.val :
        INDENT
            if self.left is not None :
            INDENT
                self.left.insert(val)
            DEDENT
            else :
            INDENT
                self.left = Tree(val)
            DEDENT
        DEDENT
        elif val > self.val :
        INDENT
            if self.right is not None :
            INDENT
                self.right.insert(val)
            DEDENT
            else :
            INDENT
                self.right = Tree(val)
            DEDENT
        DEDENT
        else :
        INDENT
            return
        DEDENT
    DEDENT
    else :
    INDENT
        self.val = val
        print ("new node added")
    DEDENT
DEDENT

    def test_delete_without_redirect(self):
        msg = 'No URL to redirect to. Provide a success_url.'
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.post('/edit/author/%d/delete/naive/' % self.author.pk)
def __init__(self, parent = None) :
INDENT
    super(App, self).__init__(parent)
    self.tab = QtGui.QWidget()
    self.setCentralWidget(self.tab)
    self.tablayout = QtGui.QVBoxLayout(self.tab)
    self.canvas = CustomFigCanvas()
    self.tablayout.addWidget(self.canvas)
DEDENT

def sublistExists(x, y) :
INDENT
    occ = [i for i, a in enumerate(x) if a == y [0]]
    for b in occ :
    INDENT
        if x [b : b + len(y)] == y :
        INDENT
            print 'YES-- SUBLIST at : ', b
            return True
        DEDENT
        if len(occ) - 1 == occ.index(b) :
        INDENT
            print 'NO SUBLIST'
            return False
        DEDENT
    DEDENT
DEDENT

def test_func_happy_path(self, MockFTP, m_open) :
INDENT
    MockFTP.return_value = Mock()
    mock_ftp_obj = MockFTP()
    m_open.return_value = Mock()
    func('localhost', 'fred', 's3Kr3t')
    assert mock_ftp_obj.retrbinary.called
    assert m_open.called
    m_open.assert_called_once_with('README', 'wb')
DEDENT

def enter(self) :
INDENT
    print "Some text describing the scene bla bla"
    raw = raw_input("Guess the number")
    if raw ! = "42" :
    INDENT
        return 'Scene1'
    DEDENT
    return 'Scene2'
DEDENT

def nested_sum(seq) :
INDENT
    stack = []
    stack.append(seq)
    result = 0
    while stack :
    INDENT
        item = stack.pop()
        if isinstance(item, list) :
        INDENT
            for e in item :
            INDENT
                stack.append(e)
            DEDENT
        DEDENT
        else :
        INDENT
            result += item
        DEDENT
    DEDENT
    return result
DEDENT

def test_val(self, val1, val2) :
INDENT
    if val1 > val2 :
    INDENT
        self.a_points += 1
    DEDENT
    elif val2 > val1 :
    INDENT
        self.b_points += 1
    DEDENT
    else :
    INDENT
        pass
    DEDENT
DEDENT

def get_square(image, square_size) :
INDENT
    height, width = image.shape
    if (height > width) :
    INDENT
        differ = height
    DEDENT
    else :
    INDENT
        differ = width
    DEDENT
    differ += 4
    mask = np.zeros((differ, differ), dtype = "uint8")
    x_pos = int((differ - width) / 2)
    y_pos = int((differ - height) / 2)
    mask [y_pos : y_pos + height, x_pos : x_pos + width] = image [0 : height, 0 : width]
    mask = cv2.resize(mask, (square_size, square_size), interpolation = cv2.INTER_AREA)
    return mask
DEDENT






































































































































































