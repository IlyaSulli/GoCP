import datetime
from unittest import mock

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings, skipUnlessDBFeature
from django.test.utils import requires_tz_support
from django.utils import timezone

from .models import Artist, Author, Book, BookSigning, Page


def _make_books(n, base_date):
    for i in range(n):
        Book.objects.create(
            name='Book %d' % i,
            slug='book-%d' % i,
            pages=100 + i,
            pubdate=base_date - datetime.timedelta(days=i))


def __init__(self, ** kwargs) :
INDENT
    available = set(kwargs)
    derivable = set()
    while True :
    INDENT
        for r in range(1, len(available) + 1) :
        INDENT
            for permutation in itertools.permutations(available, r) :
            INDENT
                if permutation in self.relationships :
                INDENT
                    derivable.add(self.relationships [permutation])
                DEDENT
            DEDENT
        DEDENT
        if derivable.issubset(available) :
        INDENT
            break
        DEDENT
        else :
        INDENT
            available |= derivable
        DEDENT
    DEDENT
    underivable = set(self.relationships.values()) - available
    if len(underivable) > 0 :
    INDENT
        raise TypeError(
            "The following properties cannot be derived:\n\t{0}"
            .format(tuple(underivable)))
    DEDENT
    self._value_dict = kwargs
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

def strip_output(nb) :
INDENT
    for ws in nb.worksheets :
    INDENT
        for cell in ws.cells :
        INDENT
            if hasattr(cell, "outputs") :
            INDENT
                cell.outputs = []
            DEDENT
            if hasattr(cell, "prompt_number") :
            INDENT
                del cell ["prompt_number"]
            DEDENT
        DEDENT
    DEDENT
DEDENT

def rep_str(s, x, y) :
INDENT
    result = ""
    skip = False
    if x in s :
    INDENT
        for i in range(len(s)) :
        INDENT
            if skip :
            INDENT
                skip = False
                continue
            DEDENT
            if s [i : i + 2] == x :
            INDENT
                result += y
                skip = True
            DEDENT
            else :
            INDENT
                result += s [i : i + 1]
            DEDENT
        DEDENT
        return result
    DEDENT
    else :
    INDENT
        return s
    DEDENT
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

class TestDataMixin:

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


def sum_numbers(s) :
INDENT
    def convert_s_to_val(s) :
    INDENT
        if s :
        INDENT
            return float(s)
        DEDENT
        else :
        INDENT
            return 0
        DEDENT
    DEDENT
    sum = 0
    current = ''
    for c in s :
    INDENT
        if c.isspace() :
        INDENT
            sum += convert_s_to_val(current)
            current = ''
        DEDENT
        else :
        INDENT
            current = current + c
        DEDENT
    DEDENT
    sum += convert_s_to_val(current)
    return sum
DEDENT

def is_sorted(lst) :
INDENT
    try :
    INDENT
        sorted(lst, cmp = my_cmp)
        return True
    DEDENT
    except ValueError :
    INDENT
        return False
    DEDENT
DEDENT

def div3() :
INDENT
    divlist = []
    num = range(1, 10)
    if (num % 3 == 0) :
    INDENT
        for _ in xrange(20) :
        INDENT
            divlist.append(random.randint(0, 10))
        DEDENT
        print divlist
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

def merge(a, b, path = None) :
INDENT
    "merges b into a"
    if path is None : path = []
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
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
            DEDENT
        DEDENT
        else :
        INDENT
            a [key] = b [key]
        DEDENT
    DEDENT
    return a
DEDENT

def matched(str) :
INDENT
    ope = []
    clo = []
    for i in range(0, len(str)) :
    INDENT
        l = str [i]
        if l == "(" :
        INDENT
            ope = ope + ["("]
        DEDENT
        elif l == ")" :
        INDENT
            clo = clo + [")"]
        DEDENT
    DEDENT
    if len(ope) == len(clo) :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
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

@override_settings(ROOT_URLCONF='generic_views.urls')
class ArchiveIndexViewTests(TestDataMixin, TestCase):

    def test_archive_view(self):
        res = self.client.get('/dates/books/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.all()))
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

def listComp(listA, listB) :
INDENT
    wins = 0
    ties = 0
    losses = 0
    shuffle(listA)
    shuffle(listB)
    for a, b in zip(listA, listB) :
    INDENT
        if a < b :
        INDENT
            wins += 1
        DEDENT
        elif a == b :
        INDENT
            ties += 1
        DEDENT
        else :
        INDENT
            losses += 1
        DEDENT
    DEDENT
    return wins, ties, losses
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

def split_at_first_false(pred, seq) :
INDENT
    pos = 0
    for item in seq :
    INDENT
        if not pred(item) :
        INDENT
            return seq [: pos], seq [pos :]
        DEDENT
        pos += 1
    DEDENT
DEDENT

def main() :
INDENT
    reader, writer = multiprocessing.Pipe(False)
    video_process = Process(target = capture_video, args = [writer])
    video_process.start()
    while True :
    INDENT
        try :
        INDENT
            frame = reader.recv()
            process_frame(frame)
        DEDENT
        except KeyboardInterrupt :
        INDENT
            video_process.terminate()
            break
        DEDENT
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

def test2() :
INDENT
    import time
    import gc
    data = get_data()
    all_point_sets = []
    gc.disable()
    time_start = time.time()
    for index, row in enumerate(data) :
    INDENT
        first_points, second_points = row
        first_points = [int(i) for i in first_points.split(",")]
        second_points = [int(i) for i in second_points.split(",")]
        curr_points = [(x, y) for x, y in zip(first_points, second_points)]
        all_point_sets.append(curr_points)
    DEDENT
    time_end = time.time()
    gc.enable()
    print "variant 2 total time: ", (time_end - time_start)
DEDENT

    def test_archive_view_context_object_name(self):
        res = self.client.get('/dates/books/context_object_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['thingies']), list(Book.objects.all()))
        self.assertNotIn('latest', res.context)
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

def getPrimes(n) :
INDENT
    yield 2
    i = 1
    while i < = n - 2 :
    INDENT
        i += 2
        if isprime(i) :
        INDENT
            yield i
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

def run(self) :
INDENT
    print '>>>> abuse generator as context manager'
    for driver in self.drivergenerator(self.driverfactory) :
    INDENT
        self.dostuff(driver)
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

    def test_empty_archive_view(self):
        Book.objects.all().delete()
        res = self.client.get('/dates/books/')
        self.assertEqual(res.status_code, 404)

def find_longest_path(graph, start) :
INDENT
    cache = {}
    maxlen = find_longest_path_rec(graph, start, cache)
    path = [start]
    for i in range(maxlen - 1, 0, - 1) :
    INDENT
        for node in graph [path [- 1]] :
        INDENT
            if cache [node] == i :
            INDENT
                path.append(node)
                break
            DEDENT
        DEDENT
        else :
        INDENT
            assert (0)
        DEDENT
    DEDENT
    return path
DEDENT

def format(self, record) :
INDENT
    levelname = record.levelname
    if self.use_color and levelname in self.COLORS :
    INDENT
        fore_color = 30 + self.COLORS [levelname]
        levelname_color = self.COLOR_SEQ % fore_color + levelname + self.RESET_SEQ
        record.levelname = levelname_color
    DEDENT
    return logging.Formatter.format(self, record)
DEDENT

    def test_allow_empty_archive_view(self):
        Book.objects.all().delete()
        res = self.client.get('/dates/books/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [])
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

def getdetails(p, dictionary) :
INDENT
    result = []
    if type(dictionary) is not dict :
    INDENT
        return result
    DEDENT
    for key in dictionary :
    INDENT
        if key == p :
        INDENT
            result.append(dictionary [p])
        DEDENT
        result += getdetails(p, dictionary [key])
    DEDENT
    return result
DEDENT

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

def createfile() :
INDENT
    var = """#!/bin/sh
             echo ${test}
          """
    script_txt = ""
    for line in var :
    INDENT
        script_txt += line.lstrip(" ")
    DEDENT
    return script_txt
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

    def test_archive_view_template(self):
        res = self.client.get('/dates/books/template_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.all()))
        self.assertTemplateUsed(res, 'generic_views/list.html')

def print_table(table) :
INDENT
    longest_cols = [
        (max([len(str(row [i])) for row in table]) + 3) for i in range(len(table [0]))
        ]
    row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in table :
    INDENT
        print (row_format.format(* row))
    DEDENT
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

    def test_archive_view_template_suffix(self):
        res = self.client.get('/dates/books/template_name_suffix/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.all()))
        self.assertTemplateUsed(res, 'generic_views/book_detail.html')

def add_months(start_date, months) :
INDENT
    import calendar
    year = start_date.year + (months / 12)
    month = start_date.month + (months % 12)
    day = start_date.day
    if month > 12 :
    INDENT
        month = month % 12
        year = year + 1
    DEDENT
    days_next = calendar.monthrange(year, month) [1]
    if day > days_next :
    INDENT
        day = days_next
    DEDENT
    return start_date.replace(year, month, day)
DEDENT

def Compare(left, ops, comparators) :
INDENT
    if not ops [0](left, comparators [0]) :
    INDENT
        return False
    DEDENT
    for i, comparator in enumerate(comparators [1 :], start = 1) :
    INDENT
        if not ops [i](comparators [i - 1], comparator) :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

    def test_archive_view_invalid(self):
        msg = (
            'BookArchive is missing a QuerySet. Define BookArchive.model, '
            'BookArchive.queryset, or override BookArchive.get_queryset().'
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/dates/books/invalid/')

def ordinal(n) :
INDENT
    if 10 < = n % 100 < 20 :
    INDENT
        return str(n) + 'th'
    DEDENT
    else :
    INDENT
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")
    DEDENT
DEDENT

def __init__(self) :
INDENT
    super(Window, self).__init__()
    textBox = QTextEdit()
    textBox.setReadOnly(True)
    self.button = QPushButton('Click')
    vertLayout = QVBoxLayout()
    vertLayout.addWidget(textBox)
    vertLayout.addWidget(self.button)
    self.setLayout(vertLayout)
    self.button.clicked.connect(self.buttonPressed)
    self.bee = Worker(self.someProcess, ())
    self.bee.finished.connect(self.restoreUi)
    self.bee.terminated.connect(self.restoreUi)
    consoleHandler = ConsoleWindowLogHandler()
    consoleHandler.sigLog.connect(textBox.append)
    logger.addHandler(consoleHandler)
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

def fib() :
INDENT
    a, b = 0, 1
    while True :
    INDENT
        yield a
        a, b = b, a + b
    DEDENT
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

    def test_archive_view_by_month(self):
        res = self.client.get('/dates/books/by_month/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'month', 'DESC')))

def function(argument) :
INDENT
    max_arg = max(argument)
    argument.remove(max_arg)
    s = 0
    for i in argument :
    INDENT
        s += i
        if s == max_arg :
        INDENT
            return "true"
        DEDENT
    DEDENT
    return "false"
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

def printLine(self, Event) :
INDENT
    word_list = []
    counter = 0
    unique_words_in_string = []
    total_times_word_appears = {}
    for word in self.inputField.get().split() :
    INDENT
        word_list.append(word)
        if word not in unique_words_in_string :
        INDENT
            unique_words_in_string.append(word)
        DEDENT
    DEDENT
    for word in unique_words_in_string :
    INDENT
        counter = 0
        for other_word in word_list :
        INDENT
            if word == other_word :
            INDENT
                counter += 1
            DEDENT
        DEDENT
        total_times_word_appears [word] = counter
    DEDENT
    self.outputField.delete(0, "end")
    self.outputField.insert("end", total_times_word_appears)
DEDENT

def __init__(self, pos, angle) :
INDENT
    super().__init__()
    self.image = pg.transform.rotate(BULLET_IMAGE, - angle)
    self.rect = self.image.get_rect(center = pos)
    offset = Vector2(40, 0).rotate(angle)
    self.pos = Vector2(pos) + offset
    self.velocity = Vector2(1, 0).rotate(angle) * 9
DEDENT

    def test_paginated_archive_view(self):
        _make_books(20, base_date=datetime.date.today())
        res = self.client.get('/dates/books/paginated/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.all()[0:10]))
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

        res = self.client.get('/dates/books/paginated/?page=2')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['page_obj'].number, 2)
        self.assertEqual(list(res.context['latest']), list(Book.objects.all()[10:20]))

def validate(input_function) :
INDENT
    def wrapper(self, * args, ** kwargs) :
    INDENT
        self.validated = self.getvalue()
        if not self.validated :
        INDENT
            print "Not validated."
            return
        DEDENT
        input_function(self, validated = self.validated, * args, ** kwargs)
    DEDENT
    return wrapper
DEDENT

def main(data) :
INDENT
    data_writer = csv.writer(f2)
    for row in data :
    INDENT
        update_header_dict(row)
        data_writer.writerow(get_row_data_dict(row))
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

def __init__(self, parent = None) :
INDENT
    self.fig = plt.figure(1)
    self.ax = self.fig.add_subplot(111)
    self.ax.grid(True)
    super(mplCanvas, self).__init__(figure = self.fig)
    self.setParent(parent)
    self.init_figure()
DEDENT

def searchWordlist() :
INDENT
    path = str(raw_input(PATH))
    word = str(raw_input(WORD))
    with open(path) as f :
    INDENT
        for line in f :
        INDENT
            if word in line :
            INDENT
                print "Word found"
                return 1
            DEDENT
        DEDENT
    DEDENT
    print "Word not found"
    return 0
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

    def test_paginated_archive_view_does_not_load_entire_table(self):
        # Regression test for #18087
        _make_books(20, base_date=datetime.date.today())
        # 1 query for years list + 1 query for books
        with self.assertNumQueries(2):
            self.client.get('/dates/books/')
        # same as above + 1 query to test if books exist + 1 query to count them
        with self.assertNumQueries(4):
            self.client.get('/dates/books/paginated/')

def makeArchive(fileList, archive, path_prefix = None) :
INDENT
    try :
    INDENT
        a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
        for f in fileList :
        INDENT
            print "archiving file %s" % (f)
            if path_prefix is None :
            INDENT
                a.write(f)
            DEDENT
            else :
            INDENT
                a.write(f, f [len(path_prefix) :] if f.startswith(path_prefix) else f)
            DEDENT
        DEDENT
        a.close()
        return True
    DEDENT
    except : return False
DEDENT

def Max(lst) :
INDENT
    l = len(lst)
    if l > 1 :
    INDENT
        mid = l / 2
        m1 = Max(lst [: mid])
        m2 = Max(lst [mid :])
        return m1 if m1 > m2 else m2
    DEDENT
    return lst [0]
DEDENT

def find_items_within(list1, list2, within) :
INDENT
    i2_idx = 0
    shared = []
    for i1 in list1 :
    INDENT
        while shared and abs(shared [0] - i1) > within :
        INDENT
            shared.pop(0)
        DEDENT
        while i2_idx < len(list2) and abs(list2 [i2_idx] - i1) < = within :
        INDENT
            shared.append(list2 [i2_idx])
            i2_idx += 1
        DEDENT
        for result in zip([i1] * len(shared), shared) :
        INDENT
            yield result
        DEDENT
    DEDENT
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

def SumOdds(x, y) :
INDENT
    count = 0
    for i in range(x, y + 1) :
    INDENT
        if i % 2 == 1 :
        INDENT
            count = count + i
        DEDENT
    DEDENT
    print (count)
DEDENT

def get_user_attributes(cls, exclude_methods = True) :
INDENT
    base_attrs = dir(type('dummy', (object,), {}))
    this_cls_attrs = dir(cls)
    res = []
    for attr in this_cls_attrs :
    INDENT
        if base_attrs.count(attr) or (callable(getattr(cls, attr)) and exclude_methods) :
        INDENT
            continue
        DEDENT
        res += [attr]
    DEDENT
    return res
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

def read_logfile(master_log) :
INDENT
    last_line_holder = []
    for line in master_log :
    INDENT
        if line.contains('[76:Health]:') :
        INDENT
            last_line_holder.append(line)
        DEDENT
    DEDENT
    print (last_line_holder [- 1])
DEDENT

def folder_size(path = '.') :
INDENT
    total = 0
    for entry in os.scandir(path) :
    INDENT
        if entry.is_file() :
        INDENT
            total += entry.stat().st_size
        DEDENT
        elif entry.is_dir() :
        INDENT
            total += folder_size(entry.path)
        DEDENT
    DEDENT
    return total
DEDENT

    def test_no_duplicate_query(self):
        # Regression test for #18354
        with self.assertNumQueries(2):
            self.client.get('/dates/books/reverse/')

def chunks(l, amount) :
INDENT
    if amount < 1 :
    INDENT
        raise ValueError('amount must be positive integer')
    DEDENT
    chunk_len = len(l) / / amount
    leap_parts = len(l) % amount
    remainder = amount / / 2
    i = 0
    while i < len(l) :
    INDENT
        remainder += leap_parts
        end_index = i + chunk_len
        if remainder > = amount :
        INDENT
            remainder -= amount
            end_index += 1
        DEDENT
        yield l [i : end_index]
        i = end_index
    DEDENT
DEDENT

def __init__(self) :
INDENT
    self.root = tkinter.Tk()
    self.int_var = tkinter.IntVar()
    progbar = ttk.Progressbar(self.root, maximum = 4)
    progbar ['variable'] = self.int_var
    progbar.pack()
    self.label = ttk.Label(self.root, text = '0/4')
    self.label.pack()
    self.b_start = ttk.Button(self.root, text = 'Start')
    self.b_start ['command'] = self.start_thread
    self.b_start.pack()
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
    return (((s >> 8) & 0xff) | s < < 8) & 0xffff
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

def flatten(input) :
INDENT
    ret = []
    if not isinstance(input, (list, tuple)) :
    INDENT
        return [input]
    DEDENT
    for i in input :
    INDENT
        if isinstance(i, (list, tuple)) :
        INDENT
            ret.extend(flatten(i))
        DEDENT
        else :
        INDENT
            ret.append(i)
        DEDENT
    DEDENT
    return ret
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

def insert(self, k) :
INDENT
    t = TreeNode(k)
    parent = None
    node = self.root
    while node ! = None :
    INDENT
        parent = node
        if node.key > t.key :
        INDENT
            node = node.left
        DEDENT
        else :
        INDENT
            node = node.right
        DEDENT
    DEDENT
    t.p = parent
    if parent == None :
    INDENT
        self.root = t
    DEDENT
    elif t.key < parent.key :
    INDENT
        parent.left = t
    DEDENT
    else :
    INDENT
        parent.right = t
    DEDENT
    return t
DEDENT

    def test_datetime_archive_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        res = self.client.get('/dates/booksignings/')
        self.assertEqual(res.status_code, 200)

def distance_from_zero(n) :
INDENT
    try :
    INDENT
        n = int(n)
    DEDENT
    except ValueError :
    INDENT
        try :
        INDENT
            n = float(n)
        DEDENT
        except ValueError :
        INDENT
            print "Not a number!"
            n = float("NaN")
        DEDENT
    DEDENT
    return abs(n)
DEDENT

def distance_from_zero(n) :
INDENT
    try :
    INDENT
        n = int(n)
    DEDENT
    except ValueError :
    INDENT
        try :
        INDENT
            n = float(n)
        DEDENT
        except ValueError :
        INDENT
            print "Not a number!"
            n = float("NaN")
        DEDENT
    DEDENT
    return abs(n)
DEDENT

def __eq__(self, other) :
INDENT
    try :
    INDENT
        same_slots = self._ordered_slots == other._ordered_slots
    DEDENT
    except AttributeError :
    INDENT
        return False
    DEDENT
    if not same_slots :
    INDENT
        return False
    DEDENT
    return all(getattr(self, attr) == getattr(other, attr) for attr in self._ordered_slots)
DEDENT

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

    @requires_tz_support
    @skipUnlessDBFeature('has_zoneinfo_database')
    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_archive_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/')
        self.assertEqual(res.status_code, 200)

def ensure_even(argnum) :
INDENT
    def fdec(func) :
    INDENT
        def f(* args, ** kwargs) :
        INDENT
            assert (args [argnum] % 2 == 0)
            return func(* args, ** kwargs)
        DEDENT
        return f
    DEDENT
    return fdec
DEDENT

def test() :
INDENT
    fn = 'users.txt.txt'
    f = open(fn)
    output = []
    changeuser = 'peterpeter'
    userinfo = 'HeIsTall'
    for line in f :
    INDENT
        if line.strip().split(':') [0] ! = changeuser :
        INDENT
            output.append(line)
        DEDENT
        else :
        INDENT
            output.append(changeuser + ":" + userinfo + "\n")
        DEDENT
    DEDENT
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()
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

def strtr(strng, replace) :
INDENT
    buffer = []
    i, n = 0, len(strng)
    while i < n :
    INDENT
        match = False
        for s, r in replace.items() :
        INDENT
            if strng [i : len(s) + i] == s :
            INDENT
                buffer.append(r)
                i = i + len(s)
                match = True
                break
            DEDENT
        DEDENT
        if not match :
        INDENT
            buffer.append(strng [i])
            i = i + 1
        DEDENT
    DEDENT
    return ''.join(buffer)
DEDENT

    def test_date_list_order(self):
        """date_list should be sorted descending in index"""
        _make_books(5, base_date=datetime.date(2011, 12, 25))
        res = self.client.get('/dates/books/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(reversed(sorted(res.context['date_list']))))

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

    def test_archive_view_custom_sorting(self):
        Book.objects.create(name="Zebras for Dummies", pages=600, pubdate=datetime.date(2007, 5, 1))
        res = self.client.get('/dates/books/sortedbyname/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.order_by('name').all()))
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

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

def prob7(mylist) :
INDENT
    tempList = []
    if mylist :
    INDENT
        for i in mylist :
        INDENT
            if not isinstance(i, list) :
            INDENT
                print tempList, 'if', i, isinstance(i, list)
                tempList.append(i)
            DEDENT
            else :
            INDENT
                print tempList, 'else', i
                tempList.extend(prob7(i))
            DEDENT
        DEDENT
    DEDENT
    return tempList
DEDENT

def find_values(id, obj) :
INDENT
    results = []
    def _find_values(id, obj) :
    INDENT
        try :
        INDENT
            for key, value in obj.iteritems() :
            INDENT
                if key == id :
                INDENT
                    results.append(value)
                DEDENT
                elif not isinstance(value, basestring) :
                INDENT
                    _find_values(id, value)
                DEDENT
            DEDENT
        DEDENT
        except AttributeError :
        INDENT
            pass
        DEDENT
        try :
        INDENT
            for item in obj :
            INDENT
                if not isinstance(item, basestring) :
                INDENT
                    _find_values(id, item)
                DEDENT
            DEDENT
        DEDENT
        except TypeError :
        INDENT
            pass
        DEDENT
    DEDENT
    if not isinstance(obj, basestring) :
    INDENT
        _find_values(id, obj)
    DEDENT
    return results
DEDENT

def deprecated(func) :
INDENT
    @ functools.wraps(func)
    def new_func(* args, ** kwargs) :
    INDENT
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
            category = DeprecationWarning,
            stacklevel = 2)
        warnings.simplefilter('default', DeprecationWarning)
        return func(* args, ** kwargs)
    DEDENT
    return new_func
DEDENT

def is_square(integer) :
INDENT
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
DEDENT

def obj_get(self, request = None, ** kwargs) :
INDENT
    try :
    INDENT
        info = Info.get(kwargs ['pk'])
    DEDENT
    except ResourceNotFound :
    INDENT
        raise ObjectDoesNotExist('Sorry, no results on that page.')
    DEDENT
    return info
DEDENT

    def test_archive_view_custom_sorting_dec(self):
        Book.objects.create(name="Zebras for Dummies", pages=600, pubdate=datetime.date(2007, 5, 1))
        res = self.client.get('/dates/books/sortedbynamedec/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), list(Book.objects.dates('pubdate', 'year', 'DESC')))
        self.assertEqual(list(res.context['latest']), list(Book.objects.order_by('-name').all()))
        self.assertTemplateUsed(res, 'generic_views/book_archive.html')

def wrapper(* args, ** kwargs) :
INDENT
    for i in range(max_retries + 1) :
    INDENT
        print ('Try #', i + 1)
        try :
        INDENT
            return fn(* args, ** kwargs)
        DEDENT
        except exception_type as e :
        INDENT
            print ('wrapper exception:', i + 1, e)
        DEDENT
    DEDENT
DEDENT

def fib(n) :
INDENT
    global call_count
    call_count = call_count + 1
    if n < = 1 :
    INDENT
        return 1
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

def set_border(ws, cell_range) :
INDENT
    border = Border(left = Side(border_style = 'thin', color = '000000'),
        right = Side(border_style = 'thin', color = '000000'),
        top = Side(border_style = 'thin', color = '000000'),
        bottom = Side(border_style = 'thin', color = '000000'))
    rows = ws.iter_rows(cell_range)
    for row in rows :
    INDENT
        for cell in row :
        INDENT
            cell.border = border
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

def run_query(query, database, s3_output) :
INDENT
    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString = query,
        QueryExecutionContext = {
            'Database' : database},
        ResultConfiguration = {
            'OutputLocation' : s3_output,
            })
    print ('Execution ID: ' + response ['QueryExecutionId'])
    return response
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

    def test_archive_view_without_date_field(self):
        msg = 'BookArchiveWithoutDateField.date_field is required.'
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/dates/books/without_date_field/')


def traceit(self, frame, event, arg) :
INDENT
    if event == "line" :
    INDENT
        lineno = frame.f_lineno
        filename = frame.f_globals ["__file__"]
        if filename == "<stdin>" :
        INDENT
            filename = "traceit.py"
        DEDENT
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")) :
        INDENT
            filename = filename [: - 1]
        DEDENT
        name = frame.f_globals ["__name__"]
        line = linecache.getline(filename, lineno)
        if frame.f_back is self.lastframe :
        INDENT
            print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
        DEDENT
        else :
        INDENT
            print "%s:%s:%s(%s)" % (name, lineno, frame.f_code.co_name, str.join(', ', ("%s=%r" % item for item in frame.f_locals.iteritems())))
            print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
        DEDENT
        self.lastframe = frame.f_back
    DEDENT
    return self.traceit
DEDENT

def eval_expr(cls, expr, subs = None) :
INDENT
    if subs is None :
    INDENT
        frame = sys._getframe()
        subs = {}
        subs.update(frame.f_globals)
        if frame.f_back :
        INDENT
            subs.update(frame.f_back.f_globals)
        DEDENT
    DEDENT
    expr_tree = ast.parse(expr, mode = 'eval').body
    return cls.eval(expr_tree, subs)
DEDENT

def overlap(string1, string2) :
INDENT
    count = 0;
    len1 = len(string1)
    len2 = len(string2)
    smallLen = len1
    if len2 < len1 :
    INDENT
        smallLen = len2
    DEDENT
    for i in range(smallLen) :
    INDENT
        if string1 [i] == string2 [i] :
        INDENT
            count += 1
        DEDENT
    DEDENT
    return count
DEDENT

def bitwise_or(num1, num2) :
INDENT
    new_num1 = list(num1 [2 :])
    new_num2 = list(num2 [2 :])
    if len(num1) > len(num2) :
    INDENT
        new_num2 [: 0] = '0' * (len(num1) - len(num2))
    DEDENT
    elif len(num1) < len(num2) :
    INDENT
        new_num1 [: 0] = '0' * (len(num2) - len(num1))
    DEDENT
    new_num = []
    for c1, c2 in zip(new_num1, new_num2) :
    INDENT
        if c1 == "1" or c2 == "1" :
        INDENT
            new_num.append("1")
        DEDENT
        else :
        INDENT
            new_num.append(c1)
        DEDENT
    DEDENT
    return '0b' + ''.join(new_num)
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class YearArchiveViewTests(TestDataMixin, TestCase):

    def test_year_view(self):
        res = self.client.get('/dates/books/2008/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [datetime.date(2008, 10, 1)])
        self.assertEqual(res.context['year'], datetime.date(2008, 1, 1))
        self.assertTemplateUsed(res, 'generic_views/book_archive_year.html')

        # Since allow_empty=False, next/prev years must be valid (#7164)
        self.assertIsNone(res.context['next_year'])
        self.assertEqual(res.context['previous_year'], datetime.date(2006, 1, 1))

def compose(* funcs) :
INDENT
    def f(x) :
    INDENT
        ret = x
        for func in funcs [: : - 1] :
        INDENT
            ret = func(ret)
        DEDENT
        return ret
    DEDENT
    return f
DEDENT

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

def get_target_path(path, matrix) :
INDENT
    try :
    INDENT
        return reduce(operator.getitem, path, matrix)
    DEDENT
    except KeyError :
    INDENT
        return None
    DEDENT
DEDENT

def combinations(iterable, r) :
INDENT
    pool = tuple(iterable)
    n = len(pool)
    if r > n :
    INDENT
        return
    DEDENT
    indices = list(range(r))
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
        if 1 in tuple(pool [i] for i in indices) and 3 in tuple(pool [i] for i in indices) :
        INDENT
            pass
        DEDENT
        else :
        INDENT
            yield tuple(pool [i] for i in indices)
        DEDENT
    DEDENT
DEDENT

    def test_year_view_make_object_list(self):
        res = self.client.get('/dates/books/2006/make_object_list/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [datetime.date(2006, 5, 1)])
        self.assertEqual(list(res.context['book_list']), list(Book.objects.filter(pubdate__year=2006)))
        self.assertEqual(list(res.context['object_list']), list(Book.objects.filter(pubdate__year=2006)))
        self.assertTemplateUsed(res, 'generic_views/book_archive_year.html')

def turns(NumOfTries, word) :
INDENT
    score = 0
    guesses = set()
    for i in range(len(w)) :
    INDENT
        guess = str(raw_input('Guess a letter (caps only): '))
        guesses.add(guess)
        if guess in word :
        INDENT
            score += 1
        DEDENT
        print [c if c in guesses else "_" for c in w]
    DEDENT
    return score
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

def recursive_add(s) :
INDENT
    print "DEBUG: recursive_add(%s)" % repr(s)
    sum = 0
    print "DEBUG: sum: %d" % sum
    if len(s) == 1 :
    INDENT
        sum += s [0] ** 2
        print "DEBUG: sum: %d" % sum
    DEDENT
    else :
    INDENT
        recursive_add(s [1 :])
        sum += s [0] ** 2
        print "DEBUG: sum: %d" % sum
    DEDENT
    return sum
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

    def test_year_view_empty(self):
        res = self.client.get('/dates/books/1999/')
        self.assertEqual(res.status_code, 404)
        res = self.client.get('/dates/books/1999/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [])
        self.assertEqual(list(res.context['book_list']), [])

        # Since allow_empty=True, next/prev are allowed to be empty years (#7164)
        self.assertEqual(res.context['next_year'], datetime.date(2000, 1, 1))
        self.assertEqual(res.context['previous_year'], datetime.date(1998, 1, 1))

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

def change_keys(obj) :
INDENT
    new_obj = obj
    for k in new_obj :
    INDENT
        if hasattr(obj [k], '__getitem__') :
        INDENT
            change_keys(obj [k])
        DEDENT
        if '.' in k :
        INDENT
            obj [k.replace('.', '$')] = obj [k]
            del obj [k]
        DEDENT
    DEDENT
DEDENT

def power_function(decimal, integer) :
INDENT
    num = 1
    if integer > 0 :
    INDENT
        for function in range(integer) :
        INDENT
            num = num * decimal
        DEDENT
    DEDENT
    if integer < 0 :
    INDENT
        num = 1.0
        for function in range(- integer) :
        INDENT
            num = num / decimal
        DEDENT
    DEDENT
    return num
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

def __getitem__(self, item) :
INDENT
    if isinstance(item, numbers.Integral) :
    INDENT
        return item
    DEDENT
    if isinstance(item, slice) :
    INDENT
        return list(range(item.start or 0, item.stop or len(self), item.step or 1))
    DEDENT
    else :
    INDENT
        raise TypeError('{cls} indices must be integers or slices, not {idx}'.format(
                cls = type(self).__name__,
                idx = type(item).__name__,
                ))
    DEDENT
DEDENT

def printFigure(rows) :
INDENT
    for x in range(rows) :
    INDENT
        items = [str(i) for i in range(1, x + 1)]
        if x % 2 == 0 :
        INDENT
            items = items [: : - 1]
        DEDENT
        print (''.join(items))
    DEDENT
DEDENT

    def test_year_view_allow_future(self):
        # Create a new book in the future
        year = datetime.date.today().year + 1
        Book.objects.create(name="The New New Testement", pages=600, pubdate=datetime.date(year, 1, 1))
        res = self.client.get('/dates/books/%s/' % year)
        self.assertEqual(res.status_code, 404)

        res = self.client.get('/dates/books/%s/allow_empty/' % year)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), [])

        res = self.client.get('/dates/books/%s/allow_future/' % year)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [datetime.date(year, 1, 1)])

def find_nearest(array, value) :
INDENT
    idx = np.searchsorted(array, value, side = "left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array [idx - 1]) < math.fabs(value - array [idx])) :
    INDENT
        return array [idx - 1]
    DEDENT
    else :
    INDENT
        return array [idx]
    DEDENT
DEDENT

def completer(text, state) :
INDENT
    options = [x for x in addrs if x.startswith(text)]
    try :
    INDENT
        return options [state]
    DEDENT
    except IndexError :
    INDENT
        return None
    DEDENT
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

def default(self, obj) :
INDENT
    if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)) :
    INDENT
        return int(obj)
    DEDENT
    elif isinstance(obj, (np.float_, np.float16, np.float32,
            np.float64)) :
    INDENT
        return float(obj)
    DEDENT
    elif isinstance(obj, (np.ndarray,)) :
    INDENT
        return obj.tolist()
    DEDENT
    return json.JSONEncoder.default(self, obj)
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

    def test_year_view_paginated(self):
        res = self.client.get('/dates/books/2006/paginated/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), list(Book.objects.filter(pubdate__year=2006)))
        self.assertEqual(list(res.context['object_list']), list(Book.objects.filter(pubdate__year=2006)))
        self.assertTemplateUsed(res, 'generic_views/book_archive_year.html')

def create_webview(self) :
INDENT
    webview = WebView(activity)
    activity.addContentView(webview, LayoutParams(- 1, - 1))
    webview.getSettings().setJavaScriptEnabled(True)
    html = "<html><body style='margin:0;padding:0;'>\
            <script type='text/javascript'\
            src='http://ad.leadboltads.net/show_app_ad.js?section_id=ID_HERE'>\
            </script></body></html>"
    activity.setContentView(webview)
    webview.loadData(html, "text/html", "utf-8")
    layout = LinearLayout(activity)
    layout.addView(activity.mView)
    activity.setContentView(layout)
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

def f() :
INDENT
    for key, val in measurements.items() :
    INDENT
        exec ('global {};{} = {}'.format(key, key, val))
    DEDENT
    print ('tg: ', tg)
    vars = globals()
    for key in measurements.keys() :
    INDENT
        print ('Key: ', key, ', Value: ', vars [key])
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

def listFunc(lst) :
INDENT
    if len(lst) == 0 : return ''
    if len(lst) == 1 : return lst [0]
    firstPart = lst [: - 1]
    retFirst = ", ".join(firstPart)
    retSecond = ", and " + lst [- 1]
    return retFirst + retSecond;
DEDENT

def decorator(f) :
INDENT
    @ wraps(f)
    def wrapped(* args, ** kargs) :
    INDENT
        event.fire(* args, ** kargs)
        return f(* args, ** kargs)
    DEDENT
    return wrapped
DEDENT

    def test_year_view_custom_sort_order(self):
        # Zebras comes after Dreaming by name, but before on '-pubdate' which is the default sorting
        Book.objects.create(name="Zebras for Dummies", pages=600, pubdate=datetime.date(2006, 9, 1))
        res = self.client.get('/dates/books/2006/sortedbyname/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [datetime.date(2006, 5, 1), datetime.date(2006, 9, 1)])
        self.assertEqual(
            list(res.context['book_list']),
            list(Book.objects.filter(pubdate__year=2006).order_by('name'))
        )
        self.assertEqual(
            list(res.context['object_list']),
            list(Book.objects.filter(pubdate__year=2006).order_by('name'))
        )
        self.assertTemplateUsed(res, 'generic_views/book_archive_year.html')

def perm(n) :
INDENT
    p = []
    for i in range(0, n + 1) :
    INDENT
        p.append(i)
    DEDENT
    while True :
    INDENT
        for i in range(1, n + 1) :
        INDENT
            print(p [i], end = ' ')
        DEDENT
        print ("")
        i = n - 1
        found = 0
        while (not found and i > 0) :
        INDENT
            if p [i] < p [i + 1] :
            INDENT
                found = 1
            DEDENT
            else :
            INDENT
                i = i - 1
            DEDENT
        DEDENT
        k = n
        while p [i] > p [k] :
        INDENT
            k = k - 1
        DEDENT
        aux = p [i]
        p [i] = p [k]
        p [k] = aux
        for j in range(1, (n - i) / 2 + 1) :
        INDENT
            aux = p [i + j]
            p [i + j] = p [n - j + 1]
            p [n - j + 1] = aux
        DEDENT
        if not found :
        INDENT
            break
        DEDENT
    DEDENT
DEDENT

def add_list_attributes(klass) :
INDENT
    def new(cls, * args, ** kwargs) :
    INDENT
        result = super(cls, cls).__new__(cls)
        for attribute in klass.list_attributes :
        INDENT
            setattr(result, attribute, [])
        DEDENT
        return result
    DEDENT
    klass.__new__ = staticmethod(new)
    return klass
DEDENT

def __init__(self, * args, ** kwds) :
INDENT
    super(MyOrderedDict, self).__init__()
    if len(args) > 0 :
    INDENT
        for i in args [0] :
        INDENT
            super(MyOrderedDict, self).__setitem__(i.id, i)
        DEDENT
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

    def test_year_view_two_custom_sort_orders(self):
        Book.objects.create(name="Zebras for Dummies", pages=300, pubdate=datetime.date(2006, 9, 1))
        Book.objects.create(name="Hunting Hippos", pages=400, pubdate=datetime.date(2006, 3, 1))
        res = self.client.get('/dates/books/2006/sortedbypageandnamedec/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context['date_list']),
            [datetime.date(2006, 3, 1), datetime.date(2006, 5, 1), datetime.date(2006, 9, 1)]
        )
        self.assertEqual(
            list(res.context['book_list']),
            list(Book.objects.filter(pubdate__year=2006).order_by('pages', '-name'))
        )
        self.assertEqual(
            list(res.context['object_list']),
            list(Book.objects.filter(pubdate__year=2006).order_by('pages', '-name'))
        )
        self.assertTemplateUsed(res, 'generic_views/book_archive_year.html')

def index(filename, lst) :
INDENT
    lst = set(lst)
    dic = {}
    with open(filename, 'r') as fobj :
    INDENT
        for lineno, line in enumerate(fobj, 1) :
        INDENT
            words = line.split()
            for word in words :
            INDENT
                if word in lst :
                INDENT
                    dic.setdefault(word, []).append(lineno)
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return dic
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

def __init__(self) :
INDENT
    root = Tk()
    root.geometry('250x150')
    root.title("DiscreteMaths_3_1")
    usertext = StringVar()
    Label_1 = Label(root, text = "Input")
    Label_2 = Label(root, text = "Output")
    inputField = Entry(root, textvariable = usertext)
    outputField = Entry(root)
    inputField.bind('<Return>', lambda _ : printLine())
    def printLine() :
    INDENT
        counter = {}
        words = inputField.get().split()
        for word in words :
        INDENT
            counter [word] = counter.get(word, 0) + 1
            Ans = counter [word] - 1
            print(Ans, end = " ")
            outputField.insert(END, str(Ans))
        DEDENT
    DEDENT
    Label_1.grid(row = 0)
    Label_2.grid(row = 1)
    inputField.grid(row = 0, column = 1)
    outputField.grid(row = 1, column = 1)
    root.mainloop()
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

    def test_year_view_invalid_pattern(self):
        res = self.client.get('/dates/books/no_year/')
        self.assertEqual(res.status_code, 404)

def nostdout(func) :
INDENT
    def wrapper(* args, ** kwargs) :
    INDENT
        save_stdout = sys.stdout
        sys.stdout = DummyFile()
        func(* args, ** kwargs)
        sys.stdout = save_stdout
    DEDENT
    return wrapper
DEDENT

def is_monotone(heights) :
INDENT
    if len(heights) == 0 :
    INDENT
        return True
    DEDENT
    steps = []
    for j in range(len(heights) - 1) :
    INDENT
        steps.append(heights [j + 1] - heights [j])
    DEDENT
    if all(step > = 0 for step in steps) or all(step < = 0 for step in steps) :
    INDENT
        return True
    DEDENT
    return False
DEDENT

def __init__(self, ** kwargs) :
INDENT
    super(MutexInit, self).__init__()
    for arg in kwargs :
    INDENT
        setattr(self, arg, kwargs.get(arg))
    DEDENT
    self._arg_method_dict = {}
    for attr_name in dir(self) :
    INDENT
        attr = getattr(self, attr_name)
        if getattr(attr, "_isrequiredargsmethod", False) :
        INDENT
            self._arg_method_dict [attr.args] = attr
        DEDENT
    DEDENT
    provided_args = tuple(sorted(
            [arg for arg in kwargs if kwargs [arg] is not None]))
    sub_init = self._arg_method_dict.get(provided_args, None)
    if sub_init :
    INDENT
        sub_init(** kwargs)
    DEDENT
    else :
    INDENT
        raise AttributeError('Insufficient arguments')
    DEDENT
DEDENT

def scale_bar(ax, proj, length, location = (0.5, 0.05), linewidth = 3,
units = 'km', m_per_unit = 1000) :
INDENT
    x0, x1, y0, y1 = ax.get_extent(proj.as_geodetic())
    utm = ccrs.UTM(utm_from_lon((x0 + x1) / 2))
    x0, x1, y0, y1 = ax.get_extent(utm)
    sbcx, sbcy = x0 + (x1 - x0) * location [0], y0 + (y1 - y0) * location [1]
    bar_xs = [sbcx - length * m_per_unit / 2, sbcx + length * m_per_unit / 2]
    buffer = [patheffects.withStroke(linewidth = 5, foreground = "w")]
    ax.plot(bar_xs, [sbcy, sbcy], transform = utm, color = 'k',
        linewidth = linewidth, path_effects = buffer)
    buffer = [patheffects.withStroke(linewidth = 3, foreground = "w")]
    t0 = ax.text(sbcx, sbcy, str(length) + ' ' + units, transform = utm,
        horizontalalignment = 'center', verticalalignment = 'bottom',
        path_effects = buffer, zorder = 2)
    left = x0 + (x1 - x0) * 0.05
    t1 = ax.text(left, sbcy, u'\u25B2\nN', transform = utm,
        horizontalalignment = 'center', verticalalignment = 'bottom',
        path_effects = buffer, zorder = 2)
    ax.plot(bar_xs, [sbcy, sbcy], transform = utm, color = 'k',
        linewidth = linewidth, zorder = 3)
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

def __init__(self, master, * args, ** kwargs) :
INDENT
    tk.Toplevel.__init__(self, master)
    if 'title' in kwargs :
    INDENT
        self.title(kwargs ['title'])
    DEDENT
    self.hide_main_button = tk.Button(self, text = "Hide/Show MainWindow")
    self.hide_main_button ['command'] = self.master.toggle_hide
    self.hide_main_button.pack()
DEDENT

def same_structure(a, b) :
INDENT
    if a == [] or b == [] :
    INDENT
        return a == b
    DEDENT
    elif is_list(a [0]) ! = is_list(b [0]) :
    INDENT
        return False
    DEDENT
    elif not is_list(a [0]) :
    INDENT
        return same_structure(a [1 :], b [1 :])
    DEDENT
    else :
    INDENT
        return same_structure(a [0], b [0]) and same_structure(a [1 :], b [1 :])
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

def partition(pred, iterable,
filter = itertools.ifilter,
filterfalse = itertools.ifilterfalse,
tee = itertools.tee) :
INDENT
    'Use a predicate to partition entries into false entries and true entries'
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)
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

    def test_no_duplicate_query(self):
        # Regression test for #18354
        with self.assertNumQueries(4):
            self.client.get('/dates/books/2008/reverse/')

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

def pdf_view(request) :
INDENT
    with open('/path/to/my/file.pdf', 'r') as pdf :
    INDENT
        response = HttpResponse(pdf.read(), mimetype = 'application/pdf')
        response ['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    DEDENT
    pdf.closed
DEDENT

def family_lineage(familytree, lineage) :
INDENT
    if not familytree :
    INDENT
        return False
    DEDENT
    try :
    INDENT
        reduce(lambda d, k : d [k], lineage, familytree)
        return True
    DEDENT
    except KeyError :
    INDENT
        return any(family_lineage(val, lineage) for val in familytree.itervalues())
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

    def test_datetime_year_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        res = self.client.get('/dates/booksignings/2008/')
        self.assertEqual(res.status_code, 200)

def numPens(n) :
INDENT
    if n < 5 :
    INDENT
        return False
    DEDENT
    elif n == 5 or n == 8 or n == 24 :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)
    DEDENT
DEDENT

def is_magic(items) :
INDENT
    if len(set(items)) ! = 9 :
    INDENT
        return 'Invalid'
    DEDENT
    for x in range(0, 9, 3) :
    INDENT
        l = items [x : x + 3]
        if sum(l) ! = 15 :
        INDENT
            return 'Invalid'
        DEDENT
    DEDENT
    for x in range(3) :
    INDENT
        l = [items [x], items [x + 3], items [x + 6]]
        if sum(l) ! = 15 :
        INDENT
            return 'Invalid'
        DEDENT
    DEDENT
    l = [items [0], items [4], items [8]]
    if sum(l) ! = 15 :
    INDENT
        return 'Invalid'
    DEDENT
    l = [items [2], items [4], items [6]]
    if sum(l) ! = 15 :
    INDENT
        return 'Invalid'
    DEDENT
    return 'Valid'
DEDENT

def is_binary(file_name) :
INDENT
    try :
    INDENT
        with open(file_name, 'tr') as check_file :
        INDENT
            check_file.read()
            return False
        DEDENT
    DEDENT
    except :
    INDENT
        return True
    DEDENT
DEDENT

def __init__(self, key, value = None) :
INDENT
    self.key = key
    self.value = value
    if not key in Master.existent :
    INDENT
        Master.existent [key] = self
    DEDENT
DEDENT

    @skipUnlessDBFeature('has_zoneinfo_database')
    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_year_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/2008/')
        self.assertEqual(res.status_code, 200)

def get_drives() :
INDENT
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    letter = ord('A')
    while bitmask > 0 :
    INDENT
        if bitmask & 1 :
        INDENT
            drives.append(chr(letter) + ':\\')
        DEDENT
        bitmask >>= 1
        letter += 1
    DEDENT
    return drives
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
        if not 'SERVICE_NAME' in settings_dict :
        INDENT
            dsn = Database.makedsn(settings_dict ['HOST'],
                int(settings_dict ['PORT']),
                settings_dict ['NAME'])
        DEDENT
        else :
        INDENT
            dsn = Database.makedsn(host = settings_dict ['HOST'],
                port = int(settings_dict ['PORT']),
                service_name = settings_dict ['SERVICE_NAME'].strip())
        DEDENT
    DEDENT
    else :
    INDENT
        dsn = settings_dict ['NAME']
    DEDENT
    return "%s/%s@%s" % (settings_dict ['USER'],
        settings_dict ['PASSWORD'], dsn)
DEDENT

    def test_date_list_order(self):
        """date_list should be sorted ascending in year view"""
        _make_books(10, base_date=datetime.date(2011, 12, 25))
        res = self.client.get('/dates/books/2011/')
        self.assertEqual(list(res.context['date_list']), list(sorted(res.context['date_list'])))

def myfunc(lst) :
INDENT
    ret = []
    a = b = lst [0]
    for el in lst [1 :] :
    INDENT
        if el == b + 1 :
        INDENT
            b = el
        DEDENT
        else :
        INDENT
            ret.append(a if a == b else (a, b))
            a = b = el
        DEDENT
    DEDENT
    ret.append(a if a == b else (a, b))
    return ret
DEDENT

def flatten(x) :
INDENT
    flat = True
    ans = []
    for i in x :
    INDENT
        if (i.__class__ is list) :
        INDENT
            ans = flatten(i)
        DEDENT
        else :
        INDENT
            ans.append(i)
        DEDENT
    DEDENT
    return ans
DEDENT

def oddn(* numbers) :
INDENT
    try :
    INDENT
        return max(x for x in numbers if x % 2 == 1)
    DEDENT
    except ValueError :
    INDENT
        print 'No odd number is found'
        return None
    DEDENT
DEDENT

def stemming(verb) :
INDENT
    suffixes = ["ing", "ed", "es", "s"]
    stem = verb
    for suffix in suffixes :
    INDENT
        if stem.endswith(suffix) :
        INDENT
            stem = stem [: - len(suffix)]
            break
        DEDENT
    DEDENT
    return stem
DEDENT

    @mock.patch('django.views.generic.list.MultipleObjectMixin.get_context_data')
    def test_get_context_data_receives_extra_context(self, mock):
        """
        MultipleObjectMixin.get_context_data() receives the context set by
        BaseYearArchiveView.get_dated_items(). This behavior is implemented in
        BaseDateListView.get().
        """
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        with self.assertRaisesMessage(TypeError, 'context must be a dict rather than MagicMock.'):
            self.client.get('/dates/booksignings/2008/')
        args, kwargs = mock.call_args
        # These are context values from get_dated_items().
        self.assertEqual(kwargs['year'], datetime.date(2008, 1, 1))
        self.assertIsNone(kwargs['previous_year'])
        self.assertIsNone(kwargs['next_year'])

def compare(a, b) :
INDENT
    i_zip = list(enumerate(zip(a, b)))
    llen = len(a)
    hp = llen / / 2
    def find_index(i_zip) :
    INDENT
        for i, (x, y) in i_zip :
        INDENT
            if x ! = y :
            INDENT
                return i
            DEDENT
        DEDENT
        return i_zip [0] [0]
    DEDENT
    n = find_index(i_zip [: hp])
    p = find_index(i_zip [hp :])
    m = llen - p
    q = llen - n
    if a [: n] + a [p : q] + a [m : p] + a [n : m] + a [q :] ! = b :
    INDENT
        return None
    DEDENT
    return n, m
DEDENT

def __setattr__(self, name, value) :
INDENT
    try :
    INDENT
        index = MyObject.indexes [name]
    DEDENT
    except KeyError :
    INDENT
        index = weakref.WeakValueDictionary()
        MyObject.indexes [name] = index
    DEDENT
    try :
    INDENT
        old_val = getattr(self, name)
        del index [old_val]
    DEDENT
    except (KeyError, AttributeError) :
    INDENT
        pass
    DEDENT
    object.__setattr__(self, name, value)
    index [value] = self
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

def test_val(a_points, b_points, val1, val2) :
INDENT
    if val1 > val2 :
    INDENT
        a_points += 1
    DEDENT
    elif val2 > val1 :
    INDENT
        b_points += 1
    DEDENT
    return a_points, b_points
DEDENT

def sanity_check(test, name = 'undefined', ontrue = None, onfalse = None) :
INDENT
    if test :
    INDENT
        log.debug(name)
        if ontrue is not None :
        INDENT
            ontrue()
        DEDENT
    DEDENT
    else :
    INDENT
        log.warn(name)
        if onfalse is not None :
        INDENT
            onfalse()
        DEDENT
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

def todict(obj) :
INDENT
    data = {}
    for key, value in obj.__dict__.iteritems() :
    INDENT
        try :
        INDENT
            data [key] = todict(value)
        DEDENT
        except AttributeError :
        INDENT
            data [key] = value
        DEDENT
    DEDENT
    return data
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

    def test_get_dated_items_not_implemented(self):
        msg = 'A DateView must provide an implementation of get_dated_items()'
        with self.assertRaisesMessage(NotImplementedError, msg):
            self.client.get('/BaseDateListViewTest/')


def countSubStringMatchRecursive(target, key, count = 0) :
INDENT
    index = target.find(key)
    if index > = 0 :
    INDENT
        count += 1
        target = target [index + len(key) :]
        count = countSubStringMatchRecursive(target, key, count)
    DEDENT
    return count
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

def checkLen() :
INDENT
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for position, day in enumerate(days) :
    INDENT
        if day == "Monday" :
        INDENT
            print ("Found it")
            print (position)
        DEDENT
    DEDENT
DEDENT

def update_position(self) :
INDENT
    rotation = self.get_rotation()
    self.set_rotation(0)
    self.set_va(self.__Va)
    self.set_ha(self.__Ha)
    renderer = self.axes.figure.canvas.get_renderer()
    bbox1 = self.get_window_extent(renderer = renderer)
    self.set_va('center')
    self.set_ha('center')
    bbox2 = self.get_window_extent(renderer = renderer)
    dr = np.array(bbox2.get_points() [0] - bbox1.get_points() [0])
    rad = np.deg2rad(rotation)
    rot_mat = np.array([
            [np.cos(rad), np.sin(rad)],
            [- np.sin(rad), np.cos(rad)]])
    drp = np.dot(dr, rot_mat)
    offset = matplotlib.transforms.Affine2D().translate(- drp [0], - drp [1])
    self.set_rotation(rotation)
    return offset
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class MonthArchiveViewTests(TestDataMixin, TestCase):

    def test_month_view(self):
        res = self.client.get('/dates/books/2008/oct/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/book_archive_month.html')
        self.assertEqual(list(res.context['date_list']), [datetime.date(2008, 10, 1)])
        self.assertEqual(list(res.context['book_list']),
                         list(Book.objects.filter(pubdate=datetime.date(2008, 10, 1))))
        self.assertEqual(res.context['month'], datetime.date(2008, 10, 1))

        # Since allow_empty=False, next/prev months must be valid (#7164)
        self.assertIsNone(res.context['next_month'])
        self.assertEqual(res.context['previous_month'], datetime.date(2006, 5, 1))

def divisor_function(n) :
INDENT
    "Returns the sum of divisors of n"
    checked = {}
    factors = prime_factors(n)
    sum_of_divisors = 1
    for x in factors :
    INDENT
        if checked.get(x, False) :
        INDENT
            continue
        DEDENT
        else :
        INDENT
            count = factors.count(x)
            tmp = (x ** (count + 1) - 1) / / (x - 1)
            sum_of_divisors *= tmp
            checked [x] = True
        DEDENT
    DEDENT
    return sum_of_divisors
DEDENT

def permutations(l) :
INDENT
    permutations = []
    length = len(l)
    for x in xrange(factorial(length)) :
    INDENT
        available = list(l)
        newPermutation = []
        for radix in xrange(length, 0, - 1) :
        INDENT
            placeValue = factorial(radix - 1)
            index = x / placeValue
            newPermutation.append(available.pop(index))
            x -= index * placeValue
        DEDENT
        permutations.append(newPermutation)
    DEDENT
    return permutations
DEDENT

    def test_month_view_allow_empty(self):
        # allow_empty = False, empty month
        res = self.client.get('/dates/books/2000/jan/')
        self.assertEqual(res.status_code, 404)

        # allow_empty = True, empty month
        res = self.client.get('/dates/books/2000/jan/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['date_list']), [])
        self.assertEqual(list(res.context['book_list']), [])
        self.assertEqual(res.context['month'], datetime.date(2000, 1, 1))

        # Since allow_empty=True, next/prev are allowed to be empty months (#7164)
        self.assertEqual(res.context['next_month'], datetime.date(2000, 2, 1))
        self.assertEqual(res.context['previous_month'], datetime.date(1999, 12, 1))

        # allow_empty but not allow_future: next_month should be empty (#7164)
        url = datetime.date.today().strftime('/dates/books/%Y/%b/allow_empty/').lower()
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(res.context['next_month'])

def release(self) :
INDENT
    if self.released :
    INDENT
        return False
    DEDENT
    signal.signal(self.sig, self.original_handler)
    self.released = True
    return True
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

def outer(v) :
INDENT
    def inner(varname = 'v', scope = locals()) :
    INDENT
        scope [varname] += 1
        return scope [varname]
    DEDENT
    return inner
DEDENT

    def test_month_view_allow_future(self):
        future = (datetime.date.today() + datetime.timedelta(days=60)).replace(day=1)
        urlbit = future.strftime('%Y/%b').lower()
        b = Book.objects.create(name="The New New Testement", pages=600, pubdate=future)

        # allow_future = False, future month
        res = self.client.get('/dates/books/%s/' % urlbit)
        self.assertEqual(res.status_code, 404)

        # allow_future = True, valid future month
        res = self.client.get('/dates/books/%s/allow_future/' % urlbit)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['date_list'][0], b.pubdate)
        self.assertEqual(list(res.context['book_list']), [b])
        self.assertEqual(res.context['month'], future)

        # Since allow_future = True but not allow_empty, next/prev are not
        # allowed to be empty months (#7164)
        self.assertIsNone(res.context['next_month'])
        self.assertEqual(res.context['previous_month'], datetime.date(2008, 10, 1))

        # allow_future, but not allow_empty, with a current month. So next
        # should be in the future (yup, #7164, again)
        res = self.client.get('/dates/books/2008/oct/allow_future/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['next_month'], future)
        self.assertEqual(res.context['previous_month'], datetime.date(2006, 5, 1))

def censored(sentence, * words) :
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

def rep_str(s, x, y) :
INDENT
    while x in s :
    INDENT
        s = s [: s.index(x)] + y + s [s.index(x) + len(x) :]
    DEDENT
    return s
DEDENT

def initUI(self) :
INDENT
    self.icon = QSystemTrayIcon()
    r = self.icon.isSystemTrayAvailable()
    print r
    self.icon.setIcon(QtGui.QIcon('/home/vzades/Desktop/web.png'))
    self.icon.show()
    self.setGeometry(300, 300, 250, 150)
    self.setWindowIcon(QtGui.QIcon('/home/vzades/Desktop/web.png'))
    self.setWindowTitle('Message box')
    self.show()
    self.icon.activated.connect(self.activate)
    self.show()
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

def __init__(self, fd) :
INDENT
    RawPcapReaderFD.__init__(self, fd)
    try :
    INDENT
        self.LLcls = conf.l2types [self.linktype]
    DEDENT
    except KeyError :
    INDENT
        warning("PcapReader: unknown LL type [%i]/[%#x]. Using Raw packets" % (self.linktype, self.linktype))
        self.LLcls = conf.raw_layer
    DEDENT
DEDENT

def dfs(graph, node) :
INDENT
    print '{0}_start'.format(node)
    if node not in graph :
    INDENT
        print '{0}_end'.format(node)
        return
    DEDENT
    for i, nd in enumerate(graph [node]) :
    INDENT
        if i > 0 :
        INDENT
            print '{0}_middle'.format(node)
        DEDENT
        dfs(graph, nd)
    DEDENT
    print '{0}_end'.format(node)
DEDENT

def sigmoid(x) :
INDENT
    try :
    INDENT
        res = 1 / (1 + math.exp(- x))
    DEDENT
    except OverflowError :
    INDENT
        res = 0.0
    DEDENT
    return res
DEDENT

    def test_month_view_paginated(self):
        res = self.client.get('/dates/books/2008/oct/paginated/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context['book_list']),
            list(Book.objects.filter(pubdate__year=2008, pubdate__month=10))
        )
        self.assertEqual(
            list(res.context['object_list']),
            list(Book.objects.filter(pubdate__year=2008, pubdate__month=10))
        )
        self.assertTemplateUsed(res, 'generic_views/book_archive_month.html')

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

def query_yes_no(question, default = True) :
INDENT
    yes_list = ["yes", "y"]
    no_list = ["no", "n"]
    default_dict = {
        None : "[y/n]",
        True : "[Y/n]",
        False : "[y/N]",
        }
    default_str = default_dict [default]
    prompt_str = "%s %s " % (question, default_str)
    while True :
    INDENT
        choice = input_(prompt_str).lower()
        if not choice and default is not None :
        INDENT
            return default
        DEDENT
        if choice in yes_list :
        INDENT
            return True
        DEDENT
        if choice in no_list :
        INDENT
            return False
        DEDENT
        notification_str = "Please respond with 'y' or 'n'"
        print (notification_str)
    DEDENT
DEDENT

def prime(n, a) :
INDENT
    i = a
    while (n % i ! = 0 and i * i < n) :
    INDENT
        i += 1
    DEDENT
    if (i * i < n) :
    INDENT
        return prime(n / i, i)
    DEDENT
    else :
    INDENT
        print ("The highest prime factor is: "), n
    DEDENT
DEDENT

    def test_custom_month_format(self):
        res = self.client.get('/dates/books/2008/10/')
        self.assertEqual(res.status_code, 200)

def change_keys(obj) :
INDENT
    new_obj = obj
    for k in new_obj :
    INDENT
        if hasattr(obj [k], '__getitem__') :
        INDENT
            change_keys(obj [k])
        DEDENT
        if '.' in k :
        INDENT
            obj [k.replace('.', '$')] = obj [k]
            del obj [k]
        DEDENT
    DEDENT
DEDENT

def split(s, n) :
INDENT
    if len(s) < n :
    INDENT
        return []
    DEDENT
    elif len(s) == n :
    INDENT
        return [s]
    DEDENT
    else :
    INDENT
        return split(s [: n], n) + split(s [n :], n)
    DEDENT
DEDENT

def switch(mode) :
INDENT
    switcher = {
        'a' : a,
        'b' : b,
        'ab' : (a, b)}
    try :
    INDENT
        switcher [mode]()
    DEDENT
    except TypeError :
    INDENT
        for fn in switcher [mode] :
        INDENT
            fn()
        DEDENT
    DEDENT
DEDENT

def find(needle, haystack) :
INDENT
    if needle == haystack : return []
    if isinstance(haystack, str) and len(haystack) < = 1 : return None
    try :
    INDENT
        for i, e in enumerate(haystack) :
        INDENT
            r = find(needle, e)
            if r is not None :
            INDENT
                r.insert(0, i)
                return r
            DEDENT
        DEDENT
    DEDENT
    except TypeError :
    INDENT
        pass
    DEDENT
    return None
DEDENT

    def test_month_view_invalid_pattern(self):
        res = self.client.get('/dates/books/2007/no_month/')
        self.assertEqual(res.status_code, 404)

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

def mssl(x) :
INDENT
    max_ending_here = max_so_far = 0
    for a in x :
    INDENT
        max_ending_here = max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
    DEDENT
    return max_so_far
DEDENT

def on_success(self, data) :
INDENT
    print data ['text']
    with open('scratch1.json', 'ab') as outfile :
    INDENT
        json.dump(data, outfile, indent = 4)
    DEDENT
    with open('scratch2.json', 'ab') as xoutfile :
    INDENT
        json.dump(data, xoutfile, indent = 4)
    DEDENT
    return
DEDENT

def two_powers(num) :
INDENT
    if num < (1 < < 8) :
    INDENT
        num_bits = 8
    DEDENT
    elif num < (1 < < 16) :
    INDENT
        num_bits = 16
    DEDENT
    elif num < (1 < < 24) :
    INDENT
        num_bits = 24
    DEDENT
    elif num < (1 < < 32) :
    INDENT
        num_bits = 32
    DEDENT
    else :
    INDENT
        num_bits = math.floor(math.log2(num)) + 1
    DEDENT
    return [1 < < p for p in range(num_bits) if num & (1 < < p)]
DEDENT

def repeat(a, n) :
INDENT
    def rep(a, c) :
    INDENT
        if c > 0 :
        INDENT
            print (a)
            rep(a, c - 1)
        DEDENT
    DEDENT
    return rep(a * n, n)
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

    def test_previous_month_without_content(self):
        "Content can exist on any day of the previous month. Refs #14711"
        self.pubdate_list = [
            datetime.date(2010, month, day)
            for month, day in ((9, 1), (10, 2), (11, 3))
        ]
        for pubdate in self.pubdate_list:
            name = str(pubdate)
            Book.objects.create(name=name, slug=name, pages=100, pubdate=pubdate)

        res = self.client.get('/dates/books/2010/nov/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['previous_month'], datetime.date(2010, 10, 1))
        # The following test demonstrates the bug
        res = self.client.get('/dates/books/2010/nov/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['previous_month'], datetime.date(2010, 10, 1))
        # The bug does not occur here because a Book with pubdate of Sep 1 exists
        res = self.client.get('/dates/books/2010/oct/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['previous_month'], datetime.date(2010, 9, 1))

def getPrint(func, * args, ** kwds) :
INDENT
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try :
    INDENT
        func(* args, ** kwds)
    DEDENT
    except :
    INDENT
        raise
    DEDENT
    else :
    INDENT
        return sys.stdout.getvalue()
    DEDENT
    finally :
    INDENT
        sys.stdout = old_stdout
    DEDENT
DEDENT

def calculate_speed(radius) :
INDENT
    global speeds, speed_idx
    t1 = time.time()
    speeds [speed_idx] = radius / (t1 - t0)
    print (sum(speeds) / iterations, 'mm/sek')
    speed_idx += 1
    speed_idx %= iterations
DEDENT

def __call__(self, parser, args, values, option_string = None) :
INDENT
    if values is None :
    INDENT
        self.values += 1
    DEDENT
    else :
    INDENT
        try :
        INDENT
            self.values = int(values)
        DEDENT
        except ValueError :
        INDENT
            self.values = values.count('v') + 1
        DEDENT
    DEDENT
    setattr(args, self.dest, self.values)
DEDENT

def on_click(event, i, j) :
INDENT
    global player
    board [i] [j] ['bg'] = player
    for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)) :
    INDENT
        if ii < 0 or ii > = rows or jj < 0 or jj > = cols : continue
        neighbor = board [ii] [jj]
        if neighbor ['bg'] ! = 'grey' and (ii, jj) ! = (i, j) :
        INDENT
            neighbor ['bg'] = other [neighbor ['bg']]
        DEDENT
    DEDENT
    check_for_winner()
    player = other [player]
DEDENT

def count(l) :
INDENT
    total = 0
    result = []
    for val in l :
    INDENT
        total += val
        result.append(total)
    DEDENT
    return result
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

def execute(command) :
INDENT
    process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    while True :
    INDENT
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None :
        INDENT
            break
        DEDENT
        sys.stdout.write(nextline)
        sys.stdout.flush()
    DEDENT
    output = process.communicate() [0]
    exitCode = process.returncode
    if (exitCode == 0) :
    INDENT
        return output
    DEDENT
    else :
    INDENT
        raise ProcessException(command, exitCode, output)
    DEDENT
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

def some_function(eggs) :
INDENT
    error_code = 0
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
        do_error()
        error_code = 1
    DEDENT
    if error_code == 0 :
    INDENT
        do_something_4()
        do_something_5()
        do_something_6()
    DEDENT
    return
DEDENT

    def test_datetime_month_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 2, 1, 12, 0))
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        BookSigning.objects.create(event_date=datetime.datetime(2008, 6, 3, 12, 0))
        res = self.client.get('/dates/booksignings/2008/apr/')
        self.assertEqual(res.status_code, 200)

def numPens(n) :
INDENT
    if n < 0 :
    INDENT
        return False
    DEDENT
    if n == 0 :
    INDENT
        return True
    DEDENT
    for x in (24, 8, 5) :
    INDENT
        if numPens(n - x) :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def ask_digit() :
INDENT
    while True :
    INDENT
        digit = raw_input("Please enter a number between 1 and 5: ")
        if re.match(r"[1-5]$", digit) :
        INDENT
            return int(digit)
        DEDENT
    DEDENT
DEDENT

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

def __init__(self) :
INDENT
    super(Dialog, self).__init__()
    layout = QtGui.QVBoxLayout()
    self.setLayout(layout)
    list_widget = QtGui.QListWidget()
    layout.addWidget(list_widget)
    gripper = Grip(self, list_widget)
    layout.addWidget(QtGui.QLabel("Test"))
    self.setGeometry(200, 500, 200, 500)
DEDENT

    def test_month_view_get_month_from_request(self):
        oct1 = datetime.date(2008, 10, 1)
        res = self.client.get('/dates/books/without_month/2008/?month=oct')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/book_archive_month.html')
        self.assertEqual(list(res.context['date_list']), [oct1])
        self.assertEqual(list(res.context['book_list']), list(Book.objects.filter(pubdate=oct1)))
        self.assertEqual(res.context['month'], oct1)

def group() :
INDENT
    import numpy as np
    values = np.array(np.random.randint(0, 1 < < 32, size = 35000000), dtype = 'u4')
    values.sort()
    l = np.dstack((values, values.searchsorted(values, side = 'right') - values.searchsorted(values, side = 'left')))
    index = np.fromiter(l, dtype = 'u4,u2')
DEDENT

def __eq__(self, other) :
INDENT
    if not isinstance(other, FrozenDict) :
    INDENT
        return dict(self.iteritems()) == other
    DEDENT
    if len(self) ! = len(other) :
    INDENT
        return False
    DEDENT
    for key, value in self.iteritems() :
    INDENT
        try :
        INDENT
            if value ! = other [key] :
            INDENT
                return False
            DEDENT
        DEDENT
        except KeyError :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def paren(n, known = {}) :
INDENT
    if n in known :
    INDENT
        return known [n]
    DEDENT
    ps = set(['(' * n + ')' * n])
    for i in range(1, n) :
    INDENT
        for f in paren(i, known) :
        INDENT
            for s in paren(n - i, known) :
            INDENT
                ps.add(f + s)
            DEDENT
        DEDENT
    DEDENT
    known [n] = ps
    return ps
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

    def test_month_view_without_month_in_url(self):
        res = self.client.get('/dates/books/without_month/2008/')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.context['exception'], 'No month specified')

def __new__(klass, ** slots) :
INDENT
    klass.__slots__ = []
    for k in slots :
    INDENT
        klass.__slots__.append(k)
    DEDENT
    return super(MySlottedClassBA, klass).__new__(klass)
DEDENT

def __new__(metacls, cls, bases, classdict) :
INDENT
    if type(classdict) is dict :
    INDENT
        original_dict = classdict
        classdict = _EnumDict()
        for k, v in original_dict.items() :
        INDENT
            classdict [k] = v
        DEDENT
    DEDENT
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

def next_bigger(a) :
INDENT
    a = map(int, str(a))
    tmp = list(reversed(a))
    for i, item_a in enumerate(reversed(a)) :
    INDENT
        for j in (range(i)) :
        INDENT
            if item_a < tmp [j] :
            INDENT
                tmp [i] = tmp [j]
                print (list(reversed(tmp [i :])))
                tmp [j] = item_a
                fin = list(reversed(tmp [i :])) + sorted(tmp [: i])
                return functools.reduce(lambda x, y : x * 10 + y, fin)
            DEDENT
        DEDENT
    DEDENT
    return - 1
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

    @skipUnlessDBFeature('has_zoneinfo_database')
    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_month_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 2, 1, 12, 0, tzinfo=timezone.utc))
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        BookSigning.objects.create(event_date=datetime.datetime(2008, 6, 3, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/2008/apr/')
        self.assertEqual(res.status_code, 200)

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

def run(self) :
INDENT
    while True :
    INDENT
        try :
        INDENT
            signature = self.transport.recv()
        DEDENT
        except EOFError :
        INDENT
            break
        DEDENT
        else :
        INDENT
            self._emit(* signature)
        DEDENT
    DEDENT
DEDENT

def __next__(self) :
INDENT
    if self.state == 10 :
    INDENT
        raise StopIteration
    DEDENT
    self.state += 1
    return self.state - 1
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

def reverseParentheses(s) :
INDENT
    if s.find('(') == - 1 :
    INDENT
        return s
    DEDENT
    if s.find('(') < s.find(')') :
    INDENT
        beg, end = s.find('('), s.rfind(')')
    DEDENT
    else :
    INDENT
        beg, end = s.find(')'), s.rfind('(')
    DEDENT
    return s [: beg] + reverseParentheses(s [beg + 1 : end] [: : - 1]) + s [end + 1 :]
DEDENT

    def test_date_list_order(self):
        """date_list should be sorted ascending in month view"""
        _make_books(10, base_date=datetime.date(2011, 12, 25))
        res = self.client.get('/dates/books/2011/dec/')
        self.assertEqual(list(res.context['date_list']), list(sorted(res.context['date_list'])))


def main(data) :
INDENT
    data_writer = csv.writer(f2)
    for row in data :
    INDENT
        update_header_dict(row)
        data_writer.writerow(get_row_data_dict(row))
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

def create_response(self, request, data, response_class = HttpResponse, ** response_kwargs) :
INDENT
    try :
    INDENT
        stripped_data = data.get('objects')
    DEDENT
    except AttributeError :
    INDENT
        stripped_data = data
    DEDENT
    desired_format = self.determine_format(request)
    serialized = self.serialize(request, stripped_data, desired_format)
    response = response_class(content = serialized,
        content_type = build_content_type(desired_format),
        ** response_kwargs)
    try :
    INDENT
        for name, value in data.get('meta', {}).items() :
        INDENT
            response ['Meta-' + name.title().replace('_', '-')] = str(value)
        DEDENT
    DEDENT
    except AttributeError :
    INDENT
        response ['Meta-Empty'] = True
    DEDENT
    return response
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class WeekArchiveViewTests(TestDataMixin, TestCase):

    def test_week_view(self):
        res = self.client.get('/dates/books/2008/week/39/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/book_archive_week.html')
        self.assertEqual(res.context['book_list'][0], Book.objects.get(pubdate=datetime.date(2008, 10, 1)))
        self.assertEqual(res.context['week'], datetime.date(2008, 9, 28))

        # Since allow_empty=False, next/prev weeks must be valid
        self.assertIsNone(res.context['next_week'])
        self.assertEqual(res.context['previous_week'], datetime.date(2006, 4, 30))

def save(self, * args, ** kwargs) :
INDENT
    imageTemproary = Image.open(self.uploadedImage)
    outputIoStream = BytesIO()
    imageTemproaryResized = imageTemproary.resize((1020, 573))
    imageTemproaryResized.save(outputIoStream, format = 'JPEG', quality = 85)
    outputIoStream.seek(0)
    self.uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.uploadedImage.name.split('.') [0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    super(ImageUpload, self).save(* args, ** kwargs)
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

def froze_it(cls) :
INDENT
    cls.__frozen = False
    def frozensetattr(self, key, value) :
    INDENT
        if self.__frozen and not hasattr(self, key) :
        INDENT
            print ("Class {} is frozen. Cannot set {} = {}"
                .format(cls.__name__, key, value))
        DEDENT
        else :
        INDENT
            object.__setattr__(self, key, value)
        DEDENT
    DEDENT
    def init_decorator(func) :
    INDENT
        @ wraps(func)
        def wrapper(self, * args, ** kwargs) :
        INDENT
            func(self, * args, ** kwargs)
            self.__frozen = True
        DEDENT
        return wrapper
    DEDENT
    cls.__setattr__ = frozensetattr
    cls.__init__ = init_decorator(cls.__init__)
    return cls
DEDENT

    def test_week_view_allow_empty(self):
        # allow_empty = False, empty week
        res = self.client.get('/dates/books/2008/week/12/')
        self.assertEqual(res.status_code, 404)

        # allow_empty = True, empty month
        res = self.client.get('/dates/books/2008/week/12/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), [])
        self.assertEqual(res.context['week'], datetime.date(2008, 3, 23))

        # Since allow_empty=True, next/prev are allowed to be empty weeks
        self.assertEqual(res.context['next_week'], datetime.date(2008, 3, 30))
        self.assertEqual(res.context['previous_week'], datetime.date(2008, 3, 16))

        # allow_empty but not allow_future: next_week should be empty
        url = datetime.date.today().strftime('/dates/books/%Y/week/%U/allow_empty/').lower()
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(res.context['next_week'])

def recursiveHalfString(s) :
INDENT
    if s == '' :
    INDENT
        return True
    DEDENT
    if (len(s)) % 2 == 0 :
    INDENT
        if s [0] ! = s [(len(s) / 2)] :
        INDENT
            return False
        DEDENT
        else :
        INDENT
            left = s [1 : len(s) / 2]
            right = s [(len(s) / 2) + 1 : len(s)]
            return recursiveHalfString(left + right)
        DEDENT
    DEDENT
    else :
    INDENT
        return "Error: odd string"
    DEDENT
DEDENT

def __setattr__(self, name, value) :
INDENT
    if name == "x" :
    INDENT
        super(Test, self).__setattr__(name, value)
    DEDENT
    else :
    INDENT
        print "setting attr %s" % name
    DEDENT
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

def decorator(f) :
INDENT
    @ wraps(f)
    def wrapped(* args, ** kargs) :
    INDENT
        result = f(* args, ** kargs)
        event.fire(* args, ** kargs)
        return result
    DEDENT
    return wrapped
DEDENT

    def test_week_view_allow_future(self):
        # January 7th always falls in week 1, given Python's definition of week numbers
        future = datetime.date(datetime.date.today().year + 1, 1, 7)
        future_sunday = future - datetime.timedelta(days=(future.weekday() + 1) % 7)
        b = Book.objects.create(name="The New New Testement", pages=600, pubdate=future)

        res = self.client.get('/dates/books/%s/week/1/' % future.year)
        self.assertEqual(res.status_code, 404)

        res = self.client.get('/dates/books/%s/week/1/allow_future/' % future.year)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), [b])
        self.assertEqual(res.context['week'], future_sunday)

        # Since allow_future = True but not allow_empty, next/prev are not
        # allowed to be empty weeks
        self.assertIsNone(res.context['next_week'])
        self.assertEqual(res.context['previous_week'], datetime.date(2008, 9, 28))

        # allow_future, but not allow_empty, with a current week. So next
        # should be in the future
        res = self.client.get('/dates/books/2008/week/39/allow_future/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['next_week'], future_sunday)
        self.assertEqual(res.context['previous_week'], datetime.date(2006, 4, 30))

def __init__(self, ** kwargs) :
INDENT
    available = set(kwargs)
    derivable = set()
    while True :
    INDENT
        for r in range(1, len(available) + 1) :
        INDENT
            for permutation in itertools.permutations(available, r) :
            INDENT
                if permutation in self.relationships :
                INDENT
                    derivable.add(self.relationships [permutation])
                DEDENT
            DEDENT
        DEDENT
        if derivable.issubset(available) :
        INDENT
            break
        DEDENT
        else :
        INDENT
            available |= derivable
        DEDENT
    DEDENT
    underivable = set(self.relationships.values()) - available
    if len(underivable) > 0 :
    INDENT
        raise TypeError(
            "The following properties cannot be derived:\n\t{0}"
            .format(tuple(underivable)))
    DEDENT
    self._value_dict = kwargs
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

    def test_week_view_paginated(self):
        week_start = datetime.date(2008, 9, 28)
        week_end = week_start + datetime.timedelta(days=7)
        res = self.client.get('/dates/books/2008/week/39/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context['book_list']),
            list(Book.objects.filter(pubdate__gte=week_start, pubdate__lt=week_end))
        )
        self.assertEqual(
            list(res.context['object_list']),
            list(Book.objects.filter(pubdate__gte=week_start, pubdate__lt=week_end))
        )
        self.assertTemplateUsed(res, 'generic_views/book_archive_week.html')

def children(self) :
INDENT
    if self._children_cache is not None :
    INDENT
        return self._children_cache
    DEDENT
    self._children_cache = self.collectChildren()
    return self._children_cache
DEDENT

    def test_week_view_invalid_pattern(self):
        res = self.client.get('/dates/books/2007/week/no_week/')
        self.assertEqual(res.status_code, 404)

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

def matcher(x) :
INDENT
    l = [item for item in physical if item.lower() in x.lower()]
    length = len(l)
    if length == 0 :
    INDENT
        return 'other'
    DEDENT
    elif length == 1 :
    INDENT
        return l [0]
    DEDENT
    else :
    INDENT
        return 'mix'
    DEDENT
DEDENT

def update_document(document, data_dict) :
INDENT
    def field_value(field, value) :
    INDENT
        if field.__class__ in (fields.ListField, fields.SortedListField) :
        INDENT
            return [
                field_value(field.field, item) for item in value
                ]
        DEDENT
        if field.__class__ in (
            fields.EmbeddedDocumentField,
            fields.GenericEmbeddedDocumentField,
            fields.ReferenceField,
            fields.GenericReferenceField) :
        INDENT
            return field.document_type(** value)
        DEDENT
        else :
        INDENT
            return value
        DEDENT
    DEDENT
    [setattr(
            document, key,
            field_value(document._fields [key], value)) for key, value in data_dict.items()]
    return document
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

def __str__(self) :
INDENT
    if self.cards :
    INDENT
        rep = ""
        for card in self.cards :
        INDENT
            rep += str(card) + "\t"
        DEDENT
    DEDENT
    else :
    INDENT
        rep = "<empty>"
    DEDENT
    return rep
DEDENT

def send_mail(send_from, send_to, subject, message, files = [],
server = "localhost", port = 587, username = '', password = '',
use_tls = True) :
INDENT
    msg = MIMEMultipart()
    msg ['From'] = send_from
    msg ['To'] = COMMASPACE.join(send_to)
    msg ['Date'] = formatdate(localtime = True)
    msg ['Subject'] = subject
    msg.attach(MIMEText(message))
    for path in files :
    INDENT
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file :
        INDENT
            part.set_payload(file.read())
        DEDENT
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
            'attachment; filename="{}"'.format(op.basename(path)))
        msg.attach(part)
    DEDENT
    smtp = smtplib.SMTP(server, port)
    if use_tls :
    INDENT
        smtp.starttls()
    DEDENT
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
DEDENT

    def test_week_start_Monday(self):
        # Regression for #14752
        res = self.client.get('/dates/books/2008/week/39/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['week'], datetime.date(2008, 9, 28))

        res = self.client.get('/dates/books/2008/week/39/monday/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['week'], datetime.date(2008, 9, 29))

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

def __init__(self, interval, function, * args, ** kwargs) :
INDENT
    self._timer = None
    self.function = function
    self.interval = interval
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.start()
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

def __init__(self, width = 1024, height = 576, caption = "Pokémon Life and Death: Esploratori del proprio Destino", fps = True, * args, ** kwargs) :
INDENT
    super(main, self).__init__(width, height, * args, ** kwargs)
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()
    self.xDisplay = int(screen.width / 2 - self.width / 2)
    self.yDisplay = int(screen.height / 2 - self.height / 2)
    self.set_location(self.xDisplay, self.yDisplay)
    self.sprites = OrderedDict()
    if fps :
    INDENT
        self.sprites ['fps_label'] = pyglet.text.Label('0 fps', x = 10, y = 10)
        self.last_update = time()
        self.fps_count = 0
    DEDENT
    self.keys = OrderedDict()
    self.mouse_x = 0
    self.mouse_y = 0
    self.alive = 1
DEDENT

def postalValidate(S) :
INDENT
    S = S.replace(" ", "")
    if len(S) ! = 6 or S.isalpha() or S.isdigit() :
    INDENT
        return False
    DEDENT
    if not S [0 : 5 : 2].isalpha() :
    INDENT
        return False
    DEDENT
    if not S [1 : 6 : 2].isdigit() :
    INDENT
        return False
    DEDENT
    return S.upper()
DEDENT

    def test_unknown_week_format(self):
        with self.assertRaisesMessage(ValueError, "Unknown week format '%T'. Choices are: %U, %W"):
            self.client.get('/dates/books/2008/week/39/unknown_week_format/')

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

def transformFactorList(factorList) :
INDENT
    twos = [x for x in factorList if x == 2]
    rest = [x for x in factorList if x ! = 2]
    if twos :
    INDENT
        rest.insert(0, 2 if len(twos) == 1 else "2 ^ %d" % len(twos))
    DEDENT
    return rest
DEDENT

def run(self) :
INDENT
    while True :
    INDENT
        try : line = self.fdRead.readline()
        except IOError, exc :
        INDENT
            if exc.errno == errno.EAGAIN :
            INDENT
                return
            DEDENT
            raise
        DEDENT
        self.__run(line)
    DEDENT
DEDENT

def html_to_text(html) :
INDENT
    "Creates a formatted text email message as a string from a rendered html template (page)"
    soup = BeautifulSoup(html, 'html.parser')
    body, text = soup.body, []
    for element in body.descendants :
    INDENT
        if type(element) == NavigableString :
        INDENT
            if element.parent.name in ('script', 'style') :
            INDENT
                continue
            DEDENT
            string = ' '.join(element.string.split())
            if string :
            INDENT
                if element.parent.name == 'a' :
                INDENT
                    a_tag = element.parent
                    string = a_tag ['href']
                    if (type(a_tag.previous_sibling) == NavigableString and
                        a_tag.previous_sibling.string.strip()) :
                    INDENT
                        text [- 1] = text [- 1] + ' ' + string
                        continue
                    DEDENT
                DEDENT
                elif element.previous_sibling and element.previous_sibling.name == 'a' :
                INDENT
                    text [- 1] = text [- 1] + ' ' + string
                    continue
                DEDENT
                elif element.parent.name == 'p' :
                INDENT
                    string = '\n' + string
                DEDENT
                text += [string]
            DEDENT
        DEDENT
    DEDENT
    doc = '\n'.join(text)
    return doc
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

    def test_datetime_week_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        res = self.client.get('/dates/booksignings/2008/week/13/')
        self.assertEqual(res.status_code, 200)

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

def square(x = None) :
INDENT
    try :
    INDENT
        return float(x) ** 2
    DEDENT
    except TypeError :
    INDENT
        print "You did not enter a real number"
        return None
    DEDENT
DEDENT

def _get_modules_from_db(dictionary) :
INDENT
    leaves = []
    for k, v in dictionary.iteritems() :
    INDENT
        if (isinstance(v, dict) and
            not sorted(v.keys()) == ['path_to_file', 'sha512sum']) :
        INDENT
            leaves.extend(_get_modules_from_db(v))
        DEDENT
        else :
        INDENT
            leaves.append(v)
        DEDENT
    DEDENT
    return leaves
DEDENT

def matched(str) :
INDENT
    diffCounter = 0
    length = len(str)
    for i in range(length) :
    INDENT
        if str [i] == '(' :
        INDENT
            diffCounter += 1
        DEDENT
        elif str [i] == ')' :
        INDENT
            diffCounter -= 1
        DEDENT
    DEDENT
    if diffCounter == 0 :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
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

    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_week_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/2008/week/13/')
        self.assertEqual(res.status_code, 200)


def NumRange(a, x, y) :
INDENT
    hd, tl = a [0], a [1 :]
    if tl == [] :
    INDENT
        return 1 if hd > = x and hd < = y else 0
    DEDENT
    else :
    INDENT
        return (1 if hd > = x and hd < = y else 0) + NumRange(tl, x, y)
    DEDENT
DEDENT

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

def __enter__(self) :
INDENT
    if self.level is not None :
    INDENT
        self.old_level = self.logger.level
        self.logger.setLevel(self.level)
    DEDENT
    if self.handler :
    INDENT
        self.logger.addHandler(self.handler)
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

def __init__(self) :
INDENT
    super().__init__()
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(widget)
    start_btn = QtWidgets.QPushButton('Start')
    start_btn.clicked.connect(self.start)
    layout.addWidget(start_btn)
    self.setCentralWidget(widget)
    self.log_dialog = LogDialog()
    self.running = False
    handler = LogHandler()
    handler.emitter.sigLog.connect(self.log_dialog.log_txt.appendPlainText)
    self.q = multiprocessing.Queue()
    self.ql = QueueListener(self.q, handler)
    self.ql.start()
    self.main_log = logging.getLogger('main')
    self.main_log.propagate = False
    self.main_log.setLevel(logging.INFO)
    self.main_log.addHandler(QueueHandler(self.q))
    self.pool = multiprocessing.Pool(1, worker_init, [self.q])
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class DayArchiveViewTests(TestDataMixin, TestCase):

    def test_day_view(self):
        res = self.client.get('/dates/books/2008/oct/01/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/book_archive_day.html')
        self.assertEqual(list(res.context['book_list']),
                         list(Book.objects.filter(pubdate=datetime.date(2008, 10, 1))))
        self.assertEqual(res.context['day'], datetime.date(2008, 10, 1))

        # Since allow_empty=False, next/prev days must be valid.
        self.assertIsNone(res.context['next_day'])
        self.assertEqual(res.context['previous_day'], datetime.date(2006, 5, 1))

def compress(factors) :
INDENT
    for (factor, copies) in itertools.groupby(factors) :
    INDENT
        power = len(list(copies))
        yield (factor, power)
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

def future6(A) :
INDENT
    known = []
    result = []
    for idx in xrange(len(A) - 1, - 1, - 1) :
    INDENT
        value = A [idx]
        known = [(x, y) for x, y in known if y > value]
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

    def test_day_view_allow_empty(self):
        # allow_empty = False, empty month
        res = self.client.get('/dates/books/2000/jan/1/')
        self.assertEqual(res.status_code, 404)

        # allow_empty = True, empty month
        res = self.client.get('/dates/books/2000/jan/1/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), [])
        self.assertEqual(res.context['day'], datetime.date(2000, 1, 1))

        # Since it's allow empty, next/prev are allowed to be empty months (#7164)
        self.assertEqual(res.context['next_day'], datetime.date(2000, 1, 2))
        self.assertEqual(res.context['previous_day'], datetime.date(1999, 12, 31))

        # allow_empty but not allow_future: next_month should be empty (#7164)
        url = datetime.date.today().strftime('/dates/books/%Y/%b/%d/allow_empty/').lower()
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertIsNone(res.context['next_day'])

def wrapper(* a, ** ka) :
INDENT
    with open(os.devnull, 'w') as devnull :
    INDENT
        with contextlib.redirect_stdout(devnull) :
        INDENT
            func(* a, ** ka)
        DEDENT
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

    def test_day_view_allow_future(self):
        future = (datetime.date.today() + datetime.timedelta(days=60))
        urlbit = future.strftime('%Y/%b/%d').lower()
        b = Book.objects.create(name="The New New Testement", pages=600, pubdate=future)

        # allow_future = False, future month
        res = self.client.get('/dates/books/%s/' % urlbit)
        self.assertEqual(res.status_code, 404)

        # allow_future = True, valid future month
        res = self.client.get('/dates/books/%s/allow_future/' % urlbit)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['book_list']), [b])
        self.assertEqual(res.context['day'], future)

        # allow_future but not allow_empty, next/prev must be valid
        self.assertIsNone(res.context['next_day'])
        self.assertEqual(res.context['previous_day'], datetime.date(2008, 10, 1))

        # allow_future, but not allow_empty, with a current month.
        res = self.client.get('/dates/books/2008/oct/01/allow_future/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['next_day'], future)
        self.assertEqual(res.context['previous_day'], datetime.date(2006, 5, 1))

        # allow_future for yesterday, next_day is today (#17192)
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        res = self.client.get('/dates/books/%s/allow_empty_and_future/'
                              % yesterday.strftime('%Y/%b/%d').lower())
        self.assertEqual(res.context['next_day'], today)

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

    def test_day_view_paginated(self):
        res = self.client.get('/dates/books/2008/oct/1/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context['book_list']),
            list(Book.objects.filter(pubdate__year=2008, pubdate__month=10, pubdate__day=1))
        )
        self.assertEqual(
            list(res.context['object_list']),
            list(Book.objects.filter(pubdate__year=2008, pubdate__month=10, pubdate__day=1))
        )
        self.assertTemplateUsed(res, 'generic_views/book_archive_day.html')

def __init__(self, t) :
INDENT
    self.width = 320
    self.height = 200
    self.i = Tkinter.PhotoImage(width = self.width, height = self.height)
    rgb_colors = ([random.randint(0, 255) for i in range(0, 3)] for j in range(0, self.width * self.height))
    pixels = " ".join(("{" + " ".join(('#%02x%02x%02x' %
                    tuple(next(rgb_colors)) for i in range(self.width))) + "}" for j in range(self.height)))
    self.i.put(pixels, (0, 0, self.width - 1, self.height - 1))
    c = Tkinter.Canvas(t, width = self.width, height = self.height); c.pack()
    c.create_image(0, 0, image = self.i, anchor = Tkinter.NW)
DEDENT

def __init__(self, parent = None) :
INDENT
    super(AppRemovalPage, self).__init__(parent = parent)
    self.setTitle('Apps to Remove')
    self.setSubTitle('Listview')
    self.list_view = QtGui.QListView(self)
    self.list_view.setMinimumSize(465, 200)
    layout = QtGui.QVBoxLayout(self)
    layout.addWidget(self.list_view)
    self.setLayout(layout)
    self.items = []
    self.isWritten = False
    loo = "/home/test1/file.txt"
    self.model = QtGui.QStandardItemModel(self.list_view)
    self.model.itemChanged.connect(self.setItems)
    file = QtCore.QFile(loo)
    if file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text) :
    INDENT
        while not file.atEnd() :
        INDENT
            line = bytearray(file.readLine()).decode().strip()
            item = QtGui.QStandardItem(line)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.model.appendRow(item)
        DEDENT
    DEDENT
    self.list_view.setModel(self.model)
    self.list_view.show()
DEDENT

def sub_seq(li, n) :
INDENT
    res = defaultdict(list)
    for k, g in groupby(enumerate(li), itemgetter(1)) :
    INDENT
        l = list(map(itemgetter(0), g))
        if n < = len(l) : res [k] += l [0 : len(l) - n + 1]
    DEDENT
    return res
DEDENT

def __init__(self) :
INDENT
    self.queue = Queue.Queue()
    self.gui = GuiPart(self.queue, self.endApplication)
    self.gui.show()
    self.timer = qt.QTimer()
    qt.QObject.connect(self.timer,
        qt.SIGNAL("timeout()"),
        self.periodicCall)
    self.timer.start(100)
    self.running = 1
    self.thread1 = threading.Thread(target = self.workerThread1)
    self.thread1.start()
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

def run(self) :
INDENT
    print '>>>> check driver ok but not ensure driver quit'
    driver, ok = self.driverfactory()
    if ok :
    INDENT
        self.dostuff(driver)
    DEDENT
    else :
    INDENT
        print 'skip because driver not ok'
    DEDENT
    driver.quit()
DEDENT

def calculate_tax(people) :
INDENT
    while True :
    INDENT
        try :
        INDENT
            iterating_people = people.keys()
            for key in iterating_people :
            INDENT
                earning = people [key]
                if earning < = 1000 :
                INDENT
                    people [key] = 0
                DEDENT
                elif earning in range(1001, 10001) :
                INDENT
                    tax1 = 0 * 1000
                    tax2 = 0.1 * (earning - 1000)
                    total_tax = tax1 + tax2
                    people [key] = total_tax
                DEDENT
                elif earning in range(10001, 20201) :
                INDENT
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * (earning - 10000)
                    total_tax = tax1 + tax2 + tax3
                    people [key] = total_tax
                DEDENT
                elif earning in range(20201, 30751) :
                INDENT
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.20 * (earning - 20200)
                    total_tax = tax1 + tax2 + tax3 + tax4
                    people [key] = total_tax
                DEDENT
                elif earning in range(30751, 50001) :
                INDENT
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.20 * 10550
                    tax5 = 0.25 * (earning - 30750)
                    total_tax = tax1 + tax2 + tax3 + tax4 + tax5
                    people [key] = total_tax
                DEDENT
                elif earning > 50000 :
                INDENT
                    tax1 = 0 * 1000
                    tax2 = 0.1 * 9000
                    tax3 = 0.15 * 10200
                    tax4 = 0.20 * 10550
                    tax5 = 0.25 * 19250
                    tax6 = 0.3 * (earning - 50000)
                    total_tax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6
                    people [key] = total_tax
                DEDENT
            DEDENT
            return people
            break
        DEDENT
        except (AttributeError, TypeError) :
        INDENT
            raise ValueError('The provided input is not a dictionary')
        DEDENT
    DEDENT
DEDENT

    def test_next_prev_context(self):
        res = self.client.get('/dates/books/2008/oct/01/')
        self.assertEqual(res.content, b"Archive for Oct. 1, 2008. Previous day is May 1, 2006\n")

def problem(n) :
INDENT
    myList = []
    for i in xrange(1, int(n ** 0.5 + 1)) :
    INDENT
        if n % i == 0 :
        INDENT
            if (i ! = n / i) :
            INDENT
                myList.append(i)
                myList.append(n / i)
            DEDENT
            else :
            INDENT
                myList.append(i)
            DEDENT
        DEDENT
    DEDENT
    return myList
DEDENT

def sierpinski(a, t, size) :
INDENT
    if a == 0 :
    INDENT
        for i in range(3) :
        INDENT
            t.forward(size)
            t.left(120)
        DEDENT
    DEDENT
    else :
    INDENT
        sierpinski(a - 1, t, size / 2)
        t.forward(size / 2)
        sierpinski(a - 1, t, size / 2)
        t.forward(size / 2)
        t.left(120)
        t.forward(size / 2)
        sierpinski(a - 1, t, size / 2)
        t.forward(size / 2)
        t.left(120)
        t.forward(size)
        t.left(120)
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

    def test_custom_month_format(self):
        res = self.client.get('/dates/books/2008/10/01/')
        self.assertEqual(res.status_code, 200)

def breakdown(a) :
INDENT
    y = []
    q = len(a)
    while q > 0 :
    INDENT
        y += [list(a)]
        a.pop()
        q -= 1
    DEDENT
    return y
DEDENT

def biggest() :
INDENT
    big_x, big_y, max_seen, prod = 0, 0, 0, 0
    for r in xrange(maxFactor, minFactor - 1, - 1) :
    INDENT
        if r * r < max_seen : break
        for i in xrange(0, maxFactor - r + 1) :
        INDENT
            prod = (r + i) * (r - i)
            if prod < max_seen : break
            if is_palindrome(prod) :
            INDENT
                big_x, big_y, max_seen = r + i, r - i, prod
            DEDENT
        DEDENT
        for i in xrange(0, maxFactor - r + 1) :
        INDENT
            prod = (r + i) * (r - i - 1)
            if prod < max_seen : break
            if is_palindrome(prod) :
            INDENT
                big_x, big_y, max_seen = r + i, r - i - 1, prod
            DEDENT
        DEDENT
    DEDENT
    return big_x, big_y, max_seen
DEDENT

def sublistExists(list, sublist) :
INDENT
    for i in range(len(list) - len(sublist) + 1) :
    INDENT
        if sublist == list [i : i + len(sublist)] :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
DEDENT

def to_string(my_list, delimiter) :
INDENT
    string = ''
    if my_list :
    INDENT
        string = my_list [0]
        for elem in my_list [1 :] :
        INDENT
            string += delimiter + str(elem)
        DEDENT
    DEDENT
    return my_list, string
DEDENT

def linear_merge(list1, list2) :
INDENT
    merged_list = []
    i = 0
    j = 0
    try :
    INDENT
        while True :
        INDENT
            if list1 [i] < = list2 [j] :
            INDENT
                merged_list.append(list1 [i])
                i += 1
            DEDENT
            else :
            INDENT
                merged_list.append(list2 [j])
                j += 1
            DEDENT
        DEDENT
    DEDENT
    except IndexError :
    INDENT
        if i == len(list1) :
        INDENT
            merged_list.extend(list2 [j :])
        DEDENT
        if j == len(list2) :
        INDENT
            merged_list.extend(list1 [i :])
        DEDENT
    DEDENT
    return merged_list
DEDENT

def my_function(lst) :
INDENT
    items = (lst [i : i + 3] for i in xrange(0, len(lst), 3))
    for group in items :
    INDENT
        yield group [0] * 10
        yield group [1]
        yield 'foo' + group [2]
    DEDENT
DEDENT

def time_overlap_projected_graph_parallel(bi, nodes) :
INDENT
    uni = nx.MultiGraph()
    for u in nodes :
    INDENT
        uni.add_node(u)
        u_adj = bi.adj [u]
        for (w, uw_attr) in u_adj.iteritems() :
        INDENT
            w_adj = bi.adj [w]
            for (v, wv_attr) in w_adj.iteritems() :
            INDENT
                if v == u :
                INDENT
                    continue
                DEDENT
                elif uni.has_edge(u, v) :
                INDENT
                    continue
                DEDENT
                for uspell in uw_attr.itervalues() :
                INDENT
                    ustart = uspell [1]
                    uend = uspell [2]
                    for vspell in wv_attr.itervalues() :
                    INDENT
                        vstart = vspell [1]
                        vend = vspell [2]
                        if uend > vstart and vend > ustart :
                        INDENT
                            ostart = max(ustart, vstart)
                            oend = min(uend, vend)
                            olen = (oend - ostart + 1) / 86400
                            ocell = w
                            uni.add_edge(u, v, ** {0 : olen, 1 : ostart, 2 : oend, 3 : ocell})
                        DEDENT
                    DEDENT
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return uni
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

def is_prime(x) :
INDENT
    if x < 2 :
    INDENT
        return False
    DEDENT
    for n in range(2, (x) - 1) :
    INDENT
        if x % n == 0 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

    def test_day_view_invalid_pattern(self):
        res = self.client.get('/dates/books/2007/oct/no_day/')
        self.assertEqual(res.status_code, 404)

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

def count_chars(p) :
INDENT
    indx = collections.Counter()
    with open(p) as f :
    INDENT
        for line in f :
        INDENT
            for c in line :
            INDENT
                indx [c] += 1
            DEDENT
        DEDENT
    DEDENT
    print indx
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

    def test_today_view(self):
        res = self.client.get('/dates/books/today/')
        self.assertEqual(res.status_code, 404)
        res = self.client.get('/dates/books/today/allow_empty/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['day'], datetime.date.today())

def get_with_default(colour, colours, default) :
INDENT
    search = (d for d in colours if d ['color'] in (colour, default))
    match_or_default = next(search)
    if match_or_default ['color'] ! = default or default == colour :
    INDENT
        return match_or_default
    DEDENT
    return next(search, match_or_default)
DEDENT

def fib(n) :
INDENT
    if (n == 0) :
    INDENT
        return (0, 1)
    DEDENT
    elif (n == 1) :
    INDENT
        return (1, 1)
    DEDENT
    else :
    INDENT
        a, b = fib(n - 1)
        return (b, a + b)
    DEDENT
DEDENT

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

def __init__(self) :
INDENT
    super().__init__()
    self.title = 'Control Stages'
    self.left = 10
    self.top = 10
    self.width = 320
    self.height = 100
    self.AxesMapping = [0, 1, 2, 3]
    self.initUI()
DEDENT

def split_at_first_false(pred, seq) :
INDENT
    pos = 0
    for item in seq :
    INDENT
        if not pred(item) :
        INDENT
            return seq [: pos], seq [pos :]
        DEDENT
        pos += 1
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

def findError(func) :
INDENT
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
    return wrapper
DEDENT

    def test_datetime_day_view(self):
        BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        res = self.client.get('/dates/booksignings/2008/apr/2/')
        self.assertEqual(res.status_code, 200)

def is_palindrome(word) :
INDENT
    if len(word) < 3 :
    INDENT
        print 'Enter a word with at least three letters'
    DEDENT
    else :
    INDENT
        for letter in range(len(word) / 2) :
        INDENT
            if word [letter] ! = word [- letter - 1] :
            INDENT
                print "This word is not a palindrome"
                return
            DEDENT
        DEDENT
        print "This word is a palindrome"
    DEDENT
DEDENT

def fib(n) :
INDENT
    global call_count
    call_count = call_count + 1
    if n < = 1 :
    INDENT
        return 1
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

def longest(list1) :
INDENT
    l = 0
    if type(list1) is list :
    INDENT
        l = len(list1)
        if l > 0 :
        INDENT
            l = max(l, max(longest(elem) for elem in list1))
        DEDENT
    DEDENT
    return l
DEDENT

def __init__(self, name, childTrees = None) :
INDENT
    self.name = name
    if childTrees is None :
    INDENT
        childTrees = []
    DEDENT
    self.childTrees = childTrees
DEDENT

def change(amount) :
INDENT
    if amount < 24 :
    INDENT
        return [0]
    DEDENT
    assert (amount > = 24)
    if amount == 24 :
    INDENT
        return [5, 5, 7, 7]
    DEDENT
    if amount == 25 :
    INDENT
        return [5, 5, 5, 5, 5]
    DEDENT
    if amount == 26 :
    INDENT
        return [5, 7, 7, 7]
    DEDENT
    if amount > 1000 :
    INDENT
        return [0]
    DEDENT
    coins = change(amount - 5)
    coins.append(5)
    return coins
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

    @requires_tz_support
    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_day_view(self):
        bs = BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/2008/apr/2/')
        self.assertEqual(res.status_code, 200)
        # 2008-04-02T00:00:00+03:00 (beginning of day) > 2008-04-01T22:00:00+00:00 (book signing event date)
        bs.event_date = datetime.datetime(2008, 4, 1, 22, 0, tzinfo=timezone.utc)
        bs.save()
        res = self.client.get('/dates/booksignings/2008/apr/2/')
        self.assertEqual(res.status_code, 200)
        # 2008-04-03T00:00:00+03:00 (end of day) > 2008-04-02T22:00:00+00:00 (book signing event date)
        bs.event_date = datetime.datetime(2008, 4, 2, 22, 0, tzinfo=timezone.utc)
        bs.save()
        res = self.client.get('/dates/booksignings/2008/apr/2/')
        self.assertEqual(res.status_code, 404)


def get_cost(x) :
INDENT
    t_zone = 720
    max_rate = 5.5
    rate = 0.0208
    duration = x ['t1']
    if duration < t_zone :
    INDENT
        if (duration * rate) > = max_rate :
        INDENT
            return max_rate
        DEDENT
        else :
        INDENT
            return (duration * rate)
        DEDENT
    DEDENT
    else :
    INDENT
        if duration > = 720 :
        INDENT
            x = int(duration / 720)
            y = ((duration % 720) * rate)
            if y > = max_rate :
            INDENT
                return ((x * max_rate) + max_rate)
            DEDENT
            else :
            INDENT
                return ((x * max_rate) + y)
            DEDENT
        DEDENT
    DEDENT
DEDENT

def integer(s) :
INDENT
    if isinstance(s, int) :
    INDENT
        return True
    DEDENT
    if isinstance(s, str) :
    INDENT
        for i in s :
        INDENT
            if i in "0123456789" :
            INDENT
                return True
            DEDENT
        DEDENT
    DEDENT
    return False
DEDENT

def encrypt(plain) :
INDENT
    answer = []
    for ch in plain :
    INDENT
        if ord(ch) % 2 == 1 :
        INDENT
            answer.append(pycipher.Affine(7, 6).encipher(ch))
        DEDENT
        else :
        INDENT
            answer.append(pycipher.Affine(3, 0).encipher(ch))
        DEDENT
    DEDENT
    return ''.join(answer)
DEDENT

def run(self) :
INDENT
    t = datetime(* datetime.now().timetuple() [: 5])
    while 1 :
    INDENT
        for e in self.events :
        INDENT
            e.check(t)
        DEDENT
        t += timedelta(minutes = 1)
        n = datetime.now()
        while n < t :
        INDENT
            s = (t - n).seconds + 1
            time.sleep(s)
            n = datetime.now()
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

def __init__(self, parent = None) :
INDENT
    super(MyScrollArea, self).__init__(parent)
    w = QtWidgets.QWidget()
    w.setFixedSize(640, 480)
    self.setWidget(w)
    vScrollBar = CustomScrollBar(QtCore.Qt.Vertical)
    self.setVerticalScrollBar(vScrollBar)
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

def translate_non_alphanumerics(to_translate, translate_to = u'_') :
INDENT
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
    if isinstance(to_translate, unicode) :
    INDENT
        translate_table = dict((ord(char), unicode(translate_to)) for char in not_letters_or_digits)
    DEDENT
    else :
    INDENT
        assert isinstance(to_translate, str)
        translate_table = string.maketrans(not_letters_or_digits,
            translate_to
            * len(not_letters_or_digits))
    DEDENT
    return to_translate.translate(translate_table)
DEDENT

@override_settings(ROOT_URLCONF='generic_views.urls')
class DateDetailViewTests(TestDataMixin, TestCase):

    def test_date_detail_by_pk(self):
        res = self.client.get('/dates/books/2008/oct/01/%s/' % self.book1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.book1)
        self.assertEqual(res.context['book'], self.book1)
        self.assertTemplateUsed(res, 'generic_views/book_detail.html')

def two_pair(ranks) :
INDENT
    newlist = []
    for i in set(ranks) :
    INDENT
        if ranks.count(i) == 2 :
        INDENT
            newlist.append(i)
        DEDENT
    DEDENT
    newlist.sort(reverse = True)
    newlist = tuple(newlist)
    return None if newlist == () else newlist
DEDENT

def mssl(l) :
INDENT
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l) :
    INDENT
        if cur + i > 0 :
        INDENT
            cur += i
        DEDENT
        else :
        INDENT
            cur, curi = 0, ind + 1
        DEDENT
        if cur > best :
        INDENT
            starti, besti, best = curi, ind + 1, cur
        DEDENT
    DEDENT
    return starti, besti, best
DEDENT

def chunks(iterable, n) :
INDENT
    iterable = iter(iterable)
    while True :
    INDENT
        result = []
        for i in range(n) :
        INDENT
            try :
            INDENT
                a = next(iterable)
            DEDENT
            except StopIteration :
            INDENT
                break
            DEDENT
            else :
            INDENT
                result.append(a)
            DEDENT
        DEDENT
        if result :
        INDENT
            yield result
        DEDENT
        else :
        INDENT
            break
        DEDENT
    DEDENT
DEDENT

def __new__(cls, name, bases, dct) :
INDENT
    def generate_test_method() :
    INDENT
        def test_method(self) :
        INDENT
            pass
        DEDENT
        return test_method
    DEDENT
    dct ['test_method'] = generate_test_method()
    return type.__new__(cls, name, bases, dct)
DEDENT

    def test_date_detail_by_slug(self):
        res = self.client.get('/dates/books/2006/may/01/byslug/dreaming-in-code/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['book'], Book.objects.get(slug='dreaming-in-code'))

def micro_world(bacteria, K) :
INDENT
    sarg = [i [0] for i in sorted(enumerate(bacteria), key = lambda x : x [1])]
    sortedbac = [bacteria [i] for i in sarg]
    diff = [j - i for i, j in zip(sortedbac [: - 1], sortedbac [1 :])] + [K + 1]
    idx = [i for i, v in enumerate(diff) if v > K]
    return [bacteria [i] for i in sorted([sarg [i] for i in idx])]
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

def reverseParentheses(s) :
INDENT
    def reverse_interior(m) :
    INDENT
        s = m.group()
        return s [- 2 : 0 : - 1]
    DEDENT
    old = ""
    while old ! = s :
    INDENT
        old = s
        s = re.sub(r'(\([^\(\)]*\))', reverse_interior, s)
    DEDENT
    return s
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

def R(A) :
INDENT
    z = {}
    for i in r :
    INDENT
        if A [i] ! = 0 : continue
        h = {}
        for j in r : h [A [j] if j / 9 == i / 9 or j % 9 == i % 9 or j / 27 == i / 27 and j % 9 / 3 == i % 9 / 3 else 0] = 1
        z [9 - len(h)] = h, i
    DEDENT
    for l, (h, i) in sorted(z.items(), cmp, lambda x : x [0]) :
    INDENT
        for j in s :
        INDENT
            if j not in h :
            INDENT
                A [i] = j
                if R(A) : return A
            DEDENT
        DEDENT
        A [i] = 0; return []
    DEDENT
    return A
DEDENT

    def test_date_detail_custom_month_format(self):
        res = self.client.get('/dates/books/2008/10/01/%s/' % self.book1.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['book'], self.book1)

def parse_name(name) :
INDENT
    fl = name.split()
    first_name = fl [0]
    last_name = ' '.join(fl [1 :])
    if "." in first_name :
    INDENT
        first_initial = first_name
    DEDENT
    else :
    INDENT
        first_initial = first_name [0] + "."
    DEDENT
    return {'FirstName' : first_name, 'FirstInitial' : first_initial, 'LastName' : last_name}
DEDENT

def remove_element(value, array) :
INDENT
    reading_idx = writing_idx = 0
    while reading_idx < len(array) :
    INDENT
        if array [reading_idx] ! = value :
        INDENT
            array [writing_idx] = array [reading_idx]
            writing_idx += 1
        DEDENT
        reading_idx += 1
    DEDENT
    while writing_idx < len(array) :
    INDENT
        array [writing_idx] = None
        writing_idx += 1
    DEDENT
DEDENT

def wordsInListsCounter(stringList) :
INDENT
    elements = []
    for element in stringList :
    INDENT
        if len(element) < = threshold :
        INDENT
            elements.append(element)
        DEDENT
    DEDENT
    return elements
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

    def test_date_detail_allow_future(self):
        future = (datetime.date.today() + datetime.timedelta(days=60))
        urlbit = future.strftime('%Y/%b/%d').lower()
        b = Book.objects.create(name="The New New Testement", slug="new-new", pages=600, pubdate=future)

        res = self.client.get('/dates/books/%s/new-new/' % urlbit)
        self.assertEqual(res.status_code, 404)

        res = self.client.get('/dates/books/%s/%s/allow_future/' % (urlbit, b.id))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['book'], b)
        self.assertTemplateUsed(res, 'generic_views/book_detail.html')

def countSubStringMatchRecursive(target, key, count = 0) :
INDENT
    index = target.find(key)
    if index > = 0 :
    INDENT
        count += 1
        target = target [index + len(key) :]
        count = countSubStringMatchRecursive(target, key, count)
    DEDENT
    return count
DEDENT

def json_debug_handler(obj) :
INDENT
    print ("object received:")
    print (type(obj))
    print ("\n\n")
    if isinstance(obj, datetime.datetime) :
    INDENT
        return obj.isoformat()
    DEDENT
    elif isinstance(obj, MStuff) :
    INDENT
        attrs = {}
        for key in obj.__dict__ :
        INDENT
            if not (key.startswith("_") or key == "content") :
            INDENT
                attrs [key] = obj.__dict__ [key]
            DEDENT
        DEDENT
        return {'orig' : obj.content, 'attrs' : attrs}
    DEDENT
    else :
    INDENT
        return None
    DEDENT
DEDENT

    def test_year_out_of_range(self):
        urls = [
            '/dates/books/9999/',
            '/dates/books/9999/12/',
            '/dates/books/9999/week/52/',
        ]
        for url in urls:
            with self.subTest(url=url):
                res = self.client.get(url)
                self.assertEqual(res.status_code, 404)
                self.assertEqual(res.context['exception'], 'Date out of range')

def get_value(d, ks) :
INDENT
    for k in ks :
    INDENT
        try :
        INDENT
            d = d [k]
        DEDENT
        except (KeyError, TypeError) :
        INDENT
            return 0
        DEDENT
    DEDENT
    return d
DEDENT

def flatten(items) :
INDENT
    for x in items :
    INDENT
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)) :
        INDENT
            for sub_x in flatten(x) :
            INDENT
                yield sub_x
            DEDENT
        DEDENT
        else :
        INDENT
            yield x
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

def getPrimes(n) :
INDENT
    yield 2
    i = 1
    while i < = n - 2 :
    INDENT
        i += 2
        if isprime(i) :
        INDENT
            yield i
        DEDENT
    DEDENT
DEDENT

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

def __init__(self, parent = None) :
INDENT
    super(MyScrollArea, self).__init__(parent)
    w = QtWidgets.QWidget()
    w.setFixedSize(640, 480)
    self.setWidget(w)
    vScrollBar = CustomScrollBar(QtCore.Qt.Vertical)
    self.setVerticalScrollBar(vScrollBar)
DEDENT

def __init__(self, * args, ** kwargs) :
INDENT
    ttk.Frame.__init__(self, * args, ** kwargs)
    self.columnconfigure(0, weight = 1)
    self.columnconfigure(1, weight = 0)
    self.rowconfigure(0, weight = 1)
    self.scrollbar = Scrollbar(self)
    self.scrollbar.grid(row = 0, column = 1, sticky = (N, S, E))
    self.text = Text(self, yscrollcommand = self.scrollbar.set)
    self.text.grid(row = 0, column = 0, sticky = (N, S, E, W))
    self.scrollbar.config(command = self.text.yview)
    self.logging_handler = LoggingHandlerFrame.Handler(self.text)
DEDENT

def __init__(self, parent) :
INDENT
    tk.Frame.__init__(self, parent)
    self.textvar = tk.StringVar()
    self.textvar.set("Hello, world!")
    self.entry = tk.Entry(self, textvariable = self.textvar)
    self.text = TextWithVar(self, textvariable = self.textvar,
        borderwidth = 1, relief = "sunken",
        background = "bisque")
    self.entry.pack(side = "top", fill = "x", expand = True)
    self.text.pack(side = "top", fill = "both", expand = True)
DEDENT

def summary(xs) :
INDENT
    for item in xs :
    INDENT
        s = 0
        for value in item :
        INDENT
            s += value ** 2
        DEDENT
        print (s)
    DEDENT
DEDENT

    def test_invalid_url(self):
        msg = (
            'Generic detail view BookDetail must be called with either an '
            'object pk or a slug in the URLconf.'
        )
        with self.assertRaisesMessage(AttributeError, msg):
            self.client.get("/dates/books/2008/oct/01/nopk/")

def unique_file(input_filename, output_filename) :
INDENT
    file = open(input_filename, "r")
    contents = file.read()
    word_list = contents.split()
    output_file = open(output_filename, 'w+')
    seen = set()
    for word in word_list :
    INDENT
        if word not in seen :
        INDENT
            output_file.write(word + '\n')
        DEDENT
        seen.add(word)
    DEDENT
    file.close()
    output_file.close()
    print ('Done')
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

def game_intro() :
INDENT
    intro = True
    while intro :
    INDENT
        for event in pygame.event.get() :
        INDENT
            if event.type == pygame.QUIT :
            INDENT
                pygame.quit()
                quit()
            DEDENT
        DEDENT
    DEDENT
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Run Abush Run!", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    mouse = pygame.mouse.get_pos()
    if 150 + 100 > mouse [0] > 150 and 450 + 50 > mouse [1] > 450 :
    INDENT
        pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
    DEDENT
    else :
    INDENT
        pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
    DEDENT
    pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
    pygame.display.update()
    clock.tick(15)
DEDENT

def transform_non_affine(self, a) :
INDENT
    result = np.empty_like(a)
    a_idx = 0
    csum = 0
    for left, right in self._breaks :
    INDENT
        while a_idx < len(a) and a [a_idx] < left :
        INDENT
            result [a_idx] = a [a_idx] - csum
            a_idx += 1
        DEDENT
        while a_idx < len(a) and a [a_idx] < = right :
        INDENT
            result [a_idx] = left - csum
            a_idx += 1
        DEDENT
        csum += right - left
    DEDENT
    while a_idx < len(a) :
    INDENT
        result [a_idx] = a [a_idx] - csum
        a_idx += 1
    DEDENT
    return result
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

def unique(l) :
INDENT
    s = set(); n = 0
    for x in l :
    INDENT
        if x not in s : s.add(x); l [n] = x; n += 1
    DEDENT
    del l [n :]
DEDENT

def rec(chk, i) :
INDENT
    print (locals())
    i += 1
    chk = chk + [i]
    if i ! = 4 :
    INDENT
        rec(chk, i)
        print (locals())
    DEDENT
DEDENT

    def test_get_object_custom_queryset(self):
        """
        Custom querysets are used when provided to
        BaseDateDetailView.get_object().
        """
        res = self.client.get(
            '/dates/books/get_object_custom_queryset/2006/may/01/%s/' % self.book2.pk)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object'], self.book2)
        self.assertEqual(res.context['book'], self.book2)
        self.assertTemplateUsed(res, 'generic_views/book_detail.html')

        res = self.client.get(
            '/dates/books/get_object_custom_queryset/2008/oct/01/9999999/')
        self.assertEqual(res.status_code, 404)

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

def get_object(self) :
INDENT
    for field in self.lookup_fields :
    INDENT
        if field in self.kwargs :
        INDENT
            self.lookup_field = field
            break
        DEDENT
    DEDENT
    else :
    INDENT
        raise AssertionError(
            'Expected view %s to be called with one of the lookup_fields: %s' %
            (self.__class__.__name__, self.lookup_fields))
    DEDENT
    return super().get_object()
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

    def test_get_object_custom_queryset_numqueries(self):
        with self.assertNumQueries(1):
            self.client.get('/dates/books/get_object_custom_queryset/2006/may/01/2/')

def consec(n, l) :
INDENT
    it = iter(l)
    prev = next(it)
    st = set()
    while prev ! = "" :
    INDENT
        for i in range(n - 1) :
        INDENT
            ele = next(it, "")
            if ele ! = prev or ele == "" :
            INDENT
                break
            DEDENT
            prev = ele
        DEDENT
        else :
        INDENT
            st.add(ele)
        DEDENT
        prev = ele
    DEDENT
    return st
DEDENT

def do_loop(self) :
INDENT
    for line in self.connections [0].iter_lines() :
    INDENT
        if self.new_conn.is_set() :
        INDENT
            break
        DEDENT
        print line
    DEDENT
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

def prime_factors(n) :
INDENT
    factors = []
    d = 2
    while (d * d < = n) :
    INDENT
        while (n > 1) :
        INDENT
            while n % d == 0 :
            INDENT
                factors.append(d)
                n = n / d
            DEDENT
            d += 1
        DEDENT
    DEDENT
    return factors [- 1]
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

def hit(bx, by, r, px, py, h) :
INDENT
    if by > = py and by < = py + h :
    INDENT
        print "Y satisfied."
        if bx < = px + r :
        INDENT
            print "HIT"
            return True
        DEDENT
        print "X not satisfied."
    DEDENT
    print "not hit."
    return False
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

def run(self) :
INDENT
    while True :
    INDENT
        try :
        INDENT
            record = self.queue.get()
            logger = logging.getLogger(record.name)
            logger.callHandlers(record)
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

    def test_datetime_date_detail(self):
        bs = BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0))
        res = self.client.get('/dates/booksignings/2008/apr/2/%d/' % bs.pk)
        self.assertEqual(res.status_code, 200)

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

def removeRec(node, value) :
INDENT
    if isinstance(node, EmptyNode) :
    INDENT
        print ("Cannot remove value from an empty list")
        return None
    DEDENT
    elif node.data == value :
    INDENT
        return node.next
    DEDENT
    else :
    INDENT
        rec_result = removeRec(node.next, value)
        if rec_result is None :
        INDENT
            return rec_result
        DEDENT
        else :
        INDENT
            node.next = rec_result
            return node
        DEDENT
    DEDENT
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

def unique(l) :
INDENT
    s = set(); n = 0
    for x in l :
    INDENT
        if x not in s : s.add(x); l [n] = x; n += 1
    DEDENT
    del l [n :]
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

    @requires_tz_support
    @override_settings(USE_TZ=True, TIME_ZONE='Africa/Nairobi')
    def test_aware_datetime_date_detail(self):
        bs = BookSigning.objects.create(event_date=datetime.datetime(2008, 4, 2, 12, 0, tzinfo=timezone.utc))
        res = self.client.get('/dates/booksignings/2008/apr/2/%d/' % bs.pk)
        self.assertEqual(res.status_code, 200)
        # 2008-04-02T00:00:00+03:00 (beginning of day) > 2008-04-01T22:00:00+00:00 (book signing event date)
        bs.event_date = datetime.datetime(2008, 4, 1, 22, 0, tzinfo=timezone.utc)
        bs.save()
        res = self.client.get('/dates/booksignings/2008/apr/2/%d/' % bs.pk)
        self.assertEqual(res.status_code, 200)
        # 2008-04-03T00:00:00+03:00 (end of day) > 2008-04-02T22:00:00+00:00 (book signing event date)
        bs.event_date = datetime.datetime(2008, 4, 2, 22, 0, tzinfo=timezone.utc)
        bs.save()
        res = self.client.get('/dates/booksignings/2008/apr/2/%d/' % bs.pk)
        self.assertEqual(res.status_code, 404)
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

def GetTheSentences(infile) :
INDENT
    with open(infile) as fp :
    INDENT
        for result in re.findall('DELIMITER1(.*?)DELIMITER2', fp.read(), re.S) :
        INDENT
            print result
        DEDENT
    DEDENT
DEDENT

def characters(nameLst) :
INDENT
    outLst = []
    for name in nameLst :
    INDENT
        outlst.append(len(name))
    DEDENT
    return outLst
    def main() :
    INDENT
        nameLst = ["Dan", "jason", "may", "cole", "Zhan"]
        characters(nameLst)
    DEDENT
    if __name__ == '__main__' :
    INDENT
        main()
    DEDENT
DEDENT

def fit(self, X, y, n_jobs = 1) :
INDENT
    self = super(LinearRegression, self).fit(X, y, n_jobs)
    sse = np.sum((self.predict(X) - y) ** 2, axis = 0) / float(X.shape [0] - X.shape [1])
    se = np.array([
            np.sqrt(np.diagonal(sse [i] * np.linalg.inv(np.dot(X.T, X)))) for i in range(sse.shape [0])
            ])
    self.t = self.coef_ / se
    self.p = 2 * (1 - stats.t.cdf(np.abs(self.t), y.shape [0] - X.shape [1]))
    return self
DEDENT

def qsort(user, begin, end) :
INDENT
    if begin > = end :
    INDENT
        return
    DEDENT
    L = begin + 1
    R = begin
    while L < end :
    INDENT
        if user [begin] > user [L] :
        INDENT
            R += 1
            user [R], user [L] = user [L], user [R]
        DEDENT
        L += 1
    DEDENT
    user [R], user [begin] = user [begin], user [R]
    qsort(user, 0, R)
    qsort(user, R + 1, end)
DEDENT

def convert(items, ID) :
INDENT
    for key, value in items.items() :
    INDENT
        for keys, values in ID.items() :
        INDENT
            if keys == key :
            INDENT
                items [key] = values
            DEDENT
        DEDENT
    DEDENT
    return items
DEDENT






















































































































































































































































































































































































































