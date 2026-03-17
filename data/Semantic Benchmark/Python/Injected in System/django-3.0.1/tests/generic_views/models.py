from django.db import models
from django.db.models import QuerySet
from django.db.models.manager import BaseManager
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'professional artist'
        verbose_name_plural = 'professional artists'

    def __str__(self):
        return self.name

def encrypt(self, raw) :
INDENT
    if raw is None or len(raw) == 0 :
    INDENT
        raise NameError("No value given to encrypt")
    DEDENT
    raw = raw + '\0' * (self.blk_sz - len(raw) % self.blk_sz)
    raw = raw.encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')
DEDENT

def parse_entities(data) :
INDENT
    results = []
    for category in data.keys() :
    INDENT
        results += list(map(lambda x : '{0}:{1}'.format(x ['name'], x ['sentiment']),
                filter(lambda i : i ['sentiment'] ! = 'none', data [category])))
    DEDENT
    return ','.join(results)
DEDENT

def __init__(self, name, mode) :
INDENT
    self.fl = open(name, mode)
    self.fl.write('\n')
    self.stdout = sys.stdout
    self.stdout.write('\n')
    self.stderr = sys.stderr
    sys.stdout = self
    sys.stderr = self
DEDENT

def split_at_first_false(pred, seq) :
INDENT
    for i, item in enumerate(seq) :
    INDENT
        if not pred(item) :
        INDENT
            return seq [: i], seq [i :]
        DEDENT
    DEDENT
DEDENT

def is_cgi(self) :
INDENT
    mime = MimeTypes()
    request = self.path.split('?')
    if len(request) == 2 :
    INDENT
        path, args = request
    DEDENT
    else :
    INDENT
        path, args = request, None
    DEDENT
    if isinstance(path, list) :
    INDENT
        path = path [0]
    DEDENT
    url = urllib.pathname2url(path)
    mime_type = mime.guess_type(url)
    if 'python' in mime_type [0] :
    INDENT
        self.cgi_info = '', self.path [1 :]
        return True
    DEDENT
    else :
    INDENT
        self.cgi_info = '', '/static.py?path=%s' % path [1 :]
        print self.cgi_info
        return True
    DEDENT
DEDENT

def unique(list) :
INDENT
    s = {}
    output = []
    for x in list :
    INDENT
        count = 1
        if (s.has_key(x)) :
        INDENT
            count = s [x] + 1
        DEDENT
        s [x] = count
    DEDENT
    for x in list :
    INDENT
        count = s [x]
        if (count > 0) :
        INDENT
            s [x] = 0
            output.append(x)
        DEDENT
    DEDENT
    return output
DEDENT

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.id})


def validator(validate_func) :
INDENT
    func = partial(patched, validate_func, input)
    patch = unittest.mock.patch('builtins.input', func)
    patch.start()
    try :
    INDENT
        yield
    DEDENT
    finally :
    INDENT
        patch.stop()
    DEDENT
DEDENT

def qsort(arr) :
INDENT
    if len(arr) < = 1 :
    INDENT
        return arr
    DEDENT
    else :
    INDENT
        return qsort([x for x in arr [1 :] if x < arr [0]]) + [arr [0]] + qsort([x for x in arr [1 :] if x > = arr [0]])
    DEDENT
DEDENT

def qsort(list) :
INDENT
    if len(list) < 2 :
    INDENT
        return list
    DEDENT
    pivot = list.pop()
    left = filter(lambda x : x < = pivot, list)
    right = filter(lambda x : x > pivot, list)
    return qsort(left) + [pivot] + qsort(right)
DEDENT

class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


def modify_duplicates_ordered(original) :
INDENT
    D = {}
    result = [];
    for value in original : D [value] = 0;
    for value in original :
    INDENT
        result.append(value + D [value] * 0.0001);
        D [value] += 1;
    DEDENT
    return result;
DEDENT

def char_first_index(s, c, index = 0) :
INDENT
    if len(s) == index :
    INDENT
        return None
    DEDENT
    if s [index] == c :
    INDENT
        return index
    DEDENT
    return char_first_index(s, c, index + 1)
DEDENT

def to_int(bin) :
INDENT
    x = int(bin, 2)
    if bin [0] == '1' :
    INDENT
        x -= 2 ** len(bin)
    DEDENT
    return x
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

class DoesNotExistQuerySet(QuerySet):
    def get(self, *args, **kwargs):
        raise Author.DoesNotExist


def main() :
INDENT
    converted_images = []
    for image in [mouse, background] :
    INDENT
        converted_images.append(Image_loader(img))
    DEDENT
    background, mouse = converted_images
DEDENT

def getdetails(p) :
INDENT
    if p in ids :
    INDENT
        return ids [p]
    DEDENT
    for k, v in ids.iteritems() :
    INDENT
        if p in v ['subid'] :
        INDENT
            return v ['subid'] [p]
        DEDENT
    DEDENT
DEDENT

def xirr(transactions) :
INDENT
    years = [(ta [0] - transactions [0] [0]).days / 365.0 for ta in transactions]
    residual = 1
    step = 0.05
    guess = 0.05
    epsilon = 0.0001
    limit = 10000
    while abs(residual) > epsilon and limit > 0 :
    INDENT
        limit -= 1
        residual = 0.0
        for i, ta in enumerate(transactions) :
        INDENT
            residual += ta [1] / pow(guess, years [i])
        DEDENT
        if abs(residual) > epsilon :
        INDENT
            if residual > 0 :
            INDENT
                guess += step
            DEDENT
            else :
            INDENT
                guess -= step
                step /= 2.0
            DEDENT
        DEDENT
    DEDENT
    return guess - 1
DEDENT

def getPrint(thefun, * a, ** k) :
INDENT
    savstdout = sys.stdout
    sys.stdout = cStringIO.StringIO()
    try :
    INDENT
        thefun(* a, ** k)
    DEDENT
    finally :
    INDENT
        v = sys.stdout.getvalue()
        sys.stdout = savstdout
    DEDENT
    return v
DEDENT

def sum_numbers(s) :
INDENT
    sm = i = 0
    while i < len(s) :
    INDENT
        t = ""
        while i < len(s) and not s [i].isspace() :
        INDENT
            t += s [i]
            i += 1
        DEDENT
        if t :
        INDENT
            sm += float(t)
        DEDENT
        else :
        INDENT
            i += 1
        DEDENT
    DEDENT
    return sm
DEDENT

def get_most_ooo_word(words) :
INDENT
    if type(words) == list and len(words) > 0 :
    INDENT
        words = words [0].split()
    DEDENT
    else :
    INDENT
        words = words.split()
    DEDENT
    k = words [0]
    for i in range(1, len(words) - 1) :
    INDENT
        if words [i].count('o') > words [i - 1].count('o') :
        INDENT
            k = words [i]
        DEDENT
    DEDENT
    return (k)
DEDENT

def matcher(x) :
INDENT
    val = None
    for p in physical :
    INDENT
        for y in x.split() :
        INDENT
            if p == y.lower() :
            INDENT
                if val is not None :
                INDENT
                    return 'mix'
                DEDENT
                val = p
            DEDENT
        DEDENT
        return val if val else 'other'
    DEDENT
DEDENT

def get_word_len_dict(text) :
INDENT
    result_dict = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}
    for word in text.split() :
    INDENT
        n = len(word)
        if n in result_dict and word not in result_dict [n] :
        INDENT
            result_dict [n].append(word)
        DEDENT
    DEDENT
    return result_dict
DEDENT

def file_len(fname) :
INDENT
    p = subprocess.Popen(['wc', '-l', fname], stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode ! = 0 :
    INDENT
        raise IOError(err)
    DEDENT
    return int(result.strip().split() [0])
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

def outer() :
INDENT
    def inner() :
    INDENT
        outer.y += 1
        return outer.y
    DEDENT
    return inner
DEDENT

def sameSet(list1, list2) :
INDENT
    if contained(list1, list2) and contained(list2, list1) :
    INDENT
        print ("the same!!")
    DEDENT
    else :
    INDENT
        print ("not the same")
    DEDENT
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

def _add(self, node, value) :
INDENT
    if value < = node.value :
    INDENT
        if node.left :
        INDENT
            self._add(node.left, value)
        DEDENT
        else :
        INDENT
            node.left = Node(value)
        DEDENT
    DEDENT
    else :
    INDENT
        if node.right :
        INDENT
            self._add(node.right, value)
        DEDENT
        else :
        INDENT
            node.right = Node(value)
        DEDENT
    DEDENT
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

DoesNotExistBookManager = BaseManager.from_queryset(DoesNotExistQuerySet)


class Book(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    pages = models.IntegerField()
    authors = models.ManyToManyField(Author)
    pubdate = models.DateField()

    objects = models.Manager()
    does_not_exist = DoesNotExistBookManager()

    class Meta:
        ordering = ['-pubdate']

    def __str__(self):
        return self.name


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

def __new__(metaclass, classname, bases, classdict) :
INDENT
    clsobj = super(metaclass, metaclass).__new__(metaclass, classname,
        bases, classdict)
    if classname ! = 'Foo' and 'write' in classdict :
    INDENT
        def call_base_write_after(self, * args, ** kwargs) :
        INDENT
            classdict ['write'](self, * args, ** kwargs)
            Foo.write(self, * args, ** kwargs)
        DEDENT
        setattr(clsobj, 'write', call_base_write_after)
    DEDENT
    return clsobj
DEDENT

def todict(obj) :
INDENT
    if isinstance(obj, basestring) :
    INDENT
        return obj
    DEDENT
    elif isinstance(obj, dict) :
    INDENT
        return dict((key, todict(val)) for key, val in obj.items())
    DEDENT
    elif isinstance(obj, collections.Iterable) :
    INDENT
        return [todict(val) for val in obj]
    DEDENT
    elif hasattr(obj, '__dict__') :
    INDENT
        return todict(vars(obj))
    DEDENT
    elif hasattr(obj, '__slots__') :
    INDENT
        return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
    DEDENT
    return obj
DEDENT

def touch(fname) :
INDENT
    try :
    INDENT
        os.utime(fname, None)
    DEDENT
    except OSError :
    INDENT
        open(fname, 'a').close()
    DEDENT
DEDENT

class Page(models.Model):
    content = models.TextField()
    template = models.CharField(max_length=255)


class BookSigning(models.Model):
    event_date = models.DateTimeField()

































