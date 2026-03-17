from django.core import signing
from django.http import HttpRequest, HttpResponse
from django.test import SimpleTestCase, override_settings
from django.test.utils import freeze_time


class SignedCookieTest(SimpleTestCase):

    def test_can_set_and_read_signed_cookies(self):
        response = HttpResponse()
        response.set_signed_cookie('c', 'hello')
        self.assertIn('c', response.cookies)
        self.assertTrue(response.cookies['c'].value.startswith('hello:'))
        request = HttpRequest()
        request.COOKIES['c'] = response.cookies['c'].value
        value = request.get_signed_cookie('c')
        self.assertEqual(value, 'hello')

def synchronized(f) :
INDENT
    @ functools.wraps(f)
    def wrapper(self, * args, ** kwargs) :
    INDENT
        try :
        INDENT
            _ = self._lock
        DEDENT
        except AttributeError :
        INDENT
            self._lock = threading.Lock()
        DEDENT
        with self._lock :
        INDENT
            return f(self, * args, ** kwargs)
        DEDENT
    DEDENT
    return wrapper
DEDENT

def syracuse(n) :
INDENT
    syracuse_sequence = [n]
    while True :
    INDENT
        if n == 1 :
        INDENT
            print (syracuse_sequence)
            return 0
        DEDENT
        elif n % 2 == 0 :
        INDENT
            n /= 2
            syracuse_sequence.append(round(n))
            continue
        DEDENT
        else :
        INDENT
            n = (n * 3) + 1
            syracuse_sequence.append(round(n))
            continue
        DEDENT
    DEDENT
DEDENT

def checkfortie() :
INDENT
    tie = True
    for i in range(w) :
    INDENT
        for j in range(h) :
        INDENT
            if board [i] [j] == 0 :
            INDENT
                tie = False
            DEDENT
        DEDENT
    DEDENT
    if tie :
    INDENT
        print ("It's a tie!")
    DEDENT
DEDENT

def fib(n) :
INDENT
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n) [3 :] :
    INDENT
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1' : v1, v2, v3 = v1 + v2, v1, v2
    DEDENT
    return v2
DEDENT

def addToInventory(inventory, addedItems) :
INDENT
    print ('Your inventory now has:')
    for item in addedItems :
    INDENT
        stuff [item] = stuff.get(item, 0) + 1
    DEDENT
DEDENT

def backtrack(res, temp, nums, start) :
INDENT
    res.append(temp [:])
    for i in range(start, len(nums)) :
    INDENT
        temp.append(nums [i])
        backtrack(res, temp, nums, i + 1)
        temp.pop()
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

def __init__(self, parent = None) :
INDENT
    QtGui.QMainWindow.__init__(self)
    self.tab_list = []
    self.setTabShape(QtGui.QTabWidget.Rounded)
    self.centralwidget = QtGui.QWidget(self)
    self.top_level_layout = QtGui.QGridLayout(self.centralwidget)
    self.tabWidget = QtGui.QTabWidget(self.centralwidget)
    self.top_level_layout.addWidget(self.tabWidget, 1, 0, 25, 25)
    process_button = QtGui.QPushButton("Process")
    self.top_level_layout.addWidget(process_button, 0, 1)
    QtCore.QObject.connect(process_button, QtCore.SIGNAL("clicked()"), self.process)
    self.setCentralWidget(self.centralwidget)
    self.centralwidget.setLayout(self.top_level_layout)
    for i in range(0, 10) :
    INDENT
        name = 'tab' + str(i)
        self.tab_list.append(Tab(self.tabWidget, Worker(name)))
        self.tabWidget.addTab(self.tab_list [- 1], name)
    DEDENT
DEDENT

    def test_can_use_salt(self):
        response = HttpResponse()
        response.set_signed_cookie('a', 'hello', salt='one')
        request = HttpRequest()
        request.COOKIES['a'] = response.cookies['a'].value
        value = request.get_signed_cookie('a', salt='one')
        self.assertEqual(value, 'hello')
        with self.assertRaises(signing.BadSignature):
            request.get_signed_cookie('a', salt='two')

def update_url(self) :
INDENT
    url_obj = self._get_url()
    url_obj.write(
        {'name' : self.url1 or False,
            'url_seniat' : self.url2 and False,
            'url_seniat2' : self.url3 and False})
    return {}
DEDENT

def __enter__(self) :
INDENT
    self.interrupted = False
    self.released = False
    self.original_handler = signal.getsignal(self.sig)
    def handler(signum, frame) :
    INDENT
        self.release()
        self.interrupted = True
    DEDENT
    signal.signal(self.sig, handler)
    return self
DEDENT

def time_limit(seconds) :
INDENT
    def signal_handler(signum, frame) :
    INDENT
        raise TimeoutException("Timed out!")
    DEDENT
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try :
    INDENT
        yield
    DEDENT
    finally :
    INDENT
        signal.alarm(0)
    DEDENT
DEDENT

def iterate(i) :
INDENT
    empty = True
    for value in i :
    INDENT
        yield value
        empty = False
    DEDENT
    if empty :
    INDENT
        print "empty"
    DEDENT
DEDENT

    def test_detects_tampering(self):
        response = HttpResponse()
        response.set_signed_cookie('c', 'hello')
        request = HttpRequest()
        request.COOKIES['c'] = response.cookies['c'].value[:-2] + '$$'
        with self.assertRaises(signing.BadSignature):
            request.get_signed_cookie('c')

def get_or_415(self, pk) :
INDENT
    instance = self.get(pk)
    if not instance :
    INDENT
        raise HttpException(code = 415)
    DEDENT
    return instance
DEDENT

def convert_timestamp(date_timestamp = None) :
INDENT
    if zone [2] in date_timestamp :
    INDENT
        d = datetime.strptime(date_timestamp, "%Y-%m-%d %H:%M:%S %Z")
    DEDENT
    else :
    INDENT
        d = datetime.strptime(date_timestamp, "%Y-%m-%d %H:%M:%S")
    DEDENT
    return d.strftime("%Y-%m-%d")
DEDENT

def find_random_pattern(theme) :
INDENT
    with open('poempatterns.txt', 'r') as pattern :
    INDENT
        found_lines = [line for line in pattern if theme in line]
    DEDENT
    selectedline = random.choice(found_lines)
    return selectedline
DEDENT

def permutations(head, tail = '') :
INDENT
    if len(head) == 0 : print tail
    else :
    INDENT
        for i in range(len(head)) :
        INDENT
            permutations(head [0 : i] + head [i + 1 :], tail + head [i])
        DEDENT
    DEDENT
DEDENT

def __call__(self) :
INDENT
    while True :
    INDENT
        next_action = self.queue.get()
        success = next_action(* self.args, ** self.kwargs)
        if not success :
        INDENT
            self.add_task(next_action)
        DEDENT
    DEDENT
DEDENT

def spiral(width, height) :
INDENT
    if width < 1 or height < 1 :
    INDENT
        raise ValueError
    DEDENT
    x, y = width / / 2, height / / 2
    dx, dy = NORTH
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True :
    INDENT
        count += 1
        matrix [y] [x] = count
        new_dx, new_dy = turn_right [dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 < = new_x < width and 0 < = new_y < height and
            matrix [new_y] [new_x] is None) :
        INDENT
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        DEDENT
        else :
        INDENT
            x, y = x + dx, y + dy
            if not (0 < = x < width and 0 < = y < height) :
            INDENT
                return matrix
            DEDENT
        DEDENT
    DEDENT
DEDENT

    def test_default_argument_suppresses_exceptions(self):
        response = HttpResponse()
        response.set_signed_cookie('c', 'hello')
        request = HttpRequest()
        request.COOKIES['c'] = response.cookies['c'].value[:-2] + '$$'
        self.assertIsNone(request.get_signed_cookie('c', default=None))

def is_sorted(lst) :
INDENT
    it = iter(lst)
    try :
    INDENT
        prev = it.next()
    DEDENT
    except StopIteration :
    INDENT
        return True
    DEDENT
    for x in it :
    INDENT
        if prev > x :
        INDENT
            return False
        DEDENT
        prev = x
    DEDENT
    return True
DEDENT

def acquire_data(filename_or_list) :
INDENT
    try :
    INDENT
        with open(filename_or_list) as f :
        INDENT
            data = list(f)
        DEDENT
    DEDENT
    except TypeError :
    INDENT
        data = list(filename_or_list)
    DEDENT
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

def msg_decorator(f) :
INDENT
    def inner_dec(* args, ** kwargs) :
    INDENT
        g = f.__globals__
        sentinel = object()
        oldvalue = g.get('var', sentinel)
        g ['var'] = value
        try :
        INDENT
            res = f(* args, ** kwargs)
        DEDENT
        finally :
        INDENT
            if oldvalue is sentinel :
            INDENT
                del g ['var']
            DEDENT
            else :
            INDENT
                g ['var'] = oldvalue
            DEDENT
        DEDENT
        return res
    DEDENT
    return inner_dec
DEDENT

def longest(x) :
INDENT
    if x in _longest :
    INDENT
        _longest.clear()
        return False
    DEDENT
    _longest.add(x)
    return True
DEDENT

    def test_max_age_argument(self):
        value = 'hello'
        with freeze_time(123456789):
            response = HttpResponse()
            response.set_signed_cookie('c', value)
            request = HttpRequest()
            request.COOKIES['c'] = response.cookies['c'].value
            self.assertEqual(request.get_signed_cookie('c'), value)

        with freeze_time(123456800):
            self.assertEqual(request.get_signed_cookie('c', max_age=12), value)
            self.assertEqual(request.get_signed_cookie('c', max_age=11), value)
            with self.assertRaises(signing.SignatureExpired):
                request.get_signed_cookie('c', max_age=10)

def count(list1) :
INDENT
    x = 0
    total = 0
    while x < len(list1) :
    INDENT
        total += list [x]
        print total
        x = x + 1
    DEDENT
    return total
DEDENT

def order_fields(form, field_list, throw_away = False) :
INDENT
    if throw_away :
    INDENT
        form.fields.keyOrder = field_list
    DEDENT
    else :
    INDENT
        for field in field_list [: : - 1] :
        INDENT
            form.fields.insert(0, field, form.fields.pop(field))
        DEDENT
    DEDENT
DEDENT

def unique(items) :
INDENT
    seen = set()
    for i in xrange(len(items) - 1, - 1, - 1) :
    INDENT
        it = items [i]
        if it in seen :
        INDENT
            del items [i]
        DEDENT
        else :
        INDENT
            seen.add(it)
        DEDENT
    DEDENT
DEDENT

def seq(start, end, step) :
INDENT
    if step == 0 :
    INDENT
        raise ValueError("step must not be 0")
    DEDENT
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)
DEDENT

    @override_settings(SECRET_KEY=b'\xe7')
    def test_signed_cookies_with_binary_key(self):
        response = HttpResponse()
        response.set_signed_cookie('c', 'hello')

        request = HttpRequest()
        request.COOKIES['c'] = response.cookies['c'].value
        self.assertEqual(request.get_signed_cookie('c'), 'hello')
def window(seq, size, step = 1) :
INDENT
    iters = [iter(seq) for i in range(size)]
    [next(iters [i]) for j in range(size) for i in range(- 1, - j - 1, - 1)]
    while (True) :
    INDENT
        yield [next(i) for i in iters]
        [next(i) for i in iters for j in range(step - 1)]
    DEDENT
DEDENT

def get_info(session, title, url) :
INDENT
    r = session.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for items in soup.select("ul.list-unstyled") :
    INDENT
        try :
        INDENT
            phone = items.select_one("a[href^='tel:']").text
        DEDENT
        except :
        INDENT
            continue
        DEDENT
        else :
        INDENT
            print (title, phone)
            break
        DEDENT
    DEDENT
DEDENT

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

def dashboard(request) :
INDENT
    form = FilterForm()
    sightings = []
    if request.POST :
    INDENT
        form = FilterForm(request.POST)
        if form.is_valid() :
        INDENT
            selectedplant = form.cleaned_data ['selectedplant']
            sightings = Sighting.objects.filter(IMS_plant = selectedplant)
        DEDENT
        else :
        INDENT
            sightings = Sighting.objects.all().order_by('date')
        DEDENT
    DEDENT
    else :
    INDENT
        sightings = Sighting.objects.all().order_by('date')
    DEDENT
    context = {'sightings' : sightings, 'form' : form}
    return render_to_response('dashboard.html', context, context_instance = RequestContext(request))
DEDENT

def sumvars(x, y, z, mode = 'default') :
INDENT
    d = {}
    s = x
    d ['first_step'] = s
    s += y
    d ['second_step'] = s
    s += z
    d ['final'] = s
    if mode == 'default' :
    INDENT
        return s
    DEDENT
    else :
    INDENT
        return d
    DEDENT
DEDENT

def perm(line) :
INDENT
    seq = [c for c in line]
    if len(seq) < = 1 :
    INDENT
        return seq
    DEDENT
    else :
    INDENT
        return pzip(seq [0], perm(seq [1 :]))
    DEDENT
DEDENT

def partition(A, a, b) :
INDENT
    p = randint(a, b)
    piv = A [p]
    A [p] = A [b]
    A [b] = piv
    i = a
    j = b - 1
    while i < = j :
    INDENT
        while A [i] < = piv and i < = j :
        INDENT
            i += 1
        DEDENT
        while A [j] > = piv and j > = i :
        INDENT
            j -= 1
        DEDENT
        if i < j :
        INDENT
            t = A [i]
            A [i] = A [j]
            A [j] = t
        DEDENT
    DEDENT
    A [b] = A [i]
    A [i] = piv
    return i
DEDENT

def json_debug_handler(obj) :
INDENT
    print ("object received:")
    print type(obj)
    print ("\n\n")
    if isinstance(obj, collections.Mapping) :
    INDENT
        for key, value in obj.iteritems() :
        INDENT
            if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
            INDENT
                value = json_debug_handler(value)
            DEDENT
            obj [key] = convert(value)
        DEDENT
    DEDENT
    elif isinstance(obj, collections.MutableSequence) :
    INDENT
        for index, value in enumerate(obj) :
        INDENT
            if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
            INDENT
                value = json_debug_handler(value)
            DEDENT
            obj [index] = convert(value)
        DEDENT
    DEDENT
    return obj
DEDENT




































