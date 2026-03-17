import time

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase, override_settings
from django.test.utils import require_jinja2
from django.urls import resolve
from django.views.generic import RedirectView, TemplateView, View

from . import views


class SimpleView(View):
    """
    A simple view with a docstring.
    """
    def get(self, request):
        return HttpResponse('This is a simple view')


def get_icon_path(mimetype, size = 32) :
INDENT
    icon = Gio.content_type_get_icon(mimetype)
    theme = Gtk.IconTheme.get_default()
    info = theme.choose_icon(icon.get_names(), size, 0)
    if info :
    INDENT
        print (info.get_filename())
    DEDENT
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

def combine_word_documents(files) :
INDENT
    combined_document = Document('empty.docx')
    count, number_of_files = 0, len(files)
    for file in files :
    INDENT
        sub_doc = Document(file)
        if count < number_of_files - 1 :
        INDENT
            sub_doc.add_page_break()
        DEDENT
        for element in sub_doc._document_part.body._element :
        INDENT
            combined_document._document_part.body._element.append(element)
        DEDENT
        count += 1
    DEDENT
    combined_document.save('combined_word_documents.docx')
DEDENT

class SimplePostView(SimpleView):
    post = SimpleView.get


class PostOnlyView(View):
    def post(self, request):
        return HttpResponse('This view only accepts POST')


def __init__(self, * args, ** kwargs) :
INDENT
    super(Map, self).__init__(* args, ** kwargs)
    for arg in args :
    INDENT
        if isinstance(arg, dict) :
        INDENT
            for k, v in arg.iteritems() :
            INDENT
                self [k] = v
            DEDENT
        DEDENT
    DEDENT
    if kwargs :
    INDENT
        for k, v in kwargs.iteritems() :
        INDENT
            self [k] = v
        DEDENT
    DEDENT
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

def fib(n) :
INDENT
    a = 0
    b = 1
    for i in range(1, n + 1) :
    INDENT
        c = a + b
        print c
        a = b
        b = c
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

def partition(array, begin, end) :
INDENT
    pivot = begin
    for i in xrange(begin + 1, end + 1) :
    INDENT
        if array [i] < = array [begin] :
        INDENT
            pivot += 1
            array [i], array [pivot] = array [pivot], array [i]
        DEDENT
    DEDENT
    array [pivot], array [begin] = array [begin], array [pivot]
    return pivot
DEDENT

def checkLen() :
INDENT
    days = ["Monday", "Tuesday", "Wednesday", "Thursday" "Friday", "Saturday", "Sunday"]
    try :
    INDENT
        position = days.index("Monday")
        print ("Found it")
    DEDENT
    except ValueError :
    INDENT
        position = None
        print ("Not present")
    DEDENT
    print (position)
DEDENT

class CustomizableView(SimpleView):
    parameter = {}


def decorator(view):
    view.is_decorated = True
    return view


def ask_digit(calls = 0) :
INDENT
    if calls > 10 :
    INDENT
        print "You are so boring..."
        raise ValueError("Can't get answer from user")
    DEDENT
    try :
    INDENT
        num = int(raw_input("Enter number 1-5: "))
    DEDENT
    except ValueError :
    INDENT
        print "Not a digit"
        return ask_digit(calls + 1)
    DEDENT
    if num < 1 or num > 5 :
    INDENT
        print "Not valid"
        return ask_digit(calls + 1)
    DEDENT
    return num
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

class DecoratedDispatchView(SimpleView):

    @decorator
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def run(self, timeout) :
INDENT
    def target() :
    INDENT
        print 'Thread started'
        self.process = subprocess.Popen(self.cmd, shell = True)
        self.process.communicate()
        print 'Thread finished'
    DEDENT
    thread = threading.Thread(target = target)
    thread.start()
    thread.join(timeout)
    if thread.is_alive() :
    INDENT
        print 'Terminating process'
        self.process.terminate()
        thread.join()
    DEDENT
    print self.process.returncode
DEDENT

def run(self) :
INDENT
    while True :
    INDENT
        frameNum, frameData = self.task_queue.get()
        m = random.randint(0, 1000000)
        while m > = 0 :
        INDENT
            m -= 1
        DEDENT
        self.result_queue.put("result from image " + str(frameNum))
    DEDENT
    return
DEDENT

def is_valid_hostname(hostname) :
INDENT
    if len(hostname) > 255 :
    INDENT
        return False
    DEDENT
    hostname = hostname.rstrip(".")
    allowed = re.compile("(?!-)[A-Z\d\-\_]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))
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

def sigmoid(x) :
INDENT
    "Numerically-stable sigmoid function."
    if x > = 0 :
    INDENT
        z = exp(- x)
        return 1 / (1 + z)
    DEDENT
    else :
    INDENT
        z = exp(x)
        return z / (1 + z)
    DEDENT
DEDENT

class AboutTemplateView(TemplateView):
    def get(self, request):
        return self.render_to_response({})

def run(self) :
INDENT
    self.socket.listen(5)
    while True :
    INDENT
        print 'Waiting for connection..'
        client, caddr = self.socket.accept()
        print 'Connected To', caddr
        data = client.recv(self.bufsize)
        if not data :
        INDENT
            continue
        DEDENT
        print data
    DEDENT
DEDENT

def __init__(self) :
INDENT
    self.window = gtk.Window()
    self.window.set_size_request(100, 150)
    self.window.connect("delete_event", self.delete_event)
    vbox = gtk.VBox()
    buttons = Buttons()
    vbox.pack_start(buttons.hbox, False, False, 1)
    vbox.pack_start(Lister(buttons).hbox)
    self.window.add(vbox)
    self.window.show_all()
    return
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

    def get_template_names(self):
        return ['generic_views/about.html']


def __setattr__(self, name, value) :
INDENT
    if not hasattr(self, name) :
    INDENT
        raise AttributeError("Model instances do not accept arbitrary attributes")
    DEDENT
    else :
    INDENT
        object.__setattr__(self, name, value)
    DEDENT
DEDENT

class AboutTemplateAttributeView(TemplateView):
    template_name = 'generic_views/about.html'

    def get(self, request):
        return self.render_to_response(context={})


def run(cmd, timeout_sec) :
INDENT
    proc = Popen(shlex.split(cmd), stdout = PIPE, stderr = PIPE)
    timer = Timer(timeout_sec, proc.kill)
    try :
    INDENT
        timer.start()
        stdout, stderr = proc.communicate()
    DEDENT
    finally :
    INDENT
        timer.cancel()
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

def avg(self) :
INDENT
    for items in self :
    INDENT
        if not isinstance(items, int) :
        INDENT
            raise ValueError('Invalid item in list. All items need to be an integer.')
        DEDENT
    DEDENT
    return sum(self) / len(self)
DEDENT

class InstanceView(View):

    def get(self, request):
        return self


def visit_Call(self, node) :
INDENT
    if (node.func.id == self.fnName) :
    INDENT
        if len(node.args) == len(self.varNames) :
        INDENT
            print "expand call to " + self.fnName + "(" + (", ".join(self.varNames)) + ")" + " with arguments " + ", ".join(map(toSource, node.args))
            old_node = node
            args = map(self.visit, node.args)
            names = dict(zip(self.varNames, args))
            node = substitute(self.fnExpr, names)
            self.modified = True
            return node
        DEDENT
        else :
        INDENT
            raise Exception("invalid arity " + toSource(node))
        DEDENT
    DEDENT
    else :
    INDENT
        return self.generic_visit(node)
    DEDENT
DEDENT

def sub_seq(li, n) :
INDENT
    d = defaultdict(list)
    rle = [(k, len(list(g))) for k, g in groupby(li)]
    endpoints = accumulate(size for k, size in rle)
    for end_index, (value, count) in zip(endpoints, rle) :
    INDENT
        for index in range(end_index - count, end_index - n + 1) :
        INDENT
            d [value].append(index)
        DEDENT
    DEDENT
    return dict(d)
DEDENT

def on_success(self, data) :
INDENT
    if dt.datetime.now() > self.stop_time :
    INDENT
        raise Exception('Time expired')
    DEDENT
    fileName = self.fileDirectory + 'Tweets_' + dt.datetime.now().strftime("%Y_%m_%d_%H") + '.txt'
    open(fileName, 'a').write(json.dumps(data) + '\n')
DEDENT

def next_bigger(n) :
INDENT
    arr = [int(x) for x in str(n)]
    i = len(arr) - 1
    while i > 0 and arr [i - 1] > = arr [i] :
    INDENT
        i -= 1
    DEDENT
    if i < = 0 :
    INDENT
        return - 1
    DEDENT
    j = len(arr) - 1
    while arr [j] < = arr [i - 1] :
    INDENT
        j -= 1
    DEDENT
    arr [i - 1], arr [j] = arr [j], arr [i - 1]
    arr [i :] = arr [len(arr) - 1 : i - 1 : - 1]
    return int(''.join(str(x) for x in arr))
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

class ViewTest(SimpleTestCase):
    rf = RequestFactory()

    def _assert_simple(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a simple view')

def index(filename, lst) :
INDENT
    with open(filename, 'r') as infile :
    INDENT
        lines = [line.split() for line in infile]
    DEDENT
    word2linenumbers = defaultdict(list)
    for linenumber, line in enumerate(lines, 1) :
    INDENT
        for word in line :
        INDENT
            if word in lst :
            INDENT
                word2linenumbers [word].append(linenumber)
            DEDENT
        DEDENT
    DEDENT
    return word2linenumbers
DEDENT

def scraper(pageNum) :
INDENT
    req = Request("http://www.someurl.com/Search/page=" + str(pageNum) + "&facet_Category=20", headers = {"User-Agent" : "Mozilla/5.0"})
    html = urlopen(req).read()
    bsObj = BeautifulSoup(html)
    for result in bsObj.select("h2 a") :
    INDENT
        print (result ["href"])
    DEDENT
    scraper(pageNum + 1)
DEDENT

def print_table(data, cols, wide) :
INDENT
    n, r = divmod(len(data), cols)
    pat = '{{:{}}}'.format(wide)
    line = '\n'.join(pat * cols for _ in range(n))
    last_line = pat * r
    print (line.format(* data))
    print (last_line.format(* data [n * cols :]))
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    super(ContestForm, self).__init__(* args, ** kwargs)
    self.fields.keyOrder = [
        'name',
        'description',
        'image',
        'video_link',
        'category']
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

    def test_no_init_kwargs(self):
        """
        A view can't be accidentally instantiated before deployment
        """
        msg = 'This method is available only on the class, not on instances.'
        with self.assertRaisesMessage(AttributeError, msg):
            SimpleView(key='value').as_view()

def transformFactorList(factorList) :
INDENT
    oldsize = len(factorList)
    factorList = [f for f in factorList if f ! = 2]
    num2s = oldsize - len(factorList)
    if num2s == 0 :
    INDENT
        return []
    DEDENT
    if num2s == 1 :
    INDENT
        return [2] + factorList
        return ['2 ^ %s' % num2s] + [factorList]
    DEDENT
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
    index_list = []
    for model_index in self.view.selectionModel().selectedRows() :
    INDENT
        index = QPersistentModelIndex(model_index)
        index_list.append(index)
    DEDENT
    for index in index_list :
    INDENT
        model.removeRow(index.row())
    DEDENT
DEDENT

def __getitem__(self, keys) :
INDENT
    if isinstance(keys, str) :
    INDENT
        return super().__getitem__(keys)
    DEDENT
    cur = self
    for key in keys :
    INDENT
        cur = cur.get(key, {})
    DEDENT
    return cur
DEDENT

def swap(inp) :
INDENT
    inp = inp.split()
    out = []
    d1 = ['i am', 'you are', 'i\'m', 'you\'re', 'my', 'your', 'I', 'my', 'you']
    d2 = ['you are', 'I am', 'you\'re', 'I\'m', 'your', 'my', 'you', 'your', 'I']
    for item in inp :
    INDENT
        itm = item.replace(',', '')
        if itm not in d1 :
        INDENT
            out.append(item)
        DEDENT
        else : out.append(d2 [d1.index(itm)])
    DEDENT
    return ' '.join(out)
    print (swap('you love your version of my couch because I love you, and you\'re a couch-lover.'))
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

    def test_no_init_args(self):
        """
        A view can't be accidentally instantiated before deployment
        """
        msg = 'as_view() takes 1 positional argument but 2 were given'
        with self.assertRaisesMessage(TypeError, msg):
            SimpleView.as_view('value')

def main(data) :
INDENT
    global how_many
    atexit.register(cleanup, len(data))
    db = DB()
    skip = False
    if how_many :
    INDENT
        skip = how_many
    DEDENT
    for each in data :
    INDENT
        if not skip :
        INDENT
            db.consume(each)
        DEDENT
        else :
        INDENT
            skip -= 1
            if not skip :
            INDENT
                print ("Finished skipping {} records.".format(how_many))
            DEDENT
        DEDENT
        how_many += 1
    DEDENT
    print ("Completed loading available data.")
    db.csv_out()
DEDENT

def _compute_pos_order_total(self) :
INDENT
    Order_id = self.env ['pos.order'].search([('partner_id', '=', self.id)])
    for Order in Order_id :
    INDENT
        total = 0.0
        total += Order.amount_total
    DEDENT
    self.pos_order_total = total
DEDENT

def biggest() :
INDENT
    big_x, big_y, max_seen = 0, 0, 0
    for x in xrange(999, 99, - 1) :
    INDENT
        for y in xrange(x, 99, - 1) :
        INDENT
            if x * y < max_seen : continue
            if is_palindrome(x * y) :
            INDENT
                big_x, big_y, max_seen = x, y, x * y
            DEDENT
        DEDENT
    DEDENT
    return big_x, big_y, max_seen
DEDENT

def treeToList(node, order = Order.INORDER) :
INDENT
    if node is None :
    INDENT
        return []
    DEDENT
    right = treeToList(node.right, order)
    down = treeToList(node.down, order)
    current = [node.data]
    if order == Order.PREORDER :
    INDENT
        return current + right + down
    DEDENT
    if order == Order.INORDER :
    INDENT
        return right + current + down
    DEDENT
    if order == Order.POSTORDER :
    INDENT
        return right + down + current
    DEDENT
DEDENT

def switch(mode) :
INDENT
    switcher = {
        'a' : a,
        'b' : b,
        'ab' : (a, b)}
    for i in mode :
    INDENT
        switcher [i]()
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

    def test_pathological_http_method(self):
        """
        The edge case of a http request that spoofs an existing method name is caught.
        """
        self.assertEqual(SimpleView.as_view()(
            self.rf.get('/', REQUEST_METHOD='DISPATCH')
        ).status_code, 405)

def calculate_speed(radius) :
INDENT
    global t0
    t1 = time.clock
    interval = t1 - t0
    speed = radius / interval
    print (speed, 'mm/sek')
    speed_records.append(speed)
    if len(speed_records) > = 5 :
    INDENT
        last_five_records = speed_records [- 5 :]
        average = sum(last_five_records) / 5
        print ('Average Speed:', average)
    DEDENT
    if len(speed_records) > 10 :
    INDENT
        speed_records = list(set(speed_records) - set(speed_records [: 5]))
    DEDENT
DEDENT

def flatten(items, seqtypes = (list, tuple)) :
INDENT
    for i, x in enumerate(items) :
    INDENT
        while i < len(items) and isinstance(items [i], seqtypes) :
        INDENT
            items [i : i + 1] = items [i]
        DEDENT
    DEDENT
    return items
DEDENT

def __call__(self, file) :
INDENT
    hash = self.algorithm()
    with open(file, 'rb') as f :
    INDENT
        for chunk in iter(lambda : f.read(4096), '') :
        INDENT
            hash.update(chunk)
        DEDENT
    DEDENT
    return hash.hexdigest()
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

    def test_get_only(self):
        """
        Test a view which only allows GET doesn't allow other methods.
        """
        self._assert_simple(SimpleView.as_view()(self.rf.get('/')))
        self.assertEqual(SimpleView.as_view()(self.rf.post('/')).status_code, 405)
        self.assertEqual(SimpleView.as_view()(
            self.rf.get('/', REQUEST_METHOD='FAKE')
        ).status_code, 405)

def increment(self) :
INDENT
    i = len(self.number) - 1
    while i > = 0 :
    INDENT
        while (self.number [i] < 9) :
        INDENT
            self.number [i] += 1
        DEDENT
        self.number [i] = 0
        i -= 1
    DEDENT
DEDENT

def add_months(d, months) :
INDENT
    for i in range(4) :
    INDENT
        day = d.day - i
        try :
        INDENT
            return d.replace(day = day).replace(year = d.year + int(months) / / 12).replace(month = (d.month + int(months)) % 12)
        DEDENT
        except :
        INDENT
            pass
        DEDENT
    DEDENT
    raise Exception("should not happen")
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

def match_class(target) :
INDENT
    def do_match(tag) :
    INDENT
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    DEDENT
    return do_match
DEDENT

    def test_get_and_head(self):
        """
        Test a view which supplies a GET method also responds correctly to HEAD.
        """
        self._assert_simple(SimpleView.as_view()(self.rf.get('/')))
        response = SimpleView.as_view()(self.rf.head('/'))
        self.assertEqual(response.status_code, 200)

def main() :
INDENT
    global imgs_in_pygame_format
    for name, data in imgs_to_load.items() :
    INDENT
        imgs_in_pygame_format [name] = Image_loader(data)
    DEDENT
    for image in imgs_in_pygame_format :
    INDENT
        print image
    DEDENT
    print imgs_in_pygame_format ["bg"]
    print imgs_in_pygame_format ["mouse"]
DEDENT

def queryset(self, request, queryset) :
INDENT
    if self.value() :
    INDENT
        return set(comment for comment in queryset if comment.posted_by_guest())
    DEDENT
    elif not self.value() :
    INDENT
        return set(comment for comment in queryset if not comment.posted_by_guest())
    DEDENT
DEDENT

    def test_head_no_get(self):
        """
        Test a view which supplies no GET method responds to HEAD with HTTP 405.
        """
        response = PostOnlyView.as_view()(self.rf.head('/'))
        self.assertEqual(response.status_code, 405)

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

def scan(words) :
INDENT
    result = []
    for word in words.split() :
    INDENT
        found_category = 'error'
        for category, category_lexicon in _LEXICON.items() :
        INDENT
            if word in category_lexicon :
            INDENT
                found_category = category
                break
            DEDENT
        DEDENT
        result.append((found_category, word))
    DEDENT
    return result
DEDENT

def is_continuous(seq) :
INDENT
    non_null_indices = [i for i, obj in enumerate(seq) if obj is not None]
    for i, index in enumerate(non_null_indices [: - 1]) :
    INDENT
        if non_null_indices [i + 1] - index > 1 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def __op__(self, op, other) :
INDENT
    if other is None :
    INDENT
        print "%s(%s)" % (op, self)
        self, other = coerce(self, 0.0)
        return getattr(self, op)()
    DEDENT
    else :
    INDENT
        print "%s %s %s" % (self, op, other)
        self, other = coerce(self, other)
        return getattr(self, op)(other)
    DEDENT
DEDENT

def removeRec(node, value) :
INDENT
    if node.value == value :
    INDENT
        node.value = node.next.value
        node.next = node.next.next
        return True
    DEDENT
    if node.next == None :
    INDENT
        return False
    DEDENT
    if node.next.value == value :
    INDENT
        node.next = node.next.next
        return True
    DEDENT
    return removeRec(node.next, value)
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

def linspace(a, b, n = 100) :
INDENT
    if n < 2 :
    INDENT
        return b
    DEDENT
    diff = (float(b) - a) / (n - 1)
    return [diff * i + a for i in range(n)]
DEDENT

    def test_get_and_post(self):
        """
        Test a view which only allows both GET and POST.
        """
        self._assert_simple(SimplePostView.as_view()(self.rf.get('/')))
        self._assert_simple(SimplePostView.as_view()(self.rf.post('/')))
        self.assertEqual(SimplePostView.as_view()(
            self.rf.get('/', REQUEST_METHOD='FAKE')
        ).status_code, 405)

def enum(* names) :
INDENT
    class Foo(object) :
    INDENT
        __metaclass__ = M_add_class_attribs(enumerate(names))
        def __setattr__(self, name, value) :
        INDENT
            raise NotImplementedError
        DEDENT
    DEDENT
    return Foo()
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

    def test_invalid_keyword_argument(self):
        """
        View arguments must be predefined on the class and can't
        be named like a HTTP method.
        """
        msg = (
            "You tried to pass in the %s method name as a keyword argument "
            "to SimpleView(). Don't do that."
        )
        # Check each of the allowed method names
        for method in SimpleView.http_method_names:
            with self.assertRaisesMessage(TypeError, msg % method):
                SimpleView.as_view(**{method: 'value'})

        # Check the case view argument is ok if predefined on the class...
        CustomizableView.as_view(parameter="value")
        # ...but raises errors otherwise.
        msg = (
            "CustomizableView() received an invalid keyword 'foobar'. "
            "as_view only accepts arguments that are already attributes of "
            "the class."
        )
        with self.assertRaisesMessage(TypeError, msg):
            CustomizableView.as_view(foobar="value")

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

def create_webview(self, * args) :
INDENT
    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    wvc = WebViewClient();
    webview.setWebViewClient(wvc);
    activity.setContentView(webview)
    webview.loadUrl('http://www.google.com')
DEDENT

def __enter__(self) :
INDENT
    self.save_logger('', logging.getLogger())
    for name, logger in logging.Logger.manager.loggerDict.items() :
    INDENT
        self.save_logger(name, logger)
    DEDENT
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

    def test_calling_more_than_once(self):
        """
        Test a view can only be called once.
        """
        request = self.rf.get('/')
        view = InstanceView.as_view()
        self.assertNotEqual(view(request), view(request))

def decrypt(key, iv, ciphertext) :
INDENT
    assert len(key) == key_bytes
    iv_int = int(iv.encode('hex'), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value = iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter = ctr)
    plaintext = aes.decrypt(ciphertext)
    return plaintext
DEDENT

def escaped_split(str, ch) :
INDENT
    if len(ch) > 1 :
    INDENT
        raise ValueError('Expected split character. Found string!')
    DEDENT
    out = []
    part = ''
    escape = False
    for i in range(len(str)) :
    INDENT
        if not escape and str [i] == ch :
        INDENT
            out.append(part)
            part = ''
        DEDENT
        else :
        INDENT
            part += str [i]
            escape = not escape and str [i] == '\\'
        DEDENT
    DEDENT
    if len(part) :
    INDENT
        out.append(part)
    DEDENT
    return out
DEDENT

def do_GET(self) :
INDENT
    if '?' in self.path :
    INDENT
        self.path = self.path.split('?') [0]
    DEDENT
    SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
DEDENT

def __iter__(self) :
INDENT
    "implement the iterator protocol"
    for v in chain(* imap(iter, self.children)) :
    INDENT
        yield v
    DEDENT
    yield self.value
DEDENT

def countWords(s) :
INDENT
    d = {}
    for word in s.split() :
    INDENT
        try :
        INDENT
            d [word] += 1
        DEDENT
        except KeyError :
        INDENT
            d [word] = 1
        DEDENT
    DEDENT
    return d
DEDENT

def punk(s) :
INDENT
    count = 0
    for letter in s :
    INDENT
        if letter == "z" or letter == "Z" :
        INDENT
            count += 1
        DEDENT
    DEDENT
    if count > = 3 :
    INDENT
        return 1
    DEDENT
    else :
    INDENT
        return 0
    DEDENT
DEDENT

def execute(cmd) :
INDENT
    process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    (result, error) = process.communicate()
    rc = process.wait()
    if rc ! = 0 :
    INDENT
        print "Error: failed to execute command:", cmd
        print error
    DEDENT
    return result
DEDENT

    def test_class_attributes(self):
        """
        The callable returned from as_view() has proper
        docstring, name and module.
        """
        self.assertEqual(SimpleView.__doc__, SimpleView.as_view().__doc__)
        self.assertEqual(SimpleView.__name__, SimpleView.as_view().__name__)
        self.assertEqual(SimpleView.__module__, SimpleView.as_view().__module__)

def greet(lines, cheers) :
INDENT
    for i in range(lines) :
    INDENT
        output = (" ") * i + "Go"
        for j in range(cheers) :
        INDENT
            if cheers == 1 :
            INDENT
                print output
                break
            DEDENT
            output += "Budddy Go"
        DEDENT
        print output
    DEDENT
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

    def test_dispatch_decoration(self):
        """
        Attributes set by decorators on the dispatch method
        are also present on the closure.
        """
        self.assertTrue(DecoratedDispatchView.as_view().is_decorated)

def nested_sum(L) :
INDENT
    total = 0
    for i in L :
    INDENT
        if isinstance(i, list) :
        INDENT
            total += nested_sum(i)
        DEDENT
        else :
        INDENT
            total += i
        DEDENT
    DEDENT
    return total
DEDENT

def test_run(files_dir) :
INDENT
    queue = mp.Queue()
    procs = [mp.Process(target = worker, args = [queue]) for i in mp.cpu_count()]
    for p in procs :
    INDENT
        p.start()
    DEDENT
    files = os.listdir(files_dir)
    for f1, f2 in IT.product(files, repeat = 2) :
    INDENT
        queue.put((f1, f2))
    DEDENT
    for p in procs :
    INDENT
        queue.put(SENTINEL)
    DEDENT
    for p in procs :
    INDENT
        p.join()
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

def todict(obj, classkey = None) :
INDENT
    if isinstance(obj, dict) :
    INDENT
        data = {}
        for (k, v) in obj.items() :
        INDENT
            data [k] = todict(v, classkey)
        DEDENT
        return data
    DEDENT
    elif hasattr(obj, "_ast") :
    INDENT
        return todict(obj._ast())
    DEDENT
    elif hasattr(obj, "__iter__") and not isinstance(obj, str) :
    INDENT
        return [todict(v, classkey) for v in obj]
    DEDENT
    elif hasattr(obj, "__dict__") :
    INDENT
        data = dict([(key, todict(value, classkey)) for key, value in obj.__dict__.items()
                if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__") :
        INDENT
            data [classkey] = obj.__class__.__name__
        DEDENT
        return data
    DEDENT
    else :
    INDENT
        return obj
    DEDENT
DEDENT

def format(self, record, colour = False) :
INDENT
    message = super().format(record)
    if not colour :
    INDENT
        return message
    DEDENT
    level_no = record.levelno
    if level_no > = logging.CRITICAL :
    INDENT
        colour = self.RED
    DEDENT
    elif level_no > = logging.ERROR :
    INDENT
        colour = self.RED
    DEDENT
    elif level_no > = logging.WARNING :
    INDENT
        colour = self.YELLOW
    DEDENT
    elif level_no > = logging.INFO :
    INDENT
        colour = self.RESET
    DEDENT
    elif level_no > = logging.DEBUG :
    INDENT
        colour = self.BRGREEN
    DEDENT
    else :
    INDENT
        colour = self.RESET
    DEDENT
    message = colour + message + self.RESET
    return message
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

def access(obj, indexes) :
INDENT
    try :
    INDENT
        return reduce(list.__getitem__, indexes, obj)
    DEDENT
    except Exception :
    INDENT
        return None
    DEDENT
DEDENT

    def test_options(self):
        """
        Views respond to HTTP OPTIONS requests with an Allow header
        appropriate for the methods implemented by the view class.
        """
        request = self.rf.options('/')
        view = SimpleView.as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response['Allow'])

def timeout(func, args = (), kwargs = {}, timeout_duration = 1, default = None) :
INDENT
    import signal
    class TimeoutError(Exception) :
    INDENT
        pass
    DEDENT
    def handler(signum, frame) :
    INDENT
        raise TimeoutError()
    DEDENT
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try :
    INDENT
        result = func(* args, ** kwargs)
    DEDENT
    except TimeoutError as exc :
    INDENT
        result = default
    DEDENT
    finally :
    INDENT
        signal.alarm(0)
    DEDENT
    return result
DEDENT

def has_add_permission(self, request) :
INDENT
    base_add_permission = super(SettingAdmin, self).has_add_permission(request)
    if base_add_permission :
    INDENT
        count = Setting.objects.all().count()
        if count == 0 :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def __init__(self, some_var) :
INDENT
    QtCore.QObject.__init__(self, parent = None)
    self.some_var = some_var
    self.queue = mp.Queue()
    self.process = mp.Process(
        target = workermodule.some_complex_processing,
        args = (self.queue,))
DEDENT

def reverse(s) :
INDENT
    rev = [_t for _t in s]
    t = ''
    while len(rev) ! = 0 :
    INDENT
        t += rev.pop()
    DEDENT
    return t
DEDENT

    def test_options_for_get_view(self):
        """
        A view implementing GET allows GET and HEAD.
        """
        request = self.rf.options('/')
        view = SimpleView.as_view()
        response = view(request)
        self._assert_allows(response, 'GET', 'HEAD')

def length_of_string(mystring) :
INDENT
    try :
    INDENT
        int(mystring)
        return "invalid entry"
    DEDENT
    except ValueError :
    INDENT
        return len(mystring)
    DEDENT
DEDENT

def DnaCheck() :
INDENT
    if any(c in squence_str for c in ['A', 'C', 'T', 'G']) :
    INDENT
        return "yes"
    DEDENT
    else :
    INDENT
        return "no"
    DEDENT
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    super(MainFrame, self).__init__(None, * args, ** kwargs)
    self.Title = 'Basic wxPython module'
    self.SetMenuBar(MenuBar(self))
    self.ToolBar = MainToolbar(self)
    self.status_bar = StatusBar(self).status_bar
    self.Bind(wx.EVT_CLOSE, self.on_quit_click)
    panel = MainPanel(self)
    sizer = wx.BoxSizer()
    sizer.Add(panel)
    self.SetSizerAndFit(sizer)
    self.Centre()
    self.Show()
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

def run(self) :
INDENT
    print '>>>> abuse generator as context manager'
    for driver in self.drivergenerator(self.driverfactory) :
    INDENT
        self.dostuff(driver)
    DEDENT
DEDENT

def some_function(eggs) :
INDENT
    options = {1 : do_something_1, 2 : do_something_2, 3 : do_something_3}
    if eggs in options :
    INDENT
        options [eggs]()
        do_something_4()
        do_something_5()
        do_something_6()
    DEDENT
    else :
    INDENT
        do_error()
        return
    DEDENT
DEDENT

    def test_options_for_get_and_post_view(self):
        """
        A view implementing GET and POST allows GET, HEAD, and POST.
        """
        request = self.rf.options('/')
        view = SimplePostView.as_view()
        response = view(request)
        self._assert_allows(response, 'GET', 'HEAD', 'POST')

def save(self, * args, ** kwargs) :
INDENT
    if self.photo :
    INDENT
        image = Img.open(StringIO.StringIO(self.photo.read()))
        image.thumbnail((200, 200), Img.ANTIALIAS)
        output = StringIO.StringIO()
        image.save(output, format = 'JPEG', quality = 75)
        output.seek(0)
        self.photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.photo.name, 'image/jpeg', output.len, None)
    DEDENT
    super(Mymodel, self).save(* args, ** kwargs)
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

    def test_options_for_post_view(self):
        """
        A view implementing POST allows POST.
        """
        request = self.rf.options('/')
        view = PostOnlyView.as_view()
        response = view(request)
        self._assert_allows(response, 'POST')

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

def __init__(self, result) :
INDENT
    super().__init__()
    self.result = result
    print ('a: {}'.format(result ['a']))
    print ('b: {}'.format(result ['b']))
    print ('c: {}'.format(result ['c']))
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

def sum13(nums) :
INDENT
    n = nums
    while 13 in n :
    INDENT
        wheres13 = n.index(13)
        n = n [0 : wheres13] + n [wheres13 + 2 :]
    DEDENT
    return sum(n)
DEDENT

    def _assert_allows(self, response, *expected_methods):
        "Assert allowed HTTP methods reported in the Allow response header"
        response_allows = set(response['Allow'].split(', '))
        self.assertEqual(set(expected_methods + ('OPTIONS',)), response_allows)

def encrypt(key, plaintext) :
INDENT
    assert len(key) == key_bytes
    iv = Random.new().read(AES.block_size)
    iv_int = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value = iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter = ctr)
    ciphertext = aes.encrypt(plaintext)
    return (iv, ciphertext)
DEDENT

def intersect(string1, string2) :
INDENT
    common = []
    for char in set(string1) :
    INDENT
        common.extend(char * min(string1.count(char), string2.count(char)))
    DEDENT
    return common
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

def permutations(iterable, r = None) :
INDENT
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n :
    INDENT
        return
    DEDENT
    indices = range(n)
    cycles = range(n, n - r, - 1)
    yield tuple(pool [i] for i in indices [: r])
    while n :
    INDENT
        for i in reversed(range(r)) :
        INDENT
            cycles [i] -= 1
            if cycles [i] == 0 :
            INDENT
                indices [i :] = indices [i + 1 :] + indices [i : i + 1]
                cycles [i] = n - i
            DEDENT
            else :
            INDENT
                j = cycles [i]
                indices [i], indices [- j] = indices [- j], indices [i]
                yield tuple(pool [i] for i in indices [: r])
                break
            DEDENT
        DEDENT
        else :
        INDENT
            return
        DEDENT
    DEDENT
DEDENT

    def test_args_kwargs_request_on_self(self):
        """
        Test a view only has args, kwargs & request once `as_view`
        has been called.
        """
        bare_view = InstanceView()
        view = InstanceView.as_view()(self.rf.get('/'))
        for attribute in ('args', 'kwargs', 'request'):
            self.assertNotIn(attribute, dir(bare_view))
            self.assertIn(attribute, dir(view))

def __init__(self) :
INDENT
    wx.Frame.__init__(self, None, - 1, "Test", size = (500, 270))
    panel = wx.Panel(self, - 1)
    self.buttonStart = wx.Button(panel, - 1, label = "Start thread", pos = (0, 0))
    self.buttonChange = wx.Button(panel, - 1, label = "Change var", pos = (0, 30))
    panel.Bind(wx.EVT_BUTTON, self.startThread, id = self.buttonStart.GetId())
    panel.Bind(wx.EVT_BUTTON, self.changeVar, id = self.buttonChange.GetId())
DEDENT

def get_object(self) :
INDENT
    pk = self.kwargs [self.lookup_url_kwarg]
    try :
    INDENT
        self.kwargs [self.lookup_url_kwarg] = int(pk)
        self.lookup_field = 'id'
    DEDENT
    except :
    INDENT
        self.lookup_field = 'name'
    DEDENT
    return super(SomeModelDetailView, self).get_object()
DEDENT

    def test_overridden_setup(self):
        class SetAttributeMixin:
            def setup(self, request, *args, **kwargs):
                self.attr = True
                super().setup(request, *args, **kwargs)

def __init__(self, position, size) :
INDENT
    super().__init__()
    self.original_image = pygame.Surface(size)
    self.original_image.fill((255, 0, 0))
    self.original_image.set_colorkey(BACKGROUND_COLOR)
    self.image = self.original_image
    self.rect = self.image.get_rect(center = position)
    self.angle = 0
    self.position = pygame.math.Vector2(position)
    self.velocity = pygame.math.Vector2(0, 0)
DEDENT

def __new__(klass, ** slots) :
INDENT
    klass.__slots__ = []
    for k in slots :
    INDENT
        klass.__slots__.append(k)
    DEDENT
    return super(MySlottedClassXY, klass).__new__(klass)
DEDENT

def xirr(values, dates) :
INDENT
    try :
    INDENT
        return scipy.optimize.newton(lambda r : xnpv(r, values, dates), 0.0)
    DEDENT
    except RuntimeError :
    INDENT
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

def __init__(self, d = {}, ** kwd) :
INDENT
    if isinstance(d, type(self)) :
    INDENT
        self.update(d)
    DEDENT
    else :
    INDENT
        for i in d :
        INDENT
            self [i [0]] = i [1]
        DEDENT
    DEDENT
    self.update(kwd)
DEDENT

        return scipy.optimize.brentq(lambda r : xnpv(r, values, dates), - 1.0, 1e10)
    DEDENT
DEDENT

def __init__(self, a = None, b = None, ** kwargs) :
INDENT
    self.relations = {
        "e" : {"req" : ["a", "b"], "func" : lambda a, b : a + b},
        "C" : {"req" : ["e", "a"], "func" : lambda e, a : e * 1 / (a * b)},
        "A" : {"req" : ["C", "e"], "func" : lambda e, C : cmplx_func_A(e, C)},
        "a" : {"req" : ["e", "b"], "func" : lambda e, b : e / b},
        "b" : {"req" : ["e", "a"], "func" : lambda e, a : e / a}}
    self.a = a
    self.b = b
    self.e = None
    self.C = None
    self.A = None
    if kwargs :
    INDENT
        for key in kwargs :
        INDENT
            setattr(self, key, kwargs [key])
        DEDENT
    DEDENT
DEDENT

def run(self) :
INDENT
    print '>>>> check driver ok and ensure driver quit'
    driver, ok = self.driverfactory()
    try :
    INDENT
        if ok :
        INDENT
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

def DnaCheck() :
INDENT
    if any(c in squence_str for c in ['A', 'C', 'T', 'G']) :
    INDENT
        return "yes"
    DEDENT
    else :
    INDENT
        return "no"
    DEDENT
DEDENT

def on_click(i, j, event) :
INDENT
    global counter
    if counter < 100 :
    INDENT
        if board [i] [j] == None :
        INDENT
            color = "green" if counter % 2 else "red"
            enemycolor = "red" if counter % 2 else "green"
            event.widget.config(bg = color)
            board [i] [j] = color
            for k in range(- 1, 2) :
            INDENT
                for l in range(- 1, 2) :
                INDENT
                    try :
                    INDENT
                        if board [i + k] [j + l] == enemycolor :
                        INDENT
                            board [i + k] [j + l] = color
                        DEDENT
                    DEDENT
                    except IndexError :
                    INDENT
                        pass
                    DEDENT
                DEDENT
            DEDENT
            counter += 1
            global gameframe
            gameframe.destroy()
            redraw()
            root.wm_title(enemycolor + "'s turn")
        DEDENT
        else :
        INDENT
            messagebox.showinfo("Alert", "This square is already occupied!")
        DEDENT
        check_board()
    DEDENT
DEDENT

def count(list1) :
INDENT
    total = 0
    old = 0
    for position, x in enumerate(list1) :
    INDENT
        total = x + old
        old = x
        print total
    DEDENT
    return
DEDENT

def almostIncreasingSequence(sequence) :
INDENT
    if len(sequence) < = 2 :
    INDENT
        return True
    DEDENT
    def IncreasingSequence(test_sequence) :
    INDENT
        if len(test_sequence) == 2 :
        INDENT
            if test_sequence [0] < test_sequence [1] :
            INDENT
                return True
            DEDENT
        DEDENT
        else :
        INDENT
            for i in range(0, len(test_sequence) - 1) :
            INDENT
                if test_sequence [i] > = test_sequence [i + 1] :
                INDENT
                    return False
                DEDENT
                else :
                INDENT
                    pass
                DEDENT
            DEDENT
            return True
        DEDENT
    DEDENT
    for i in range(0, len(sequence) - 1) :
    INDENT
        if sequence [i] > = sequence [i + 1] :
        INDENT
            test_seq1 = sequence [: i] + sequence [i + 1 :]
            test_seq2 = sequence [: i + 1] + sequence [i + 2 :]
            if IncreasingSequence(test_seq1) == True :
            INDENT
                return True
            DEDENT
            elif IncreasingSequence(test_seq2) == True :
            INDENT
                return True
            DEDENT
            else :
            INDENT
                return False
            DEDENT
        DEDENT
    DEDENT
DEDENT

def __init__(self, parent) :
INDENT
    mystyle = FNB.FNB_DROPDOWN_TABS_LIST | FNB.FNB_FF2 | FNB.FNB_SMART_TABS | FNB.FNB_X_ON_TAB
    super(MyFlatNotebook, self).__init__(parent, style = mystyle)
    self.textctrl = wx.TextCtrl(self, value = "edit me", style = wx.TE_MULTILINE)
    self.blue = wx.Panel(self)
    self.blue.SetBackgroundColour(wx.BLUE)
    self.AddPage(self.textctrl, "Text Editor")
    self.AddPage(self.blue, "Blue Panel")
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

            self.dostuff(driver)
        DEDENT
        else :
        INDENT
            print 'skip because driver not ok'
        DEDENT
    DEDENT
    finally :
    INDENT
        driver.quit()
    DEDENT
DEDENT

        class CheckSetupView(SetAttributeMixin, SimpleView):
            def dispatch(self, request, *args, **kwargs):
                assert hasattr(self, 'attr')
                return super().dispatch(request, *args, **kwargs)

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

def twos_complement(val, nbits) :
INDENT
    if val < 0 :
    INDENT
        val = (1 < < nbits) + val
    DEDENT
    else :
    INDENT
        if (val & (1 < < (nbits - 1))) ! = 0 :
        INDENT
            val = val - (1 < < nbits)
        DEDENT
    DEDENT
    return val
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

def decorator_factory(value) :
INDENT
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
    return msg_decorator
DEDENT

def R(A) :
INDENT
    if (0 in A) - 1 : yield A; return
    def H(i) : h = set(A [j] for j in r if j / 9 == i / 9 or j % 9 == i % 9 or j / 27 == i / 27 and j % 9 / 3 == i % 9 / 3); return len(h), h, i
    l, h, i = max(H(i) for i in r if not A [i])
    for j in r [1 : 10] :
    INDENT
        if (j in h) - 1 :
        INDENT
            A [i] = j
            for S in R(A) : yield S
        DEDENT
        A [i] = 0
    DEDENT
DEDENT

        response = CheckSetupView.as_view()(self.rf.get('/'))
        self.assertEqual(response.status_code, 200)

    def test_not_calling_parent_setup_error(self):
        class TestView(View):
            def setup(self, request, *args, **kwargs):
                pass  # Not calling super().setup()

def __init__(self, year = None, month = None,
day = None, weekday = None,
hour = None, minute = None,
second = None) :
INDENT
    loc = locals()
    loc.pop("self")
def compress(factors) :
INDENT
    summands = collections.defaultdict(lambda : 0)
    for factor in factors :
    INDENT
        summands [factor] += 1
    DEDENT
    return [(base, summands [base]) for base in sorted(summands)]
DEDENT

def after_request(response) :
INDENT
    diff = time.time() - g.start
    if app.debug :
    INDENT
        print "Exec time: %s" % str(diff)
    DEDENT
    if (response.response) :
    INDENT
        response.response [0] = response.response [0].replace('__EXECUTION_TIME__', str(diff))
        response.headers ["content-length"] = len(response.response [0])
    DEDENT
    return response
DEDENT

def split_at_first_false(pred, seq) :
INDENT
    index = 0
    while index < len(seq) :
    INDENT
        if not pred(seq [index]) :
        INDENT
            return seq [: index], seq [index + 1 :]
        DEDENT
        index += 1
    DEDENT
DEDENT

    self.at = dict((k, v) for k, v in loc.iteritems() if v ! = None)
DEDENT

def two_powers(num) :
INDENT
    while num > 0 :
    INDENT
        power = int(math.log(num, 2))
        yield 2 ** power
        num = num - 2 ** power
    DEDENT
DEDENT

def zipdir(path, ziph) :
INDENT
    for root, dirs, files in os.walk(path) :
    INDENT
        if root.replace(path, '') == '' :
        INDENT
            prefix = ''
        DEDENT
        else :
        INDENT
            prefix = root.replace(path, '') + '/'
            if (prefix [0] == '/') :
            INDENT
                prefix = prefix [1 :]
            DEDENT
        DEDENT
        for filename in files :
        INDENT
            actual_file_path = root + '/' + filename
            zipped_file_path = prefix + filename
            zipf.write(actual_file_path, zipped_file_path)
        DEDENT
    DEDENT
DEDENT

def emit(self, record) :
INDENT
    stream = self.stream
    try :
    INDENT
        msg = self.format(record, stream.isatty())
        stream.write(msg)
def device_id_replace(filepath) :
INDENT
    original_id = input("What device ID are you needing to replace?")
    new_id = input("What is the new device ID?")
    with open(filepath, 'r+') as devicetxt :
    INDENT
        string = devicetxt.read()
        string = string.replace(original_id, new_id)
        devicetxt.truncate(0)
        devicetxt.seek(0)
        devicetxt.write(string)
    DEDENT
DEDENT

def partition(A, g, p) :
INDENT
    for j in range(g, p) :
    INDENT
        if A [j] < = A [p] :
        INDENT
            swap(A, j, g)
            g += 1
        DEDENT
    DEDENT
    swap(A, p, g)
    return g
DEDENT

def unique(items) :
INDENT
    found = set([])
    keep = []
    for item in items :
    INDENT
        if item not in found :
        INDENT
            found.add(item)
            keep.append(item)
        DEDENT
    DEDENT
    return keep
DEDENT

        stream.write(self.terminator)
        self.flush()
    DEDENT
    except Exception :
    INDENT
        self.handleError(record)
    DEDENT
DEDENT

        msg = (
            "TestView instance has no 'request' attribute. Did you override "
            "setup() and forget to call super()?"
        )
        with self.assertRaisesMessage(AttributeError, msg):
            TestView.as_view()(self.rf.get('/'))

    def test_direct_instantiation(self):
        """
        It should be possible to use the view by directly instantiating it
        without going through .as_view() (#21564).
        """
        view = PostOnlyView()
        response = view.dispatch(self.rf.head('/'))
        self.assertEqual(response.status_code, 405)


def censored(sentence, words) :
INDENT
    for word in words :
    INDENT
        if word in sentence :
        INDENT
            sentence = sentence.replace(word, "*" * len(word))
        DEDENT
    DEDENT
    return sentence
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

def fire(self, ** attrs) :
INDENT
    e = Event()
    e.source = self
    for k, v in attrs.iteritems() :
    INDENT
        setattr(e, k, v)
    DEDENT
    for fn in self.callbacks :
    INDENT
        fn(e)
    DEDENT
DEDENT

def seq(start, stop, step = 1, digit = 0) :
INDENT
    x = float(start)
    v = []
    while x < = stop :
    INDENT
        v.append(round(x, digit))
        x += step
    DEDENT
    return v
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class TemplateViewTest(SimpleTestCase):

    rf = RequestFactory()

    def _assert_about(self, response):
        response.render()
        self.assertContains(response, '<h1>About</h1>')

def __getitem__(self, index) :
INDENT
    t = time.time()
    print t - self.created
    if t - self.created > self.expires_time :
    INDENT
        self.created += self.expires_time
        self.pop(index)
        self.__getitem__(index)
    DEDENT
    return list.__getitem__(self, index)
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

def display_list(A, B) :
INDENT
    mylist = [("01", "02", "03", "04", "05", "06", "07"),
        ("08", "09", "10", "11", "12", "13", "14"),
        ("15", "16", "17", "18", "19", "20", "21")]
    for row_index in range(len(mylist)) :
    INDENT
        elements_list = list(mylist [row_index])
        elements_list = ["A" if int(element) == A else "B" if int(element) == B else element for element in elements_list]
        mylist [row_index] = tuple(elements_list)
    DEDENT
    print (mylist)
DEDENT

def find_nearest(array, values) :
INDENT
    array = np.asarray(array)
    values = np.expand_dims(values, axis = - 1)
    indices = np.abs(array - values).argmin(axis = - 1)
    return array [indices]
DEDENT

def enum(* names) :
INDENT
    '''
    Makes enum.
    Usage:
        E = enum( 'YOUR', 'KEYS', 'HERE' )
        print( E.HERE )
    '''
    class Enum() :
    INDENT
        pass
    DEDENT
    for index, name in enumerate(names) :
    INDENT
        setattr(Enum, name, index)
    DEDENT
    return Enum
DEDENT

def toc(self) :
INDENT
    self.tend = self.get_time()
    if self.indentation :
    INDENT
        if len(self.tstart) > 0 :
        INDENT
            self.elapsed = self.tend - self.tstart.pop()
        DEDENT
        else :
        INDENT
            self.elapsed = None
        DEDENT
    DEDENT
    else :
    INDENT
        self.elapsed = self.tend - self.tstart
    DEDENT
DEDENT

def polyfit2d(x, y, f, deg) :
INDENT
    from numpy.polynomial import polynomial
    import numpy as np
    x = np.asarray(x)
    y = np.asarray(y)
    f = np.asarray(f)
    deg = np.asarray(deg)
    vander = polynomial.polyvander2d(x, y, deg)
    vander = vander.reshape((- 1, vander.shape [- 1]))
    f = f.reshape((vander.shape [0],))
    c = np.linalg.lstsq(vander, f) [0]
    return c.reshape(deg + 1)
DEDENT

    def test_get(self):
        """
        Test a view that simply renders a template on GET
        """
        self._assert_about(AboutTemplateView.as_view()(self.rf.get('/about/')))

def num_input(s) :
INDENT
    while True :
    INDENT
        try :
        INDENT
            return decimal.Decimal(raw_input(s))
        DEDENT
        except decimal.InvalidOperation, e :
        INDENT
            print e.message
        DEDENT
    DEDENT
DEDENT

def createfile() :
INDENT
    var = """\
          #!/bin/sh
          echo ${test}
          """
    var = textwrap.dedent(var)
    funcToCreateScript(filename, var)
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

def __init__(self, key, menuname, parent = None) :
INDENT
    super(MenuManager, self).__init__(parent)
    self.settings = QtCore.QSettings('test_org', 'my_app')
    self.key = key
    self.layout = QtWidgets.QVBoxLayout(self)
    self.listWidget = QtWidgets.QListWidget()
    self.remove_btn = QtWidgets.QPushButton('Remove')
    self.layout.addWidget(self.listWidget)
    self.layout.addWidget(self.remove_btn)
    self.remove_btn.clicked.connect(self.remove_items)
    self.menu = QtWidgets.QMenu(menuname)
    load_items = self.settings.value(self.key, [])
    for name, itemdata in load_items.items() :
    INDENT
        action = QtWidgets.QAction(name, self.menu)
        action.setData(itemdata)
        self.menu.addAction(action)
        item = QtWidgets.QListWidgetItem(name)
        item.setData(QtCore.Qt.UserRole, action)
        self.listWidget.addItem(item)
    DEDENT
DEDENT

def find(l, elem) :
INDENT
    for row, i in enumerate(l) :
    INDENT
        try :
        INDENT
            column = i.index(elem)
        DEDENT
        except ValueError :
        INDENT
            continue
        DEDENT
        return row, column
    DEDENT
    return - 1
DEDENT

    def test_head(self):
        """
        Test a TemplateView responds correctly to HEAD
        """
        response = AboutTemplateView.as_view()(self.rf.head('/about/'))
        self.assertEqual(response.status_code, 200)

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

def __new__(klass, ** slots) :
INDENT
    klass.__slots__ = []
    for k in slots :
    INDENT
        klass.__slots__.append(k)
    DEDENT
    return super(MySlottedClassAB, klass).__new__(klass)
DEDENT

def square(x = None) :
INDENT
    if not isinstance(x, numbers.Number) or isinstance(x, numbers.Complex) :
    INDENT
        print ("you have not entered x")
    DEDENT
    else :
    INDENT
        y = x ** 2
        return y
    DEDENT
DEDENT

def handleError(func) :
INDENT
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
    return wrapper
DEDENT

    def test_get_template_attribute(self):
        """
        Test a view that renders a template on GET with the template name as
        an attribute on the class.
        """
        self._assert_about(AboutTemplateAttributeView.as_view()(self.rf.get('/about/')))

def initUI(self) :
INDENT
    self.parent.title("Windows")
    Label(text = "Contact List").grid(row = 0, column = 0, columnspan = 2)
    Text(width = 30, height = 15).grid(row = 1, rowspan = 9, column = 0, columnspan = 2, padx = 20)
    Button(text = "Display Contact").grid(row = 10, column = 0, columnspan = 2, pady = 10)
    Label(text = "Last Name:").grid(row = 11, column = 0, pady = 10)
    Entry().grid(row = 11, column = 1)
    Button(text = "Search").grid(row = 12, column = 0, columnspan = 2)
    Label(text = "New Contact").grid(row = 0, column = 2, columnspan = 2)
    Label(text = "First Name:").grid(row = 1, column = 2, sticky = E)
    Entry().grid(row = 1, column = 3)
    Label(text = "Last Name:").grid(row = 2, column = 2, sticky = E)
    Entry().grid(row = 2, column = 3)
    Label(text = "Phone #:").grid(row = 3, column = 2, sticky = E)
    Entry().grid(row = 3, column = 3)
    friend_check = IntVar()
    Checkbutton(variable = friend_check, command = self.friend_box, text = "Friend").grid(row = 4, column = 3, sticky = W)
    Label(text = "Email:").grid(row = 5, column = 2, sticky = E)
    Entry().grid(row = 5, column = 3)
    Label(text = "Birthday:").grid(row = 6, column = 2, sticky = E)
    Entry().grid(row = 6, column = 3)
    Button(text = "Add Contact").grid(row = 7, column = 3, sticky = E)
DEDENT

def __init__(self, interval, function, * args, ** kwargs) :
INDENT
    self._lock = Lock()
    self._timer = None
    self.function = function
    self.interval = interval
    self.args = args
    self.kwargs = kwargs
    self._stopped = True
    if kwargs.pop('autostart', True) :
    INDENT
        self.start()
    DEDENT
DEDENT

def time_overlap_projected_graph_parallel(B, nodes) :
INDENT
    G = nx.MultiGraph()
    G.add_nodes_from((n, B.node [n]) for n in nodes)
    cells = [n for n in B.nodes() if n [0] not in nodes]
    for cell in cells :
    INDENT
        for u, v in combinations(B [cell], 2) :
        INDENT
            for uspell in B.get_edge_data(u, cell).values() :
            INDENT
                ustart = uspell [1]
                uend = uspell [2]
                for vspell in B.get_edge_data(v, cell).values() :
                INDENT
                    vstart = vspell [1]
                    vend = vspell [2]
                    if uend > vstart and vend > ustart :
                    INDENT
                        ostart = max(ustart, vstart)
                        oend = min(uend, vend)
                        olen = (oend - ostart + 1) / 86400
                        ocell = cell
                        if (v not in G [u] or ostart not in [edict [1] for edict in G [u] [v].values()]) :
                        INDENT
                            G.add_edge(u, v, {0 : olen, 1 : ostart, 2 : oend, 3 : ocell})
                        DEDENT
                    DEDENT
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return G
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

    def test_get_generic_template(self):
        """
        Test a completely generic view that renders a template on GET
        with the template name as an argument at instantiation.
        """
        self._assert_about(TemplateView.as_view(template_name='generic_views/about.html')(self.rf.get('/about/')))

def _get_modules_from_db(db, leaves = None) :
INDENT
    if leaves is None :
    INDENT
        leaves = []
    DEDENT
    if not isinstance(db, dict) :
    INDENT
        return leaves
    DEDENT
    if 'path_to_file' in db and 'checksum' in db :
    INDENT
        leaves.append(db)
    DEDENT
    else :
    INDENT
        for v in db.values() :
        INDENT
            _get_modules_from_db(v, leaves)
        DEDENT
    DEDENT
    return leaves
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

def is_prime(n) :
INDENT
    if n < 2 :
    INDENT
        return False;
    DEDENT
    if n % 2 == 0 :
    INDENT
        return n == 2
    DEDENT
    k = 3
    while k * k < = n :
    INDENT
        if n % k == 0 :
        INDENT
            return False
        DEDENT
        k += 2
    DEDENT
    return True
DEDENT

def reverse(s) :
INDENT
    rev = [_t for _t in s]
    t = ''
    while len(rev) ! = 0 :
    INDENT
        t += rev.pop()
    DEDENT
    return t
DEDENT

    def test_template_name_required(self):
        """
        A template view must provide a template name.
        """
        msg = (
            "TemplateResponseMixin requires either a definition of "
            "'template_name' or an implementation of 'get_template_names()'"
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/template/no_template/')

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

def main() :
INDENT
    """Open the file, parse the input and check if it is a magic cube"""
    with open("Magic Square Input.txt") as f :
    INDENT
        for line in f.readlines() :
        INDENT
            numbers = line.split(" ")
            cube = [int(x) for x in numbers]
            is_magic(cube)
        DEDENT
    DEDENT
DEDENT

def leap_years(start, end) :
INDENT
    if not 1500 < start < 2100 :
    INDENT
        return 0
    DEDENT
    if not 1500 < end < 2100 :
    INDENT
        return 0
    DEDENT
    return sum(
        (not y % 4 and y % 100 ! = 0) or not y % 400 for y in range(start, end + 1)
        )
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

def future6(A) :
INDENT
    known = []
    result = []
    for idx in xrange(len(A) - 1, - 1, - 1) :
    INDENT
        value = A [idx]
        while known and known [- 1] [1] < value :
        INDENT
            known.pop()
        DEDENT
        if known :
        INDENT
            result.append(known [- 1] [0])
        DEDENT
        else :
        INDENT
            result.append(- 1)
        DEDENT
        known.append((idx, value))
    DEDENT
    return np.array(result) [: : - 1]
DEDENT

def findError(result) :
INDENT
    print result
    for k, v in result.iteritems() :
    INDENT
        error_nr = v % 2
        if error_nr == 0 :
        INDENT
            pass
        DEDENT
        elif error_nr > 0 :
        INDENT
            yield MyException
        DEDENT
    DEDENT
DEDENT

    @require_jinja2
    def test_template_engine(self):
        """
        A template view may provide a template engine.
        """
        request = self.rf.get('/using/')
        view = TemplateView.as_view(template_name='generic_views/using.html')
        self.assertEqual(view(request).render().content, b'DTL\n')
        view = TemplateView.as_view(template_name='generic_views/using.html', template_engine='django')
        self.assertEqual(view(request).render().content, b'DTL\n')
        view = TemplateView.as_view(template_name='generic_views/using.html', template_engine='jinja2')
        self.assertEqual(view(request).render().content, b'Jinja2\n')

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

def addition() :
INDENT
    total = 0
    while True :
    INDENT
        value = input()
        if value == "exit" :
        INDENT
            break
        DEDENT
        else :
        INDENT
            try :
            INDENT
                total += int(value)
            DEDENT
            except :
            INDENT
                print ('Please enter in a valid integer')
            DEDENT
        DEDENT
    DEDENT
    print (total)
DEDENT

def extendedString(string1, string2) :
INDENT
    if len(string1) < = len(string2) :
    INDENT
        x = string1
        y = string2
    DEDENT
    else :
    INDENT
        x = string2
        y = string1
    DEDENT
    z = ""
    for i in range(len(x)) :
    INDENT
        z += x [i]
        z += y [i]
    DEDENT
    if i < len(y) :
    INDENT
        for j in range(i + 1, len(y)) :
        INDENT
            z += x [i]
            z += y [j]
        DEDENT
    DEDENT
    return z
DEDENT

def __getattr__(self, attr) :
INDENT
    if self.has_key(attr) :
    INDENT
        return super(OrderedAttrDict, self).__getitem__(attr)
    DEDENT
    else :
    INDENT
        return super(OrderedAttrDict, self).__getattr__(attr)
    DEDENT
DEDENT

def spiral(X, Y) :
INDENT
    x = y = 0
    dx = 0
    dy = - 1
    for i in range(max(X, Y) ** 2) :
    INDENT
        if (- X / 2 < x < = X / 2) and (- Y / 2 < y < = Y / 2) :
        INDENT
            yield x, y
        DEDENT
        if x == y or (x < 0 and x == - y) or (x > 0 and x == 1 - y) :
        INDENT
            dx, dy = - dy, dx
        DEDENT
        x, y = x + dx, y + dy
    DEDENT
    spiral_matrix_size = 5
    my_list = list(range(spiral_matrix_size ** 2))
    my_list = [my_list [x : x + spiral_matrix_size] for x in range(0, len(my_list), spiral_matrix_size)]
    print (my_list)
    for i, (x, y) in enumerate(spiral(spiral_matrix_size, spiral_matrix_size)) :
    INDENT
        diff = int(spiral_matrix_size / 2)
        my_list [x + diff] [y + diff] = i
    DEDENT
    print (my_list)
DEDENT

def file_store(filename, mode = 'w') :
INDENT
    def store(items) :
    INDENT
        with open(filename, mode) as output :
        INDENT
            results = []
            for item in items :
            INDENT
                write_result(item, output)
                results.append(item)
            DEDENT
        DEDENT
        return results
    DEDENT
    return store
DEDENT

    def test_template_params(self):
        """
        A generic template view passes kwargs as context.
        """
        response = self.client.get('/template/simple/bar/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['foo'], 'bar')
        self.assertIsInstance(response.context['view'], View)

def myfunc(l) :
INDENT
    r = []
    p = q = None
    for x in l + [- 1] :
    INDENT
        if x - 1 == q :
        INDENT
            q += 1
        DEDENT
        else :
        INDENT
            if p :
            INDENT
                if q > p :
                INDENT
                    r.append('%s-%s' % (p, q))
                DEDENT
                else :
                INDENT
                    r.append(str(p))
                DEDENT
            DEDENT
            p = q = x
        DEDENT
    DEDENT
    return '(%s)' % ', '.join(r)
DEDENT

def dataType(string) :
INDENT
    odp = ''
    patternBIT = re.compile('[01]')
    patternINT = re.compile('[0-9]+')
    patternFLOAT = re.compile('[0-9]+\.[0-9]+')
    patternTEXT = re.compile('[a-zA-Z0-9]+')
    if patternTEXT.match(string) :
    INDENT
        odp = "text"
    DEDENT
    if patternFLOAT.match(string) :
    INDENT
        odp = "FLOAT"
    DEDENT
    if patternINT.match(string) :
    INDENT
        odp = "INT"
    DEDENT
    if patternBIT.match(string) :
    INDENT
        odp = "BIT"
    DEDENT
    return odp
DEDENT

def almostIncreasingSequence(sequence) :
INDENT
    t = 0
    for i in range(len(sequence)) :
    INDENT
        temp = sequence.copy()
        del temp [i]
        if temp == sorted(temp) and not (any(i == j for i, j in zip(sorted(temp), sorted(temp) [1 :]))) :
        INDENT
            t += 1
        DEDENT
    DEDENT
    return t > 0
DEDENT

def deleteDir(path) :
INDENT
    if mswindows :
    INDENT
        cmd = "RMDIR " + path + " /s /q"
    DEDENT
    else :
    INDENT
        cmd = "rm -rf " + path
    DEDENT
    result = getstatusoutput(cmd)
    if (result [0] ! = 0) :
    INDENT
        raise RuntimeError(result [1])
    DEDENT
DEDENT

def unique(seq) :
INDENT
    seen = set()
    for x in seq :
    INDENT
        if x not in seen :
        INDENT
            seen.add(x)
            yield x
        DEDENT
    DEDENT
DEDENT

def myfunc(orientation, l, w) :
INDENT
    a, b = (w, l) if orientation % 2 else (l, w)
    if orientation < = 4 :
    INDENT
        a = - a
    DEDENT
    if orientation in (3, 4, 7, 8) :
    INDENT
        b = - b
    DEDENT
    return a, b
DEDENT

def factorial(n) :
INDENT
    base = 1
    for i in range(n, 0, - 1) :
    INDENT
        base = base * i
    DEDENT
    print base
DEDENT

    def test_extra_template_params(self):
        """
        A template view can be customized to return extra context.
        """
        response = self.client.get('/template/custom/bar/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['foo'], 'bar')
        self.assertEqual(response.context['key'], 'value')
        self.assertIsInstance(response.context['view'], View)

def product(ar_list) :
INDENT
    if not ar_list :
    INDENT
        yield ()
    DEDENT
    else :
    INDENT
        for a in ar_list [0] :
        INDENT
            for prod in product(ar_list [1 :]) :
            INDENT
                yield (a,) + prod
            DEDENT
        DEDENT
    DEDENT
DEDENT

def censored(sentence, words) :
INDENT
    for word in words :
    INDENT
        if word in sentence :
        INDENT
            sentence = sentence.replace(word, "*" * len(word))
        DEDENT
    DEDENT
    return sentence
DEDENT

def query_yes_no(question, default = "yes") :
INDENT
    valid = {"yes" : True, "y" : True, "ye" : True,
        "no" : False, "n" : False}
    if default is None :
    INDENT
        prompt = " [y/n] "
    DEDENT
    elif default == "yes" :
    INDENT
        prompt = " [Y/n] "
    DEDENT
    elif default == "no" :
    INDENT
        prompt = " [y/N] "
    DEDENT
    else :
    INDENT
        raise ValueError("invalid default answer: '%s'" % default)
    DEDENT
    while True :
    INDENT
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '' :
        INDENT
            return valid [default]
        DEDENT
        elif choice in valid :
        INDENT
            return valid [choice]
        DEDENT
        else :
        INDENT
            sys.stdout.write("Please respond with 'yes' or 'no' "
                "(or 'y' or 'n').\n")
        DEDENT
    DEDENT
DEDENT

def treeview_sort_column(tv, col, reverse) :
INDENT
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    try :
    INDENT
        l.sort(key = lambda t : int(t [0]), reverse = reverse)
    DEDENT
    except ValueError :
    INDENT
        l.sort(reverse = reverse)
    DEDENT
    for index, (val, k) in enumerate(l) :
    INDENT
        tv.move(k, '', index)
    DEDENT
    tv.heading(col, command = lambda : treeview_sort_column(tv, col, not reverse))
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

def reverse(s) :
INDENT
    i = len(s) - 1
    sNew = ''
    while i > = 0 :
    INDENT
        sNew = sNew + str(s [i])
        i = i - 1
    DEDENT
    return sNew
DEDENT

    def test_cached_views(self):
        """
        A template view can be cached
        """
        response = self.client.get('/template/cached/bar/')
        self.assertEqual(response.status_code, 200)

        time.sleep(1.0)

        response2 = self.client.get('/template/cached/bar/')
        self.assertEqual(response2.status_code, 200)

        self.assertEqual(response.content, response2.content)

        time.sleep(2.0)

        # Let the cache expire and test again
        response2 = self.client.get('/template/cached/bar/')
        self.assertEqual(response2.status_code, 200)

        self.assertNotEqual(response.content, response2.content)

def default(self, o) :
INDENT
    if isinstance(o, MyClass) :
    INDENT
        return o.__repr__()
    DEDENT
    else :
    INDENT
        return super(self, o)
    DEDENT
DEDENT

def switch(mode) :
INDENT
    switcher = {'a' : a, 'b' : b, 'ab' : (a, b)}
    if type(switcher [mode]) is tuple :
    INDENT
        for func in switcher [mode] :
        INDENT
            func()
        DEDENT
    DEDENT
    else :
    INDENT
        switcher [mode]()
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

def remove_user(self, user_or_username) :
INDENT
    try :
    INDENT
        username = user_or_username.name
    DEDENT
    except AttributeError :
    INDENT
        username = user_or_username
    DEDENT
    remote.remove(username)
DEDENT

def seq(start, stop, step = 1, digit = 0) :
INDENT
    x = float(start)
    v = []
    while x < = stop :
    INDENT
        v.append(round(x, digit))
        x += step
    DEDENT
    return v
DEDENT

    def test_content_type(self):
        response = self.client.get('/template/content_type/')
        self.assertEqual(response['Content-Type'], 'text/plain')

def power_function(decimal, integer) :
INDENT
    num = 1
    for function in range(abs(integer)) :
    INDENT
        if integer > 0 :
        INDENT
            num *= decimal
        DEDENT
        if integer < 0 :
        INDENT
            num *= 1.0 / decimal
        DEDENT
        if integer == 0 :
        INDENT
            num = 1
        DEDENT
    DEDENT
    return num
DEDENT

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

def run(self) :
INDENT
    print '>>>> check driver ok and ensure driver quit'
    driver, ok = self.driverfactory()
    try :
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
    finally :
    INDENT
        driver.quit()
    DEDENT
DEDENT

    def test_resolve_view(self):
        match = resolve('/template/content_type/')
        self.assertIs(match.func.view_class, TemplateView)
        self.assertEqual(match.func.view_initkwargs['content_type'], 'text/plain')

def setup(self) :
INDENT
    from os.path import abspath, dirname
    from os import access, F_OK
    fixture_dir = abspath(dirname(__file__)) + "/fixtures/"
    self.fixture_dir = fixture_dir
    exists = access(fixture_dir, F_OK)
    assert exists, "Oops! the fixture dir should be here " + fixture_dir
    assert access(fixture_dir + "profiles-source1.csv", F_OK)
DEDENT

def countSubStringMatchRecursive(target, key, counter = 0) :
INDENT
    if find(target, key) == 0 :
    INDENT
        countSubStringMatchRecursive(target [1 :], key, counter + 1)
    DEDENT
    elif find(target, key) > 0 :
    INDENT
        countSubStringMatchRecursive(target [1 :], key, counter)
    DEDENT
    elif find(target, key) == - 1 :
    INDENT
        print counter
    DEDENT
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

    def test_resolve_login_required_view(self):
        match = resolve('/template/login_required/')
        self.assertIs(match.func.view_class, TemplateView)

def draw(self, win, left, top, width, height) :
INDENT
    label_space = 40
    label = Text(Point(Point(left + 0.5 * width, top + 0.5 * label_space)), self.label)
    label.fontSize = 20
    label.setFill(Black)
    label.draw(win)
    days = 5
    columns = [left + width * n / days for n in range(days + 1)]
    periods = 5
    rows = [top + label_space + (height - label_space) * n / periods for n in range(periods + 1)]
    for p in self.periods :
    INDENT
        p.draw(win, rows, columns)
    DEDENT
DEDENT

def __init__(self, * args, ** kwords) :
INDENT
    Text.__init__(self, * args, ** kwords)
    if not ROText.tagInit :
    INDENT
        self.init_tag()
    DEDENT
    bindTags = tuple(tag if tag ! = "Text" else "ROText" for tag in self.bindtags())
    self.bindtags(bindTags)
DEDENT

def __init__(cls, * a, ** k) :
INDENT
    mkl = cls.__class__
    class spec(mkl) : pass
    for n, v in vars(cls).items() :
    INDENT
        if isinstance(v, const) :
        INDENT
            setattr(spec, n, v)
        DEDENT
    DEDENT
    spec.__name__ = mkl.__name__
    cls.__class__ = spec
DEDENT

def dfs(current_path) :
INDENT
    row, col = current_path [- 1]
    if (row, col) == goal_state :
    INDENT
        return True
    DEDENT
    for direction in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)] :
    INDENT
        new_row, new_col = direction
        if (0 < = new_row < num_rows and 0 < = new_col < num_cols and
            matrix [new_row] [new_col] == "0" and
            (new_row, new_col) not in current_path) :
        INDENT
            current_path.append((new_row, new_col))
            if dfs(current_path) :
            INDENT
                return True
            DEDENT
            else :
            INDENT
                current_path.pop()
            DEDENT
        DEDENT
    DEDENT
DEDENT

def iterload(string_or_fp, cls = json.JSONDecoder, ** kwargs) :
INDENT
    if isinstance(string_or_fp, file) :
    INDENT
        string = string_or_fp.read()
    DEDENT
    else :
    INDENT
        string = str(string_or_fp)
    DEDENT
    decoder = cls(** kwargs)
    idx = WHITESPACE.match(string, 0).end()
    while idx < len(string) :
    INDENT
        obj, end = decoder.raw_decode(string, idx)
        yield obj
        idx = WHITESPACE.match(string, end).end()
    DEDENT
DEDENT

def is_square(apositiveint) :
INDENT
    x = apositiveint / / 2
    seen = set([x])
    while x * x ! = apositiveint :
    INDENT
        x = (x + (apositiveint / / x)) / / 2
        if x in seen : return False
        seen.add(x)
    DEDENT
    return True
DEDENT

def rep_str(string, search, replacement) :
INDENT
    result = ''
    i = 0
    while i < len(string) :
    INDENT
        if string [i : i + len(search)] == search :
        INDENT
            result += replacement
            i += len(search)
        DEDENT
        else :
        INDENT
            result += string [i]
            i += 1
        DEDENT
    DEDENT
    return result
DEDENT

def __init__(self) :
INDENT
    self.button = gtk.Button()
    self.hbox = gtk.HBox()
    self.hbox.pack_start(self.button, False)
    self.button.set_image(self.OPEN_IMAGE)
    self.button.connect('clicked', self.the_method, "plop")
    self.toggled = True
DEDENT

    def test_extra_context(self):
        response = self.client.get('/template/extra_context/')
        self.assertEqual(response.context['title'], 'Title')


def run(cmd, timeout_sec) :
INDENT
    proc = Popen(shlex.split(cmd), stdout = PIPE, stderr = PIPE)
    timer = Timer(timeout_sec, proc.kill)
    try :
    INDENT
        timer.start()
        stdout, stderr = proc.communicate()
    DEDENT
    finally :
    INDENT
        timer.cancel()
    DEDENT
DEDENT

def get_form_instance(self, step) :
INDENT
    if not self.instance_dict :
    INDENT
        if 'project_id' in self.kwargs :
        INDENT
            project_id = self.kwargs ['project_id']
            return Project.objects.get(id = project_id)
        DEDENT
    DEDENT
    return None
DEDENT

def __str__(self) :
INDENT
    rep = self.name + "\t" + super(BJ_hand, self).__str__()
    if self.total :
    INDENT
        rep += "(" + str(self.total) + ")"
    DEDENT
    return rep
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
class RedirectViewTest(SimpleTestCase):

    rf = RequestFactory()

    def test_no_url(self):
        "Without any configuration, returns HTTP 410 GONE"
        response = RedirectView.as_view()(self.rf.get('/foo/'))
        self.assertEqual(response.status_code, 410)

def decrypt(key, encoded) :
INDENT
    key = key.encode('ascii')
    padded_key = key.ljust(KEY_SIZE, b'\0')
    ciphertext = base64.b64decode(encoded.encode('ascii'))
    sg = pprp.data_source_gen(ciphertext, block_size = BLOCK_SIZE)
    dg = pprp.rjindael_decrypt_gen(padded_key, sg, block_size = BLOCK_SIZE)
    return pprp.decrypt_sink(dg).decode('utf-8')
DEDENT

def test_foo() :
INDENT
    import sys
    from foomodule import foo
    from StringIO import StringIO
    saved_stdout = sys.stdout
    try :
    INDENT
        out = StringIO()
        sys.stdout = out
        foo()
        output = out.getvalue().strip()
        assert output == 'hello world!'
    DEDENT
    finally :
    INDENT
        sys.stdout = saved_stdout
    DEDENT
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

def get_fs_type(mypath) :
INDENT
    root_type = ""
    for part in psutil.disk_partitions() :
    INDENT
        if part.mountpoint == '/' :
        INDENT
            root_type = part.fstype
            continue
        DEDENT
        if mypath.startswith(part.mountpoint) :
        INDENT
            return part.fstype
        DEDENT
    DEDENT
    return root_type
DEDENT

def pop(self, key = None, default = object()) :
INDENT
    if key is None :
    INDENT
        return self.popitem()
    DEDENT
    return super(MyOrderedDict, self).pop(self.keys() [key], default = default)
DEDENT

def get_list(self, term, offset = 0, limit = DEFAULT_PAGE_SIZE) :
INDENT
    filters = list(
        field.ilike(u'%%%s%%' % term) for field in self._cached_fields
        )
    for f in self.additional_filters :
    INDENT
        filters.append(f)
    DEDENT
    return (
        db.session.query(self.model)
        .filter(* filters)
        .all())
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

    def test_default_redirect(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.get('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def __init__(self, server_address, HandlerClass) :
INDENT
    socketserver.BaseServer.__init__(self, server_address, HandlerClass)
    self.address_family = socket.AF_INET
    self.socket = socket.socket(self.address_family, self.socket_type)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_bind()
    self.server_activate()
DEDENT

def getIsland(request) :
INDENT
    if hasattr(request, "_cached_island") :
    INDENT
        return request._cached_island
    DEDENT
    try :
    INDENT
        island = Island.objects.get(user = request.user)
    DEDENT
    except Island.DoesNotExist :
    INDENT
        island = Island(user = request.user)
        island.save()
    DEDENT
    island.update()
    request._cached_island = island
    return island
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

    def test_permanent_redirect(self):
        "Permanent redirects are an option"
        response = RedirectView.as_view(url='/bar/', permanent=True)(self.rf.get('/foo/'))
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/bar/')

def go(list1) :
INDENT
    odd = None
    even = None
    for i in range(0, len(list1)) :
    INDENT
        if list1 [i] % 2 == 1 :
        INDENT
            odd = i
            break
        DEDENT
    DEDENT
    if odd is not None :
    INDENT
        for i in range(odd, len(list1)) :
        INDENT
            if list1 [i] % 2 == 0 :
            INDENT
                even = i
                break
            DEDENT
        DEDENT
    DEDENT
    if odd is None or even is None :
    INDENT
        return - 1
    DEDENT
    else :
    INDENT
        return even - odd
    DEDENT
DEDENT

def quantityFunction(product) :
INDENT
    valid = False
    while True :
    INDENT
        if product is not None :
        INDENT
            quantity = raw_input("Please enter the amount of this item you would like to purchase: ")
            if quantity.isdigit() :
            INDENT
                return int(quantity)
                valid = True
            DEDENT
            else :
            INDENT
                print ("We didn't recognise that number. Please try again.")
                continue
            DEDENT
        DEDENT
        return False
    DEDENT
DEDENT

def random_grid(file) :
INDENT
    grid = []
    num_rows = int(raw_input("How many rows would you like in your grid? "))
    num_columns = int(raw_input("How many columns would you like in your grid? "))
    min_range = int(raw_input("What is the minimum number you would like in your grid? "))
    max_range = int(raw_input("What is the maximum number you would like in your grid? "))
    for _ in range(num_rows) :
    INDENT
        grid.append([random.randint(min_range, max_range) for _ in range(num_columns)])
    DEDENT
    grid_str = '\n'.join(' '.join(map(str, row)) for row in grid)
    with open(r"test.txt", 'w') as text_file :
    INDENT
        text_file.write(grid_str)
    DEDENT
DEDENT

def format(self, record) :
INDENT
    levelname = record.levelname
    color = COLOR_SEQ % (30 + COLORS [levelname])
    message = logging.Formatter.format(self, record)
    message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ).replace("$COLOR", color)
    for k, v in COLORS.items() :
    INDENT
        message = message.replace("$" + k, COLOR_SEQ % (v + 30)).replace("$BG" + k, COLOR_SEQ % (v + 40)).replace("$BG-" + k, COLOR_SEQ % (v + 40))
    DEDENT
    return message + RESET_SEQ
DEDENT

def pairsum_n(list1, value) :
INDENT
    set1 = set(list1)
    if list1.count(value / 2) < 2 :
    INDENT
        set1.remove(value / 2)
    DEDENT
    return set((min(x, value - x), max(x, value - x)) for x in filterfalse(lambda x : (value - x) not in set1, set1))
DEDENT

    def test_temporary_redirect(self):
        "Temporary redirects are an option"
        response = RedirectView.as_view(url='/bar/', permanent=False)(self.rf.get('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def __getattr__(self, key) :
INDENT
    try :
    INDENT
        return self [key]
    DEDENT
    except KeyError :
    INDENT
        raise AttributeError(key)
    DEDENT
DEDENT

def __init__(self, data) :
INDENT
    SudsObject.__init__(self)
    self.__keylist__ = data.keys()
    for key, value in data.items() :
    INDENT
        if isinstance(value, dict) :
        INDENT
            setattr(self, key, FakeSudsNode(value))
        DEDENT
        else :
        INDENT
            setattr(self, key, value)
        DEDENT
    DEDENT
DEDENT

def foo(x) :
INDENT
    matches = re.findall('[a-z]{2,}', x)
    for m in matches :
    INDENT
        x = x.replace(m, '","'.join(y for y in list(m)))
    DEDENT
    x = x.replace(')', '"],"')
    x = x.replace('(', '",["')
    x = '["' + x + '"]'
    x = x.replace('"",', '')
    x = x.replace(',""', '')
    try :
    INDENT
        return json.loads(x)
    DEDENT
    except :
    INDENT
        return "error"
    DEDENT
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

    def test_include_args(self):
        "GET arguments can be included in the redirected URL"
        response = RedirectView.as_view(url='/bar/')(self.rf.get('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

        response = RedirectView.as_view(url='/bar/', query_string=True)(self.rf.get('/foo/?pork=spam'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/?pork=spam')

def factorize(n) :
INDENT
    divisors = itertools.count(2)
    for divisor in divisors :
    INDENT
        if divisor ** 2 > n :
        INDENT
            yield n
            break
        DEDENT
        while n % divisor == 0 :
        INDENT
            yield divisor
            n //= divisor
        DEDENT
    DEDENT
DEDENT

def __init__(self, original_function, maxsize = 1000) :
INDENT
    self.original_function = original_function
    self.maxsize = maxsize
    self.mapping = {}
    PREV, NEXT, KEY, VALUE = 0, 1, 2, 3
    self.head = [None, None, None, None]
    self.tail = [self.head, None, None, None]
    self.head [NEXT] = self.tail
DEDENT

def send_email(user, password, recipient, subject, body) :
INDENT
    gmail_user = user
    gmail_pwd = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
DEDENT

def clean_code(self) :
INDENT
    input_code = self.cleaned_data ['code']
    try :
    INDENT
        discount_code = self.event.discounts.get(code = input_code)
    DEDENT
    except Discount.DoesNotExist :
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

def get_word_len_dict(text) :
INDENT
    result_dict = {}
    for word in text.split() :
    INDENT
        if not result_dict.get(str(len(word))) :
        INDENT
            result_dict [str(len(word))] = []
        DEDENT
        if not word in result_dict [str(len(word))] :
        INDENT
            result_dict [str(len(word))].append(word)
        DEDENT
    DEDENT
    return result_dict
DEDENT

def merge(* args) :
INDENT
    import copy
    def merge_lists(left, right) :
    INDENT
        result = []
        while (len(left) and len(right)) :
        INDENT
            which_list = (left if left [0] < = right [0] else right)
            result.append(which_list.pop(0))
        DEDENT
        return result + left + right
    DEDENT
    lists = [arg for arg in args]
    while len(lists) > 1 :
    INDENT
        left, right = copy.copy(lists.pop(0)), copy.copy(lists.pop(0))
        result = merge_lists(left, right)
        lists.append(result)
    DEDENT
    return lists.pop(0)
DEDENT

def draw() :
INDENT
    try :
    INDENT
        while True :
        INDENT
            for x in range(0, 10) :
            INDENT
                for y in range(0, 10) :
                INDENT
                    if (coord [i] [j] == 0) :
                    INDENT
                        canvas.create_rectangle((x * 40) + 10, (y * 40) + 10, (x * 40) + 50, (y * 40) + 50, fill = "white")
                    DEDENT
                    if (coord [i] [j] == 1) :
                    INDENT
                        canvas.create_rectangle((x * 40) + 10, (y * 40) + 10, (x * 40) + 50, (y * 40) + 50, fill = "red")
                    DEDENT
                    if (coord [i] [j] == 2) :
                    INDENT
                        canvas.create_rectangle((x * 40) + 10, (y * 40) + 10, (x * 40) + 50, (y * 40) + 50, fill = "darkorange")
                    DEDENT
                DEDENT
            DEDENT
        DEDENT
        time.sleep(0.03)
    DEDENT
    except Exception as e :
    INDENT
        print (e)
        raise
    DEDENT
DEDENT

def __init__(self, parent, chain_no) :
INDENT
    wx.Frame.__init__(self, parent, - 1, title = "Dialog " + str(chain_no))
    self.chain_no = self.saved_chain_no = chain_no
    self.result = None
    self.parent = parent
    panel = wx.Panel(self)
    sizer = wx.BoxSizer(wx.VERTICAL)
    if parent.dlg_prev_value ! = 0 :
    INDENT
        sizer.Add(wx.StaticText(
                panel, - 1, "Answer from previous Dialog: %s" % parent.dlg_prev_value))
    DEDENT
    sizer.Add(wx.StaticText(panel, - 1, "Try to scroll in Different Frame to "
            "see if it is blocked"))
    btn1 = wx.Button(panel, - 1, "Step " + str(self.chain_no))
    btn2 = wx.Button(panel, - 1, "Previous")
    btn3 = wx.Button(panel, - 1, "Cancel")
    self.Bind(wx.EVT_BUTTON, self.OnStep, id = btn1.GetId())
    self.Bind(wx.EVT_BUTTON, self.OnPrev, id = btn2.GetId())
    self.Bind(wx.EVT_BUTTON, self.OnCancel, id = btn3.GetId())
    sizer.Add(btn1)
    sizer.Add(btn2)
    sizer.Add(btn3)
    panel.SetSizer(sizer)
    self.Show()
DEDENT

    def test_include_urlencoded_args(self):
        "GET arguments can be URL-encoded when included in the redirected URL"
        response = RedirectView.as_view(url='/bar/', query_string=True)(
            self.rf.get('/foo/?unicode=%E2%9C%93'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/?unicode=%E2%9C%93')

def paintEvent(self, event) :
INDENT
    super(MySlider, self).paintEvent(event)
    qp = QPainter(self)
    pen = QPen()
    pen.setWidth(2)
    pen.setColor(Qt.black)
    qp.setPen(pen)
    font = QFont('Times', 10)
    qp.setFont(font)
    self.setContentsMargins(50, 50, 50, 50)
    self.setFixedSize(QSize(slider_x, slider_y))
    contents = self.contentsRect()
    max = self.maximum()
    min = self.minimum()
    y_inc = slider_y - (slider_y - groove_y) / 2
    for i in range(len(slider_step)) :
    INDENT
        qp.drawText(contents.x() - 2 * font.pointSize(), y_inc + font.pointSize() / 2, '{0:3}'.format(slider_step [i]))
        qp.drawLine(contents.x() + 2 * font.pointSize(), y_inc, contents.x() + contents.width(), y_inc)
        y_inc -= groove_y / (max - min)
    DEDENT
DEDENT

def avg(self) :
INDENT
    tot = 0
    for item in self :
    INDENT
        if isinstance(item, int) :
        INDENT
            tot += item
        DEDENT
        else :
        INDENT
            print ('Invalid item in list. All items need to be an integer.')
        DEDENT
    DEDENT
    return tot / len(self)
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

    def test_parameter_substitution(self):
        "Redirection URLs can be parameterized"
        response = RedirectView.as_view(url='/bar/%(object_id)d/')(self.rf.get('/foo/42/'), object_id=42)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/42/')

def setUp(self) :
INDENT
    APP_CONFIGS = ['/path/to/app.yaml']
    python_runtime._RUNTIME_ARGS = [
        sys.executable,
        os.path.join(os.path.dirname(dev_appserver.__file__),
            '_python_runtime.py')]
    options = devappserver2.PARSER.parse_args([
            '--admin_port', '0',
            '--port', '8123',
            '--datastore_path', ':memory:',
            '--logs_path', ':memory:',
            '--skip_sdk_update_check',
            '--',
            ] + APP_CONFIGS)
    server = devappserver2.DevelopmentServer()
    server.start(options)
    self.server = server
DEDENT

def __getitem__(self, key) :
INDENT
    if isinstance(key, int) :
    INDENT
        return super(MyOrderedDict, self).__getitem__(self.keys() [key])
    DEDENT
    if isinstance(key, slice) :
    INDENT
        return [super(MyOrderedDict, self).__getitem__(k) for k in self.keys() [key]]
    DEDENT
    return super(MyOrderedDict, self).__getitem__(key)
DEDENT

def translation_function(language) :
INDENT
    try :
    INDENT
        lang = gettext.translation('simple', localedir = 'locale', languages = [language])
        lang.install()
        while True :
        INDENT
            print (_("Running translator"), ": %s" % language)
            time.sleep(1.0)
        DEDENT
    DEDENT
    except KeyboardInterrupt :
    INDENT
        pass
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

    def test_named_url_pattern(self):
        "Named pattern parameter should reverse to the matching pattern"
        response = RedirectView.as_view(pattern_name='artist_detail')(self.rf.get('/foo/'), pk=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/detail/artist/1/')

def run(cmd, timeout_sec) :
INDENT
    proc = Popen(shlex.split(cmd), stdout = PIPE, stderr = PIPE)
    timer = Timer(timeout_sec, proc.kill)
    try :
    INDENT
        timer.start()
        stdout, stderr = proc.communicate()
    DEDENT
    finally :
    INDENT
        timer.cancel()
    DEDENT
DEDENT

def issorted(x) :
INDENT
    try :
    INDENT
        if x.dtype.kind == 'u' :
        INDENT
            x = numpy.int64(x)
        DEDENT
    DEDENT
    except AttributeError :
    INDENT
        pass
    DEDENT
    return (numpy.diff(x) > = 0).all()
DEDENT

def prob7(inlist) :
INDENT
    outlist = []
    for x in inlist :
    INDENT
        try :
        INDENT
            outlist += x
        DEDENT
        except TypeError :
        INDENT
            outlist.append(x)
        DEDENT
    DEDENT
    return outlist
DEDENT

def almostIncreasingSequence(sequence) :
INDENT
    t = 0
    for i in range(len(sequence)) :
    INDENT
        temp = sequence.copy()
        del temp [i]
        if temp == sorted(temp) and not (any(i == j for i, j in zip(sorted(temp), sorted(temp) [1 :]))) :
        INDENT
            t += 1
        DEDENT
    DEDENT
    return t > 0
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

def long_substr(data) :
INDENT
    substr = ''
    if len(data) > 1 and len(data [0]) > 0 :
    INDENT
        for i in range(len(data [0])) :
        INDENT
            for j in range(len(data [0]) - i + 1) :
            INDENT
                if j > len(substr) and is_substr(data [0] [i : i + j], data) :
                INDENT
                    substr = data [0] [i : i + j]
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return substr
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

    def test_named_url_pattern_using_args(self):
        response = RedirectView.as_view(pattern_name='artist_detail')(self.rf.get('/foo/'), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/detail/artist/1/')

def children(self) :
INDENT
    stack = [self.entities]
    push = stack.append
    pop = stack.pop
    while stack :
    INDENT
        for e in pop() :
        INDENT
            yield e
            if e.entities :
            INDENT
                push(e.entities)
            DEDENT
        DEDENT
    DEDENT
DEDENT

def foo(x) :
INDENT
    if not isinstance(x, list) :
    INDENT
        x = [x]
    DEDENT
    for y in x :
    INDENT
        do_something(y)
    DEDENT
DEDENT

def is_less(a, b) :
INDENT
    i = 0
    while i < len(a) :
    INDENT
        if a [i] < b [i] :
        INDENT
            return True
        DEDENT
        else :
        INDENT
            if a [i] > b [i] :
            INDENT
                return False
            DEDENT
        DEDENT
        i += 1
    DEDENT
    return False
DEDENT

def __call__(self, parser, namespace, values, option_string = None) :
INDENT
    def all_opt_strings(parser) :
    INDENT
        nested = (x.option_strings for x in parser._actions
            if x.option_strings)
        return itertools.chain.from_iterable(nested)
    DEDENT
    all_opts = list(all_opt_strings(parser))
    eaten = []
    while len(values) > 0 :
    INDENT
        if values [0] in all_opts :
        INDENT
            break
        DEDENT
        eaten.append(values.pop(0))
    DEDENT
    setattr(namespace, self.dest, eaten)
    _, extras = parser._parse_known_args(values, namespace)
    try :
    INDENT
        getattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR).extend(extras)
    DEDENT
    except AttributeError :
    INDENT
        setattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR, extras)
    DEDENT
DEDENT

def __call__(self, * args, ** kwargs) :
INDENT
    obj = type.__call__(self)
    obj.defaults = _DEFAULTS [obj.__class__.__name__]
    for klass in obj.__class__.__bases__ :
    INDENT
        if klass.__name__ in _DEFAULTS :
        INDENT
            obj.defaults.update(_DEFAULTS [klass.__name__])
        DEDENT
    DEDENT
    return obj
DEDENT

def fib(n) :
INDENT
    a = 0
    b = 1
    for i in range(1, n + 1) :
    INDENT
        c = a + b
        print c
        a = b
        b = c
    DEDENT
DEDENT

def test() :
INDENT
    import time
    def m_int(s, memo = {}) :
    INDENT
        if s in memo :
        INDENT
            return memo [s]
        DEDENT
        else :
        INDENT
            retval = memo [s] = int(s)
            return retval
        DEDENT
    DEDENT
    data = get_data()
    all_point_sets = []
    time_start = time.time()
    for xs, ys in data :
    INDENT
        point_set = []
        y_iter = iter(ys.split(","))
        curr_points = [Point(m_int(i), m_int(next(y_iter))) for i in xs.split(",")]
        all_point_sets.append(curr_points)
    DEDENT
    time_end = time.time()
    print "total time: ", (time_end - time_start)
DEDENT

def stemming(verb) :
INDENT
    suffixes = ["ing", "ed", "es", "s"]
    for suffix in suffixes :
    INDENT
        if verb.endswith(suffix) :
        INDENT
            return verb [: - len(suffix)]
        DEDENT
    DEDENT
    return verb
DEDENT

    def test_redirect_POST(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.post('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def date_hook(json_dict) :
INDENT
    for (key, value) in json_dict.items() :
    INDENT
        try :
        INDENT
            json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        DEDENT
        except :
        INDENT
            pass
        DEDENT
    DEDENT
    return json_dict
DEDENT

def flatten(iterable) :
INDENT
    iterator, sentinel, stack = iter(iterable), object(), []
    while True :
    INDENT
        value = next(iterator, sentinel)
        if value is sentinel :
        INDENT
            if not stack :
            INDENT
                break
            DEDENT
            iterator = stack.pop()
        DEDENT
        elif isinstance(value, str) :
        INDENT
            yield value
        DEDENT
        else :
        INDENT
            try :
            INDENT
                new_iterator = iter(value)
            DEDENT
            except TypeError :
            INDENT
                yield value
            DEDENT
            else :
            INDENT
                stack.append(iterator)
                iterator = new_iterator
            DEDENT
        DEDENT
    DEDENT
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

def __init__(self, columns, values) :
INDENT
    if len(values) ! = len(columns) :
    INDENT
        raise Exception("Bad values")
    DEDENT
    self.columns = columns
    self.values = values
    self.index = values [0]
    super(Dataframe, self).__init__(dict(zip(columns, values)))
    pass
DEDENT

    def test_redirect_HEAD(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.head('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def outer() :
INDENT
    y = 0
    def inner() :
    INDENT
        ctypes.pythonapi.PyCell_Set(id(inner.func_closure [0]), id(y + 1))
        return y
    DEDENT
    return inner
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

def download_file(url) :
INDENT
    local_filename = url.split('/') [- 1]
    r = requests.get(url, stream = True)
    with open(local_filename, 'wb') as f :
    INDENT
        shutil.copyfileobj(r.raw, f)
    DEDENT
    return local_filename
DEDENT

def dfs(graph, start) :
INDENT
    visited = {}
    stack = [(start, "XXX_THIS_NODE_DOES_NOT_EXIST_XXX")]
    while stack :
    INDENT
        node, parent = stack.pop()
        if parent is None :
        INDENT
            if visited [node] < 3 :
            INDENT
                print "{}_end".format(node)
            DEDENT
            visited [node] = 3
        DEDENT
        elif node not in visited :
        INDENT
            if visited.get(parent) == 2 :
            INDENT
                print "{}_middle".format(parent)
            DEDENT
            elif visited.get(parent) == 1 :
            INDENT
                visited [parent] = 2
            DEDENT
            print "{}_start".format(node)
            visited [node] = 1
            stack.append((node, None))
            for child in reversed(graph.get(node, [])) :
            INDENT
                if child not in visited :
                INDENT
                    stack.append((child, node))
                DEDENT
            DEDENT
        DEDENT
    DEDENT
DEDENT

def foo(hive, flag) :
INDENT
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        0, winreg.KEY_READ | flag)
    count_subkey = winreg.QueryInfoKey(aKey) [0]
    software_list = []
    for i in range(count_subkey) :
    INDENT
        software = {}
        try :
        INDENT
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software ['name'] = winreg.QueryValueEx(asubkey, "DisplayName") [0]
            try :
            INDENT
                software ['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion") [0]
            DEDENT
            except EnvironmentError :
            INDENT
                software ['version'] = 'undefined'
            DEDENT
            try :
            INDENT
                software ['publisher'] = winreg.QueryValueEx(asubkey, "Publisher") [0]
            DEDENT
            except EnvironmentError :
            INDENT
                software ['publisher'] = 'undefined'
            DEDENT
            software_list.append(software)
        DEDENT
        except EnvironmentError :
        INDENT
            continue
        DEDENT
    DEDENT
    return software_list
DEDENT

def create_random(cls, level) :
INDENT
    symbol = None
    r = random.random()
    cumulative = 0.0
    for k, v in operators.items() :
    INDENT
        cumulative += v ['prob']
        if r < = cumulative :
        INDENT
            symbol = k
            break
        DEDENT
    DEDENT
    assert symbol ! = None
    left = expression.create_random(level + 1)
    right = expression.create_random(level + 1)
    return binary_expression(symbol, left, right)
DEDENT

    def test_redirect_OPTIONS(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.options('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def scan(self, input) :
INDENT
    self.result = []
    for word in input.split() :
    INDENT
        try :
        INDENT
            self.result.append(('number', int(word)))
        DEDENT
        except ValueError :
        INDENT
            for category, item in self.mapping.items() :
            INDENT
                if word.lower() in item :
                INDENT
                    found_category = category
                    break
                DEDENT
                else :
                INDENT
                    found_category = 'error'
                DEDENT
            DEDENT
            self.result.append((found_category, word))
        DEDENT
    DEDENT
    return self.result
DEDENT

def is_float(text) :
INDENT
    try :
    INDENT
        float(text)
        if text.isalpha() :
        INDENT
            return False
        DEDENT
        return True
    DEDENT
    except ValueError :
    INDENT
        return False
    DEDENT
DEDENT

def fit(self, x, y) :
INDENT
    self = super(LinearRegression, self).fit(x, y)
    n, k = x.shape
    yHat = np.matrix(self.predict(x)).T
    x = np.hstack((np.ones((n, 1)), np.matrix(x)))
    y = np.matrix(y).T
    df = float(n - k - 1)
    sse = np.sum(np.square(yHat - y), axis = 0)
    self.sampleVariance = sse / df
    self.sampleVarianceX = x.T * x
    self.covarianceMatrix = sc.linalg.sqrtm(self.sampleVariance [0, 0] * self.sampleVarianceX.I)
    self.se = self.covarianceMatrix.diagonal() [1 :]
    self.betasTStat = np.zeros(len(self.se))
    for i in xrange(len(self.se)) :
    INDENT
        self.betasTStat [i] = self.coef_ [0, i] / self.se [i]
    DEDENT
    self.betasPValue = 1 - t.cdf(abs(self.betasTStat), df)
DEDENT

    def test_redirect_PUT(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.put('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def decorate(func) :
INDENT
    def wrap_and_call(* args, ** kwargs) :
    INDENT
        if 'str' in inspect.getargspec(func).args :
        INDENT
            kwargs ['str'] = 'Hello!'
        DEDENT
        return func(* args, ** kwargs)
    DEDENT
    return wrap_and_call
DEDENT

def leafs_of_branch(node) :
INDENT
    if len(node.children()) == 0 :
    INDENT
        return [str(node)]
    DEDENT
    else :
    INDENT
        x = []
        for des in node.children() :
        INDENT
            x += leafs_of_branch(des)
        DEDENT
        return x
    DEDENT
DEDENT

def __init__(self, parent, * args, ** kwargs) :
INDENT
    super(MainPanel, self).__init__(parent, * args, ** kwargs)
    """Create and populate main sizer."""
    sizer = wx.BoxSizer(wx.VERTICAL)
    cmd_quit = wx.Button(self, id = wx.ID_EXIT)
    cmd_quit.Bind(wx.EVT_BUTTON, parent.on_quit_click)
    sizer.Add(cmd_quit)
    self.SetSizer(sizer)
DEDENT

    def test_redirect_PATCH(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.patch('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def __add__(self, other) :
INDENT
    try :
    INDENT
        return Time.intToTime(self, Time.timeToInt(self) + Time.timeToInt(other))
    DEDENT
    except AttributeError as e :
    INDENT
        return Time.intToTime(self, Time.timeToInt(self) + other)
    DEDENT
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

    def test_redirect_DELETE(self):
        "Default is a temporary redirect"
        response = RedirectView.as_view(url='/bar/')(self.rf.delete('/foo/'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bar/')

def deep_get(d, keys, default = None) :
INDENT
    assert type(keys) is list
    if d is None :
    INDENT
        return default
    DEDENT
    if not keys :
    INDENT
        return d
    DEDENT
    return deep_get(d.get(keys [0]), keys [1 :], default)
DEDENT

def receive(self) :
INDENT
    while (self.shutdown == False) or (self.queue.empty() == False) :
    INDENT
        try :
        INDENT
            record = self.queue.get(True, self.polltime)
            self._handler.emit(record)
        DEDENT
        except Queue.Empty, e :
        INDENT
            pass
        DEDENT
    DEDENT
DEDENT

    def test_redirect_when_meta_contains_no_query_string(self):
        "regression for #16705"
        # we can't use self.rf.get because it always sets QUERY_STRING
        response = RedirectView.as_view(url='/bar/')(self.rf.request(PATH_INFO='/foo/'))
        self.assertEqual(response.status_code, 302)

def equal_dicts(d1, d2, ignore_keys) :
INDENT
    ignored = set(ignore_keys)
    for k1, v1 in d1.iteritems() :
    INDENT
        if k1 not in ignored and (k1 not in d2 or d2 [k1] ! = v1) :
        INDENT
            return False
        DEDENT
    DEDENT
    for k2, v2 in d2.iteritems() :
    INDENT
        if k2 not in ignored and k2 not in d1 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def find_mount_point(path) :
INDENT
    if not os.path.islink(path) :
    INDENT
        path = os.path.abspath(path)
    DEDENT
    elif os.path.islink(path) and os.path.lexists(os.readlink(path)) :
    INDENT
        path = os.path.realpath(path)
    DEDENT
    while not os.path.ismount(path) :
    INDENT
        path = os.path.dirname(path)
        if os.path.islink(path) and os.path.lexists(os.readlink(path)) :
        INDENT
            path = os.path.realpath(path)
        DEDENT
    DEDENT
    return path
DEDENT

def self_reference(array, index) :
INDENT
    if not isinstance(array, tuple) :
    INDENT
        raise TypeError("array must be a tuple")
    DEDENT
    if not 0 < = index < len(array) :
    INDENT
        raise IndexError("tuple assignment index out of range")
    DEDENT
    arrayobj = ctypes.py_object(array)
    refcnt = ctypes.pythonapi.Py_DecRef(arrayobj)
    for i in range(refcnt - 1) :
    INDENT
        ctypes.pythonapi.Py_DecRef(arrayobj)
    DEDENT
    try :
    INDENT
        ret = ctypes.pythonapi.PyTuple_SetItem(arrayobj, ctypes.c_ssize_t(index), arrayobj)
        if ret ! = 0 :
        INDENT
            raise RuntimeError("PyTuple_SetItem failed")
        DEDENT
    DEDENT
    except :
    INDENT
        raise SystemError("FATAL: PyTuple_SetItem failed: tuple probably unusable")
    DEDENT
    for i in range(refcnt + 1) :
    INDENT
        ctypes.pythonapi.Py_IncRef(arrayobj)
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

    def test_direct_instantiation(self):
        """
        It should be possible to use the view without going through .as_view()
        (#21564).
        """
        view = RedirectView()
        response = view.dispatch(self.rf.head('/foo/'))
        self.assertEqual(response.status_code, 410)


def setup(self) :
INDENT
    import os.path as op
    self.fixture_dir = op.join(op.abspath(op.dirname(__file__)), "fixtures")
    if not os.access(self.fixture_dir, os.F_OK) :
    INDENT
        raise AssertionError("Oops! "
            "the fixture dir should be here " + self.fixture_dir)
    DEDENT
    csvfile = op.join(self.fixture_dir, "profiles-source1.csv")
    assert os.access(csvfile, os.F_OK)
DEDENT

def get_cost(df) :
INDENT
    t_zone = 720
    max_rate = 5.5
    rate = 0.0208
    duration = df ['t1']
    ratecol = []
    for i in duration :
    INDENT
        if i < t_zone :
        INDENT
            if (i * rate) > = max_rate :
            INDENT
                ratecol.append(max_rate)
            DEDENT
            else :
            INDENT
                ratecol.append(i * rate)
            DEDENT
        DEDENT
        else :
        INDENT
            if i > = 720 :
            INDENT
                x = int(i / 720)
                y = ((i % 720) * rate)
                if y > = max_rate :
                INDENT
                    ratecol.append((x * max_rate) + max_rate)
                DEDENT
                else :
                INDENT
                    ratecol.append((x * max_rate) + y)
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return ratecol
DEDENT

def pattern_match(sequence, patterns) :
INDENT
    seq = set(sequence)
    u = set()
    for pattern in patterns :
    INDENT
        u.update(pattern)
    DEDENT
    return seq.issubset(u)
DEDENT

def backspace(self) :
INDENT
    if re.match(r'\d$', self.current) :
    INDENT
        self.display(0)
        self.new_num = True
    DEDENT
    else :
    INDENT
        self.current = self.current [: - 1]
        self.display(self.current)
    DEDENT
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

def update(self, request, * args, ** kwargs) :
INDENT
    partial = True
    instance = self.get_object()
    for photo in request.data.pop("photos") :
    INDENT
        PostImage.objects.create(post = instance, image = photo)
    DEDENT
    serializer = self.get_serializer(instance, data = request.data, partial = partial)
    serializer.is_valid(raise_exception = True)
    self.perform_update(serializer)
    return Response(serializer.data)
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

def select_weighted(d) :
INDENT
    total = 0
    for key in d :
    INDENT
        total = total + len(d [key])
    DEDENT
    accept_prob = float(1.0 / total)
    n_seen = 0
    for key in d :
    INDENT
        current_key = key
        for val in d [key] :
        INDENT
            dice_roll = random.random()
            accept_prob = float(1.0 / (total - n_seen))
            n_seen = n_seen + 1
            if dice_roll < = accept_prob :
            INDENT
                return current_key
            DEDENT
        DEDENT
    DEDENT
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

def func(ax, data, color, position) :
INDENT
    ax.plot(data [0], data [1], color = color)
    ax.spines [position].set_color(color)
    if position == 'left' :
    INDENT
        other = 'right'
    DEDENT
    elif position == 'right' :
    INDENT
        other = 'left'
    DEDENT
    ax.spines [other].set_color('None')
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

class GetContextDataTest(SimpleTestCase):

    def test_get_context_data_super(self):
        test_view = views.CustomContextView()
        context = test_view.get_context_data(kwarg_test='kwarg_value')

        # the test_name key is inserted by the test classes parent
        self.assertIn('test_name', context)
        self.assertEqual(context['kwarg_test'], 'kwarg_value')
        self.assertEqual(context['custom_key'], 'custom_value')

        # test that kwarg overrides values assigned higher up
        context = test_view.get_context_data(test_name='test_value')
        self.assertEqual(context['test_name'], 'test_value')

def changeFileCreationTime(fname, newtime) :
INDENT
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ |
        win32con.FILE_SHARE_WRITE |
        win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL,
        None)
    win32file.SetFileTime(winfile, wintime, wintime, wintime)
    winfile.close()
DEDENT

def find_subclasses(cls) :
INDENT
    results = []
    for sc in cls.__subclasses__() :
    INDENT
        for obj in gc.get_objects() :
        INDENT
            if isinstance(obj, sc) :
            INDENT
                results.append(obj)
            DEDENT
        DEDENT
    DEDENT
    return results
DEDENT

def get_size(start_path = '.') :
INDENT
    total_size = 0
    seen = {}
    for dirpath, dirnames, filenames in os.walk(start_path) :
    INDENT
        for f in filenames :
        INDENT
            fp = os.path.join(dirpath, f)
            try :
            INDENT
                stat = os.stat(fp)
            DEDENT
            except OSError :
            INDENT
                continue
            DEDENT
            try :
            INDENT
                seen [stat.st_ino]
            DEDENT
            except KeyError :
            INDENT
                seen [stat.st_ino] = True
            DEDENT
            else :
            INDENT
                continue
            DEDENT
            total_size += stat.st_size
        DEDENT
    DEDENT
    return total_size
DEDENT

    def test_object_at_custom_name_in_context_data(self):
        # Checks 'pony' key presence in dict returned by get_context_date
        test_view = views.CustomSingleObjectView()
        test_view.context_object_name = 'pony'
        context = test_view.get_context_data()
        self.assertEqual(context['pony'], test_view.object)

def __init__(self, parent = None, * args, ** kwargs) :
INDENT
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(111)
    self.ax.grid(True)
    super(CustomFigCanvas, self).__init__(self.fig)
    self.setParent(parent)
    self.init_figure()
    self.timer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.updateFigure)
    self.timer.start(1000)
DEDENT

def get(self, request, * args, ** kwargs) :
INDENT
    context = self.get_context_data()
    response = HttpResponse(content_type = 'application/pdf')
    response ['Content-Disposition'] = 'inline; filename="worksheet_pdf.pdf"'
    return response
DEDENT

def returnJSONQuestion(questionId) :
INDENT
    url = 'http://answers.yahooapis.com/AnswersService/V1/getQuestion?appid=APPIDREMOVED8&question_id={0}&output=json'
    format_url = url.format(questionId)
    try :
    INDENT
        request = urllib2.Request(format_url)
        tries = 5
        while tries > = 0 :
        INDENT
            try :
            INDENT
                urlobject = urllib2.urlopen(request)
                jsondata = json.load(urlobject)
                print jsondata
                return jsondata
            DEDENT
            except :
            INDENT
                if tries == 0 :
                INDENT
                    raise
                DEDENT
                else :
                INDENT
                    time.sleep(3)
                    tries -= 1
                    continue
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    except urllib2.HTTPError, e :
    INDENT
        print e.code
        logging.exception("Exception")
        raise
    DEDENT
    except urllib2.URLError, e :
    INDENT
        print e.reason
        logging.exception("Exception")
        raise
    DEDENT
    except (json.decoder.JSONDecodeError, ValueError) :
    INDENT
        print 'Question ID ' + questionId + ' Decode JSON has failed'
        logging.info("This qid didn't work " + questionId)
        raise
    DEDENT
DEDENT

def all_pairs(lst) :
INDENT
    if not lst :
    INDENT
        yield [tuple()]
    DEDENT
    elif len(lst) == 1 :
    INDENT
        yield [tuple(lst)]
    DEDENT
    elif len(lst) == 2 :
    INDENT
        yield [tuple(lst)]
    DEDENT
    else :
    INDENT
        if len(lst) % 2 :
        INDENT
            for i in (None, True) :
            INDENT
                if i not in lst :
                INDENT
                    lst = list(lst) + [i]
                    PAD = i
                    break
                DEDENT
            DEDENT
            else :
            INDENT
                while chr(i) in lst :
                INDENT
                    i += 1
                DEDENT
                PAD = chr(i)
                lst = list(lst) + [PAD]
            DEDENT
        DEDENT
        else :
        INDENT
            PAD = False
        DEDENT
        a = lst [0]
        for i in range(1, len(lst)) :
        INDENT
            pair = (a, lst [i])
            for rest in all_pairs(lst [1 : i] + lst [i + 1 :]) :
            INDENT
                rv = [pair] + rest
                if PAD is not False :
                INDENT
                    for i, t in enumerate(rv) :
                    INDENT
                        if PAD in t :
                        INDENT
                            rv [i] = (t [0],)
                            break
                        DEDENT
                    DEDENT
                DEDENT
                yield rv
            DEDENT
        DEDENT
    DEDENT
DEDENT

    def test_object_in_get_context_data(self):
        # Checks 'object' key presence in dict returned by get_context_date #20234
        test_view = views.CustomSingleObjectView()
        context = test_view.get_context_data()
        self.assertEqual(context['object'], test_view.object)


def __init__(cls, name, bases, dct) :
INDENT
    def make_proxy(name) :
    INDENT
        def proxy(self, * args) :
        INDENT
            return getattr(self._obj, name)
        DEDENT
        return proxy
    DEDENT
    type.__init__(cls, name, bases, dct)
    if cls.__wraps__ :
    INDENT
        ignore = set("__%s__" % n for n in cls.__ignore__.split())
        for name in dir(cls.__wraps__) :
        INDENT
            if name.startswith("__") :
            INDENT
                if name not in ignore and name not in dct :
                INDENT
                    setattr(cls, name, property(make_proxy(name)))
                DEDENT
            DEDENT
        DEDENT
    DEDENT
DEDENT

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

def save(self, * args, ** kwargs) :
INDENT
    if self.image_link and not self.image :
    INDENT
        result = urllib.urlretrieve(self.image_link)
        self.image.save(os.path.basename(self.image_link), File(open(result [0], 'r')))
        self.save()
        super(Pin, self).save()
    DEDENT
DEDENT

def findmax(input_string, tempbuffer = defaultdict(list), temp = '') :
INDENT
    if len(input_string) == 0 :
    INDENT
        tempbuffer [len(temp)].append(temp)
        output = tempbuffer [maxkey(tempbuffer)]
        tempbuffer.clear()
        return output
    DEDENT
    else :
    INDENT
        first_char = input_string [0]
        if len(temp) == 0 or first_char > temp [- 1] :
        INDENT
            temp = temp + first_char
        DEDENT
        else :
        INDENT
            tempbuffer [len(temp)].append(temp)
            temp = first_char
        DEDENT
        return findmax(input_string [1 :], tempbuffer, temp)
    DEDENT
DEDENT

def dfs(graph, start) :
INDENT
    print '{}_start'.format(start)
    try :
    INDENT
        for child in graph [start] :
        INDENT
            dfs(graph, child)
            print '{}_middle'.format(start)
        DEDENT
    DEDENT
    except KeyError :
    INDENT
        pass
    DEDENT
    print '{}_end'.format(start)
DEDENT

def remove_user(self, user_or_username) :
INDENT
    try :
    INDENT
        remote.remove(user_or_username.name)
    DEDENT
    except AttributeError :
    INDENT
        remote.remove(user_or_username)
    DEDENT
DEDENT

class UseMultipleObjectMixinTest(SimpleTestCase):
    rf = RequestFactory()

    def test_use_queryset_from_view(self):
        test_view = views.CustomMultipleObjectMixinView()
        test_view.get(self.rf.get('/'))
        # Don't pass queryset as argument
        context = test_view.get_context_data()
        self.assertEqual(context['object_list'], test_view.queryset)

def __new__(cls, name, bases, dct) :
INDENT
    new_dct = {}
    for member_name, member in dct.items() :
    INDENT
        if callable(member) :
        INDENT
            member = cls.wrap(bases, member_name, member)
        DEDENT
        new_dct [member_name] = member
    DEDENT
    return super(ReverserMetaclass, cls).__new__(cls, name, bases, new_dct)
DEDENT

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

def __init__(self) :
INDENT
    super(Dialog, self).__init__()
    layout = QtGui.QVBoxLayout(self)
    splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
    layout.addWidget(splitter)
    list_widget = QtGui.QListWidget()
    splitter.addWidget(list_widget)
    splitter.addWidget(QtGui.QLabel("Test"))
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

def to_bool(value) :
INDENT
    valid = {'true' : True, 't' : True, '1' : True,
        'false' : False, 'f' : False, '0' : False,
        }
    if isinstance(value, bool) :
    INDENT
        return value
    DEDENT
    if not isinstance(value, basestring) :
    INDENT
        raise ValueError('invalid literal for boolean. Not a string.')
    DEDENT
    lower_value = value.lower()
    if lower_value in valid :
    INDENT
        return valid [lower_value]
    DEDENT
    else :
    INDENT
        raise ValueError('invalid literal for boolean: "%s"' % value)
    DEDENT
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

    def test_overwrite_queryset(self):
        test_view = views.CustomMultipleObjectMixinView()
        test_view.get(self.rf.get('/'))
        queryset = [{'name': 'Lennon'}, {'name': 'Ono'}]
        self.assertNotEqual(test_view.queryset, queryset)
        # Overwrite the view's queryset with queryset from kwarg
        context = test_view.get_context_data(object_list=queryset)
        self.assertEqual(context['object_list'], queryset)


def _create_image(self, coord) :
INDENT
    (x, y) = coord
    self.one = ImageTk.PhotoImage(Image.open("test.jpg"))
    root.one = self.one
    self.canvas.create_image(x - 25, y - 25, image = self.one,
        anchor = 'nw', tags = "image")
    self.img_ref.append(self.one)
DEDENT

def is_sorted(stuff) :
INDENT
    for index, item in enumerate(stuff) :
    INDENT
        try :
        INDENT
            if item > stuff [index + 1] :
            INDENT
                return False
            DEDENT
        DEDENT
        except IndexError :
        INDENT
            return True
        DEDENT
    DEDENT
DEDENT

def two_powers(num) :
INDENT
    powers = []
    while num ! = 0 :
    INDENT
        powers.append(num & - num)
        num = num & (num - 1)
    DEDENT
    return powers
DEDENT

class SingleObjectTemplateResponseMixinTest(SimpleTestCase):

    def test_template_mixin_without_template(self):
        """
        We want to makes sure that if you use a template mixin, but forget the
        template, it still tells you it's ImproperlyConfigured instead of
        TemplateDoesNotExist.
        """
        view = views.TemplateResponseWithoutTemplate()
        msg = (
            "TemplateResponseMixin requires either a definition of "
            "'template_name' or an implementation of 'get_template_names()'"
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            view.get_template_names()
def arePermsEqualParity(perm0, perm1) :
INDENT
    perm1 = perm1 [:]
    transCount = 0
    for loc in range(len(perm0) - 1) :
    INDENT
        p0 = perm0 [loc]
        p1 = perm1 [loc]
        if p0 ! = p1 :
        INDENT
            sloc = perm1 [loc :].index(p0) + loc
            perm1 [loc], perm1 [sloc] = p0, p1
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

def combinations(sequence, length, NULL = object()) :
INDENT
    if length < = 0 :
    INDENT
        combos = [NULL]
    DEDENT
    else :
    INDENT
        combos = []
        for i, item in enumerate(sequence, 1) :
        INDENT
            rem_items = sequence [i :]
            rem_combos = combinations(rem_items, length - 1)
            combos.extend(item if combo is NULL else [item, combo] for combo in rem_combos)
        DEDENT
    DEDENT
    return combos
DEDENT

def split_at_first_false(pred, seq) :
INDENT
    index = 0
    while index < len(seq) :
    INDENT
        if not pred(seq [index]) :
        INDENT
            return seq [: index], seq [index + 1 :]
        DEDENT
        index += 1
    DEDENT
DEDENT

def chunker(iterable, n) :
INDENT
    it = iter(iterable)
    while True :
    INDENT
        chunk = []
        for i in range(n) :
        INDENT
            try :
            INDENT
                chunk.append(it.next())
            DEDENT
            except StopIteration :
            INDENT
                yield chunk
                raise StopIteration
            DEDENT
        DEDENT
        yield chunk
    DEDENT
DEDENT

def foo(xs) :
INDENT
    stack = [[]]
    for x in xs :
    INDENT
        if x == '(' :
        INDENT
            stack [- 1].append([])
            stack.append(stack [- 1] [- 1])
        DEDENT
        elif x == ')' :
        INDENT
            stack.pop()
            if not stack :
            INDENT
                return 'error: opening bracket is missing'
            DEDENT
        DEDENT
        else :
        INDENT
            stack [- 1].append(x)
        DEDENT
    DEDENT
    if len(stack) > 1 :
    INDENT
        return 'error: closing bracket is missing'
    DEDENT
    return stack.pop()
DEDENT

def factorial(n) :
INDENT
    base = 1
    for i in range(n, 0, - 1) :
    INDENT
        base = base * i
    DEDENT
    print base
DEDENT
























































































































































































































































































































































