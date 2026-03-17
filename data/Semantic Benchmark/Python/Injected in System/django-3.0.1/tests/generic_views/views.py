from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import AuthorForm, ContactForm
from .models import Artist, Author, Book, BookSigning, Page


class CustomTemplateView(generic.TemplateView):
    template_name = 'generic_views/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'key': 'value'})
        return context


def NumRange(a, x, y) :
INDENT
    if not a :
    INDENT
        return 0
    DEDENT
    if x < = a [0] < = y :
    INDENT
        return 1 + NumRange(a [1 :], x, y)
    DEDENT
    else :
    INDENT
        return NumRange(a [1 :], x, y)
    DEDENT
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    tk.Tk.__init__(self)
    self.title("This is the MainWindow")
    self._is_hidden = False
    self.window1 = OtherWindow(self, title = "window 1")
    self.window2 = OtherWindow(self, title = "window 2")
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

def __init__(self, f, fieldnames, restval = "", extrasaction = "raise",
dialect = "excel", * args, ** kwds) :
INDENT
    self.fieldnames = fieldnames
    self.restval = restval
    if extrasaction.lower() not in ("raise", "ignore") :
    INDENT
        raise ValueError, ("extrasaction (%s) must be 'raise' or 'ignore'" %
            extrasaction)
    DEDENT
    self.extrasaction = extrasaction
    self.writer = writer(f, dialect, * args, ** kwds)
DEDENT

def run_query(self) :
INDENT
    queries = [self.query]
    for q in queries :
    INDENT
        res = self.load_conf(q)
    DEDENT
    try :
    INDENT
        query_status = None
        while query_status == 'QUEUED' or query_status == 'RUNNING' or query_status is None :
        INDENT
            query_status = self.client.get_query_execution(QueryExecutionId = res ["QueryExecutionId"]) ['QueryExecution'] ['Status'] ['State']
            print (query_status)
            if query_status == 'FAILED' or query_status == 'CANCELLED' :
            INDENT
                raise Exception('Athena query with the string "{}" failed or was cancelled'.format(self.query))
            DEDENT
            time.sleep(10)
        DEDENT
        print ("Query %s finished.")
        df = self.obtain_data()
        return df
    DEDENT
    except Exception as e :
    INDENT
        print (e)
    DEDENT
DEDENT

class ObjectDetail(generic.DetailView):
    template_name = 'generic_views/detail.html'

    def get_object(self):
        return {'foo': 'bar'}


def length_of_string(mystring) :
INDENT
    if type(mystring) is int :
    INDENT
        return "invalid entry"
    DEDENT
    else :
    INDENT
        return len(mystring)
    DEDENT
DEDENT

def formatTime(self, record, datefmt = None) :
INDENT
    ct = self.converter(record.created)
    if datefmt :
    INDENT
        s = ct.strftime(datefmt)
    DEDENT
    else :
    INDENT
        t = ct.strftime("%Y-%m-%d %H:%M:%S")
        s = "%s,%03d" % (t, record.msecs)
    DEDENT
    return s
DEDENT

def treeview_sort_column(tv, col, reverse) :
INDENT
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(key = lambda t : int(t [0]), reverse = reverse)
    for index, (val, k) in enumerate(l) :
    INDENT
        tv.move(k, '', index)
    DEDENT
    tv.heading(col,
        command = lambda : treeview_sort_column(tv, col, not reverse))
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

def convertType(value) :
INDENT
    try :
    INDENT
        return float(value)
    DEDENT
    except : pass
    try :
    INDENT
        return int(value)
    DEDENT
    except :
    INDENT
        return value
    DEDENT
DEDENT

def receive(self) :
INDENT
    while True :
    INDENT
        try :
        INDENT
            record = self.queue.get()
            self._handler.emit(record)
        DEDENT
        except (KeyboardInterrupt, SystemExit) :
        INDENT
            raise
        DEDENT
        except EOFError :
        INDENT
            break
        DEDENT
        except :
        INDENT
            traceback.print_exc(file = sys.stderr)
        DEDENT
    DEDENT
DEDENT

class ArtistDetail(generic.DetailView):
    queryset = Artist.objects.all()


class AuthorDetail(generic.DetailView):
    queryset = Author.objects.all()


class AuthorCustomDetail(generic.DetailView):
    template_name = 'generic_views/author_detail.html'
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        # Ensures get_context_object_name() doesn't reference self.object.
        author = self.get_object()
        context = {'custom_' + self.get_context_object_name(author): author}
        return self.render_to_response(context)


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

def outer() :
INDENT
    outer.y = 0
    def inner() :
    INDENT
        outer.y += 1
        return outer.y
    DEDENT
    return inner
DEDENT

def is_member(x) :
INDENT
    a = [1, 5, 3, 9, 4, 100]
    i = 0
    found = False
    while found == False :
    INDENT
        if i > = len(a) :
        INDENT
            return False
        DEDENT
        if x == a [i] :
        INDENT
            found = True
            break
        DEDENT
        i += 1
    DEDENT
    if found == True :
    INDENT
        return "True"
    DEDENT
    else :
    INDENT
        return "False"
    DEDENT
DEDENT

class PageDetail(generic.DetailView):
    queryset = Page.objects.all()
    template_name_field = 'template'


class DictList(generic.ListView):
    """A ListView that doesn't use a model."""
    queryset = [
        {'first': 'John', 'last': 'Lennon'},
        {'first': 'Yoko', 'last': 'Ono'}
    ]
    template_name = 'generic_views/list.html'


class ArtistList(generic.ListView):
    template_name = 'generic_views/list.html'
    queryset = Artist.objects.all()


class AuthorList(generic.ListView):
    queryset = Author.objects.all()


class AuthorListGetQuerysetReturnsNone(AuthorList):
    def get_queryset(self):
        return None


def recursiveHalfString(s, offset = 0) :
INDENT
    half, odd = divmod(len(s), 2)
    assert (not odd)
    if not s or offset > half :
    INDENT
        return True
    DEDENT
    if s [offset] ! = s [half + offset] :
    INDENT
        return False
    DEDENT
    return recursiveHalfString(s, offset + 1)
DEDENT

def int_to_roman(num) :
INDENT
    _values = [
        1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    _strings = [
        'M', 'C', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    decimal = num
    while decimal > 0 :
    INDENT
        for i in range(len(_values)) :
        INDENT
            if decimal > = _values [i] :
            INDENT
                if _values [i] > 1000 :
                INDENT
                    result += u'\u0304'.join(list(_strings [i])) + u'\u0304'
                DEDENT
                else :
                INDENT
                    result += _strings [i]
                DEDENT
                decimal -= _values [i]
                break
            DEDENT
        DEDENT
    DEDENT
    return result
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

class BookList(generic.ListView):
    model = Book


class CustomPaginator(Paginator):
    def __init__(self, queryset, page_size, orphans=0, allow_empty_first_page=True):
        super().__init__(queryset, page_size, orphans=2, allow_empty_first_page=allow_empty_first_page)


def sum67(nums) :
INDENT
    nums = nums [:]
    while 6 in nums :
    INDENT
        i = nums.index(6)
        j = nums.index(7, i)
        del nums [i : j + 1]
    DEDENT
    return sum(nums)
DEDENT

def __init__(self) :
INDENT
    tk.Tk.__init__(self)
    self.queue = queue.Queue()
    self.listbox = tk.Listbox(self, width = 20, height = 5)
    self.progressbar = ttk.Progressbar(self, orient = 'horizontal',
        length = 300, mode = 'determinate')
    self.button = tk.Button(self, text = "Start", command = self.spawnthread)
    self.listbox.pack(padx = 10, pady = 10)
    self.progressbar.pack(padx = 10, pady = 10)
    self.button.pack(padx = 10, pady = 10)
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

class AuthorListCustomPaginator(AuthorList):
    paginate_by = 5

    def get_paginator(self, queryset, page_size, orphans=0, allow_empty_first_page=True):
        return super().get_paginator(queryset, page_size, orphans=2, allow_empty_first_page=allow_empty_first_page)


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

def countSubStringMatchRecursive(target, key, start_index = 0) :
INDENT
    index = target.find(key, start_index)
    if index > = 0 :
    INDENT
        return countSubStringMatchRecursive(target, key, index + len(key)) + 1
    DEDENT
    return 0
DEDENT

def execute(command) :
INDENT
    popen = subprocess.Popen(command, stdout = subprocess.PIPE, bufsize = 1)
    lines_iterator = iter(popen.stdout.readline, b"")
    while popen.poll() is None :
    INDENT
        for line in lines_iterator :
        INDENT
            nline = line.rstrip()
            print(nline.decode("latin"), end = "\r\n", flush = True)
        DEDENT
    DEDENT
DEDENT

def fires() :
INDENT
    def beforeDecorator(f, event) :
    INDENT
        @ wraps(f)
        def wrapped(* args, ** kargs) :
        INDENT
            event.fire(* args, ** kargs)
            return f(* args, ** kargs)
        DEDENT
        return wrapped
    DEDENT
    def afterDecorator(f, event) :
    INDENT
        @ wraps(f)
        def wrapped(* args, ** kargs) :
        INDENT
            try :
            INDENT
                result = f(* args, ** kargs)
            DEDENT
            finally :
            INDENT
                event.fire(* args, ** kargs)
            DEDENT
            return result
        DEDENT
        return wrapped
    DEDENT
    def closure(event, after = False) :
    INDENT
        def decorator(function) :
        INDENT
            if after :
            INDENT
                return afterDecorator(function, event)
            DEDENT
            else :
            INDENT
                return beforeDecorator(function, event)
            DEDENT
        DEDENT
        return decorator
    DEDENT
    return closure
DEDENT

class ContactView(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('authors_list')
    template_name = 'generic_views/form.html'


class ArtistCreate(generic.CreateView):
    model = Artist
    fields = '__all__'


class NaiveAuthorCreate(generic.CreateView):
    queryset = Author.objects.all()
    fields = '__all__'


class TemplateResponseWithoutTemplate(generic.detail.SingleObjectTemplateResponseMixin, generic.View):
    # we don't define the usual template_name here

    def __init__(self):
        # Dummy object, but attr is required by get_template_name()
        self.object = None


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

def fib(n) :
INDENT
    a = 0
    b = 1
    for i in range(1, n + 1) :
    INDENT
        c = a + b
        print b
        a = b
        b = c
    DEDENT
DEDENT

def __init__(self, locations) :
INDENT
    if not locations :
    INDENT
        print ('board is full!')
        raise ValueError
    DEDENT
    self.coordinates = random.choice(locations)
    del locations [locations.index(self.coordinates)]
    self.name = 'Random name'
    self.tribe = random.choice(('gauls', 'teutons'))
DEDENT

def hit(bx, by, r, px, py, h) :
INDENT
    if bx > = px - r and py < = by < = py + h :
    INDENT
        True
    DEDENT
    else :
    INDENT
        False
    DEDENT
DEDENT

def combine_word_documents(input_files) :
INDENT
    for filnr, file in enumerate(input_files) :
    INDENT
        if 'offerte_template' in file :
        INDENT
            file = os.path.join(settings.MEDIA_ROOT, file)
        DEDENT
        if filnr == 0 :
        INDENT
            merged_document = Document(file)
            merged_document.add_page_break()
        DEDENT
        else :
        INDENT
            sub_doc = Document(file)
            if filnr < len(input_files) - 1 :
            INDENT
                sub_doc.add_page_break()
            DEDENT
            for element in sub_doc.element.body :
            INDENT
                merged_document.element.body.append(element)
            DEDENT
        DEDENT
    DEDENT
    return merged_document
DEDENT

class AuthorCreate(generic.CreateView):
    model = Author
    success_url = '/list/authors/'
    fields = '__all__'


class SpecializedAuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'generic_views/form.html'
    context_object_name = 'thingy'

    def get_success_url(self):
        return reverse('author_detail', args=[self.object.id])


def check_names(part_names, full_name_list) :
INDENT
    for full_name in full_name_list :
    INDENT
        for part_name in part_names :
        INDENT
            if part_name in full_name :
            INDENT
                yield full_name
            DEDENT
        DEDENT
    DEDENT
DEDENT

def merge(a, b, path = []) :
INDENT
    for key in b :
    INDENT
        if key in a :
        INDENT
            if isinstance(a [key], dict) and isinstance(b [key], dict) :
            INDENT
                merge(a [key], b [key], path + [str(key)])
            DEDENT
            elif a [key] == b [key] :
            INDENT
                pass
            DEDENT
            else :
            INDENT
                raise Exception('Conflict at `{path}\''.format(path = '.'.join(path + [str(key)])))
            DEDENT
        DEDENT
        else :
        INDENT
            if isinstance(b [key], dict) :
            INDENT
                a [key] = clone_dict(b [key])
            DEDENT
            else :
            INDENT
                a [key] = b [key]
            DEDENT
        DEDENT
    DEDENT
    return a
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

def reverse(text) :
INDENT
    lst = []
    count = 1
    for i in range(0, len(text)) :
    INDENT
        lst.append(text [len(text) - count])
        count += 1
    DEDENT
    lst = ''.join(lst)
    return lst
DEDENT

class AuthorCreateRestricted(AuthorCreate):
    post = method_decorator(login_required)(AuthorCreate.post)


class ArtistUpdate(generic.UpdateView):
    model = Artist
    fields = '__all__'


class NaiveAuthorUpdate(generic.UpdateView):
    queryset = Author.objects.all()
    fields = '__all__'


class AuthorUpdate(generic.UpdateView):
    get_form_called_count = 0  # Used to ensure get_form() is called once.
    model = Author
    success_url = '/list/authors/'
    fields = '__all__'

    def get_form(self, *args, **kwargs):
        self.get_form_called_count += 1
        return super().get_form(*args, **kwargs)


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

def backwalk(mymap, start, origin) :
INDENT
    yield start
    current = mymap [start]
    while current ! = origin :
    INDENT
        yield current
        current = mymap [current]
    DEDENT
DEDENT

def __init__(self) :
INDENT
    self.fields = []
    for field_name in dir(self) :
    INDENT
        field = getattr(self, field_name)
        if isinstance(field, Field) :
        INDENT
            field.name = field_name
            self.fields.append(field)
        DEDENT
    DEDENT
    self.fields.sort(key = operator.attrgetter('count'))
DEDENT

def avg(self) :
INDENT
    if all(isinstance(item, int) for item in self) :
    INDENT
        return sum(self) / len(self)
    DEDENT
    else :
    INDENT
        raise ValueError('Invalid item in list. All items need to be an integer.')
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

def handleError(func) :
INDENT
    errors = []
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
    return wrapper
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

class OneAuthorUpdate(generic.UpdateView):
    success_url = '/list/authors/'
    fields = '__all__'

    def get_object(self):
        return Author.objects.get(pk=1)


def is_binary(filename) :
INDENT
    fin = open(filename, 'rb')
    try :
    INDENT
        CHUNKSIZE = 1024
        while 1 :
        INDENT
            chunk = fin.read(CHUNKSIZE)
            if '\0' in chunk :
            INDENT
                return True
            DEDENT
            if len(chunk) < CHUNKSIZE :
            INDENT
                break
            DEDENT
        DEDENT
    DEDENT
    finally :
    INDENT
        fin.close()
    DEDENT
    return False
DEDENT

def fixup(m) :
INDENT
    text = m.group(0)
    if text [: 2] == "&#" :
    INDENT
        try :
        INDENT
            if text [: 3] == "&#x" :
            INDENT
                return unichr(int(text [3 : - 1], 16))
            DEDENT
            else :
            INDENT
                return unichr(int(text [2 : - 1]))
            DEDENT
        DEDENT
        except ValueError :
        INDENT
            print "Value Error"
            pass
        DEDENT
    DEDENT
    else :
    INDENT
        try :
        INDENT
            if text [1 : - 1] == "amp" :
            INDENT
                text = "&amp;amp;"
            DEDENT
            elif text [1 : - 1] == "gt" :
            INDENT
                text = "&amp;gt;"
            DEDENT
            elif text [1 : - 1] == "lt" :
            INDENT
                text = "&amp;lt;"
            DEDENT
            else :
            INDENT
                print text [1 : - 1]
                text = unichr(htmlentitydefs.name2codepoint [text [1 : - 1]])
            DEDENT
        DEDENT
        except KeyError :
        INDENT
            print "keyerror"
            pass
        DEDENT
    DEDENT
    return text
DEDENT

def test_run(pool) :
INDENT
    filelist = os.listdir(files_dir)
    for f1 in filelist :
    INDENT
        for f2 in filelist :
        INDENT
            pool.apply_async(worker, args = (f1, f2))
        DEDENT
    DEDENT
DEDENT

def pay_with_coins(amount) :
INDENT
    coins = [0 for i in range(len(currencies))]
    amount = int(amount * 100)
    values = [c * 100 for c in currencies]
    for currency in values :
    INDENT
        i = values.index(currency)
        coins [i] = 0
        while amount > = currency :
        INDENT
            amount -= currency
            coins [i] += 1
        DEDENT
    DEDENT
    return coins
DEDENT

def pairsum_n(list1, value) :
INDENT
    set1 = set(list1)
    list1 = sorted(set1)
    solution = []
    maxi = value / 2
    for i in list1 :
    INDENT
        if i > = maxi :
        INDENT
            break
        DEDENT
        j = value - i
        if j in set1 :
        INDENT
            solution.append((i, j))
        DEDENT
    DEDENT
    return solution
DEDENT

class SpecializedAuthorUpdate(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'generic_views/form.html'
    context_object_name = 'thingy'

    def get_success_url(self):
        return reverse('author_detail', args=[self.object.id])


def find_v0(theta) :
INDENT
    v0 = 8
    while (True) :
    INDENT
        v0x = v0 * np.cos(theta)
        v0y = v0 * np.sin(theta)
        z0 = np.array([0, v0x, ystar, v0y])
        t, z = explicit_midpoint(rhs, z0, 5, 1000)
        for k in range(1001) :
        INDENT
            if z [k, 0] > xstar :
            INDENT
                z [k, 0] = 0
                z [k, 2] = 0
            DEDENT
        DEDENT
        x = np.trim_zeros(z [:, 0])
        y = np.trim_zeros(z [:, 2])
        diff = difference(x [- 1], y [- 1])
        if diff < 0.1 :
        INDENT
            break
        DEDENT
        else : v0 += 0.01
    DEDENT
    return v0
DEDENT

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

def overload(funcOrType, map = {}, type = None) :
INDENT
    if not inspect.isclass(funcOrType) :
    INDENT
        if (type) :
        INDENT
            map [type] = funcOrType
        DEDENT
        else :
        INDENT
            map ['default_function'] = funcOrType
        DEDENT
    DEDENT
    else :
    INDENT
        def overloadWithType(func) :
        INDENT
            return overload(func, map, funcOrType)
        DEDENT
        return overloadWithType
    DEDENT
    def doOverload(* args, ** kwargs) :
    INDENT
        for type in [t for t in map.keys() if t ! = 'default_function'] :
        INDENT
            if isinstance(args [1], type) :
            INDENT
                return map [type](* args, ** kwargs)
            DEDENT
        DEDENT
        return map ['default_function'](* args, ** kwargs)
    DEDENT
    return doOverload
DEDENT

def countWords(arg) :
INDENT
    dd = co.defaultdict(int)
    for i in arg.split() :
    INDENT
        dd [i] += 1
    DEDENT
    return dd
DEDENT

def combinations(iterable, r, combIndeciesExclusions = set()) :
INDENT
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r) :
    INDENT
        if (len(combIndeciesExclusions) == 0 or not combIndeciesExclusions.issubset(indices)) and sorted(indices) == list(indices) :
        INDENT
            yield tuple(pool [i] for i in indices)
        DEDENT
    DEDENT
DEDENT

class NaiveAuthorDelete(generic.DeleteView):
    queryset = Author.objects.all()


class AuthorDelete(generic.DeleteView):
    model = Author
    success_url = '/list/authors/'


class SpecializedAuthorDelete(generic.DeleteView):
    queryset = Author.objects.all()
    template_name = 'generic_views/confirm_delete.html'
    context_object_name = 'thingy'
    success_url = reverse_lazy('authors_list')


class BookConfig:
    queryset = Book.objects.all()
    date_field = 'pubdate'


class BookArchive(BookConfig, generic.ArchiveIndexView):
    pass


class BookYearArchive(BookConfig, generic.YearArchiveView):
    pass


class BookMonthArchive(BookConfig, generic.MonthArchiveView):
    pass


class BookWeekArchive(BookConfig, generic.WeekArchiveView):
    pass


class BookDayArchive(BookConfig, generic.DayArchiveView):
    pass


class BookTodayArchive(BookConfig, generic.TodayArchiveView):
    pass


class BookDetail(BookConfig, generic.DateDetailView):
    pass


class AuthorGetQuerySetFormView(generic.edit.ModelFormMixin):
    fields = '__all__'

    def get_queryset(self):
        return Author.objects.all()


def write(self, data) :
INDENT
    self.stream.write(data)
    self.stream.flush()
    self.data += data
    tmp = str(self.data)
    if '\x0a' in tmp or '\x0d' in tmp :
    INDENT
        tmp = tmp.rstrip('\x0a\x0d')
        log.info('%s%s' % (self.prefix, tmp))
        self.data = ''
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

def __enter__(self) :
INDENT
    with self._cleanup_on_error() :
    INDENT
        self.wrappers = [self.enter_context(r) for r in self.resources]
    DEDENT
    return self.wrappers
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

class BookDetailGetObjectCustomQueryset(BookDetail):
    def get_object(self, queryset=None):
        return super().get_object(queryset=Book.objects.filter(pk=self.kwargs['pk']))


def problem(n) :
INDENT
    myList = []
    for i in range(1, n + 1) :
    INDENT
        if n % i == 0 :
        INDENT
            myList.append(i)
        DEDENT
    DEDENT
    return myList
DEDENT

def __op__(self, op, args) :
INDENT
    try :
    INDENT
        other = args [0]
    DEDENT
    except IndexError :
    INDENT
        other = None
    DEDENT
    print "%s %s %s" % (self, op, other)
    self, other = coerce(self, other)
    return getattr(self, op)(* args)
DEDENT

def countconvolve(N) :
INDENT
    np.random.seed()
    count = 0
    iters = 1000000
    l = 12
    k = 12
    l0 = l + k - 1
    for n in range(N) :
    INDENT
        t = np.random.choice(np.array([- 1, 1], dtype = np.int8), size = l0 * iters)
        v = np.random.choice(np.array([- 1, 1], dtype = np.int8), size = l * iters)
        for i in xrange(iters) :
        INDENT
            if (not np.convolve(v [(l * i) : (l * (i + 1))], t [(l0 * i) : (l0 * (i + 1))], 'valid').any()) :
            INDENT
                count += 1
            DEDENT
        DEDENT
    DEDENT
    return count
DEDENT

def md5sum(filename) :
INDENT
    with open(filename, mode = 'rb') as f :
    INDENT
        d = hashlib.md5()
        while True :
        INDENT
            buf = f.read(4096)
            if not buf :
            INDENT
                break
            DEDENT
            d.update(buf)
        DEDENT
        return d.hexdigest()
    DEDENT
DEDENT

class CustomMultipleObjectMixinView(generic.list.MultipleObjectMixin, generic.View):
    queryset = [
        {'name': 'John'},
        {'name': 'Yoko'},
    ]

    def get(self, request):
        self.object_list = self.get_queryset()


def decrypt(self, enc) :
INDENT
    if enc is None or len(enc) == 0 :
    INDENT
        raise NameError("No value given to decrypt")
    DEDENT
    enc = base64.b64decode(enc)
    iv = enc [: 16]
    cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, iv)
    return re.sub(b'\x00*$', b'', cipher.decrypt(enc [16 :])).decode('utf-8')
DEDENT

def default(self, obj) :
INDENT
    if isinstance(obj, TYPES.values()) :
    INDENT
        key = '__%s__' % obj.__class__.__name__
        return {key : obj.__dict__}
    DEDENT
    return json.JSONEncoder.default(self, obj)
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

def running_average(data, windowSize) :
INDENT
    dShape = np.shape(data)
    try :
    INDENT
        dShape [1]
    DEDENT
    except :
    INDENT
        data = [data]
        dShape = np.shape(data)
    DEDENT
    raOut = np.zeros(dShape)
    for col in dShape [1] :
    INDENT
        rSum = 0.0
        for row, value in enumerate(data [:] [col]) :
        INDENT
            if row < windowSize :
            INDENT
                rSum += float(value)
            DEDENT
            else :
            INDENT
                rSum = rSum - data [row - windowSize] [col] + value
            DEDENT
            raOut [row] [col] = rSum / windowSize
        DEDENT
    DEDENT
    return np.squeeze(raOut)
DEDENT

def fileCount(path, extension) :
INDENT
    count = 0
    for root, dirs, files in os.walk(path) :
    INDENT
        for file in files :
        INDENT
            if file.endswith(extension) :
            INDENT
                count += 1
            DEDENT
        DEDENT
    DEDENT
    return count
DEDENT

class CustomContextView(generic.detail.SingleObjectMixin, generic.View):
    model = Book
    object = Book(name='dummy')

    def get_object(self):
        return Book(name="dummy")

def numPens(n) :
INDENT
    if n < 5 :
    INDENT
        return False
    DEDENT
    if n % 8 == 0 or n % 5 == 0 :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return numPens(n - 8) or numPens(n - 5)
    DEDENT
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    super(MainWindow, self).__init__(* args, ** kwargs)
    self.result_windows = []
    self.thread_pool = QtCore.QThreadPool().globalInstance()
    self.thread_pool.setMaxThreadCount(1)
    self.start_capturing_data()
DEDENT

def longest(lst) :
INDENT
    if type(lst) is not list :
    INDENT
        return 0
    DEDENT
    max = len(lst)
    for i in lst :
    INDENT
        max_i = longest(i)
        if max_i > max :
        INDENT
            max = max_i
        DEDENT
    DEDENT
    return max
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

def calculate_tax(income_input) :
INDENT
    for item in income_input :
    INDENT
        income = income_input [item]
        if (income > = 0) and (income < = 1000) :
        INDENT
            tax = (0 * income)
        DEDENT
        elif (income > 1000) and (income < = 10000) :
        INDENT
            tax = (0.1 * (income - 1000))
        DEDENT
        elif (income > 10000) and (income < = 20200) :
        INDENT
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (income - 10000)))
        DEDENT
        elif (income > 20200) and (income < = 30750) :
        INDENT
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (income - 20200)))
        DEDENT
        elif (income > 30750) and (income < = 50000) :
        INDENT
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (30750 - 20200)) + (0.25 * (income - 30750)))
        DEDENT
        elif (income > 50000) :
        INDENT
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (30750 - 20200)) + (0.25 * (50000 - 30750)) + (0.3 * (income - 50000)))
        DEDENT
        else :
        INDENT
            pass
        DEDENT
        income_input [item] = int(tax)
    DEDENT
    return income_input
DEDENT

def decorator(function) :
INDENT
    if after :
    INDENT
        return afterDecorator(function, event)
    DEDENT
    else :
    INDENT
        return beforeDecorator(function, event)
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

    def get_context_data(self, **kwargs):
        context = {'custom_key': 'custom_value'}
        context.update(kwargs)
        return super().get_context_data(**context)

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

def plotPerfect(df, spline) :
INDENT
    ax = df.plot()
    if not spline :
    INDENT
        for i in ['top', 'right', 'bottom', 'left'] :
        INDENT
            ax.spines [i].set_visible(False)
        DEDENT
    DEDENT
    return (ax)
DEDENT

def longestSubstringFinder(string1, string2) :
INDENT
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1) :
    INDENT
        for j in range(len2) :
        INDENT
            lcs_temp = 0
            match = ''
            while ((i + lcs_temp < len1) and (j + lcs_temp < len2) and string1 [i + lcs_temp] == string2 [j + lcs_temp]) :
            INDENT
                match += string2 [j + lcs_temp]
                lcs_temp += 1
            DEDENT
            if (len(match) > len(answer)) :
            INDENT
                answer = match
            DEDENT
        DEDENT
    DEDENT
    return answer
DEDENT

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

    def get_context_object_name(self, obj):
        return "test_name"


def get_info(session, title, url) :
INDENT
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    script = next((i for i in map(str, soup.find_all("script", type = "text/javascript"))
            if 'mapOptions' in i), None)
    if script :
    INDENT
        js_dict = script.split('__mapOptions = ') [1].split(';\n') [0]
        d = yaml.load(js_dict)
        print (title, d ['mapStore'] ['phone'])
    DEDENT
DEDENT

def checksum(pkt) :
INDENT
    if len(pkt) % 2 == 1 :
    INDENT
        pkt += "\0"
    DEDENT
    s = sum(array.array("H", pkt))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    s = ~ s
    return s & 0xffff
DEDENT

def overlap(string1, string2) :
INDENT
    count = 0
    for i in range(min(len(string1), len(string2))) :
    INDENT
        if string1 [i] == string2 [i] :
        INDENT
            count = count + 1
        DEDENT
    DEDENT
    return count
DEDENT

def draw() :
INDENT
    for x in range(0, 10) :
    INDENT
        for y in range(0, 10) :
        INDENT
            item = canvas.create_rectangle((x * 40) + 10, (y * 40) + 10,
                (x * 40) + 50, (y * 40) + 50)
            if (coord [i] [j] == 0) :
            INDENT
                canvas.itemconfig(item, fill = "white")
            DEDENT
            if (coord [i] [j] == 1) :
            INDENT
                canvas.itemconfig(item, fill = "red")
            DEDENT
            if (coord [i] [j] == 2) :
            INDENT
                canvas.itemconfig(item, fill = "darkorange")
            DEDENT
        DEDENT
    DEDENT
    canvas.after(30, draw)
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

def outer() :
INDENT
    def inner() :
    INDENT
        inner.y += 1
        return inner.y
    DEDENT
    inner.y = 0
    return inner
DEDENT

def execute(cmd) :
INDENT
    popen = subprocess.Popen(cmd, stdout = subprocess.PIPE, universal_newlines = True)
    for stdout_line in iter(popen.stdout.readline, "") :
    INDENT
        yield stdout_line
    DEDENT
    popen.stdout.close()
    return_code = popen.wait()
    if return_code :
    INDENT
        raise subprocess.CalledProcessError(return_code, cmd)
    DEDENT
DEDENT

def getSurroundingTiles(self, tile, horizontal = True, vertical = True) :
INDENT
    index = list(self.getTiles()).index(tile)
    maxtile = self.sqrtnum - 1
    fhv = (horizontal, vertical)
    ij = (int(math.floor(index / self.sqrtnum)),
        int(index % self.sqrtnum))
    surroundingTiles = []
    for ihv in range(2) :
    INDENT
        if fhv [ihv] :
        INDENT
            for k in range(4) :
            INDENT
                n = [sum(p) for p in zip(ij, d [ihv] [k])]
                if all([0 < = n [i] < = maxtile for i in range(2)]) :
                INDENT
                    surroundingTiles.append(self [n [0]] [n [1]])
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return surroundingTiles
DEDENT

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

class CustomSingleObjectView(generic.detail.SingleObjectMixin, generic.View):
    model = Book
    object = Book(name="dummy")


class BookSigningConfig:
    model = BookSigning
    date_field = 'event_date'
    # use the same templates as for books

    def get_template_names(self):
        return ['generic_views/book%s.html' % self.template_name_suffix]


def memoize(fn) :
INDENT
    def defaultget(key) :
    INDENT
        return (False,)
    DEDENT
    memo = Memo()
    memo.get = defaultget
    def vset(key, value) :
    INDENT
        oldget = memo.get
        def newget(ky) :
        INDENT
            if key == ky : return (True, value)
            return oldget(ky)
        DEDENT
        memo.get = newget
    DEDENT
    def mfun(* args) :
    INDENT
        cache = memo.get(args)
        if cache [0] : return cache [1]
        val = apply(fn, args)
        vset(args, val)
        return val
    DEDENT
    return mfun
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

def normalize(x) :
INDENT
    try :
    INDENT
        x = x / np.linalg.norm(x, ord = 1)
        return x
    DEDENT
    except :
    INDENT
        raise
    DEDENT
DEDENT

def get_client_ip(request) :
INDENT
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for :
    INDENT
        ip = x_forwarded_for.split(',') [0]
    DEDENT
    else :
    INDENT
        ip = request.META.get('REMOTE_ADDR')
    DEDENT
    return ip
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

def __init__(self, parent) :
INDENT
    wx.Frame.__init__(self, parent, - 1, title = "Dialog Request Frame", size = (500, 500))
    self.parent = parent
    self.parent.btn.Enable(False)
    self.stored_results = {}
    self.dlg_chain_no = 0
    self.dlg_prev_value = 0
    panel = wx.Panel(self)
    self.btn = wx.Button(panel, - 1, "open dialog")
    self.Bind(wx.EVT_BUTTON, self.OnOpenDialog, id = self.btn.GetId())
    self.Bind(wx.EVT_CLOSE, self.OnClose)
    self.Centre()
    self.Show()
DEDENT

def func(ax, data, color, position) :
INDENT
    ax.plot(data [0], data [1], color = color)
    ax.spines [position].set_color(color)
    for pos in ['left', 'right'] :
    INDENT
        if pos ! = position :
        INDENT
            ax.spines [pos].set_visible(False)
        DEDENT
    DEDENT
DEDENT

class BookSigningArchive(BookSigningConfig, generic.ArchiveIndexView):
    pass


class BookSigningYearArchive(BookSigningConfig, generic.YearArchiveView):
    pass


class BookSigningMonthArchive(BookSigningConfig, generic.MonthArchiveView):
    pass


class BookSigningWeekArchive(BookSigningConfig, generic.WeekArchiveView):
    pass


class BookSigningDayArchive(BookSigningConfig, generic.DayArchiveView):
    pass


class BookSigningTodayArchive(BookSigningConfig, generic.TodayArchiveView):
    pass


class BookArchiveWithoutDateField(generic.ArchiveIndexView):
    queryset = Book.objects.all()


class BookSigningDetail(BookSigningConfig, generic.DateDetailView):
    context_object_name = 'book'


class NonModel:
    id = "non_model_1"

    _meta = None


class NonModelDetail(generic.DetailView):

    template_name = 'generic_views/detail.html'
    model = NonModel

    def get_object(self, queryset=None):
        return NonModel()


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

def __init__(cls, name, bases, dct) :
INDENT
    type.__init__(cls, name, bases, dct)
    old_setattr = cls.__setattr__
    def __setattr__(self, key, value) :
    INDENT
        cls.assert_attribute_mutable(key)
        old_setattr(self, key, value)
    DEDENT
    cls.__setattr__ = __setattr__
DEDENT

def softmax(X, theta = 1.0, axis = None) :
INDENT
    y = np.atleast_2d(X)
    if axis is None :
    INDENT
        axis = next(j [0] for j in enumerate(y.shape) if j [1] > 1)
    DEDENT
    y = y * float(theta)
    y = y - np.expand_dims(np.max(y, axis = axis), axis)
    y = np.exp(y)
    ax_sum = np.expand_dims(np.sum(y, axis = axis), axis)
    p = y / ax_sum
    if len(X.shape) == 1 : p = p.flatten()
    return p
DEDENT

def __init__(self, * args, ** kw) :
INDENT
    super(ModelForm, self).__init__(* args, ** kw)
    self.fields.keyOrder = [
        'super_user',
        'all_districts',
        'multi_district',
        'all_schools',
        'manage_users',
        'direct_login',
        'student_detail',
        'license']
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

class ObjectDoesNotExistDetail(generic.DetailView):
    def get_queryset(self):
        return Book.does_not_exist.all()


def find_longest_path(graph) :
INDENT
    max_path = []
    for node in graph :
    INDENT
        candidate_path = find_longest_path_from(graph, node)
        if len(candidate_path) > len(max_path) :
        INDENT
            max_path = candidate_path
        DEDENT
    DEDENT
    return max_path
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

def unescape(text) :
INDENT
    def fixup(m) :
    INDENT
        text = m.group(0)
        if text [: 2] == "&#" :
        INDENT
            try :
            INDENT
                if text [: 3] == "&#x" :
                INDENT
                    return unichr(int(text [3 : - 1], 16))
                DEDENT
                else :
                INDENT
                    return unichr(int(text [2 : - 1]))
                DEDENT
            DEDENT
            except ValueError :
            INDENT
                pass
            DEDENT
        DEDENT
        else :
        INDENT
            try :
            INDENT
                text = unichr(htmlentitydefs.name2codepoint [text [1 : - 1]])
            DEDENT
            except KeyError :
            INDENT
                pass
            DEDENT
        DEDENT
        return text
    DEDENT
    return re.sub("&#?\w+;", fixup, text)
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

class LateValidationView(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('authors_list')
    template_name = 'generic_views/form.html'

    def form_valid(self, form):
        form.add_error(None, 'There is an error')
        return self.form_invalid(form)
def __setitem__(self, key, value) :
INDENT
    if key in self :
    INDENT
        self.inverse [self [key]].remove(key)
    DEDENT
    super(bidict, self).__setitem__(key, value)
    self.inverse.setdefault(value, []).append(key)
DEDENT

def decrypt(key, iv, ciphertext) :
INDENT
    assert len(key) == key_bytes
    iv_int = int(iv.encode('hex'), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value = iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter = ctr)
    plaintext = aes.decrypt(ciphertext)
    return plaintext
DEDENT

def __init__(self) :
INDENT
    super(Main, self).__init__()
    self.resize(300, 200)
    self.index = QWidget()
    self.index.setMinimumHeight(1000)
    self.index.setMinimumWidth(500)
    self.setWidget(self.index)
    self.setWidgetResizable(True)
    with open('a.qss', 'r') as f :
    INDENT
        self.a_text = f.read()
        self.setStyleSheet(self.a_text)
    DEDENT
    with open('b.qss', 'r') as f :
    INDENT
        self.b_text = f.read()
    DEDENT
    with open('c.qss', 'r') as f :
    INDENT
        self.c_text = f.read()
    DEDENT
    self.value = 0
    self.pre_value = 0
    self.pauseCond = True
    self.timer = QTimer()
    self.timer.timeout.connect(self.timerout)
    self.verticalScrollBar().actionTriggered.connect(self.change)
    self.timer.start(300)
DEDENT

def unique(l) :
INDENT
    s = set(); n = 0
    for x in l :
    INDENT
        if x not in s : s.add(x); l [n] = x; n += 1
    DEDENT
    del l [n :]
DEDENT

















































































































