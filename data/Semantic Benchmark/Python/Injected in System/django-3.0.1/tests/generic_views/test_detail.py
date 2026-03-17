import datetime

from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin

from .models import Artist, Author, Book, Page


@override_settings(ROOT_URLCONF='generic_views.urls')
class DetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.artist1 = Artist.objects.create(name='Rene Magritte')
        cls.author1 = Author.objects.create(name='Roberto Bolaño', slug='roberto-bolano')
        cls.author2 = Author.objects.create(name='Scott Rosenberg', slug='scott-rosenberg')
        cls.book1 = Book.objects.create(name='2066', slug='2066', pages=800, pubdate=datetime.date(2008, 10, 1))
        cls.book1.authors.add(cls.author1)
        cls.book2 = Book.objects.create(
            name='Dreaming in Code', slug='dreaming-in-code', pages=300, pubdate=datetime.date(2006, 5, 1)
        )
        cls.page1 = Page.objects.create(
            content='I was once bitten by a moose.', template='generic_views/page_template.html'
        )

def leafs_of_branch(node) :
INDENT
    traverse = [node]
    leafs = []
    while traverse :
    INDENT
        node = traverse.pop()
        children = node.children()
        if children :
        INDENT
            traverse.extend(children)
        DEDENT
        else :
        INDENT
            leafs.append(str(node))
        DEDENT
    DEDENT
    return leafs
DEDENT

def count_occurrences(p, letter) :
INDENT
    count = 0
    for elem in p :
    INDENT
        if isinstance(elem, basestring) :
        INDENT
            if elem [0] == letter :
            INDENT
                count = count + 1
            DEDENT
        DEDENT
        else :
        INDENT
            raise TypeError("String expected")
        DEDENT
    DEDENT
    return count
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

def initUI(self) :
INDENT
    style = self.style()
    icon = style.standardIcon(QtGui.QStyle.SP_MediaSeekForward)
    self.tray_icon = QtGui.QSystemTrayIcon()
    self.tray_icon.setIcon(QtGui.QIcon(icon))
    self.setWindowIcon(QtGui.QIcon(icon))
    self.tray_icon.activated.connect(self.restore_window)
DEDENT

def __init__(self, parent = None) :
INDENT
    QtGui.QWidget.__init__(self, parent)
    l = QtGui.QVBoxLayout(self)
    cdf = self.get_data_frame()
    self._tm = TableModel(self)
    self._tm.update(cdf)
    self._tv = TableView(self)
    self._tv.setModel(self._tm)
    for row in range(0, self._tm.rowCount()) :
    INDENT
        self._tv.openPersistentEditor(self._tm.index(row, 4))
    DEDENT
    self.setGeometry(300, 300, 550, 200)
    l.addWidget(self._tv)
DEDENT

    def test_simple_object(self):
        res = self.client.get('/detail/obj/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], {'foo': 'bar'})
        self.assertIsInstance(res.context['view'], View)
        self.assertTemplateUsed(res, 'generic_views/detail.html')

def minimum(lst, current_min = None) :
INDENT
    if not lst :
    INDENT
        return current_min
    DEDENT
    if current_min is None :
    INDENT
        current_min = lst [0]
    DEDENT
    elif lst [0] < current_min :
    INDENT
        current_min = lst [0]
    DEDENT
    return minimum(lst [1 :], current_min)
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

def __call__(self, n) :
INDENT
    if n not in self.cache :
    INDENT
        if n == 0 :
        INDENT
            self.cache [n] = 1
        DEDENT
        else :
        INDENT
            self.cache [n] = n * self.__call__(n - 1)
        DEDENT
    DEDENT
    return self.cache [n]
DEDENT

def __init__(self, verbosity = 1) :
INDENT
    TestResult.__init__(self)
    self.stdout0 = None
    self.stderr0 = None
    self.success_count = 0
    self.failure_count = 0
    self.error_count = 0
    self.verbosity = verbosity
    self.result = []
DEDENT

def __init__(self, button) :
INDENT
    self.hbox = gtk.HBox()
    self.button = button
    liststore = gtk.ListStore(str)
    liststore.append(["foo"])
    liststore.append(["bar"])
    treeview = gtk.TreeView(liststore)
    self.hbox.pack_start(treeview, False)
    cell = gtk.CellRendererText()
    col = gtk.TreeViewColumn("Column 1")
    col.pack_start(cell, True)
    col.set_attributes(cell, text = 0)
    treeview.connect('row-activated', self.open_file)
    treeview.append_column(col)
DEDENT

def fib(n) :
INDENT
    def fibseq(n) :
    INDENT
        a, b = 0, 1
        for _ in xrange(n) :
        INDENT
            yield a
            a, b = b, a + b
        DEDENT
    DEDENT
    return sum(v for v in fibseq(n))
DEDENT

def partition(predicate, values) :
INDENT
    results = ([], [])
    for item in values :
    INDENT
        results [predicate(item)].append(item)
    DEDENT
    return results
DEDENT

def fileCount(path, extension) :
INDENT
    count = 0
    for root, dirs, files in os.walk(path) :
    INDENT
        count += sum(f.endswith(extension) for f in files)
    DEDENT
    return count
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

    def test_detail_by_pk(self):
        res = self.client.get('/detail/author/%s/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

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

def __init__(self, widget) :
INDENT
    logging.Handler.__init__(self)
    self.setLevel(logging.DEBUG)
    self.widget = widget
    self.widget.config(state = 'disabled')
    self.widget.tag_config("INFO", foreground = "black")
    self.widget.tag_config("DEBUG", foreground = "grey")
    self.widget.tag_config("WARNING", foreground = "orange")
    self.widget.tag_config("ERROR", foreground = "red")
    self.widget.tag_config("CRITICAL", foreground = "red", underline = 1)
    self.red = self.widget.tag_configure("red", foreground = "red")
DEDENT

def __init__(self, parent) :
INDENT
    pre = wx.PreDialog()
    pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
    pre.Create(parent, - 1, "sample dialog", size = (200, 100), style = wx.CAPTION | wx.RESIZE_BORDER)
    self.PostCreate(pre)
    self.parent = parent
    self.Bind(wx.EVT_KEY_DOWN, self.parent._on_key_down)
    self.Bind(wx.EVT_KEY_UP, self.parent._on_key_up)
    btn = wx.Button(self, - 1, "OK")
    btn.Bind(wx.EVT_BUTTON, self._OnClick)
DEDENT

def test(data) :
INDENT
    all_point_sets = []
    for row in data :
    INDENT
        point_set = []
        first_points, second_points = row
        first_points = map(int, first_points.split(","))
        second_points = map(int, second_points.split(","))
        paired_points = zip(first_points, second_points)
        curr_points = [Point(p [0], p [1]) for p in paired_points]
        all_point_sets.append(curr_points)
    DEDENT
    return all_point_sets
DEDENT

def __init__(self, input, output) :
INDENT
    try :
    INDENT
        self.input = open(input, 'r')
        self.output = open(output, 'w')
    DEDENT
    except BaseException as exc :
    INDENT
        self.__exit___(type(exc), exc, exc.__traceback__)
        raise
    DEDENT
DEDENT

    def test_detail_missing_object(self):
        res = self.client.get('/detail/author/500/')
        self.assertEqual(res.status_code, 404)

def product(* args, ** kwds) :
INDENT
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools :
    INDENT
        result = [x + [y] for x in result for y in pool]
    DEDENT
    for prod in result :
    INDENT
        yield tuple(prod)
    DEDENT
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

def insertionSort(L, reverse = False) :
INDENT
    if reverse :
    INDENT
        cmpfunc = lambda a, b : cmp(b, a)
    DEDENT
    else :
    INDENT
        cmpfunc = cmp
    DEDENT
    for j in xrange(1, len(L)) :
    INDENT
        valToInsert = L [j]
        i = j - 1
        while i > = 0 and cmpfunc(L [i], valToInsert) > 0 :
        INDENT
            L [i + 1] = L [i]
            i -= 1
        DEDENT
        L [i + 1] = valToInsert
    DEDENT
    return L
DEDENT

def quicksort(array, begin = 0, end = None) :
INDENT
    if end is None :
    INDENT
        end = len(array) - 1
    DEDENT
    def _quicksort(array, begin, end) :
    INDENT
        if begin > = end :
        INDENT
            return
        DEDENT
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)
    DEDENT
    return _quicksort(array, begin, end)
DEDENT

def file_filter(name, idtile) :
INDENT
    lst = []
    id_str = "%d %d " % idtile
    with open(name) as f :
    INDENT
        for line in f :
        INDENT
            if line.startswith(id_str) :
            INDENT
                element = line.split()
                lst.append(element [2 :])
                dy, dx = int(element [0]), int(element [1])
            DEDENT
        DEDENT
    DEDENT
    return (lst, dy, dx)
DEDENT

    def test_detail_object_does_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            self.client.get('/detail/doesnotexist/1/')

def seriesrun(x, n) :
INDENT
    result = 0
    term = 1
    for _ in range(n) :
    INDENT
        result += term
        term *= - x
    DEDENT
    return result
DEDENT

def add_months(date, months) :
INDENT
    months_count = date.month + months
    year = date.year + int(months_count / 12)
    month = (months_count % 12)
    if month == 0 :
    INDENT
        month = 12
    DEDENT
    day = date.day
    last_day_of_month = calendar.monthrange(year, month) [1]
    if day > last_day_of_month :
    INDENT
        day = last_day_of_month
    DEDENT
    new_date = datetime.date(year, month, day)
    return new_date
DEDENT

def outer() :
INDENT
    class context :
    INDENT
        y = 0
    DEDENT
    def inner() :
    INDENT
        context.y += 1
        return context.y
    DEDENT
    return inner
DEDENT

def evaluate(expr) :
INDENT
    if len(expr) == 3 :
    INDENT
        l, op, r = expr
        return ops [op](l, r)
    DEDENT
    else :
    INDENT
        for op_list in precedence :
        INDENT
            for op in expr :
            INDENT
                if op in op_list :
                INDENT
                    idx = expr.index(op) - 1
                    result = evaluate([expr.pop(idx) for i in range(3)])
                    expr.insert(idx, result)
                    return evaluate(expr)
                DEDENT
            DEDENT
        DEDENT
    DEDENT
DEDENT

def md5sum(filename) :
INDENT
    with open(filename, mode = 'rb') as f :
    INDENT
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b'') :
        INDENT
            d.update(buf)
        DEDENT
    DEDENT
    return d.hexdigest()
DEDENT

def wrapper(arg1) :
INDENT
    errors = []
    result = func(arg1)
    for k, v in result.iteritems() :
    INDENT
        error_nr = v % 2
        if error_nr > 0 :
        INDENT
            errors.append((k, v, error_nr))
        DEDENT
    DEDENT
    if errors :
    INDENT
        raise MyException, errors
    DEDENT
    return result
DEDENT

def convertType(value) :
INDENT
    try :
    INDENT
        return int(value) if value.strip().isdigit() else float(value)
    DEDENT
    except :
    INDENT
        return value
    DEDENT
DEDENT

    def test_detail_by_custom_pk(self):
        res = self.client.get('/detail/author/bycustompk/%s/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def fib(n) :
INDENT
    if n == 1 :
    INDENT
        return (1);
    DEDENT
    elif n == 0 :
    INDENT
        return (0);
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2);
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

def __str__(self) :
INDENT
    dd = (
        ("Car Type     %s", ''),
        ("  mpg:       %.1f", self.mpg),
        ("  hp:        %.2f", self.hp),
        ("  pc:        %i", self.pc),
        ("  unit cost: $%.2f", self.cost),
        ("  price:     $%.2f", self.price),
        )
    fmt = ''.join("%s\n" % t [0] for t in dd)
    return fmt % tuple(t [1] for t in dd)
DEDENT

    def test_detail_by_slug(self):
        res = self.client.get('/detail/author/byslug/scott-rosenberg/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], Author.objects.get(slug='scott-rosenberg'))
        self.assertEqual(res.context['author'], Author.objects.get(slug='scott-rosenberg'))
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def tail(f, n, offset = None) :
INDENT
    avg_line_length = 74
    to_read = n + (offset or 0)
    while 1 :
    INDENT
        try :
        INDENT
            f.seek(- (avg_line_length * to_read), 2)
        DEDENT
        except IOError :
        INDENT
            f.seek(0)
        DEDENT
        pos = f.tell()
        lines = f.read().splitlines()
        if len(lines) > = to_read or pos == 0 :
        INDENT
            return lines [- to_read : offset and - offset or None], len(lines) > to_read or pos > 0
        DEDENT
        avg_line_length *= 1.3
    DEDENT
DEDENT

def tail(the_file, lines_2find = 20) :
INDENT
    the_file.seek(0, 2)
    bytes_in_file = the_file.tell()
    lines_found, total_bytes_scanned = 0, 0
    while lines_2find + 1 > lines_found and bytes_in_file > total_bytes_scanned :
    INDENT
        byte_block = min(1024, bytes_in_file - total_bytes_scanned)
        the_file.seek(- (byte_block + total_bytes_scanned), 2)
        total_bytes_scanned += byte_block
        lines_found += the_file.read(1024).count('\n')
    DEDENT
    the_file.seek(- total_bytes_scanned, 2)
    line_list = list(the_file.readlines())
    return line_list [- lines_2find :]
DEDENT

def tail(f, window = 1) :
INDENT
    if window == 0 :
    INDENT
        return b''
    DEDENT
    BUFSIZE = 1024
    f.seek(0, 2)
    end = f.tell()
    nlines = window + 1
    data = []
    while nlines > 0 and end > 0 :
    INDENT
        i = max(0, end - BUFSIZE)
        nread = min(end, BUFSIZE)
        f.seek(i)
        chunk = f.read(nread)
        data.append(chunk)
        nlines -= chunk.count(b'\n')
        end -= nread
    DEDENT
    return b'\n'.join(b''.join(reversed(data)).splitlines() [- window :])
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

def strtr(strng, replace) :
INDENT
    if replace and strng :
    INDENT
        s, r = replace.popitem()
        return r.join(strtr(subs, dict(replace)) for subs in strng.split(s))
    DEDENT
    return strng
DEDENT

    def test_detail_by_custom_slug(self):
        res = self.client.get('/detail/author/bycustomslug/scott-rosenberg/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], Author.objects.get(slug='scott-rosenberg'))
        self.assertEqual(res.context['author'], Author.objects.get(slug='scott-rosenberg'))
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

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

def qsort(A, lo, hi) :
INDENT
    if lo < hi :
    INDENT
        p = partition(A, lo, hi)
        qsort(A, lo, p)
        qsort(A, p + 1, hi)
    DEDENT
DEDENT

def wrapper(arg1) :
INDENT
    result = func(arg1)
    for err in findError(result) :
    INDENT
        errors.append(err)
    DEDENT
    print errors
    return result
DEDENT

def __call__(self, * args) :
INDENT
    types = tuple(arg.__class__ for arg in args)
    function = self.typemap.get(types)
    if function is None :
    INDENT
        raise TypeError("no match")
    DEDENT
    return function(* args)
DEDENT

    def test_detail_by_pk_ignore_slug(self):
        res = self.client.get('/detail/author/bypkignoreslug/%s-roberto-bolano/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

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

def __new__(metacls, name, bases, attrs) :
INDENT
    assert "__slots__" in attrs
    attrs ["_ordered_slots"] = tuple(sorted(attrs ["__slots__"]))
    attrs ["__init__"] = create_init(attrs ["__slots__"])
    attrs ["__eq__"] = create_eq()
    attrs ["__str__"] = create_str()
    cls = super(MySlottedClassMeta, metacls).__new__(metacls, name, bases, attrs)
    return cls
DEDENT

def searchWordlist() :
INDENT
    path = str(raw_input(PATH))
    word = str(raw_input(WORD))
    loc = - 1
    with open(path) as f :
    INDENT
        for i, line in enumerate(f) :
        INDENT
            if word in line :
            INDENT
                loc = i
                break
            DEDENT
        DEDENT
    DEDENT
    if loc > = 0 :
    INDENT
        print ("Word found at line {}".format(loc))
    DEDENT
    else :
    INDENT
        print ("Word not found")
    DEDENT
DEDENT

def moto_boto() :
INDENT
    mock_s3().start()
    res = boto3.resource('s3')
    res.create_bucket(Bucket = BUCKET)
    yield
    mock_s3.stop()
DEDENT

def checksum(msg) :
INDENT
    s = 0
    for i in range(0, len(msg), 2) :
    INDENT
        w = ord(msg [i]) + (ord(msg [i + 1]) < < 8)
        s = carry_around_add(s, w)
    DEDENT
    return ~ s & 0xffff
DEDENT

def __init__(self, maxlen, * a, ** k) :
INDENT
    self.maxlen = maxlen
    self.d = dict(* a, ** k)
    while len(self) > maxlen :
    INDENT
        self.popitem()
    DEDENT
DEDENT

def completer(text, state) :
INDENT
    options = [i for i in commands if i.startswith(text)]
    if state < len(options) :
    INDENT
        return options [state]
    DEDENT
    else :
    INDENT
        return None
    DEDENT
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

    def test_detail_by_pk_ignore_slug_mismatch(self):
        res = self.client.get('/detail/author/bypkignoreslug/%s-scott-rosenberg/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def characters(nameLst) :
INDENT
    outLst = []
    for i in range(len(nameLst)) :
    INDENT
        outLst = outlst.append(len(nameLst))
    DEDENT
    return (outLst)
DEDENT

def __init__(self, items, attrs) :
INDENT
    super(IndexedList, self).__init__(items)
    self._attrs = tuple(attrs)
    self._index = {}
    _add = self._addindex
    for obj in self :
    INDENT
        _add(obj)
    DEDENT
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

def reverse(text) :
INDENT
    a = ""
    l = len(text)
    while (l > = 1) :
    INDENT
        a += text [l - 1]
        l -= 1
    DEDENT
    return a
DEDENT

    def test_detail_by_pk_and_slug(self):
        res = self.client.get('/detail/author/bypkandslug/%s-roberto-bolano/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def two_pair(ranks) :
INDENT
    if len(set(ranks)) ! = 3 :
    INDENT
        return None
    DEDENT
    pairs = []
    preceding = None
    for card in ranks :
    INDENT
        if card == preceding :
        INDENT
            pairs.append(card)
        DEDENT
        preceding = card
    DEDENT
    return tuple(pairs)
DEDENT

def is_magic(cube) :
INDENT
    """Check if cube is magic.
    There are two conditions that must be satisfied:
    1 - There must not be any repetitions of the numbers
    2 - All vertical/horizontal/diagonal sums must be 15
    """
    if not dupe(cube) and check_sum(cube) :
    INDENT
        print ('Valid')
    DEDENT
    else :
    INDENT
        print ('Invalid')
    DEDENT
DEDENT

def set_border(ws, cell_range) :
INDENT
    rows = ws.range(cell_range)
    for row in rows :
    INDENT
        row [0].style.borders.left.border_style = Border.BORDER_THIN
        row [- 1].style.borders.right.border_style = Border.BORDER_THIN
    DEDENT
    for c in rows [0] :
    INDENT
        c.style.borders.top.border_style = Border.BORDER_THIN
    DEDENT
    for c in rows [- 1] :
    INDENT
        c.style.borders.bottom.border_style = Border.BORDER_THIN
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

def __str__(self) :
INDENT
    left_str = self.left.__str__()
    right_str = self.right.__str__()
    op_str = self.symbol
    if self.left.precedence() > self.precedence() :
    INDENT
        left_str = '(' + left_str + ')'
    DEDENT
    if self.right.precedence() > self.precedence() :
    INDENT
        right_str = '(' + right_str + ')'
    DEDENT
    if operators [self.symbol] ['prec'] > = 30 :
    INDENT
        op_str = ' ' + op_str + ' '
    DEDENT
    return left_str + op_str + right_str
DEDENT

    def test_detail_by_pk_and_slug_mismatch_404(self):
        res = self.client.get('/detail/author/bypkandslug/%s-scott-rosenberg/' % self.author1.pk)
        self.assertEqual(res.status_code, 404)

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

def leafs_of_branch(node) :
INDENT
    leafs = []
    for des in node.children() :
    INDENT
        leafs.extend(leafs_of_branch(des))
    DEDENT
    if len(leafs) == 0 :
    INDENT
        leafs.append(str(node))
    DEDENT
    return leafs
DEDENT

def tariter(filename) :
INDENT
    with tarfile.open(filename) as archive :
    INDENT
        for tarinfo in archive :
        INDENT
            if tarinfo.isreg() :
            INDENT
                handle = archive.extractfile(tarinfo.name)
                data = handle.read()
                handle.close()
                yield tarinfo, data
            DEDENT
        DEDENT
    DEDENT
DEDENT

def permutation(list) :
INDENT
    if len(list) == 0 :
    INDENT
        return [[]]
    DEDENT
    else :
    INDENT
        return [[x] + ys for x in list for ys in permutation(delete(list, x))]
    DEDENT
DEDENT

    def test_verbose_name(self):
        res = self.client.get('/detail/artist/%s/' % self.artist1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.artist1)
        self.assertEqual(res.context['artist'], self.artist1)
        self.assertTemplateUsed(res, 'generic_views/artist_detail.html')

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

def file_len(fname) :
INDENT
    counts = itertools.count()
    with open(fname) as f :
    INDENT
        for _ in f : counts.next()
    DEDENT
    return counts.next()
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

def _connect_string(self) :
INDENT
    settings_dict = self.settings_dict
    if not settings_dict ['HOST'].strip() :
    INDENT
        settings_dict ['HOST'] = 'localhost'
    DEDENT
    if settings_dict ['PORT'].strip() :
    INDENT
        dsn = Database.makedsn(settings_dict ['HOST'],
            int(settings_dict ['PORT']),
            settings_dict ['NAME'])
    DEDENT
    else :
    INDENT
        dsn = settings_dict ['NAME']
    DEDENT
    return "%s/%s@%s" % (settings_dict ['USER'],
        settings_dict ['PASSWORD'], dsn)
DEDENT

def reverse(text) :
INDENT
    a = ""
    l = len(text)
    while (l > = 1) :
    INDENT
        a += text [l - 1]
        l -= 1
    DEDENT
    return a
DEDENT

    def test_template_name(self):
        res = self.client.get('/detail/author/%s/template_name/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/about.html')

def __init__(self) :
INDENT
    self.root = Tk.Tk()
    self.root.wm_title("Fibonacci Calculator")
    self.label = Tk.Label(self.root, text = "Set the digit number you want.")
    self.label.pack()
    self.digits = Tk.StringVar()
    Tk.Entry(self.root, textvariable = self.digits).pack()
    self.buttontext = Tk.StringVar()
    self.buttontext.set("Calculate")
    Tk.Button(self.root,
        textvariable = self.buttontext,
        command = self.clicked1).pack()
    self.label = Tk.Label(self.root, text = " ")
    self.label.pack()
    self.root.mainloop()
DEDENT

def get(self, request, * args, ** kwargs) :
INDENT
    objkey = self.kwargs.get('pk', None)
    pdf = get_object_or_404(Pdf, pk = objkey)
    fname = pdf.filename()
    path = os.path.join(settings.MEDIA_ROOT, 'docs\\' + fname)
    response = FileResponse(open(path, 'rb'), content_type = "application/pdf")
    response ["Content-Disposition"] = "filename={}".format(fname)
    return response
DEDENT

def get_file_list(directory = '.') :
INDENT
    files = []
    for i in os.listdir(directory) :
    INDENT
        if os.path.isdir(i) :
        INDENT
            files.extend(get_file_list(i))
        DEDENT
        else :
        INDENT
            files.append(i)
        DEDENT
    DEDENT
    return files
DEDENT

def merge(xs, ys) :
INDENT
    xs = iter(xs)
    ys = iter(ys)
    try :
    INDENT
        y = next(ys)
    DEDENT
    except StopIteration :
    INDENT
        for x in xs :
        INDENT
            yield x
        DEDENT
        raise StopIteration
    DEDENT
    while True :
    INDENT
        for x in xs :
        INDENT
            if x > y :
            INDENT
                yield y
                break
            DEDENT
            yield x
        DEDENT
        else :
        INDENT
            yield y
            for y in ys :
            INDENT
                yield y
            DEDENT
            break
        DEDENT
        xs, ys, y = ys, xs, x
    DEDENT
DEDENT

def json_debug_handler(obj) :
INDENT
    obj = obj.originalObject
    print ("object received:")
    print type(obj)
    print ("\n\n")
    if isinstance(obj, datetime.datetime) :
    INDENT
        return obj.isoformat()
    DEDENT
    elif isinstance(obj, mDict) :
    INDENT
        return {'orig' : obj, 'attrs' : vars(obj)}
    DEDENT
    elif isinstance(obj, mList) :
    INDENT
        return {'orig' : obj, 'attrs' : vars(obj)}
    DEDENT
    else :
    INDENT
        return obj
    DEDENT
DEDENT

    def test_template_name_suffix(self):
        res = self.client.get('/detail/author/%s/template_name_suffix/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['author'], self.author1)
        self.assertTemplateUsed(res, 'generic_views/author_view.html')

def __init__(self, parent) :
INDENT
    tk.Frame.__init__(self, parent)
    t = ScrolledText(self, wrap = "word")
    t.insert("end", "Hello\nworld")
    t.configure(state = "disabled")
    t.pack(side = "top", fill = "both", expand = True)
    t.bind("<1>", lambda event : t.focus_set())
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

def __init__(self, parent) :
INDENT
    wx.Dialog.__init__(self, parent, - 1, "Validated Dialog")
    self.SetAutoLayout(True)
    VSPACE = 10
    fgs = wx.FlexGridSizer(0, 2)
    fgs.Add((1, 1));
    fgs.Add(wx.StaticText(self, - 1,
            "These controls must have text entered into them.  Each\n"
            "one has a validator that is checked when the Okay\n"
            "button is clicked."))
    fgs.Add((1, VSPACE)); fgs.Add((1, VSPACE))
    label = wx.StaticText(self, - 1, "First: ")
    fgs.Add(label, 0, wx.ALIGN_RIGHT | wx.CENTER)
    fgs.Add(wx.TextCtrl(self, - 1, "", validator = TextObjectValidator()))
    fgs.Add((1, VSPACE)); fgs.Add((1, VSPACE))
    label = wx.StaticText(self, - 1, "Second: ")
    fgs.Add(label, 0, wx.ALIGN_RIGHT | wx.CENTER)
    fgs.Add(wx.TextCtrl(self, - 1, "", validator = TextObjectValidator()))
    buttons = wx.StdDialogButtonSizer()
    b = wx.Button(self, wx.ID_OK, "OK")
    b.SetDefault()
    buttons.AddButton(b)
    buttons.AddButton(wx.Button(self, wx.ID_CANCEL, "Cancel"))
    buttons.Realize()
    border = wx.BoxSizer(wx.VERTICAL)
    border.Add(fgs, 1, wx.GROW | wx.ALL, 25)
    border.Add(buttons)
    self.SetSizer(border)
    border.Fit(self)
    self.Layout()
DEDENT

def printPascal(n) :
INDENT
    Pascal_List = []
    if n == 0 :
    INDENT
        Pascal_List.append([1])
        return Pascal_List
    DEDENT
    if n == 1 :
    INDENT
        Pascal_List.append([1])
        Pascal_List.append([1, 1])
        return Pascal_List
    DEDENT
    else :
    INDENT
        new_row = [1]
        final_r = printPascal(n - 1)
        last_row = final_r [- 1]
        for k in range(len(last_row) - 1) :
        INDENT
            new_row.append(last_row [k] + last_row [k + 1])
        DEDENT
        new_row.append(1)
        final_r.append(new_row)
        return final_r
    DEDENT
DEDENT

def matched(str) :
INDENT
    count = 0
    for i in str :
    INDENT
        if i == "(" :
        INDENT
            count += 1
        DEDENT
        elif i == ")" :
        INDENT
            count -= 1
        DEDENT
        if count < 0 :
        INDENT
            return False
        DEDENT
    DEDENT
    return count == 0
DEDENT

    def test_template_name_field(self):
        res = self.client.get('/detail/page/%s/field/' % self.page1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.page1)
        self.assertEqual(res.context['page'], self.page1)
        self.assertTemplateUsed(res, 'generic_views/page_template.html')

def char_first_index(s, c) :
INDENT
    if len(s) == 0 :
    INDENT
        return None
    DEDENT
    elif s [0] == c :
    INDENT
        return 0
    DEDENT
    else :
    INDENT
        count = char_first_index(s [1 :], c)
        if count ! = None :
        INDENT
            return count + 1
        DEDENT
        else :
        INDENT
            return None
        DEDENT
    DEDENT
DEDENT

def scan(sentence) :
INDENT
    tuples = []
    words = sentence.split()
    for word in words :
    INDENT
        try :
        INDENT
            tuples.append((lexicons [word], word))
        DEDENT
        except KeyError :
        INDENT
            if word.isdigit() :
            INDENT
                tuples.append(('number', int(word)))
            DEDENT
            else :
            INDENT
                tuples.append(('error', word))
            DEDENT
        DEDENT
    DEDENT
    return tuples
DEDENT

def read_file() :
INDENT
    if os.path.exists('InputFile.bak') :
    INDENT
        with open('InputFile.bak', 'rb') as fname :
        INDENT
            while True :
            INDENT
                try :
                INDENT
                    item_name = cPickle.load(fname)
                    for k, v in item_name.iteritems() :
                    INDENT
                        print v [0], "\t", v [1], "\t", k
                    DEDENT
                DEDENT
                except EOFError :
                INDENT
                    break
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    else :
    INDENT
        item_name = {}
    DEDENT
DEDENT

    def test_context_object_name(self):
        res = self.client.get('/detail/author/%s/context_object_name/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertEqual(res.context['thingy'], self.author1)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def fib(lowerbound, upperbound) :
INDENT
    x = 0
    y = 1
    while x < = upperbound :
    INDENT
        if (x > = lowerbound) :
        INDENT
            yield x
        DEDENT
        x, y = y, x + y
    DEDENT
DEDENT

def curry(func) :
INDENT
    def curried(* args, ** kwargs) :
    INDENT
        if len(args) + len(kwargs) > = func.__code__.co_argcount :
        INDENT
            return func(* args, ** kwargs)
        DEDENT
        return (lambda * args2, ** kwargs2 :
            curried(* (args + args2), ** dict(kwargs, ** kwargs2)))
    DEDENT
    return curried
DEDENT

    def test_duplicated_context_object_name(self):
        res = self.client.get('/detail/author/%s/dupe_context_object_name/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.author1)
        self.assertNotIn('author', res.context)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def sum67(nbrs) :
INDENT
    total = 0
    accum = 1
    for nbr in nbrs :
    INDENT
        if nbr == 6 :
        INDENT
            accum = 0
        DEDENT
        total += nbr * accum
        if accum == 0 and nbr == 7 :
        INDENT
            accum = 1
        DEDENT
    DEDENT
    return total
DEDENT

def read_relationship(filename) :
INDENT
    data = []
    with open(filename) as f :
    INDENT
        f.next()
        for line in f :
        INDENT
            try :
            INDENT
                parts = line.rstrip().split('\t')
                query_name = parts [0]
                subject_name = parts [1]
                query_start = parts [2]
                query_end = parts [3]
                subject_start = parts [4]
                subject_end = parts [5]
                item = {
                    'source' : {
                        'id' : query_name,
                        'start' : subject_name,
                        'end' : query_start},
                    'target' : {
                        'id' : query_end,
                        'start' : subject_start,
                        'end' : subject_end}}
                data.append(item)
            DEDENT
            except ValueError :
            INDENT
                pass
            DEDENT
        DEDENT
    DEDENT
    with open('data/data.txt', 'w') as outfile :
    INDENT
        json.dump(data, outfile)
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

def replace_runs(a, N, replace = 2) :
INDENT
    a_copy = a.copy()
    pattern = np.ones(N, dtype = int)
    M = a_copy.shape [1]
    for i, row in enumerate(a_copy) :
    INDENT
        conv = np.convolve(row, pattern, mode = 'same')
        match = np.where(conv == N)
        a_copy [i] [match] = replace
        a_copy [i] [match [0] [match [0] - 1 > 0] - 1] = replace
        a_copy [i] [match [0] [match [0] + 1 < M] + 1] = replace
    DEDENT
    return a_copy
DEDENT

def tail(f, n) :
INDENT
    assert n > = 0
    pos, lines = n + 1, []
    while len(lines) < = n :
    INDENT
        try :
        INDENT
            f.seek(- pos, 2)
        DEDENT
        except IOError :
        INDENT
            f.seek(0)
            break
        DEDENT
        finally :
        INDENT
            lines = list(f)
        DEDENT
        pos *= 2
    DEDENT
    return lines [- n :]
DEDENT

def add(self, key, left_key = None, right_key = None) :
INDENT
    if key not in self.nodes :
    INDENT
        self.nodes [key] = BinaryTreeNode(key)
    DEDENT
    if left_key is None :
    INDENT
        self.nodes [key].left = None
    DEDENT
    else :
    INDENT
        if left_key not in self.nodes :
        INDENT
            self.nodes [left_key] = BinaryTreeNode(left_key)
        DEDENT
        self.nodes [key].left = self.nodes [left_key]
    DEDENT
    if right_key == None :
    INDENT
        self.nodes [key].right = None
    DEDENT
    else :
    INDENT
        if right_key not in self.nodes :
        INDENT
            self.nodes [right_key] = BinaryTreeNode(right_key)
        DEDENT
        self.nodes [key].right = self.nodes [right_key]
    DEDENT
DEDENT

def factorial(n) :
INDENT
    result = 1
    i = n * (n - 1)
    while n > = 1 :
    INDENT
        result = result * n
        n = n - 1
    DEDENT
    return result
DEDENT

    def test_custom_detail(self):
        """
        AuthorCustomDetail overrides get() and ensures that
        SingleObjectMixin.get_context_object_name() always uses the obj
        parameter instead of self.object.
        """
        res = self.client.get('/detail/author/%s/custom_detail/' % self.author1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['custom_author'], self.author1)
        self.assertNotIn('author', res.context)
        self.assertNotIn('object', res.context)
        self.assertTemplateUsed(res, 'generic_views/author_detail.html')

def outer() :
INDENT
    def setlist(newlist) :
    INDENT
        mylist = newlist
    DEDENT
    mylist = []
    def inner() :
    INDENT
        setlist(['new_list'])
    DEDENT
    inner()
DEDENT

def stemming(verb) :
INDENT
    suffix = ["ing", "ed", "es", "s"]
    for i in suffix :
    INDENT
        verb = verb.replace(i, "")
    DEDENT
    return verb
DEDENT

    def test_deferred_queryset_template_name(self):
        class FormContext(SingleObjectTemplateResponseMixin):
            request = RequestFactory().get('/')
            model = Author
            object = Author.objects.defer('name').get(pk=self.author1.pk)

        self.assertEqual(FormContext().get_template_names()[0], 'generic_views/author_detail.html')

def save(self, * args, ** kwargs) :
INDENT
    if self.id :
    INDENT
        super(Book, self).save(* args, ** kwargs)
        return
    DEDENT
    unique = False
    while not unique :
    INDENT
        try :
        INDENT
            self.id = uuid4().hex
            super(Book, self).save(* args, ** kwargs)
        DEDENT
        except IntegrityError :
        INDENT
            self.id = uuid4().hex
        DEDENT
        else :
        INDENT
            unique = True
        DEDENT
    DEDENT
DEDENT

def main() :
INDENT
    for line in data.split("\n") :
    INDENT
        items = list(map(int, line.split()))
        print (is_magic(items))
    DEDENT
DEDENT

def __exit__(self, et, ev, tb) :
INDENT
    if self.level is not None :
    INDENT
        self.logger.setLevel(self.old_level)
    DEDENT
    if self.handler :
    INDENT
        self.logger.removeHandler(self.handler)
    DEDENT
    if self.handler and self.close :
    INDENT
        self.handler.close()
    DEDENT
DEDENT

def bitwise_or(num1, num2) :
INDENT
    new_num1 = []
    new_num2 = []
    new_num = []
    for c in num1 [2 :] :
    INDENT
        new_num1.append(c)
    DEDENT
    for c in num2 [2 :] :
    INDENT
        new_num2.append(c)
    DEDENT
    if len(num1) ! = len(num2) :
    INDENT
        if len(num1) > len(num2) :
        INDENT
            diff1 = ["0"] * (len(num1) - len(num2))
            new_num2 = diff1 + new_num2
        DEDENT
        if len(num1) < len(num2) :
        INDENT
            diff1 = ["0"] * (len(num2) - len(num1))
            new_num1 = diff1 + new_num1
        DEDENT
    DEDENT
    for i in range(len(new_num1)) :
    INDENT
        if new_num1 [i] == "1" or new_num2 [i] == "1" :
        INDENT
            new_num.append("1")
        DEDENT
        else :
        INDENT
            new_num.append(new_num1 [i])
        DEDENT
    DEDENT
    final = "".join(new_num)
    return final
DEDENT

def __init__(self, parent, move_widget) :
INDENT
    super(Grip, self).__init__(parent)
    self.move_widget = move_widget
    self.setText("+")
    self.min_height = 50
    self.mouse_start = None
    self.height_start = self.move_widget.height()
    self.resizing = False
    self.setMouseTracking(True)
    self.setCursor(QtCore.Q.SizeVerCursor)
DEDENT

def remove_adjacent(nums) :
INDENT
    a = nums [: 1]
    for item in nums [1 :] :
    INDENT
        if item ! = a [- 1] :
        INDENT
            a.append(item)
        DEDENT
    DEDENT
    return a
DEDENT

def send_mail(send_from, send_to, subject, text, files = None,
server = "127.0.0.1") :
INDENT
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg ['From'] = send_from
    msg ['To'] = COMMASPACE.join(send_to)
    msg ['Date'] = formatdate(localtime = True)
    msg ['Subject'] = subject
    msg.attach(MIMEText(text))
    for f in files or [] :
    INDENT
        with open(f, "rb") as fil :
        INDENT
            part = MIMEApplication(
                fil.read(),
                Name = basename(f))
        DEDENT
        part ['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    DEDENT
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
DEDENT

    def test_deferred_queryset_context_object_name(self):
        class FormContext(ModelFormMixin):
            request = RequestFactory().get('/')
            model = Author
            object = Author.objects.defer('name').get(pk=self.author1.pk)
            fields = ('name',)

        form_context_data = FormContext().get_context_data()
        self.assertEqual(form_context_data['object'], self.author1)
        self.assertEqual(form_context_data['author'], self.author1)

def main() :
INDENT
    derived_type = type('Derived', (FooClass,), {'FooMethod' : None})
    def BarOverride(self) :
    INDENT
        print 'Hello, world!'
    DEDENT
    setattr(derived_type, 'FooMethod', BarOverride)
    instance = derived_type()
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

def __init__(self, enums) :
INDENT
    if isinstance(enums, dict) :
    INDENT
        self.__dict__.update(enums)
    DEDENT
    elif isinstance(enums, list) or isinstance(enums, tuple) :
    INDENT
        self.__dict__.update(** dict((v, k) for k, v in enumerate(enums)))
    DEDENT
    else :
    INDENT
        raise EnumTypeError
    DEDENT
DEDENT

def _add(self, val, node) :
INDENT
    if (val < node.v) :
    INDENT
        if (node.l ! = None) :
        INDENT
            self._add(val, node.l)
        DEDENT
        else :
        INDENT
            node.l = Node(val)
        DEDENT
    DEDENT
    else :
    INDENT
        if (node.r ! = None) :
        INDENT
            self._add(val, node.r)
        DEDENT
        else :
        INDENT
            node.r = Node(val)
        DEDENT
    DEDENT
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

    def test_invalid_url(self):
        with self.assertRaises(AttributeError):
            self.client.get('/detail/author/invalid/url/')

def __init__(self, localport, remoteport, remoteuser, remotehost) :
INDENT
    threading.Thread.__init__(self)
    self.localport = localport
    self.remoteport = remoteport
    self.remoteuser = remoteuser
    self.remotehost = remotehost
    self.daemon = True
DEDENT

def countSubStringMatchRecursive(target, key) :
INDENT
    index = find(target, key)
    if index > - 1 :
    INDENT
        return countSubStringMatchRecursive(target [index + 1 :], key) + 1
    DEDENT
    return 0
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

    def test_invalid_queryset(self):
        msg = (
            'AuthorDetail is missing a QuerySet. Define AuthorDetail.model, '
            'AuthorDetail.queryset, or override AuthorDetail.get_queryset().'
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/detail/author/invalid/qs/')

def get_form_instance(self, step) :
INDENT
    if not self.instance :
    INDENT
        if 'initial_id' in self.kwargs :
        INDENT
            initial_id = self.kwargs ['initial_id']
            self.instance = Project.objects.get(id = initial_id)
        DEDENT
        else :
        INDENT
            self.instance = Project()
        DEDENT
    DEDENT
    return self.instance
DEDENT

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

def square(x) :
INDENT
    if isinstance(x, int) :
    INDENT
        return x ** 2
    DEDENT
    elif isinstance(x, list) :
    INDENT
        return [square(b) for b in x]
    DEDENT
    else :
    INDENT
        raise ValueError("Only ints and list of ints/list of ints allowed")
    DEDENT
DEDENT

def transitive_closure(a) :
INDENT
    closure = set(a)
    while True :
    INDENT
        new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)
        closure_until_now = closure | new_relations
        if closure_until_now == closure :
        INDENT
            break
        DEDENT
        closure = closure_until_now
    DEDENT
    return closure
DEDENT

def get_dir_size(path) :
INDENT
    total_size = 0
    try :
    INDENT
        items = FindFilesW(path + r'\*')
    DEDENT
    except pywintypes.error, ex :
    INDENT
        return total_size
    DEDENT
    for item in items :
    INDENT
        total_size += item [5]
        if (item [0] & MASK == REQUIRED) :
        INDENT
            name = item [8]
            if name not in DIR_EXCLUDES :
            INDENT
                total_size += get_dir_size(path + '\\' + name)
            DEDENT
        DEDENT
    DEDENT
    return total_size
DEDENT

    def test_non_model_object_with_meta(self):
        res = self.client.get('/detail/nonmodel/1/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'].id, "non_model_1")
def upgrade() :
INDENT
    url = context.config.get_main_option("sqlalchemy.url")
    engine = sa.create_engine(url)
    DBSession.configure(bind = engine)
    op.create_table(
        'client_credential',
        sa.Column('id', sa.Integer(), nullable = False),
        sa.Column('created_at', sa.DateTime(), nullable = False),
        sa.Column('updated_at', sa.DateTime(), nullable = False),
        sa.Column('client_id', sa.Integer(), nullable = False),
        sa.Column('key', sa.String(length = 22), nullable = False),
        sa.Column('secret', sa.String(length = 44), nullable = False),
        sa.Column('is_active', sa.Boolean(), nullable = False),
        sa.ForeignKeyConstraint(['client_id'], ['client.id'],),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('key'))
    clients = [
        {'secret' : client.secret,
            'key' : client.key,
            'is_active' : True,
            'client_id' : client.id,
            'created_at' : sa.func.now(),
            'updated_at' : sa.func.now()} for client in Client.query.all()]
    op.bulk_insert(ClientCredential, clients)
    op.drop_column(u'client', u'secret')
    op.drop_column(u'client', u'key')
DEDENT

def flatten(some_list) :
INDENT
    for element in some_list :
    INDENT
        if type(element) in (tuple, list) :
        INDENT
            for item in flatten(element) :
            INDENT
                yield item
            DEDENT
        DEDENT
        else :
        INDENT
            yield element
        DEDENT
    DEDENT
DEDENT

def sum13(nums) :
INDENT
    if 13 in nums :
    INDENT
        index13 = nums.index(13)
        del nums [index13 : index13 + 2]
        return sum13(nums)
    DEDENT
    else :
    INDENT
        return sum(nums)
    DEDENT
DEDENT

def same_structure(a, b) :
INDENT
    if len(a) ! = len(b) :
    INDENT
        return False
    DEDENT
    return all(is_list(x) and is_list(y) and same_structure(x, y) or
        not is_list(x) and not is_list(y) for x, y in zip(a, b))
DEDENT

def remove_user(self, user) :
INDENT
    if hasattr(user, "name") :
    INDENT
        self.remove(user.name)
    DEDENT
    else :
    INDENT
        self.remove(user)
    DEDENT
DEDENT


























































































































