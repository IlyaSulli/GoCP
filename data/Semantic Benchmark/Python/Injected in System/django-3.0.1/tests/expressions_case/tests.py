import unittest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from operator import attrgetter, itemgetter
from uuid import UUID

from django.core.exceptions import FieldError
from django.db import models
from django.db.models import F, Max, Min, Q, Sum, Value
from django.db.models.expressions import Case, When
from django.test import SimpleTestCase, TestCase

from .models import CaseTestModel, Client, FKCaseTestModel, O2OCaseTestModel

try:
    from PIL import Image
except ImportError:
    Image = None


class CaseExpressionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        o = CaseTestModel.objects.create(integer=1, integer2=1, string='1')
        O2OCaseTestModel.objects.create(o2o=o, integer=1)
        FKCaseTestModel.objects.create(fk=o, integer=1)

        o = CaseTestModel.objects.create(integer=2, integer2=3, string='2')
        O2OCaseTestModel.objects.create(o2o=o, integer=2)
        FKCaseTestModel.objects.create(fk=o, integer=2)
        FKCaseTestModel.objects.create(fk=o, integer=3)

        o = CaseTestModel.objects.create(integer=3, integer2=4, string='3')
        O2OCaseTestModel.objects.create(o2o=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=4)

        o = CaseTestModel.objects.create(integer=2, integer2=2, string='2')
        O2OCaseTestModel.objects.create(o2o=o, integer=2)
        FKCaseTestModel.objects.create(fk=o, integer=2)
        FKCaseTestModel.objects.create(fk=o, integer=3)

        o = CaseTestModel.objects.create(integer=3, integer2=4, string='3')
        O2OCaseTestModel.objects.create(o2o=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=4)

        o = CaseTestModel.objects.create(integer=3, integer2=3, string='3')
        O2OCaseTestModel.objects.create(o2o=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=3)
        FKCaseTestModel.objects.create(fk=o, integer=4)

        o = CaseTestModel.objects.create(integer=4, integer2=5, string='4')
        O2OCaseTestModel.objects.create(o2o=o, integer=1)
        FKCaseTestModel.objects.create(fk=o, integer=5)

        # GROUP BY on Oracle fails with TextField/BinaryField; see #24096.
        cls.non_lob_fields = [
            f.name for f in CaseTestModel._meta.get_fields()
            if not (f.is_relation and f.auto_created) and not isinstance(f, (models.BinaryField, models.TextField))
        ]

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

def run(self) :
INDENT
    while True :
    INDENT
        log_level, message = self.queue.get()
        if log_level is None :
        INDENT
            self.log.info("Shutting down Central Logging process")
            break
        DEDENT
        else :
        INDENT
            self.log.log(log_level, message)
        DEDENT
    DEDENT
DEDENT

    def test_annotate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(test=Case(
                When(integer=1, then=Value('one')),
                When(integer=2, then=Value('two')),
                default=Value('other'),
                output_field=models.CharField(),
            )).order_by('pk'),
            [(1, 'one'), (2, 'two'), (3, 'other'), (2, 'two'), (3, 'other'), (3, 'other'), (4, 'other')],
            transform=attrgetter('integer', 'test')
        )

def __init__(self, server_address, HandlerClass, config) :
INDENT
    socketserver.BaseServer.__init__(self, server_address, HandlerClass)
    self.address_family = socket.AF_INET6
    self.connected = []
    self.logger = config ['logger']
    self.config = config
    self.socket = socket.socket(self.address_family, self.socket_type)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sc = Context(TLSv1_METHOD)
    sc.set_verify(VERIFY_PEER | VERIFY_FAIL_IF_NO_PEER_CERT, _sni.verify_cb)
    sc.set_tlsext_servername_callback(_sni.pick_certificate)
    self.sc = sc
    self.server_bind()
    self.server_activate()
DEDENT

def print_checked_items(self) :
INDENT
    for index in range(self.model.rowCount()) :
    INDENT
        item = self.model.item(index)
        if item.checkState() == QtCore.Qt.Checked :
        INDENT
            if self.isWritten :
            INDENT
                mode = "a"
            DEDENT
            else :
            INDENT
                mode = "w"
                self.isWritten = True
            DEDENT
            print ('%s' % item.text())
        DEDENT
    DEDENT
    print ("print checked items executed")
DEDENT

def int_to_roman(number) :
INDENT
    result = ""
    for (arabic, roman) in ROMAN :
    INDENT
        (factor, number) = divmod(number, arabic)
        result += roman * factor
    DEDENT
    return result
DEDENT

def acquire_data(arg) :
INDENT
    if isinstance(arg, file) :
    INDENT
        data = arg.read()
    DEDENT
    elif isinstance(arg, basestring) :
    INDENT
        data = open(arg, 'r').read()
    DEDENT
    else :
    INDENT
        data = arg
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

def brute_force(string, length, goal) :
INDENT
    if not length :
    INDENT
        if string == goal :
        INDENT
            return string
        DEDENT
        return False
    DEDENT
    for c in chars :
    INDENT
        s = brute_force(string + c, length - 1, goal)
        if s :
        INDENT
            return s
        DEDENT
    DEDENT
    return False
DEDENT

    def test_annotate_without_default(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(test=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
                output_field=models.IntegerField(),
            )).order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'test')
        )

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

def change(amount) :
INDENT
    if not (24 < = amount < = 1000) :
    INDENT
        return [0]
    DEDENT
    k = int(3 * amount / 7)
    return [5] * (3 * amount - 7 * k) + [7] * (5 * k - 2 * amount)
DEDENT

def chunker(seq, size) :
INDENT
    res = []
    for el in seq :
    INDENT
        res.append(el)
        if len(res) == size :
        INDENT
            yield res
            res = []
        DEDENT
    DEDENT
    if res :
    INDENT
        yield res
    DEDENT
DEDENT

def partition(A, lo, hi) :
INDENT
    pivot = A [lo]
    i, j = lo - 1, hi + 1
    while True :
    INDENT
        i += 1
        j -= 1
        while (A [i] < pivot) : i += 1
        while (A [j] > pivot) : j -= 1
        if i > = j :
        INDENT
            return j
        DEDENT
        A [i], A [j] = A [j], A [i]
    DEDENT
DEDENT

    def test_annotate_with_expression_as_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(f_test=Case(
                When(integer=1, then=F('integer') + 1),
                When(integer=2, then=F('integer') + 3),
                default='integer',
            )).order_by('pk'),
            [(1, 2), (2, 5), (3, 3), (2, 5), (3, 3), (3, 3), (4, 4)],
            transform=attrgetter('integer', 'f_test')
        )

def NumRange(a, x, y) :
INDENT
    def rec(a, acc) :
    INDENT
        if not a :
        INDENT
            return acc
        DEDENT
        head, tail = a [0], a [1 :]
        incr = int(x < = head and head < = y)
        return rec(tail, acc + incr)
    DEDENT
    return rec(a, 0)
DEDENT

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

def addToInventory(inventory, addedItems) :
INDENT
    for v in addedItems :
    INDENT
        if v in inventory.keys() :
        INDENT
            inventory [v] += 1
        DEDENT
        else :
        INDENT
            inventory [v] = 1
        DEDENT
    DEDENT
DEDENT

def lone_sum(* args) :
INDENT
    seen = set()
    summands = set()
    for x in args :
    INDENT
        if x not in seen :
        INDENT
            summands.add(x)
            seen.add(x)
        DEDENT
        else :
        INDENT
            summands.discard(x)
        DEDENT
    DEDENT
    return sum(summands)
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

def deep_get(_dict, keys, default = None) :
INDENT
    def _reducer(d, key) :
    INDENT
        if isinstance(d, dict) :
        INDENT
            return d.get(key, default)
        DEDENT
        return default
    DEDENT
    return reduce(_reducer, keys, _dict)
DEDENT

    def test_annotate_with_expression_as_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(f_test=Case(
                When(integer2=F('integer'), then=Value('equal')),
                When(integer2=F('integer') + 1, then=Value('+1')),
                output_field=models.CharField(),
            )).order_by('pk'),
            [(1, 'equal'), (2, '+1'), (3, '+1'), (2, 'equal'), (3, '+1'), (3, 'equal'), (4, '+1')],
            transform=attrgetter('integer', 'f_test')
        )

def run(self) :
INDENT
    invalid = True
    while invalid :
    INDENT
        try :
        INDENT
            invalid = False
            self.socket.connect(self.addr)
        DEDENT
        except :
        INDENT
            invalid = True
        DEDENT
    DEDENT
    while True :
    INDENT
        data = raw_input('> ')
        if not data :
        INDENT
            continue
        DEDENT
        data = name + ' said : ' + data
        tcpClient.send(data)
    DEDENT
DEDENT

    def test_annotate_with_join_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(join_test=Case(
                When(integer=1, then=F('o2o_rel__integer') + 1),
                When(integer=2, then=F('o2o_rel__integer') + 3),
                default='o2o_rel__integer',
            )).order_by('pk'),
            [(1, 2), (2, 5), (3, 3), (2, 5), (3, 3), (3, 3), (4, 1)],
            transform=attrgetter('integer', 'join_test')
        )

def Max(s) :
INDENT
    if len(s) == 1 :
    INDENT
        return s [0]
    DEDENT
    else :
    INDENT
        m = Max(s [1 :])
        if m > s [0] :
        INDENT
            return m
        DEDENT
        else :
        INDENT
            return s [0]
        DEDENT
    DEDENT
DEDENT

def increase_by_one(d) :
INDENT
    for key in d :
    INDENT
        try :
        INDENT
            d [key] += 1
        DEDENT
        except :
        INDENT
            increase_by_one(d [key])
        DEDENT
    DEDENT
    return d
DEDENT

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

def pdf_view(request) :
INDENT
    try :
    INDENT
        return FileResponse(open('foobar.pdf', 'rb'), content_type = 'application/pdf')
    DEDENT
    except FileNotFoundError :
    INDENT
        raise Http404()
    DEDENT
DEDENT

def merge(arr1, arr2) :
INDENT
    merged = []
    while arr1 and arr2 :
    INDENT
        if arr1 [0] > arr2 [0] :
        INDENT
            arr1, arr2 = arr2, arr1
        DEDENT
        merged.append(arr1.pop(0))
    DEDENT
    merged.extend(arr1 or arr2)
    return merged
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

    def test_annotate_with_in_clause(self):
        fk_rels = FKCaseTestModel.objects.filter(integer__in=[5])
        self.assertQuerysetEqual(
            CaseTestModel.objects.only('pk', 'integer').annotate(in_test=Sum(Case(
                When(fk_rel__in=fk_rels, then=F('fk_rel__integer')),
                default=Value(0),
            ))).order_by('pk'),
            [(1, 0), (2, 0), (3, 0), (2, 0), (3, 0), (3, 0), (4, 5)],
            transform=attrgetter('integer', 'in_test')
        )

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

def __setattr__(self, name, value) :
INDENT
    if name in ("_proxy", "collection") :
    INDENT
        object.__setattr__(self, name, value)
    DEDENT
    else :
    INDENT
        proxied = self._proxy
        collection = self._collection
        old = getattr(proxied, name)
        setattr(proxy, name, value)
        collection.signal_change(proxied, name, old, value)
    DEDENT
DEDENT

def wordsInListsCounter() :
INDENT
    elements = listOfWords(list)
    if len(elements) ! = 0 :
    INDENT
        strLessThanThreshold = [x for x in elements if len(x) < = threshold]
        return strLessThanThreshold
    DEDENT
    elif len(elements) == 0 :
    INDENT
        emptyString = "There are no words in this list"
        return emptyString
    DEDENT
    else :
    INDENT
        error = "There is invalid information"
        return error
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

def __new__(cls, name, bases, attrs) :
INDENT
    def func(self) :
    INDENT
        self.assertTrue(1)
    DEDENT
    func.__name__ = 'test_sample'
    attrs [func.__name__] = func
    return super(DocTestMeta, cls).__new__(cls, name, bases, attrs)
DEDENT

def run_command(cmd) :
INDENT
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        stdin = subprocess.PIPE,
        startupinfo = startupinfo).communicate()
DEDENT

    def test_annotate_with_join_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(join_test=Case(
                When(integer2=F('o2o_rel__integer'), then=Value('equal')),
                When(integer2=F('o2o_rel__integer') + 1, then=Value('+1')),
                default=Value('other'),
                output_field=models.CharField(),
            )).order_by('pk'),
            [(1, 'equal'), (2, '+1'), (3, '+1'), (2, 'equal'), (3, '+1'), (3, 'equal'), (4, 'other')],
            transform=attrgetter('integer', 'join_test')
        )

def Compare(left, ops, comparators) :
INDENT
    for x, op, y in zip([left] + comparators [: - 1], ops, comparators) :
    INDENT
        if not op(x, y) :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
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

def search(request) :
INDENT
    if request.method == "GET" :
    INDENT
        search_terms = request.GET ['title']
        search_terms = search_terms.split(',')
        search_terms = set(search_terms)
        queryargs = [Q(title__contains = i) for i in search_terms]
        jobs = Job.objects.filter(* queryargs)
    DEDENT
DEDENT

def __call__(cls, alias, * args, ** kwargs) :
INDENT
    if cls ! = Bullet :
    INDENT
        raise TypeError("Bullet subclass %r objects should not to "
            "be explicitly constructed." % cls.__name__)
    DEDENT
    elif alias not in cls.registry :
    INDENT
        raise NotImplementedError("Unknown Bullet subclass %r" %
            str(alias))
    DEDENT
    subclass = cls.registry [alias]
    return type.__call__(subclass, * args, ** kwargs)
DEDENT

def queryset(self, request, queryset) :
INDENT
    expected_value = self.value()
    excludes = []
    for comment in queryset :
    INDENT
        if comment.posted_by_guest() ! = expected_value :
        INDENT
            excludes.append(comment.id)
        DEDENT
    DEDENT
    return queryset.exclude(pk__in = excludes)
DEDENT

    def test_annotate_with_join_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(join_test=Case(
                When(o2o_rel__integer=1, then=Value('one')),
                When(o2o_rel__integer=2, then=Value('two')),
                When(o2o_rel__integer=3, then=Value('three')),
                default=Value('other'),
                output_field=models.CharField(),
            )).order_by('pk'),
            [(1, 'one'), (2, 'two'), (3, 'three'), (2, 'two'), (3, 'three'), (3, 'three'), (4, 'one')],
            transform=attrgetter('integer', 'join_test')
        )

def escaped_split(s, delim) :
INDENT
    escaped_delim = '\\' + delim
    sections = [p.split(delim) for p in s.split(escaped_delim)]
    ret = []
    prev = None
    for parts in sections :
    INDENT
        if prev is None :
        INDENT
            if len(parts) > 1 :
            INDENT
                ret.append(parts [0])
            DEDENT
        DEDENT
        else :
        INDENT
            ret.append(escaped_delim.join([prev, parts [0]]))
        DEDENT
        for part in parts [1 : - 1] :
        INDENT
            ret.append(part)
        DEDENT
        prev = parts [- 1]
    DEDENT
    return ret
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

def __str__(self) :
INDENT
    s = '{0!s} {1} {2!s}'.format(self.left, self.operator, self.right)
    if self.grouped :
    INDENT
        return '({0})'.format(s)
    DEDENT
    else :
    INDENT
        return s
    DEDENT
DEDENT

def froze_it(cls) :
INDENT
    def frozensetattr(self, key, value) :
    INDENT
        if not hasattr(self, key) and inspect.stack() [1] [3] ! = "__init__" :
        INDENT
            print ("Class {} is frozen. Cannot set {} = {}"
                .format(cls.__name__, key, value))
        DEDENT
        else :
        INDENT
            self.__dict__ [key] = value
        DEDENT
    DEDENT
    cls.__setattr__ = frozensetattr
    return cls
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

    def test_annotate_with_annotation_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f_plus_1=F('integer') + 1,
                f_plus_3=F('integer') + 3,
            ).annotate(
                f_test=Case(
                    When(integer=1, then='f_plus_1'),
                    When(integer=2, then='f_plus_3'),
                    default='integer',
                ),
            ).order_by('pk'),
            [(1, 2), (2, 5), (3, 3), (2, 5), (3, 3), (3, 3), (4, 4)],
            transform=attrgetter('integer', 'f_test')
        )

def get_with_default(colour, L, default = '') :
INDENT
    temp = None
    for d in L :
    INDENT
        if d ['color'] == colour :
        INDENT
            return d
        DEDENT
        elif d ['color'] == default :
        INDENT
            temp = d
        DEDENT
    DEDENT
    return temp
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

def duplicate(self) :
INDENT
    fks_to_copy = list(self.fkeys_a.all()) + list(self.fkeys_b.all())
    self.pk = None
    self.save()
    foreign_keys = {}
    for fk in fks_to_copy :
    INDENT
        fk.pk = None
        try :
        INDENT
            foreign_keys [fk.__class__].append(fk)
        DEDENT
        except KeyError :
        INDENT
            foreign_keys [fk.__class__] = [fk]
        DEDENT
    DEDENT
    for cls, list_of_fks in foreign_keys.items() :
    INDENT
        cls.objects.bulk_create(list_of_fks)
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

    def test_annotate_with_annotation_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f_plus_1=F('integer') + 1,
            ).annotate(
                f_test=Case(
                    When(integer2=F('integer'), then=Value('equal')),
                    When(integer2=F('f_plus_1'), then=Value('+1')),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [(1, 'equal'), (2, '+1'), (3, '+1'), (2, 'equal'), (3, '+1'), (3, 'equal'), (4, '+1')],
            transform=attrgetter('integer', 'f_test')
        )

def draw(self, win, rows, columns) :
INDENT
    for day, (start, length) in self.schedule :
    INDENT
        box = Rectangle(
            Point(columns [day], rows [start]),
            Point(columns [day + 1], rows [start + length]))
        box.setFill(self.bg)
        box.setOutline(self.border)
        box.draw(win)
        label = Text(Point(columns [day] + 10, rows [start] + 40), self.name)
        label.fontSize = 9
        label.setFill(self.text)
        label.draw(win)
    DEDENT
DEDENT

def save(self, * args, ** kwargs) :
INDENT
    if self.image_url :
    INDENT
        import urllib, os
        from urlparse import urlparse
        file_save_dir = self.upload_path
        filename = urlparse(self.image_url).path.split('/') [- 1]
        urllib.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
        self.image = os.path.join(file_save_dir, filename)
        self.image_url = ''
    DEDENT
    super(tweet_photos, self).save()
DEDENT

def pattern_match(sequence, patterns) :
INDENT
    if len(sequence) == len(patterns) :
    INDENT
        return all(item in my_set for item, my_set in zip(sequence, patterns))
    DEDENT
    else :
    INDENT
        return False
    DEDENT
DEDENT

def DnaCheck() :
INDENT
    squence_str = set(squence_str.upper())
    for char in ['A', 'C', 'T', 'G'] :
    INDENT
        if char not in squence_str :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def CardsAssignment() :
INDENT
    Cards += 1
    print (Cards)
    if want_to_break_while_loop :
    INDENT
        return False
    DEDENT
    else :
    INDENT
        return True
    DEDENT
DEDENT

def repeat(a, n, already_ran = 0) :
INDENT
    if n == 0 :
    INDENT
        print (a * (n + already_ran))
    DEDENT
    else :
    INDENT
        print (a * (n + already_ran))
        repeat(a, n - 1, already_ran + 1)
    DEDENT
DEDENT

def __str__(self) :
INDENT
    return textwrap.dedent('''\
        Car Type
        mpg: %.1f
        hp: %.2f
        pc: %i
        unit cost: $%.2f
        price: $%.2f''' % (self.mpg, self.hp, self.pc, self.cost, self.price))
DEDENT

def __init__(self, parent) :
INDENT
    wx.Panel.__init__(self, parent)
    self.figure = mplFigure(figsize = (9, 6))
    self.ax = self.figure.add_subplot(111)
    self.ax.plot([1, 2, 3, 4], [2, 3, 5, 8], marker = "o", markersize = 20, picker = 10, linestyle = "None")
    self.canvas = mplCanvas(self, - 1, self.figure)
    self.figure.canvas.mpl_connect('pick_event', self.onClick)
    self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_down)
    self.canvas.Bind(wx.EVT_KEY_UP, self._on_key_up)
    self.states = {"cmd" : False, "ctrl" : False, "shift" : False}
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

    def test_annotate_with_annotation_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f_minus_2=F('integer') - 2,
            ).annotate(
                test=Case(
                    When(f_minus_2=-1, then=Value('negative one')),
                    When(f_minus_2=0, then=Value('zero')),
                    When(f_minus_2=1, then=Value('one')),
                    default=Value('other'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [(1, 'negative one'), (2, 'zero'), (3, 'one'), (2, 'zero'), (3, 'one'), (3, 'one'), (4, 'other')],
            transform=attrgetter('integer', 'test')
        )

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

    def test_annotate_with_aggregation_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                min=Min('fk_rel__integer'),
                max=Max('fk_rel__integer'),
            ).annotate(
                test=Case(
                    When(integer=2, then='min'),
                    When(integer=3, then='max'),
                ),
            ).order_by('pk'),
            [(1, None, 1, 1), (2, 2, 2, 3), (3, 4, 3, 4), (2, 2, 2, 3), (3, 4, 3, 4), (3, 4, 3, 4), (4, None, 5, 5)],
            transform=itemgetter('integer', 'test', 'min', 'max')
        )

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

def __init__(self, parent = None) :
INDENT
    super(MainWindow, self).__init__(parent)
    layout = QtWidgets.QHBoxLayout(self)
    menu_btn = QtWidgets.QPushButton()
    open_list_btn = QtWidgets.QPushButton('open list')
    layout.addWidget(menu_btn)
    layout.addWidget(open_list_btn)
    menu = QtWidgets.QMenu()
    menu_btn.setMenu(menu)
    self.menu_manager = MenuManager("menu_items", "Menu")
    menu.addMenu(self.menu_manager.menu)
    self.menu_manager.menu.triggered.connect(self.menu_clicked)
    open_list_btn.clicked.connect(self.menu_manager.show)
DEDENT

    def test_annotate_with_aggregation_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                min=Min('fk_rel__integer'),
                max=Max('fk_rel__integer'),
            ).annotate(
                test=Case(
                    When(integer2=F('min'), then=Value('min')),
                    When(integer2=F('max'), then=Value('max')),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [(1, 1, 'min'), (2, 3, 'max'), (3, 4, 'max'), (2, 2, 'min'), (3, 4, 'max'), (3, 3, 'min'), (4, 5, 'min')],
            transform=itemgetter('integer', 'integer2', 'test')
        )

def __init__(self, parent = None) :
INDENT
    super(myWindow, self).__init__(parent)
    self.pushButton = QtGui.QPushButton(self)
    self.pushButton.setText("Send Log Message")
    self.pushButton.clicked.connect(self.on_pushButton_clicked)
    self.pushButtonThread = QtGui.QPushButton(self)
    self.pushButtonThread.setText("Start Threading")
    self.pushButtonThread.clicked.connect(self.on_pushButtonThread_clicked)
    self.lineEdit = QtGui.QLineEdit(self)
    self.lineEdit.setText("Hello!")
    self.label = QtGui.QLabel(self)
    self.layout = QtGui.QVBoxLayout(self)
    self.layout.addWidget(self.lineEdit)
    self.layout.addWidget(self.pushButton)
    self.layout.addWidget(self.pushButtonThread)
    self.layout.addWidget(self.label)
    self.logBuffer = logBuffer()
    self.logBuffer.bufferMessage.connect(self.on_logBuffer_bufferMessage)
    logFormatter = logging.Formatter('%(levelname)s: %(message)s')
    logHandler = logging.StreamHandler(self.logBuffer)
    logHandler.setFormatter(logFormatter)
    self.logger = logging.getLogger()
    self.logger.setLevel(logging.INFO)
    self.logger.addHandler(logHandler)
    self.thread = myThread(self)
    self.thread1 = myThread1(self)
DEDENT

    def test_annotate_with_aggregation_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                max=Max('fk_rel__integer'),
            ).annotate(
                test=Case(
                    When(max=3, then=Value('max = 3')),
                    When(max=4, then=Value('max = 4')),
                    default=Value(''),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [(1, 1, ''), (2, 3, 'max = 3'), (3, 4, 'max = 4'), (2, 3, 'max = 3'),
             (3, 4, 'max = 4'), (3, 4, 'max = 4'), (4, 5, '')],
            transform=itemgetter('integer', 'max', 'test')
        )

def convert_timestamp(date_timestamp = None) :
INDENT
    try :
    INDENT
        d = datetime.strptime(date_timestamp, "%Y-%m-%d %H:%M:%S %Z")
    DEDENT
    except ValueError :
    INDENT
        d = datetime.strptime(date_timestamp, "%Y-%m-%d %H:%M:%S")
    DEDENT
    return d.strftime("%Y-%m-%d")
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

def touch(file_name) :
INDENT
    if not os.path.exists(file_name) :
    INDENT
        return
    DEDENT
    try :
    INDENT
        os.utime(file_name, None)
    DEDENT
    except Exception :
    INDENT
        open(file_name, 'a').close()
    DEDENT
DEDENT

def __call__(cls, * args, ** kwargs) :
INDENT
    self = cls.__new__(cls)
    set_mutability(self, True)
    self.__init__(* args, ** kwargs)
    set_mutability(self, False)
    return self
DEDENT

    def test_annotate_exclude(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(test=Case(
                When(integer=1, then=Value('one')),
                When(integer=2, then=Value('two')),
                default=Value('other'),
                output_field=models.CharField(),
            )).exclude(test='other').order_by('pk'),
            [(1, 'one'), (2, 'two'), (2, 'two')],
            transform=attrgetter('integer', 'test')
        )

def second_smallest(list) :
INDENT
    if len(list) < 2 :
    INDENT
        raise ValueError("too few elements to find second_smallest")
    DEDENT
    a, b, rest = list [0], list [1], list [2 :]
    if b < a :
    INDENT
        return recurse(b, a, rest)
    DEDENT
    else :
    INDENT
        return recurse(a, b, rest)
    DEDENT
DEDENT

def encrypt(key, plaintext) :
INDENT
    key = key.encode('ascii')
    plaintext = plaintext.encode('utf-8')
    padded_key = key.ljust(KEY_SIZE, b'\0')
    sg = pprp.data_source_gen(plaintext, block_size = BLOCK_SIZE)
    eg = pprp.rjindael_encrypt_gen(padded_key, sg, block_size = BLOCK_SIZE)
    ciphertext = pprp.encrypt_sink(eg)
    encoded = base64.b64encode(ciphertext)
    return encoded.decode('ascii')
DEDENT

def f() :
INDENT
    ldict = {}
    for key, val in measurements.items() :
    INDENT
        ldict.update(locals())
        exec (key + ' = val', globals(), ldict)
        key = ldict [key]
    DEDENT
    print (ldict ['tg'])
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

def oddn(x, y, z) :
INDENT
    odd_number_keeper = []
    for item in [x, y, z] :
    INDENT
        if item % 2 == 1 :
        INDENT
            odd_number_keeper.append(item)
        DEDENT
    DEDENT
    if not odd_number_keeper :
    INDENT
        print 'No odd number is found'
        return
    DEDENT
    return max(odd_number_keeper)
DEDENT

    def test_annotate_values_not_in_order_by(self):
        self.assertEqual(
            list(CaseTestModel.objects.annotate(test=Case(
                When(integer=1, then=Value('one')),
                When(integer=2, then=Value('two')),
                When(integer=3, then=Value('three')),
                default=Value('other'),
                output_field=models.CharField(),
            )).order_by('test').values_list('integer', flat=True)),
            [1, 4, 3, 3, 3, 2, 2]
        )

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

def default(self, v) :
INDENT
    types = {
        'ObjectId' : lambda v : str(v),
        'datetime' : lambda v : v.isoformat()}
    vtype = type(v).__name__
    if vtype in types :
    INDENT
        return types [type(v).__name__](v)
    DEDENT
    else :
    INDENT
        return json.JSONEncoder.default(self, v)
    DEDENT
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

def run(self) :
INDENT
    print '>>>> abuse generator as context manager'
    for driver in self.drivergenerator(self.driverfactory) :
    INDENT
        self.dostuff(driver)
    DEDENT
DEDENT

def findmax(s) :
INDENT
    matches = []
    current = [s [0]]
    for index, character in enumerate(s [1 :]) :
    INDENT
        if character > = s [index] :
        INDENT
            current.append(character)
        DEDENT
        else :
        INDENT
            matches.append(current)
            current = [character]
        DEDENT
    DEDENT
    matches.append(current)
    maxlen = len(max(matches, key = len))
    return ["".join(match) for match in matches if len(match) == maxlen]
DEDENT

def __init__(self, parent) :
INDENT
    wx.Panel.__init__(self, parent)
    self.figure = mplFigure(figsize = (9, 6))
    self.ax = self.figure.add_subplot(111)
    self.ax.plot([1, 2, 3, 4], [2, 3, 5, 8], marker = "o", markersize = 20, picker = 10, linestyle = "None")
    self.canvas = mplCanvas(self, - 1, self.figure)
    self.figure.canvas.mpl_connect('pick_event', self.onClick)
    self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_down)
    self.canvas.Bind(wx.EVT_KEY_UP, self._on_key_up)
    self.states = {"cmd" : False, "ctrl" : False, "shift" : False}
DEDENT

def __init__(self, resources, acquire_resource, release_resource,
check_resource_ok = None) :
INDENT
    super().__init__()
    self.acquire_resource = acquire_resource
    self.release_resource = release_resource
    if check_resource_ok is None :
    INDENT
        def check_resource_ok(resource) :
        INDENT
            return True
        DEDENT
    DEDENT
    self.check_resource_ok = check_resource_ok
    self.resources = resources
    self.wrappers = []
DEDENT

    def test_annotate_with_empty_when(self):
        objects = CaseTestModel.objects.annotate(
            selected=Case(
                When(pk__in=[], then=Value('selected')),
                default=Value('not selected'), output_field=models.CharField()
            )
        )
        self.assertEqual(len(objects), CaseTestModel.objects.count())
        self.assertTrue(all(obj.selected == 'not selected' for obj in objects))

def quantityFunction(product) :
INDENT
    valid = False
    while True :
    INDENT
        if product is not None :
        INDENT
            quantity = raw_input("Please enter the amount of this item you would like to purchase: ")
            try :
            INDENT
                return int(quantity)
            DEDENT
            except ValueError :
            INDENT
                print ("We didn't recognise that number. Please try again.")
            DEDENT
        DEDENT
        return False
    DEDENT
DEDENT

def is_continuous(seq) :
INDENT
    try :
    INDENT
        first_none_pos = next(i for i, x in enumerate(seq) if x is not None)
        last_none_pos = - next(i for i, x in enumerate(reversed(seq)) if x is not None) or None
    DEDENT
    except StopIteration :
    INDENT
        return False
    DEDENT
    return None not in seq [first_none_pos : last_none_pos]
DEDENT

def __init__(self, type, parent = None) :
INDENT
    super().__init__()
    self.parent = parent
    self.Type = type
    self.setStyleSheet("""QSlider::groove:vertical {
    border: 1px solid black;
    height: """ + str(groove_y) + """ px;
    width: 10px;
    border-radius: 2px;
    }
    QSlider::handle:vertical {
        background: red;
        border: 1px solid red;
        height: """ + str(handle_height) + """ px;
        margin: 2px 0;
        border-radius: 1px;
    }
    QSlider::add-page:vertical {
        background: blue;
    }
    QSlider::sub-page:vertical {
        background: red;
""")
DEDENT

def repeat(a, n, already_ran = 0) :
INDENT
    if n == 0 :
    INDENT
        print (a * (n + already_ran))
    DEDENT
    else :
    INDENT
        print (a * (n + already_ran))
        repeat(a, n - 1, already_ran + 1)
    DEDENT
DEDENT

def partition(A, lo, hi) :
INDENT
    pivot = A [lo]
    i, j = lo - 1, hi + 1
    while True :
    INDENT
        i += 1
        j -= 1
        while (A [i] < pivot) : i += 1
        while (A [j] > pivot) : j -= 1
        if i > = j :
        INDENT
            return j
        DEDENT
        A [i], A [j] = A [j], A [i]
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

    def test_combined_expression(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                test=Case(
                    When(integer=1, then=2),
                    When(integer=2, then=1),
                    default=3,
                    output_field=models.IntegerField(),
                ) + 1,
            ).order_by('pk'),
            [(1, 3), (2, 2), (3, 4), (2, 2), (3, 4), (3, 4), (4, 4)],
            transform=attrgetter('integer', 'test')
        )

def increment(self) :
INDENT
    for i, num in enumerate(reversed(self.numbers)) :
    INDENT
        if num :
        INDENT
            self.numbers [- i - 1] = 0 if num == 9 else num + 1
            break
        DEDENT
    DEDENT
DEDENT

def __init__(self, obj) :
INDENT
    if self.__wraps__ is None :
    INDENT
        raise TypeError("base class Wrapper may not be instantiated")
    DEDENT
    elif isinstance(obj, self.__wraps__) :
    INDENT
        self._obj = obj
    DEDENT
    else :
    INDENT
        raise ValueError("wrapped object must be of %s" % self.__wraps__)
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

    def test_in_subquery(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(
                pk__in=CaseTestModel.objects.annotate(
                    test=Case(
                        When(integer=F('integer2'), then='pk'),
                        When(integer=4, then='pk'),
                        output_field=models.IntegerField(),
                    ),
                ).values('test')).order_by('pk'),
            [(1, 1), (2, 2), (3, 3), (4, 5)],
            transform=attrgetter('integer', 'integer2')
        )

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

    def test_case_reuse(self):
        SOME_CASE = Case(
            When(pk=0, then=Value('0')),
            default=Value('1'),
            output_field=models.CharField(),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(somecase=SOME_CASE).order_by('pk'),
            CaseTestModel.objects.annotate(somecase=SOME_CASE).order_by('pk').values_list('pk', 'somecase'),
            lambda x: (x.pk, x.somecase)
        )

def inf_repeat(N) :
INDENT
    i = 1
    while True :
    INDENT
        for n in range(N) :
        INDENT
            yield i
        DEDENT
        i += 1
    DEDENT
DEDENT

def test_func_happy_path(MockFTP) :
INDENT
    mock_ftp = MockFTP.return_value
    with patch('__main__.open', mock_open(), create = True) as m :
    INDENT
        func('localhost', 'fred', 's3Kr3t')
    DEDENT
    assert mock_ftp.retrbinary.called
    m.assert_called_once_with('README', 'wb')
DEDENT

def get_dir_size(root) :
INDENT
    size = 0
    for path, dirs, files in os.walk(root) :
    INDENT
        for f in files :
        INDENT
            size += os.path.getsize(os.path.join(path, f))
        DEDENT
    DEDENT
    return size
DEDENT

    def test_aggregate(self):
        self.assertEqual(
            CaseTestModel.objects.aggregate(
                one=models.Sum(Case(
                    When(integer=1, then=1),
                    output_field=models.IntegerField(),
                )),
                two=models.Sum(Case(
                    When(integer=2, then=1),
                    output_field=models.IntegerField(),
                )),
                three=models.Sum(Case(
                    When(integer=3, then=1),
                    output_field=models.IntegerField(),
                )),
                four=models.Sum(Case(
                    When(integer=4, then=1),
                    output_field=models.IntegerField(),
                )),
            ),
            {'one': 1, 'two': 2, 'three': 3, 'four': 1}
        )

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

def _extract_links(self, selector, response_url, response_encoding, base_url) :
INDENT
    links = []
    for el, attr, attr_val in self._iter_links(selector._root) :
    INDENT
        attr_val = urljoin(base_url, attr_val.strip())
        url = self.process_attr(attr_val)
        if url is None :
        INDENT
            continue
        DEDENT
        if isinstance(url, unicode) :
        INDENT
            url = url.encode(response_encoding)
        DEDENT
        url = urljoin(response_url, url)
        link = Link(url, _collect_string_content(el) or u'',
            nofollow = True if el.get('rel') == 'nofollow' else False)
        links.append(link)
    DEDENT
    return unique_list(links, key = lambda link : link.url) if self.unique else links
DEDENT

def main() :
INDENT
    p1 = Process(target = f1, args = ())
    p2 = Process(target = f2, args = ())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
DEDENT

def pdf_view(request) :
INDENT
    try :
    INDENT
        return FileResponse(open('foobar.pdf', 'rb'), content_type = 'application/pdf')
    DEDENT
    except FileNotFoundError :
    INDENT
        raise Http404()
    DEDENT
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
        DEDENT
        def q(* b) :
        INDENT
            return x(* (a + b))
        DEDENT
        return curry(q, argc - len(a))
    DEDENT
    return p
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

    def test_aggregate_with_expression_as_value(self):
        self.assertEqual(
            CaseTestModel.objects.aggregate(
                one=models.Sum(Case(When(integer=1, then='integer'))),
                two=models.Sum(Case(When(integer=2, then=F('integer') - 1))),
                three=models.Sum(Case(When(integer=3, then=F('integer') + 1))),
            ),
            {'one': 1, 'two': 2, 'three': 12}
        )

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

def consec(n, iterable) :
INDENT
    result = set()
    prev = None
    count = 0
    for item in iterable :
    INDENT
        if item == prev :
        INDENT
            count += 1
            if count == n :
            INDENT
                result.add(prev)
            DEDENT
        DEDENT
        else :
        INDENT
            prev = item
            count = 1
        DEDENT
    DEDENT
    return result
DEDENT

def main() :
INDENT
    t = np.linspace(0, 10 * np.pi, 30)
    x = np.sin(t)
    condition = np.where(x > 0, 1, 0)
    onarray, offarray = on_off_times(condition)
    print "Condition: ", condition
    print "Ontimes:   ", onarray
    print "Offtimes:  ", offarray
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

    def test_aggregate_with_expression_as_condition(self):
        self.assertEqual(
            CaseTestModel.objects.aggregate(
                equal=models.Sum(Case(
                    When(integer2=F('integer'), then=1),
                    output_field=models.IntegerField(),
                )),
                plus_one=models.Sum(Case(
                    When(integer2=F('integer') + 1, then=1),
                    output_field=models.IntegerField(),
                )),
            ),
            {'equal': 3, 'plus_one': 4}
        )

def NumRange(a, x, y) :
INDENT
    def rec(a, acc) :
    INDENT
        if not a :
        INDENT
            return acc
        DEDENT
        head, tail = a [0], a [1 :]
        incr = int(x < = head and head < = y)
        return rec(tail, acc + incr)
    DEDENT
    return rec(a, 0)
DEDENT

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

def main() :
INDENT
    for line in open("Magic Square Input.txt") :
    INDENT
        items = line.split(" ")
        items = [int(x) for x in items]
        result = [items [0 : 3], items [3 : 6], items [6 : 9]]
        print isMagic(result)
    DEDENT
DEDENT

def validate_ip(ip_str) :
INDENT
    reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(reg, ip_str) :
    INDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
DEDENT

    def test_filter(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer2=Case(
                When(integer=2, then=3),
                When(integer=3, then=4),
                default=1,
                output_field=models.IntegerField(),
            )).order_by('pk'),
            [(1, 1), (2, 3), (3, 4), (3, 4)],
            transform=attrgetter('integer', 'integer2')
        )

def shiftedColorMap(cmap, min_val, max_val, name) :
INDENT
    epsilon = 0.001
    start, stop = 0.0, 1.0
    min_val, max_val = min(0.0, min_val), max(0.0, max_val)
    midpoint = 1.0 - max_val / (max_val + abs(min_val))
    cdict = {'red' : [], 'green' : [], 'blue' : [], 'alpha' : []}
    reg_index = np.linspace(start, stop, 257)
    shift_index = np.hstack([np.linspace(0.0, midpoint, 128, endpoint = False), np.linspace(midpoint, 1.0, 129, endpoint = True)])
    for ri, si in zip(reg_index, shift_index) :
    INDENT
        if abs(si - midpoint) < epsilon :
        INDENT
            r, g, b, a = cmap(0.5)
        DEDENT
        else :
        INDENT
            r, g, b, a = cmap(ri)
        DEDENT
        cdict ['red'].append((si, r, r))
        cdict ['green'].append((si, g, g))
        cdict ['blue'].append((si, b, b))
        cdict ['alpha'].append((si, a, a))
    DEDENT
    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap = newcmap)
    return newcmap
DEDENT

def encrypt(plain) :
INDENT
    fs = [pycipher.Affine(3, 0).encipher,
        pycipher.Affine(7, 6).encipher]
    is_even = True
    d = dict()
    for ch in string.ascii_lowercase :
    INDENT
        f = fs [is_even]
        d [ch] = f(ch)
        is_even = not is_even
    DEDENT
    return ''.join([d [ch] for ch in plain])
DEDENT

def sumvars(x, y, z, d = None) :
INDENT
    s = x
    if not d is None :
    INDENT
        d ['first_step'] = s
    DEDENT
    s += y
    if not d is None :
    INDENT
        d ['second_step'] = s
    DEDENT
    s += z
    return s
DEDENT

def order_fields(* field_list) :
INDENT
    def decorator(form) :
    INDENT
        original_init = form.__init__
        def init(self, * args, ** kwargs) :
        INDENT
            original_init(self, * args, ** kwargs)
            for field in field_list [: : - 1] :
            INDENT
                self.fields.insert(0, field, self.fields.pop(field))
            DEDENT
        DEDENT
        form.__init__ = init
        return form
    DEDENT
    return decorator
DEDENT

    def test_filter_without_default(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer2=Case(
                When(integer=2, then=3),
                When(integer=3, then=4),
                output_field=models.IntegerField(),
            )).order_by('pk'),
            [(2, 3), (3, 4), (3, 4)],
            transform=attrgetter('integer', 'integer2')
        )

def greet(lines, cheers) :
INDENT
    i = 0
    line_str = ""
    while i < cheers :
    INDENT
        i += 1
        line_str += "GO" if i == cheers else "GO BUDDY "
    DEDENT
    i = 0
    while i < lines :
    INDENT
        print (" " * (i * 3) + line_str)
        i += 1
    DEDENT
DEDENT

def flatten(container) :
INDENT
    for i in container :
    INDENT
        if isinstance(i, (list, tuple)) :
        INDENT
            for j in flatten(i) :
            INDENT
                yield j
            DEDENT
        DEDENT
        else :
        INDENT
            yield i
        DEDENT
    DEDENT
DEDENT

def __getattr__(self, attr) :
INDENT
    if attr not in DICT_RESERVED_KEYS :
    INDENT
        if self ['__keyerror'] :
        INDENT
            return self [attr]
        DEDENT
        else :
        INDENT
            return self.get(attr)
        DEDENT
    DEDENT
    return getattr(self, attr)
DEDENT

def iterate(i) :
INDENT
    try :
    INDENT
        i_iter = iter(i)
        next = i_iter.next()
    DEDENT
    except StopIteration :
    INDENT
        print 'i is empty'
        return
    DEDENT
    while True :
    INDENT
        yield next
        next = i_iter.next()
    DEDENT
DEDENT

def wrapper(f) :
INDENT
    @ functools.wraps(f)
    def func(* args, ** kwargs) :
    INDENT
        if (time.time() - func.last_time) < interval :
        INDENT
            time.sleep(interval)
        DEDENT
        result = f(* args, ** kwargs)
        func.last_time = time.time()
        return result
    DEDENT
    func.last_time = time.time()
    return func
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

def is_prime(x) :
INDENT
    if x < 2 :
    INDENT
        return False
    DEDENT
    elif x == 2 :
    INDENT
        return True
    DEDENT
    for n in range(2, x) :
    INDENT
        if x % n == 0 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
DEDENT

def frange(a, b, stp = 1.0) :
INDENT
    i = a + stp / 2.0
    while i < b :
    INDENT
        yield a
        a += stp
        i += stp
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

    def test_filter_with_expression_as_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer2=Case(
                When(integer=2, then=F('integer') + 1),
                When(integer=3, then=F('integer')),
                default='integer',
            )).order_by('pk'),
            [(1, 1), (2, 3), (3, 3)],
            transform=attrgetter('integer', 'integer2')
        )

def allpaths(G, source_nodes, set_of_sink_nodes, path_prefix = ()) :
INDENT
    set_of_result_paths = set()
    for n in source_nodes :
    INDENT
        next_from_n = []
        for an in G [n] :
        INDENT
            if an in set_of_sink_nodes :
            INDENT
                set_of_result_paths.add(path_prefix + (n, an))
            DEDENT
            else :
            INDENT
                next_from_n.append(an)
            DEDENT
        DEDENT
        if next_from_n :
        INDENT
            set_of_result_paths.update(
                allpaths(G, next_from_n, set_of_sink_nodes, path_prefix + (n,)))
        DEDENT
    DEDENT
    return set_of_result_paths
DEDENT

def find_neighbors(tess) :
INDENT
    neighbors = defaultdict(set)
    for simplex in tess.simplices :
    INDENT
        for idx in simplex :
        INDENT
            other = set(simplex)
            other.remove(idx)
            neighbors [idx] = neighbors [idx].union(other)
        DEDENT
    DEDENT
    return neighbors
DEDENT

def __init__(self, * args, ** kw) :
INDENT
    wx.Frame.__init__(self, * args, ** kw)
    self.list = wx.ListCtrl(self, style = wx.LC_REPORT)
    items = ['A', 'b', 'something really REALLY long']
    self.list.InsertColumn(0, "AA")
    for item in items :
    INDENT
        self.list.InsertStringItem(0, item)
    DEDENT
    self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
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

    def test_filter_with_expression_as_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(string=Case(
                When(integer2=F('integer'), then=Value('2')),
                When(integer2=F('integer') + 1, then=Value('3')),
                output_field=models.CharField(),
            )).order_by('pk'),
            [(3, 4, '3'), (2, 2, '2'), (3, 4, '3')],
            transform=attrgetter('integer', 'integer2', 'string')
        )

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

def deprecated(message) :
INDENT
    def deprecated_decorator(func) :
    INDENT
        def deprecated_func(* args, ** kwargs) :
        INDENT
            warnings.warn("{} is a deprecated function. {}".format(func.__name__, message),
                category = DeprecationWarning,
                stacklevel = 2)
            warnings.simplefilter('default', DeprecationWarning)
            return func(* args, ** kwargs)
        DEDENT
        return deprecated_func
    DEDENT
    return deprecated_decorator
DEDENT

def zipdir(path, ziph) :
INDENT
    for root, dirs, files in os.walk(path) :
    INDENT
        for file in files :
        INDENT
            ziph.write(os.path.join(root, file))
        DEDENT
    DEDENT
DEDENT

def pay_with_coins(amount) :
INDENT
    amount = Decimal(amount)
    coins_list = [0, 0, 0, 0, 0, 0, 0, 0]
    if amount == 0 :
    INDENT
        return (coins_list)
    DEDENT
    else :
    INDENT
        while amount > Decimal("2.00") :
        INDENT
            coins_list [0] = (coins_list [0] + 1)
            amount = amount - Decimal("2.00")
        DEDENT
        while amount > = Decimal("1.00") and amount < Decimal("2.00") :
        INDENT
            coins_list [1] = (coins_list [1] + 1)
            amount = amount - Decimal("1.00")
        DEDENT
        while amount > = Decimal("0.50") and amount < Decimal("1.00") :
        INDENT
            coins_list [2] = (coins_list [2] + 1)
            amount = amount - Decimal("0.50")
        DEDENT
        while amount > = Decimal("0.20") and amount < Decimal("0.50") :
        INDENT
            coins_list [3] = (coins_list [3] + 1)
            amount = amount - Decimal("0.20")
        DEDENT
        while amount > = Decimal("0.10") and amount < Decimal("0.20") :
        INDENT
            coins_list [4] = (coins_list [4] + 1)
            amount = amount - Decimal("0.10")
        DEDENT
        while amount > = Decimal("0.05") and amount < Decimal("0.10") :
        INDENT
            coins_list [5] = (coins_list [5] + 1)
            amount = amount - Decimal("0.05")
        DEDENT
        while amount > = Decimal("0.02") and amount < Decimal("0.05") :
        INDENT
            coins_list [6] = (coins_list [6] + 1)
            amount = amount - Decimal("0.02")
        DEDENT
        while amount > = Decimal("0.01") and amount < Decimal("0.05") :
        INDENT
            coins_list [7] = (coins_list [7] + 1)
            amount = amount - Decimal("0.01")
        DEDENT
        return (coins_list)
    DEDENT
DEDENT

def returnJSONQuestion(questionId) :
INDENT
    randomSleep()
    jsondata = None
    url = 'http://answers.yahooapis.com/AnswersService/V1/getQuestion?appid=APPIDREMOVED8&question_id={0}&output=json'
    format_url = url.format(questionId)
    try :
    INDENT
        request = urllib2.Request(format_url)
        urlobject = urllib2.urlopen(request)
        time.sleep(10)
        jsondata = json.loads(urlobject.read().decode("utf-8"))
        print jsondata
    DEDENT
    except urllib2.HTTPError, e :
    INDENT
        print e.code
        logging.exception("Exception")
    DEDENT
    except urllib2.URLError, e :
    INDENT
        print e.reason
        logging.exception("Exception")
    DEDENT
    except (json.decoder.JSONDecodeError, ValueError) :
    INDENT
        print 'Question ID ' + questionId + ' Decode JSON has failed'
        logging.info("This qid didn't work " + questionId)
    DEDENT
    return jsondata
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

    def test_filter_with_join_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer2=Case(
                When(integer=2, then=F('o2o_rel__integer') + 1),
                When(integer=3, then=F('o2o_rel__integer')),
                default='o2o_rel__integer',
            )).order_by('pk'),
            [(1, 1), (2, 3), (3, 3)],
            transform=attrgetter('integer', 'integer2')
        )

def update_document(doc, data) :
INDENT
    for key, value in data.iteritems() :
    INDENT
        if hasattr(doc, key) :
        INDENT
            value = field_value(doc._fields [key], value)
            setattr(doc, key, value)
        DEDENT
        else :
        INDENT
            pass
        DEDENT
    DEDENT
    return doc
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

def emit(self, record) :
INDENT
    myrecord = copy.copy(record)
    levelno = myrecord.levelno
    if (levelno > = 50) :
    INDENT
        color = '\x1b[31m'
    DEDENT
    elif (levelno > = 40) :
    INDENT
        color = '\x1b[31m'
    DEDENT
    elif (levelno > = 30) :
    INDENT
        color = '\x1b[33m'
    DEDENT
    elif (levelno > = 20) :
    INDENT
        color = '\x1b[32m'
    DEDENT
    elif (levelno > = 10) :
    INDENT
        color = '\x1b[35m'
    DEDENT
    else :
    INDENT
        color = '\x1b[0m'
    DEDENT
    myrecord.msg = color + str(myrecord.msg) + '\x1b[0m'
    logging.StreamHandler.emit(self, myrecord)
DEDENT

    def test_filter_with_join_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer=Case(
                When(integer2=F('o2o_rel__integer') + 1, then=2),
                When(integer2=F('o2o_rel__integer'), then=3),
                output_field=models.IntegerField(),
            )).order_by('pk'),
            [(2, 3), (3, 3)],
            transform=attrgetter('integer', 'integer2')
        )

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

def __init__(self, parent = None) :
INDENT
    super(App, self).__init__(parent)
    self.tab = QtGui.QWidget()
    self.setCentralWidget(self.tab)
    self.tablayout = QtGui.QVBoxLayout(self.tab)
    self.canvas = CustomFigCanvas()
    self.tablayout.addWidget(self.canvas)
DEDENT

def find_subclasses(cls) :
INDENT
    all_refs = gc.get_referrers(cls)
    results = []
    for obj in all_refs :
    INDENT
        if (isinstance(obj, tuple) and
            getattr(obj [0], "__mro__", None) is obj) :
        INDENT
            results.append(obj [0])
        DEDENT
    DEDENT
    return results
DEDENT

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

    def test_filter_with_join_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer2=Case(
                When(o2o_rel__integer=1, then=1),
                When(o2o_rel__integer=2, then=3),
                When(o2o_rel__integer=3, then=4),
                output_field=models.IntegerField(),
            )).order_by('pk'),
            [(1, 1), (2, 3), (3, 4), (3, 4)],
            transform=attrgetter('integer', 'integer2')
        )

def get_fs_type(path) :
INDENT
    partition = {}
    for part in psutil.disk_partitions() :
    INDENT
        partition [part.mountpoint] = (part.fstype, part.device)
    DEDENT
    if path in partition :
    INDENT
        return partition [path]
    DEDENT
    splitpath = path.split(os.sep)
    for i in xrange(len(splitpath), 0, - 1) :
    INDENT
        path = os.sep.join(splitpath [: i]) + os.sep
        if path in partition :
        INDENT
            return partition [path]
        DEDENT
        path = os.sep.join(splitpath [: i])
        if path in partition :
        INDENT
            return partition [path]
        DEDENT
    DEDENT
    return ("unkown", "none")
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

def iterload(stream) :
INDENT
    buf = ""
    dec = json.JSONDecoder()
    for line in stream :
    INDENT
        line = line.rstrip()
        buf = buf + line
        if line == "}" :
        INDENT
            yield dec.raw_decode(buf)
            buf = ""
        DEDENT
    DEDENT
DEDENT

    def test_filter_with_annotation_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f=F('integer'),
                f_plus_1=F('integer') + 1,
            ).filter(
                integer2=Case(
                    When(integer=2, then='f_plus_1'),
                    When(integer=3, then='f'),
                ),
            ).order_by('pk'),
            [(2, 3), (3, 3)],
            transform=attrgetter('integer', 'integer2')
        )

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

def factors(num) :
INDENT
    numroot = int(math.sqrt(num)) + 1
    for i in xrange(2, numroot) :
    INDENT
        divider, remainder = divmod(num, i)
        if not remainder :
        INDENT
            yield i
            break
        DEDENT
    DEDENT
    else :
    INDENT
        yield num
        return
    DEDENT
    for factor in factors(divider) :
    INDENT
        yield factor
    DEDENT
DEDENT

def is_prime(x) :
INDENT
    if x < 2 :
    INDENT
        return False
    DEDENT
    elif x == 2 :
    INDENT
        return True
    DEDENT
    for n in range(2, x) :
    INDENT
        if x % n == 0 :
        INDENT
            return False
        DEDENT
    DEDENT
    return True
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

    def test_filter_with_annotation_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f_plus_1=F('integer') + 1,
            ).filter(
                integer=Case(
                    When(integer2=F('integer'), then=2),
                    When(integer2=F('f_plus_1'), then=3),
                    output_field=models.IntegerField(),
                ),
            ).order_by('pk'),
            [(3, 4), (2, 2), (3, 4)],
            transform=attrgetter('integer', 'integer2')
        )

def main(data) :
INDENT
    df = pd.DataFrame()
    chunksize = 5
    for i, item in enumerate(data) :
    INDENT
        df_c = pd.DataFrame.from_dict(item, orient = 'index').T
        df = df.append(df_c)
        if ((i % chunksize) == 0 or i == (len(data) - 1)) :
        INDENT
            df.to_csv(RESULT_FILE, index = False)
        DEDENT
    DEDENT
DEDENT

def bfs(graph_to_search, start, end) :
INDENT
    queue = [[start]]
    visited = set()
    while queue :
    INDENT
        path = queue.pop(0)
        vertex = path [- 1]
        if vertex == end :
        INDENT
            return path
        DEDENT
        elif vertex not in visited :
        INDENT
            for current_neighbour in graph_to_search.get(vertex, []) :
            INDENT
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
            DEDENT
            visited.add(vertex)
        DEDENT
    DEDENT
DEDENT

    def test_filter_with_annotation_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                f_plus_1=F('integer') + 1,
            ).filter(
                integer2=Case(
                    When(f_plus_1=3, then=3),
                    When(f_plus_1=4, then=4),
                    default=1,
                    output_field=models.IntegerField(),
                ),
            ).order_by('pk'),
            [(1, 1), (2, 3), (3, 4), (3, 4)],
            transform=attrgetter('integer', 'integer2')
        )

def syracuse(n, acc = None) :
INDENT
    if acc is None :
    INDENT
        acc = []
    DEDENT
    if n == 1 :
    INDENT
        acc.append(n)
        return acc
    DEDENT
    elif n % 2 == 0 :
    INDENT
        n /= 2
        acc.append(n)
        return syracuse(n, acc)
    DEDENT
    else :
    INDENT
        n = (n * 3) + 1
        acc.append(n)
        return syracuse(n, acc)
    DEDENT
DEDENT

def flatten(alist) :
INDENT
    if alist == [] :
    INDENT
        return []
    DEDENT
    elif type(alist) is not list :
    INDENT
        return [alist]
    DEDENT
    else :
    INDENT
        return flatten(alist [0]) + flatten(alist [1 :])
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
            perm1_map [p0], perm1_map [p1] = sloc, loc
            transCount += 1
        DEDENT
    DEDENT
    return (transCount % 2) == 0
DEDENT

def __init__(self) :
INDENT
    wx.Frame.__init__(self, None, wx.ID_ANY,
        "Text Validation Tutorial")
    panel = wx.Panel(self)
    textOne = wx.TextCtrl(panel, validator = CharValidator('no-alpha'))
    textTwo = wx.TextCtrl(panel, validator = CharValidator('no-digit'))
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(textOne, 0, wx.ALL, 5)
    sizer.Add(textTwo, 0, wx.ALL, 5)
    panel.SetSizer(sizer)
DEDENT

def strip_output(nb) :
INDENT
    for cell in nb.cells :
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

    def test_filter_with_aggregation_in_value(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                min=Min('fk_rel__integer'),
                max=Max('fk_rel__integer'),
            ).filter(
                integer2=Case(
                    When(integer=2, then='min'),
                    When(integer=3, then='max'),
                ),
            ).order_by('pk'),
            [(3, 4, 3, 4), (2, 2, 2, 3), (3, 4, 3, 4)],
            transform=itemgetter('integer', 'integer2', 'min', 'max')
        )

def save(self, * args, ** kwargs) :
INDENT
    if not self.auto_pseudoid :
    INDENT
        self.auto_pseudoid = generate_random_alphanumeric(16)
    DEDENT
    success = False
    failures = 0
    while not success :
    INDENT
        try :
        INDENT
            super(MyTemporaryObject, self).save(* args, ** kwargs)
        DEDENT
        except IntegrityError :
        INDENT
            failures += 1
            if failures > 5 :
            INDENT
                raise
            DEDENT
            else :
            INDENT
                self.auto_pseudoid = generate_random_alphanumeric(16)
            DEDENT
        DEDENT
        else :
        INDENT
            success = True
        DEDENT
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

def softmax(z) :
INDENT
    assert len(z.shape) == 2
    s = np.max(z, axis = 1)
    s = s [:, np.newaxis]
    e_x = np.exp(z - s)
    div = np.sum(e_x, axis = 1)
    div = div [:, np.newaxis]
    return e_x / div
DEDENT

def __getitem__(self, given) :
INDENT
    if isinstance(given, slice) :
    INDENT
        print ("slice", given.start, given.stop, given.step)
    DEDENT
    elif isinstance(given, tuple) :
    INDENT
        print ("multidim", given)
    DEDENT
    else :
    INDENT
        print ("plain", given)
    DEDENT
DEDENT

def handle_request(req) :
INDENT
    for (i, h) in enumerate(handlers) :
    INDENT
        if h [1].handles(req) :
        INDENT
            h [0] += 1
            while i > 0 and handlers [i] [0] > handlers [i - 1] [0] :
            INDENT
                handlers [i - 1], handlers [i] = handlers [i], handlers [i - 1]
                i -= 1
            DEDENT
            return h [1]
        DEDENT
    DEDENT
    return None
DEDENT

    def test_filter_with_aggregation_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                min=Min('fk_rel__integer'),
                max=Max('fk_rel__integer'),
            ).filter(
                integer=Case(
                    When(integer2=F('min'), then=2),
                    When(integer2=F('max'), then=3),
                ),
            ).order_by('pk'),
            [(3, 4, 3, 4), (2, 2, 2, 3), (3, 4, 3, 4)],
            transform=itemgetter('integer', 'integer2', 'min', 'max')
        )

def distance_from_zero(n) :
INDENT
    try :
    INDENT
        x = ast.literal_eval(n)
        if isinstance(x, (int, float)) :
        INDENT
            var = abs(x)
            print type(var)
            return var
        DEDENT
    DEDENT
    except :
    INDENT
        print "No!"
    DEDENT
DEDENT

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

def reverse(string) :
INDENT
    tmp = ""
    for i in range(1, len(string) + 1) :
    INDENT
        tmp += string [len(string) - i]
    DEDENT
    return tmp
DEDENT

    def test_filter_with_aggregation_in_predicate(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.values(*self.non_lob_fields).annotate(
                max=Max('fk_rel__integer'),
            ).filter(
                integer=Case(
                    When(max=3, then=2),
                    When(max=4, then=3),
                ),
            ).order_by('pk'),
            [(2, 3, 3), (3, 4, 4), (2, 2, 3), (3, 4, 4), (3, 3, 4)],
            transform=itemgetter('integer', 'integer2', 'max')
        )

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

def __init__(self) :
INDENT
    self.root = Tk.Tk()
    self.root.wm_title("Fibonacci Calculator")
    self.root.wm_iconbitmap("@icon2.xbm")
    Tk.Label(self.root, text = "Set the digit number you want.").pack()
    self.digits = Tk.StringVar()
    Tk.Entry(self.root, textvariable = self.digits).pack()
    Tk.Button(self.root, text = "Calculate", command = self.clicked).pack()
    self.result = Tk.Label(self.root, text = " ")
    self.result.pack()
    self.root.mainloop()
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

def mssl(lst, return_sublist = False) :
INDENT
    d = defaultdict(list)
    for i in range(len(lst) + 1) :
    INDENT
        for j in range(len(lst) + 1) :
        INDENT
            d [sum(lst [i : j])].append(lst [i : j])
        DEDENT
    DEDENT
    key = max(d.keys())
    if return_sublist :
    INDENT
        return (key, d [key])
    DEDENT
    return key
DEDENT

def __init__(self, parent) :
INDENT
    wx.Frame.__init__(self, parent, - 1, "Reference Frame", size = (300, 300))
    panel = wx.Panel(self)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.btn = wx.Button(panel, - 1, "open frame")
    self.Bind(wx.EVT_BUTTON, self.OnOpenFrame, id = self.btn.GetId())
    sizer.Add(self.btn)
    text = "This is a line.\n" * 100
    txtCtrl = wx.TextCtrl(panel, - 1, text, style = wx.TE_MULTILINE,
        size = (200, 200))
    sizer.Add(txtCtrl)
    panel.SetSizer(sizer)
    self.Centre()
    self.Show()
DEDENT

    def test_update(self):
        CaseTestModel.objects.update(
            string=Case(
                When(integer=1, then=Value('one')),
                When(integer=2, then=Value('two')),
                default=Value('other'),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 'one'), (2, 'two'), (3, 'other'), (2, 'two'), (3, 'other'), (3, 'other'), (4, 'other')],
            transform=attrgetter('integer', 'string')
        )

def equal_dicts(d1, d2, ignore_keys = ()) :
INDENT
    d1_, d2_ = d1.copy(), d2.copy()
    for k in ignore_keys :
    INDENT
        try :
        INDENT
            del d1_ [k]
        DEDENT
        except KeyError :
        INDENT
            pass
        DEDENT
        try :
        INDENT
            del d2_ [k]
        DEDENT
        except KeyError :
        INDENT
            pass
        DEDENT
    DEDENT
    return d1_ == d2_
DEDENT

def flatten(alist) :
INDENT
    if alist == [] :
    INDENT
        return []
    DEDENT
    elif type(alist) is not list :
    INDENT
        return [alist]
    DEDENT
    else :
    INDENT
        return flatten(alist [0]) + flatten(alist [1 :])
    DEDENT
DEDENT

def __call__(self, parser, namespace, values, option_string = None) :
INDENT
    for value in values :
    INDENT
        try :
        INDENT
            n, v = value.split('=')
            setattr(namespace, n, v)
        DEDENT
        except ValueError :
        INDENT
            setattr(namespace, '_unrecognized_args', values [values.index(value) :])
        DEDENT
    DEDENT
DEDENT

def foo(hive, flag) :
INDENT
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        0, win32con.KEY_READ | flag)
    count_subkey = winreg.QueryInfoKey(aKey) [0]
    for i in range(count_subkey) :
    INDENT
        try :
        INDENT
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            val = winreg.QueryValueEx(asubkey, "DisplayName") [0]
            print (val)
        DEDENT
        except EnvironmentError :
        INDENT
            continue
        DEDENT
    DEDENT
DEDENT

    def test_update_without_default(self):
        CaseTestModel.objects.update(
            integer2=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'integer2')
        )

def game_intro() :
INDENT
    intro = True
    while intro :
    INDENT
        for event in pygame.event.get() :
        INDENT
            if event.type == pygame.QUIT :
            INDENT
                quit()
            DEDENT
            mouse = pygame.mouse.get_pos()
            if 150 + 100 > mouse [0] > 150 and 430 + 50 > mouse [1] > 430 :
            INDENT
                pygame.draw.rect(gameDisplay, bright_green, (150, 430, 100, 50))
            DEDENT
            else :
            INDENT
                pygame.draw.rect(gameDisplay, green, (150, 430, 100, 50))
            DEDENT
        DEDENT
    DEDENT
DEDENT

def sanity_check(b, true_func, false_func) :
INDENT
    if b :
    INDENT
        logfunc = log.debug
        execfunc = true_func
    DEDENT
    else :
    INDENT
        logfunc = log.warning
        execfunc = false_func
    DEDENT
    logfunc('exec: %s', execfunc.__name__)
    execfunc()
DEDENT

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

    def test_update_with_expression_as_value(self):
        CaseTestModel.objects.update(
            integer=Case(
                When(integer=1, then=F('integer') + 1),
                When(integer=2, then=F('integer') + 3),
                default='integer',
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [('1', 2), ('2', 5), ('3', 3), ('2', 5), ('3', 3), ('3', 3), ('4', 4)],
            transform=attrgetter('string', 'integer')
        )

def factorize(n) :
INDENT
    divisors = itertools.count(2)
    divisor = divisors.next()
    while True :
    INDENT
        if divisor ** 2 > n :
        INDENT
            yield n
            break
        DEDENT
        a, b = divmod(n, divisor)
        if b == 0 :
        INDENT
            yield divisor
            n = a
        DEDENT
        else :
        INDENT
            divisor = divisors.next()
        DEDENT
    DEDENT
DEDENT

def getPrimes(n) :
INDENT
    yield 2
    i = 3
    while i < n :
    INDENT
        for a in getPrimes(int(math.sqrt(i)) + 1) :
        INDENT
            if i % a == 0 :
            INDENT
                break
            DEDENT
        DEDENT
        else :
        INDENT
            yield i
        DEDENT
        i += 2
    DEDENT
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

    def test_update_with_expression_as_condition(self):
        CaseTestModel.objects.update(
            string=Case(
                When(integer2=F('integer'), then=Value('equal')),
                When(integer2=F('integer') + 1, then=Value('+1')),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 'equal'), (2, '+1'), (3, '+1'), (2, 'equal'), (3, '+1'), (3, 'equal'), (4, '+1')],
            transform=attrgetter('integer', 'string')
        )

def date_hook(json_dict) :
INDENT
    for (key, value) in json_dict.items() :
    INDENT
        if type(value) is str and re.match('^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d*$', value) :
        INDENT
            json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        DEDENT
        elif type(value) is str and re.match('^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', value) :
        INDENT
            json_dict [key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        DEDENT
        else :
        INDENT
            pass
        DEDENT
    DEDENT
    return json_dict
DEDENT

def records(currentTime = Decimal('1.00')) :
INDENT
    first = True
    while True :
    INDENT
        token = lexer.get_token()
        if token :
        INDENT
            token = token.strip()
            if not token :
            INDENT
                break
            DEDENT
        DEDENT
        else :
        INDENT
            break
        DEDENT
        token = token.replace('\n', '')
        if Decimal(token) == currentTime :
        INDENT
            if first :
            INDENT
                first = False
            DEDENT
            else :
            INDENT
                yield record
            DEDENT
            currentTime += Decimal('0.1')
            record = [float(token)]
        DEDENT
        else :
        INDENT
            record.append(float(token))
        DEDENT
    DEDENT
    yield record
DEDENT

def deleteDir(dirPath) :
INDENT
    deleteFiles = []
    deleteDirs = []
    for root, dirs, files in os.walk(dirPath) :
    INDENT
        for f in files :
        INDENT
            deleteFiles.append(os.path.join(root, f))
        DEDENT
        for d in dirs :
        INDENT
            deleteDirs.append(os.path.join(root, d))
        DEDENT
    DEDENT
    for f in deleteFiles :
    INDENT
        os.remove(f)
    DEDENT
    for d in deleteDirs :
    INDENT
        os.rmdir(d)
    DEDENT
    os.rmdir(dirPath)
DEDENT

def __init__(self, master, textvariable = None, * args, ** kwargs) :
INDENT
    super(TextExtension, self).__init__(master)
    self._y_scrollbar = Scrollbar(self, orient = VERTICAL)
    self._text_widget = Text(self, yscrollcommand = self._y_scrollbar.set, * args, ** kwargs)
    self._text_widget.pack(side = LEFT, fill = BOTH, expand = 1)
    self._y_scrollbar.config(command = self._text_widget.yview)
    self._y_scrollbar.pack(side = RIGHT, fill = Y)
    if textvariable is not None :
    INDENT
        if not (isinstance(textvariable, Variable)) :
        INDENT
            raise TypeError("tkinter.Variable type expected, " + str(type(textvariable)) + " given.".format(type(textvariable)))
        DEDENT
        self._text_variable = textvariable
        self.var_modified()
        self._text_trace = self._text_widget.bind('<<Modified>>', self.text_modified)
        self._var_trace = textvariable.trace("w", self.var_modified)
    DEDENT
DEDENT

    def test_update_with_join_in_condition_raise_field_error(self):
        with self.assertRaisesMessage(FieldError, 'Joined field references are not permitted in this query'):
            CaseTestModel.objects.update(
                integer=Case(
                    When(integer2=F('o2o_rel__integer') + 1, then=2),
                    When(integer2=F('o2o_rel__integer'), then=3),
                    output_field=models.IntegerField(),
                ),
            )

def printTable(table) :
INDENT
    colWidths = [0] * len(table)
    for y in range(len(table)) :
    INDENT
        for x in table [y] :
        INDENT
            if colWidths [y] < len(x) :
            INDENT
                colWidths [y] = len(x)
            DEDENT
        DEDENT
    DEDENT
    for x in range(len(table [0])) :
    INDENT
        for y in range(len(table)) :
        INDENT
            print(table [y] [x].rjust(colWidths [y]), end = ' ')
        DEDENT
        print ()
        x += 1
    DEDENT
DEDENT

def initUI(self) :
INDENT
    self.parent.title("Contact Manager")
    self.pack(fill = BOTH, expand = 1)
    Label(self, text = "New Contact").grid(row = 0, column = 2, columnspan = 2, sticky = W)
    Label(self, text = "First Name:").grid(row = 1, column = 1, sticky = E)
    Label(self, text = "Last Name:").grid(row = 2, column = 1, sticky = E)
    Label(self, text = "Phone#").grid(row = 3, column = 1, sticky = E)
    self.entry1 = Entry(self)
    self.entry2 = Entry(self)
    self.entry3 = Entry(self)
    self.entry1.grid(row = 1, column = 2)
    self.entry2.grid(row = 2, column = 2)
    self.entry3.grid(row = 3, column = 2)
    friend_check = IntVar()
    self.friend_check = Checkbutton(self, variable = friend_check,
        command = self.friend_box,
        text = "Friend")
    self.friend_check.grid(row = 4, column = 2, columnspan = 2)
    Label(self, text = "Email:").grid(row = 5, column = 1, sticky = E)
    Label(self, text = "Birthday:").grid(row = 6, column = 1, sticky = E)
    self.entry4 = Entry(self)
    self.entry5 = Entry(self)
    self.entry4.grid(row = 5, column = 2)
    self.entry5.grid(row = 6, column = 2)
    Label(self, text = "Contact List").grid(row = 0)
    contact_lb = Listbox(self)
    for i in contacts :
    INDENT
        contact_lb.insert(END, i)
    DEDENT
    contact_lb.bind("<<ListboxSelect>>", self.onSelect)
    contact_lb.grid(row = 1, rowspan = 5)
DEDENT

def test_val(a_points, b_points, val1, val2) :
INDENT
    if val1 > val2 :
    INDENT
        a_points += 1
        return (a_points, b_points)
    DEDENT
    elif val2 > val1 :
    INDENT
        b_points += 1
        return (a_points, b_points)
    DEDENT
    elif val1 == val2 :
    INDENT
        return (a_points, b_points)
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
    if differ / square_size > 1 :
    INDENT
        mask = pyramid_reduce(mask, differ / square_size)
    DEDENT
    else :
    INDENT
        mask = cv2.resize(mask, (square_size, square_size), interpolation = cv2.INTER_AREA)
    DEDENT
    return mask
DEDENT

def __init__(self, fd) :
INDENT
    self.filename = "dummy"
    try :
    INDENT
        self.f = fd
        magic = self.f.read(4)
    DEDENT
    except IOError :
    INDENT
        self.f = fd
        magic = self.f.read(4)
    DEDENT
    if magic == "\xa1\xb2\xc3\xd4" :
    INDENT
        self.endian = "><![CDATA["
    DEDENT
    elif magic == "\xd4\xc3\xb2\xa1" :
    INDENT
        self.endian = "<"
    DEDENT
    else :
    INDENT
        raise Scapy_Exception("Not a pcap capture file (bad magic)")
    DEDENT
    hdr = self.f.read(20)
    if len(hdr) < 20 :
    INDENT
        raise Scapy_Exception("Invalid pcap file (too short)")
    DEDENT
    vermaj, vermin, tz, sig, snaplen, linktype = struct.unpack(self.endian + "HHIIII", hdr)
    self.linktype = linktype
DEDENT

    def test_update_with_join_in_predicate_raise_field_error(self):
        with self.assertRaisesMessage(FieldError, 'Joined field references are not permitted in this query'):
            CaseTestModel.objects.update(
                string=Case(
                    When(o2o_rel__integer=1, then=Value('one')),
                    When(o2o_rel__integer=2, then=Value('two')),
                    When(o2o_rel__integer=3, then=Value('three')),
                    default=Value('other'),
                    output_field=models.CharField(),
                ),
            )

def is_float(obj) :
INDENT
    if isinstance(obj, float) :
    INDENT
        return True
    DEDENT
    if isinstance(obj, int) :
    INDENT
        return False
    DEDENT
    elif isinstance(obj, str) :
    INDENT
        nodes = list(ast.walk(ast.parse(obj))) [1 :]
        if not isinstance(nodes [0], ast.Expr) :
        INDENT
            return False
        DEDENT
        if not isinstance(nodes [- 1], ast.Num) :
        INDENT
            return False
        DEDENT
        if not isinstance(nodes [- 1].n, float) :
        INDENT
            return False
        DEDENT
        nodes = nodes [1 : - 1]
        for i in range(len(nodes)) :
        INDENT
            if i % 2 == 0 :
            INDENT
                if not isinstance(nodes [i], ast.UnaryOp) :
                INDENT
                    return False
                DEDENT
            DEDENT
            else :
            INDENT
                if not isinstance(nodes [i], (ast.USub, ast.UAdd)) :
                INDENT
                    return False
                DEDENT
            DEDENT
        DEDENT
        return True
    DEDENT
    else :
    INDENT
        return False
    DEDENT
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

    def test_update_big_integer(self):
        CaseTestModel.objects.update(
            big_integer=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'big_integer')
        )

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

def polyfit2d(x, y, z, order = 3) :
INDENT
    ncols = (order + 1) ** 2
    G = np.zeros((x.size, ncols))
    ij = itertools.product(range(order + 1), range(order + 1))
    for k, (i, j) in enumerate(ij) :
    INDENT
        G [:, k] = x ** i * y ** j
    DEDENT
    m, _, _, _ = np.linalg.lstsq(G, z)
    return m
DEDENT

def fib(n) :
INDENT
    a, b = 1, 1
    for i in range(n - 1) :
    INDENT
        a, b = b, a + b
    DEDENT
    return a
DEDENT

    def test_update_binary(self):
        CaseTestModel.objects.update(
            binary=Case(
                When(integer=1, then=Value(b'one', output_field=models.BinaryField())),
                When(integer=2, then=Value(b'two', output_field=models.BinaryField())),
                default=Value(b'', output_field=models.BinaryField()),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, b'one'), (2, b'two'), (3, b''), (2, b'two'), (3, b''), (3, b''), (4, b'')],
            transform=lambda o: (o.integer, bytes(o.binary))
        )

def Activer(request, produit_id) :
INDENT
    try :
    INDENT
        produit = Produit.objects.get(pk = produit_id)
        if produit.user == request.user :
        INDENT
            produit.etat = "active"
            produit.save()
            return JsonResponse({'success' : True})
        DEDENT
        else :
        INDENT
            return JsonResponse({'error' : 'You are not allowed to edit this produit.'})
        DEDENT
    DEDENT
    except Produit.DoesNotExist :
    INDENT
        return JsonResponse({'error' : 'object dose not exist'})
    DEDENT
DEDENT

def go(iterable) :
INDENT
    itr = iter(iterable)
    try :
    INDENT
        next(num for num in itr if num % 2 == 1)
        return next(i for i, num in enumerate(itr, 1) if num % 2 == 0)
    DEDENT
    except StopIteration :
    INDENT
        return - 1
    DEDENT
DEDENT

def addToInventory(inventory, addedItems) :
INDENT
    for v in addedItems :
    INDENT
        if v in inventory.keys() :
        INDENT
            inventory [v] += 1
        DEDENT
        else :
        INDENT
            inventory [v] = 1
        DEDENT
    DEDENT
DEDENT

def queryset(self, request, queryset) :
INDENT
    filters = request.GET.copy()
    try :
    INDENT
        search_field_value = filters.pop('q') [0]
        query_params = [Q((key, search_field_value)) for key in self.search_field]
        try :
        INDENT
            queryset = queryset.filter(reduce(operator.or_, query_params))
        DEDENT
        except FieldError :
        INDENT
            pass
        DEDENT
    DEDENT
    except KeyError :
    INDENT
        pass
    DEDENT
    try :
    INDENT
        query_params = [Q((key, value)) for key, value in filters.dict().items()]
        queryset = queryset.filter(reduce(operator.or_, query_params))
    DEDENT
    except TypeError :
    INDENT
        pass
    DEDENT
    return queryset
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

def cartesian_product(set1, n) :
INDENT
    rv = set()
    if n == 0 :
    INDENT
        rv.add(())
    DEDENT
    else :
    INDENT
        rv = set()
        for x in set1 :
        INDENT
            for y in cartesian_product(set1, n - 1) :
            INDENT
                rv.add((x,) + y)
            DEDENT
        DEDENT
    DEDENT
    return rv
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

def urls() :
INDENT
    conn = sqlite3.connect('C:\Users\username\Desktop\History.sql')
    c = conn.cursor()
    query = "SELECT url, title FROM urls"
    c.execute(query)
    data = c.fetchall()
    if data :
    INDENT
        with open("C:\Users\username\Desktop\\historyulrs.csv", 'w') as outfile :
        INDENT
            writer = csv.writer(outfile)
            writer.writerow(['URL', 'Title'])
            for entry in data :
            INDENT
                writer.writerow([str(entry [0]), str(entry [1])])
            DEDENT
        DEDENT
    DEDENT
DEDENT

def summary(xs) :
INDENT
    for values in xs :
    INDENT
        try :
        INDENT
            x, y, z = values
            print (x * x + y * y + z * z)
        DEDENT
        except ValueError :
        INDENT
            print (0)
        DEDENT
    DEDENT
DEDENT

    def test_update_boolean(self):
        CaseTestModel.objects.update(
            boolean=Case(
                When(integer=1, then=True),
                When(integer=2, then=True),
                default=False,
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, True), (2, True), (3, False), (2, True), (3, False), (3, False), (4, False)],
            transform=attrgetter('integer', 'boolean')
        )

def _create_image(self, coord) :
INDENT
    (x, y) = coord
    if not getattr(self, 'one', None) :
    INDENT
        pil_img = Image.open("test.jpg")
        self.one = ImageTk.PhotoImage(pil_img)
    DEDENT
    self.canvas.create_image(x - 25, y - 25, image = self.one,
        anchor = 'nw', tags = "image")
DEDENT

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
            if selectedplant == None :
            INDENT
                sightings = Sighting.objects.all().order_by('date')
            DEDENT
            else :
            INDENT
                sightings = Sighting.objects.filter(IMS_plant = selectedplant)
            DEDENT
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

def __init__(self, stream = sys.stdout, verbosity = 1, title = None, description = None) :
INDENT
    self.stream = stream
    self.verbosity = verbosity
    if title is None :
    INDENT
        self.title = self.DEFAULT_TITLE
    DEDENT
    else :
    INDENT
        self.title = title
    DEDENT
    if description is None :
    INDENT
        self.description = self.DEFAULT_DESCRIPTION
    DEDENT
    else :
    INDENT
        self.description = description
    DEDENT
    self.startTime = datetime.datetime.now()
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

def run(self) :
INDENT
    print '>>>> skip body by not yielding (does not work)'
    with self.drivercontext(self.driverfactory) as driver :
    INDENT
        self.dostuff(driver)
    DEDENT
DEDENT

    def test_update_date(self):
        CaseTestModel.objects.update(
            date=Case(
                When(integer=1, then=date(2015, 1, 1)),
                When(integer=2, then=date(2015, 1, 2)),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [
                (1, date(2015, 1, 1)), (2, date(2015, 1, 2)), (3, None), (2, date(2015, 1, 2)),
                (3, None), (3, None), (4, None)
            ],
            transform=attrgetter('integer', 'date')
        )

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

    def test_update_date_time(self):
        CaseTestModel.objects.update(
            date_time=Case(
                When(integer=1, then=datetime(2015, 1, 1)),
                When(integer=2, then=datetime(2015, 1, 2)),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [
                (1, datetime(2015, 1, 1)), (2, datetime(2015, 1, 2)), (3, None), (2, datetime(2015, 1, 2)),
                (3, None), (3, None), (4, None)
            ],
            transform=attrgetter('integer', 'date_time')
        )

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

def countconvolve(N) :
INDENT
    try :
    INDENT
        sleepTime = random.randint(0, 5)
        time.sleep(sleepTime)
        count = sleepTime
    DEDENT
    except KeyboardInterrupt as e :
    INDENT
        pass
    DEDENT
    return count
DEDENT

def int_to_roman(number) :
INDENT
    result = ""
    for (arabic, roman) in ROMAN :
    INDENT
        (factor, number) = divmod(number, arabic)
        result += roman * factor
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

    def test_update_decimal(self):
        CaseTestModel.objects.update(
            decimal=Case(
                When(integer=1, then=Decimal('1.1')),
                When(integer=2, then=Decimal('2.2')),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [
                (1, Decimal('1.1')),
                (2, Decimal('2.2')),
                (3, None),
                (2, Decimal('2.2')),
                (3, None),
                (3, None),
                (4, None)
            ],
            transform=attrgetter('integer', 'decimal')
        )

def count_occurrences(p, letter) :
INDENT
    count = 0
    for elem in p :
    INDENT
        if isinstance(elem, str) and elem [0] == letter :
        INDENT
            count = count + 1
        DEDENT
    DEDENT
    return count
DEDENT

def leap_years(start, end) :
INDENT
    if start < 1500 or start > 2100 :
    INDENT
        return 0
    DEDENT
    if end < 1500 or end > 2100 :
    INDENT
        return 0
    DEDENT
    i, count = 0, 0
    for i in range(start, end + 1) :
    INDENT
        if i % 4 == 0 and (i % 100 ! = 0 or i % 400 == 0) :
        INDENT
            count += 1
        DEDENT
    DEDENT
    return count
DEDENT

def same_structure(a, b) :
INDENT
    if not is_list(a) and not is_list(b) :
    INDENT
        print '#1'
        return True
    DEDENT
    else :
    INDENT
        if is_list(a) and is_list(b) :
        INDENT
            print '#2'
            if len(a) ! = len(b) :
            INDENT
                print '#3'
                return False
            DEDENT
            if len(a) == len(b) :
            INDENT
                print '#4'
                for e in range(len(a)) :
                INDENT
                    print 'e = ', e, 'a[e]= ', a [e], 'b[e]=', b [e]
                    if not same_structure(a [e], b [e]) :
                    INDENT
                        return False
                    DEDENT
                DEDENT
                return True
            DEDENT
        DEDENT
        else :
        INDENT
            return False
        DEDENT
    DEDENT
DEDENT

def __init__(self) :
INDENT
    wx.Frame.__init__(self, None)
    grid = wx.grid.Grid(self)
    grid.SetTable(GridData())
    grid.EnableEditing(False)
    grid.SetSelectionMode(wx.grid.Grid.SelectRows)
    grid.SetRowLabelSize(0)
    grid.AutoSizeColumns()
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

    def test_update_duration(self):
        CaseTestModel.objects.update(
            duration=Case(
                # fails on sqlite if output_field is not set explicitly on all
                # Values containing timedeltas
                When(integer=1, then=Value(timedelta(1), output_field=models.DurationField())),
                When(integer=2, then=Value(timedelta(2), output_field=models.DurationField())),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, timedelta(1)), (2, timedelta(2)), (3, None), (2, timedelta(2)), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'duration')
        )

def get_drives() :
INDENT
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase :
    INDENT
        if bitmask & 1 :
        INDENT
            drives.append(letter)
        DEDENT
        bitmask >>= 1
    DEDENT
    return drives
DEDENT

def GetTheSentences(file) :
INDENT
    start_rx = re.compile('DELIMITER')
    end_rx = re.compile('DELIMITER2')
    start = False
    output = []
    with open(file, 'rb') as datafile :
    INDENT
        for line in datafile.readlines() :
        INDENT
            if re.match(start_rx, line) :
            INDENT
                start = True
            DEDENT
            elif re.match(end_rx, line) :
            INDENT
                start = False
            DEDENT
            if start :
            INDENT
                output.append(line)
            DEDENT
        DEDENT
    DEDENT
    return output
DEDENT

def read_relationship(filename) :
INDENT
    data = []
    with open(filename, 'rb') as f :
    INDENT
        reader = csv.reader(f, delimiter = '\t')
        next(reader, None)
        for row in reader :
        INDENT
            data.append([{
                        'source' : {
                            'id' : row [0],
                            'start' : int(row [2]),
                            'end' : int(row [3]),
                            },
                        'target' : {
                            'id' : row [1],
                            'start' : int(row [4]),
                            'end' : int(row [5]),
                            },
                        }])
        DEDENT
    DEDENT
    with open('data/data.txt', 'w') as outfile :
    INDENT
        json.dump(data, outfile)
    DEDENT
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

def quicksort(sequence, low, high) :
INDENT
    if low < high :
    INDENT
        pivot = partition(sequence, low, high)
        quicksort(sequence, low, pivot - 1)
        quicksort(sequence, pivot + 1, high)
    DEDENT
DEDENT

    def test_update_email(self):
        CaseTestModel.objects.update(
            email=Case(
                When(integer=1, then=Value('1@example.com')),
                When(integer=2, then=Value('2@example.com')),
                default=Value(''),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '1@example.com'), (2, '2@example.com'), (3, ''), (2, '2@example.com'), (3, ''), (3, ''), (4, '')],
            transform=attrgetter('integer', 'email')
        )

def get_info(session, title, url) :
INDENT
    r = session.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for items in soup.select("ul.list-unstyled") :
    INDENT
        if len(items.select("a[href^='tel:']")) :
        INDENT
            phone = items.select("a[href^='tel:']") [0].text
            break
        DEDENT
        else :
        INDENT
            phone = "N/A"
        DEDENT
    DEDENT
    print (title, phone)
DEDENT

def modify_duplicates_ordered(original) :
INDENT
    result = []
    for val in original :
    INDENT
        while val in result :
        INDENT
            val += 0.0001
        DEDENT
        result.append(val)
    DEDENT
DEDENT

def traceit(frame, event, arg) :
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
        print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
    DEDENT
    return traceit
DEDENT

def get_client_ip(request) :
INDENT
    remote_address = request.META.get('REMOTE_ADDR')
    ip = remote_address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for :
    INDENT
        proxies = x_forwarded_for.split(',')
        while (len(proxies) > 0 and
            proxies [0].startswith(PRIVATE_IPS_PREFIX)) :
        INDENT
            proxies.pop(0)
        DEDENT
        if len(proxies) > 0 :
        INDENT
            ip = proxies [0]
        DEDENT
    DEDENT
    return ip
DEDENT

def DnaCheck() :
INDENT
    for character in ['A', 'C', 'T', 'G'] :
    INDENT
        if character in (squence_str.upper()) :
        INDENT
            print "yes"
            break
        DEDENT
    DEDENT
    else :
    INDENT
        print "no"
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

def __new__(cls, name, * args) :
INDENT
    value = int(* args)
    if isinstance(value, int) :
    INDENT
        return super(NamedInt, cls).__new__(cls, name, value)
    DEDENT
    elif isinstance(value, long) :
    INDENT
        return NamedLong(name, value)
    DEDENT
DEDENT

def findWinner(contestants) :
INDENT
    if not contestants :
    INDENT
        raise Exception
    DEDENT
    if len(contestants) == 1 :
    INDENT
        return contestants [0]
    DEDENT
    return findWinner(contestants [1 : : 2])
DEDENT

def __init__(self, a_number, a_boolean, a_duck, a_sequence) :
INDENT
    self.a_number = a_number + 0
    self.a_boolean = not not a_boolean
    try :
    INDENT
        a_duck.quack
    DEDENT
    except AttributeError :
    INDENT
        raise TypeError, "can't use it if it doesn't quack"
    DEDENT
    else :
    INDENT
        self.a_duck = a_duck
    DEDENT
    try :
    INDENT
        iter(a_sequence)
    DEDENT
    except TypeError :
    INDENT
        raise TypeError, "expected an iterable sequence"
    DEDENT
    else :
    INDENT
        self.a_sequence = a_sequence
    DEDENT
DEDENT

def __init__(self) :
INDENT
    self.name = 'Random name'
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    self.coordinates = [x, y]
    tribe = random.randint(1, 2)
    if tribe == 1 :
    INDENT
        self.tribe = 'gauls'
    DEDENT
    elif tribe == 2 :
    INDENT
        self.tribe = 'teutons'
    DEDENT
DEDENT

def getSurroundingTiles(self, tile, horizontal = True, vertical = True) :
INDENT
    index = list(self.getTiles()).index(tile)
    maxtile = self.sqrtnum - 1
    i = int(math.floor(index / self.sqrtnum))
    j = int(index % self.sqrtnum)
    surroundingTiles = []
    startat = 0 if horizontal else 4
    stopat = 8 if vertical else 4
    for di, dj in dij [startat : stopat] :
    INDENT
        if 0 < = i + di < = maxtile and 0 < = j + dj < = maxtile :
        INDENT
            surroundingTiles.append(self [i + di] [j + dj])
        DEDENT
    DEDENT
    return surroundingTiles
DEDENT

def numpy_ewma(data, window) :
INDENT
    alpha = 2 / (window + 1.0)
    scale = 1 / (1 - alpha)
    n = data.shape [0]
    scale_arr = (1 - alpha) ** (- 1 * np.arange(n))
    weights = (1 - alpha) ** np.arange(n)
    pw0 = (1 - alpha) ** (n - 1)
    mult = data * pw0 * scale_arr
    cumsums = mult.cumsum()
    out = cumsums * scale_arr [: : - 1] / weights.cumsum()
    return out
DEDENT

def __enter__(self) :
INDENT
    super().__enter__()
    try :
    INDENT
        self.i = self.enter_context(open(self.in_file_name, 'r'))
        self.o = self.enter_context(open(self.out_file_name, 'w'))
    DEDENT
    except :
    INDENT
        if not self.__exit__(* sys.exc_info()) :
        INDENT
            raise
        DEDENT
    DEDENT
    return self
DEDENT

    def test_update_file(self):
        CaseTestModel.objects.update(
            file=Case(
                When(integer=1, then=Value('~/1')),
                When(integer=2, then=Value('~/2')),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '~/1'), (2, '~/2'), (3, ''), (2, '~/2'), (3, ''), (3, ''), (4, '')],
            transform=lambda o: (o.integer, str(o.file))
        )

def get_value(mydict, keys) :
INDENT
    if not keys :
    INDENT
        return mydict
    DEDENT
    key = keys [0]
    try :
    INDENT
        newdict = mydict [key]
    DEDENT
    except (TypeError, KeyError) :
    INDENT
        return 0
    DEDENT
    return get_value(newdict, keys [1 :])
DEDENT

def draw(self) :
INDENT
    if self._free() == 0 :
    INDENT
        return False
    DEDENT
    i = random.randint(0, 2 ** 32 - 1)
    while self.used [i] :
    INDENT
        i = (i + 1) % 2 ** 32
    DEDENT
    self.used [i] = True
    return i
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

def permute(items) :
INDENT
    length = len(items)
    def inner(ix = []) :
    INDENT
        do_yield = len(ix) == length - 1
        for i in range(0, length) :
        INDENT
            if i in ix :
            INDENT
                continue
            DEDENT
            if do_yield :
            INDENT
                yield tuple([items [y] for y in ix + [i]])
            DEDENT
            else :
            INDENT
                for p in inner(ix + [i]) :
                INDENT
                    yield p
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return inner()
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

def __init__(self, parent = None) :
INDENT
    super().__init__(parent)
    self.log_txt = QtWidgets.QPlainTextEdit(self)
    self.log_txt.setReadOnly(True)
    layout = QtWidgets.QHBoxLayout(self)
    layout.addWidget(self.log_txt)
    self.setWindowTitle('Event Log')
DEDENT

def printFigure(rows) :
INDENT
    if rows > 0 :
    INDENT
        printFigure(rows - 1)
        if rows % 2 == 0 :
        INDENT
            while (rows > 0) :
            INDENT
                print(str(rows) [: : - 1], end = '')
                rows -= 1
            DEDENT
            print ('')
        DEDENT
        else :
        INDENT
            i = 1
            while (i < = rows) :
            INDENT
                print(str(i), end = '')
                i += 1
            DEDENT
            print ('')
        DEDENT
    DEDENT
DEDENT

    def test_update_file_path(self):
        CaseTestModel.objects.update(
            file_path=Case(
                When(integer=1, then=Value('~/1')),
                When(integer=2, then=Value('~/2')),
                default=Value(''),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '~/1'), (2, '~/2'), (3, ''), (2, '~/2'), (3, ''), (3, ''), (4, '')],
            transform=attrgetter('integer', 'file_path')
        )

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

def my_function(a) :
INDENT
    a = iter(a)
    while True :
    INDENT
        yield 10 * next(a)
        yield next(a)
        yield "foo" + next(a)
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

    def test_update_float(self):
        CaseTestModel.objects.update(
            float=Case(
                When(integer=1, then=1.1),
                When(integer=2, then=2.2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1.1), (2, 2.2), (3, None), (2, 2.2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'float')
        )

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

def get_info(session, title, url) :
INDENT
    r = session.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for items in soup.select("ul.list-unstyled") :
    INDENT
        if len(items.select("a[href^='tel:']")) :
        INDENT
            phone = items.select("a[href^='tel:']") [0].text
            break
        DEDENT
        else :
        INDENT
            phone = "N/A"
        DEDENT
    DEDENT
    print (title, phone)
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

def send_email(user, pwd, recipient, subject, body) :
INDENT
    import smtplib
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try :
    INDENT
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    DEDENT
    except :
    INDENT
        print "failed to send mail"
    DEDENT
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

def bfs(graph, forefront, end) :
INDENT
    next_forefront = [(node, path + ',' + node) for i, path in forefront if i in graph for node in graph [i]]
    for node, path in next_forefront :
    INDENT
        if node == end :
        INDENT
            return path
        DEDENT
    DEDENT
    else :
    INDENT
        return bfs(graph, next_forefront, end)
    DEDENT
DEDENT

def punk(s) :
INDENT
    counter = 0
    for char in s :
    INDENT
        if char == 'z' :
        INDENT
            counter += 1
        DEDENT
    DEDENT
    return int(counter > = 3)
DEDENT

def to_bool(value) :
INDENT
    if type(value) == type('') :
    INDENT
        if value.lower() in ("yes", "y", "true", "t", "1") :
        INDENT
            return True
        DEDENT
        if value.lower() in ("no", "n", "false", "f", "0", "") :
        INDENT
            return False
        DEDENT
        raise Exception('Invalid value for boolean conversion: ' + value)
    DEDENT
    return bool(value)
DEDENT

    @unittest.skipUnless(Image, "Pillow not installed")
    def test_update_image(self):
        CaseTestModel.objects.update(
            image=Case(
                When(integer=1, then=Value('~/1')),
                When(integer=2, then=Value('~/2')),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '~/1'), (2, '~/2'), (3, ''), (2, '~/2'), (3, ''), (3, ''), (4, '')],
            transform=lambda o: (o.integer, str(o.image))
        )

def parse(self, response) :
INDENT
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//div[@id="col_3"]//div[@id="module3_1"]//div[@id="moduleData4952"]')
    items = []
    for site in sites :
    INDENT
        item = Website()
        item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
        item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c4"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c6"]//text()').extract()
        items.append(item)
    DEDENT
    self.task_urls.remove(response.url)
    if self.task_urls :
    INDENT
        r = Request(url = self.task_urls [0], callback = self.parse)
        items.append(r)
    DEDENT
    return items
DEDENT

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

def almostIncreasingSequence(list) :
INDENT
    removedIdx = []
    for idx, item in enumerate(list) :
    INDENT
        tmp = []
        for i in range(idx - 1, - 1, - 1) :
        INDENT
            if list [idx] < = list [i] :
            INDENT
                tmp.append(i)
            DEDENT
        DEDENT
        if len(tmp) > 1 :
        INDENT
            removedIdx.append(idx)
        DEDENT
        else :
        INDENT
            if len(tmp) > 0 :
            INDENT
                removedIdx.append(tmp [0])
            DEDENT
        DEDENT
    DEDENT
    return len(set(removedIdx)) < = 1
DEDENT

def add_list_attributes(klass) :
INDENT
    old_init = klass.__init__
    def new_init(self, * args, ** kwargs) :
    INDENT
        for attribute in klass.list_attributes :
        INDENT
            setattr(self, attribute, [])
        DEDENT
        old_init(self, * args, ** kwargs)
    DEDENT
    klass.__init__ = new_init
    return klass
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

    def test_update_generic_ip_address(self):
        CaseTestModel.objects.update(
            generic_ip_address=Case(
                # fails on postgresql if output_field is not set explicitly
                When(integer=1, then=Value('1.1.1.1')),
                When(integer=2, then=Value('2.2.2.2')),
                output_field=models.GenericIPAddressField(),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '1.1.1.1'), (2, '2.2.2.2'), (3, None), (2, '2.2.2.2'), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'generic_ip_address')
        )

def find_v0(xstar, v0_est, theta, ystar, g_earth, lamb, tstar_est,
eps_x = 1.0e-3, num_try = 6) :
INDENT
    flg_success = False
    v0_hist = []
    x_drag_at_tstar_hist = []
    jtry_end = None
    for jtry in range(num_try) :
    INDENT
        tstar_est, x_drag_at_tstar_est, y_drag_at_tstar_est, flg_success_x_drag = calc_x_drag_at_tstar(v0_est, theta, ystar, g_earth, lamb, tstar_est)
        v0_hist.append(v0_est)
        x_drag_at_tstar_hist.append(x_drag_at_tstar_est)
        if not flg_success_x_drag :
        INDENT
            break
        DEDENT
        elif abs(x_drag_at_tstar_est - xstar) < eps_x :
        INDENT
            flg_success = True
            jtry_end = jtry
            break
        DEDENT
        else :
        INDENT
            if len(v0_hist) < 2 :
            INDENT
                dx = xstar - x_drag_at_tstar_est
                dv0 = dx / (tstar_est * np.cos(theta))
                v0_est += dv0
            DEDENT
            else :
            INDENT
                v0_est = v0_hist [- 2] + (v0_hist [- 1] - v0_hist [- 2]) * (xstar - x_drag_at_tstar_hist [- 2]) / (x_drag_at_tstar_hist [- 1] - x_drag_at_tstar_hist [- 2])
            DEDENT
        DEDENT
    DEDENT
    return (v0_est, tstar_est, flg_success, jtry_end)
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

def __init__(self, iterable, ** kwargs) :
INDENT
    super(AttrDict, self).__init__(iterable, ** kwargs)
    for key, value in iterable.items() :
    INDENT
        if isinstance(value, dict) :
        INDENT
            self.__dict__ [key] = AttrDict(value)
        DEDENT
        else :
        INDENT
            self.__dict__ [key] = value
        DEDENT
    DEDENT
DEDENT

def paintEvent(self, event) :
INDENT
    super(MySlider, self).paintEvent(event)
    qp = QPainter(self)
    pen = QPen()
    pen.setWidth(2)
    pen.setColor(Qt.red)
    qp.setPen(pen)
    font = QFont('Times', 10)
    qp.setFont(font)
    self.setContentsMargins(50, 50, 50, 50)
    contents = self.contentsRect()
    self.setFixedSize(QSize(slider_x, slider_y))
    max_slider = self.maximum()
    min_slider = self.minimum()
    len_slider = max_slider - min_slider
    height = self.height()
    opt = QStyleOptionSlider()
    handle = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
    handle_height = handle.height()
    height_diff = height - handle_height
    point_size = font.pointSize()
    for i in range(max_slider) :
    INDENT
        y = round(((1 - i / len_slider) * height_diff + (handle_height / 2.0))) - 1
        if i == 0 :
        INDENT
            y = self.height() - handle_height / 2.0
        DEDENT
        qp.drawText(contents.x() - point_size, y + point_size / 2, '{0:2}'.format(slider_step [len_slider - i]))
        qp.drawLine(contents.x() + point_size, y, contents.x() + contents.width(), y)
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

    def test_update_null_boolean(self):
        CaseTestModel.objects.update(
            null_boolean=Case(
                When(integer=1, then=True),
                When(integer=2, then=False),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, True), (2, False), (3, None), (2, False), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'null_boolean')
        )

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

def update(d, u) :
INDENT
    for k, v in u.iteritems() :
    INDENT
        if isinstance(v, collections.Mapping) :
        INDENT
            d [k] = update(d.get(k, {}), v)
        DEDENT
        else :
        INDENT
            d [k] = v
        DEDENT
    DEDENT
    return d
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

def flattenjson(b, delim) :
INDENT
    val = {}
    for i in b.keys() :
    INDENT
        if isinstance(b [i], dict) :
        INDENT
            get = flattenjson(b [i], delim)
            for j in get.keys() :
            INDENT
                val [i + delim + j] = get [j]
            DEDENT
        DEDENT
        else :
        INDENT
            val [i] = b [i]
        DEDENT
    DEDENT
    return val
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

    def test_update_null_boolean_old(self):
        CaseTestModel.objects.update(
            null_boolean_old=Case(
                When(integer=1, then=True),
                When(integer=2, then=False),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, True), (2, False), (3, None), (2, False), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'null_boolean_old')
        )

def changeFileCreationTime(fname, newtime) :
INDENT
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)
    win32file.SetFileTime(winfile, wintime, None, None)
    winfile.close()
DEDENT

def is_sequence_same(list_a, list_b) :
INDENT
    if list_a and list_a [0] in list_b :
    INDENT
        first = list_b.index(list_a [0])
    DEDENT
    else :
    INDENT
        return False
    DEDENT
    return list_a == (list_b [first :] + list_b [: first])
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

def roll_die(die_type, print_op = False) :
INDENT
    roll_result = random.randint(1, die_type)
    if print_op :
    INDENT
        print ("Roll: {0}.".format(roll_result))
    DEDENT
    return roll_result
DEDENT

def run(self) :
INDENT
    print '>>>> skip body by not yielding (does not work)'
    with self.drivercontext(self.driverfactory) as driver :
    INDENT
        self.dostuff(driver)
    DEDENT
DEDENT

    def test_update_positive_integer(self):
        CaseTestModel.objects.update(
            positive_integer=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'positive_integer')
        )

def get_client_ip(request) :
INDENT
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for :
    INDENT
        ip = x_forwarded_for.split(',') [- 1].strip()
    DEDENT
    else :
    INDENT
        ip = request.META.get('REMOTE_ADDR')
    DEDENT
    return ip
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

    def test_update_positive_small_integer(self):
        CaseTestModel.objects.update(
            positive_small_integer=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'positive_small_integer')
        )

def searchContact() :
INDENT
    number = raw_input("Enter phone number to search data : ")
    obj1 = open("file.txt", "r")
    for line in obj1.readlines() :
    INDENT
        if number in line :
        INDENT
            print (line)
        DEDENT
    DEDENT
    obj1.close()
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

def singleton(class_) :
INDENT
    class class_w(class_) :
    INDENT
        _instance = None
        def __new__(class2, * args, ** kwargs) :
        INDENT
            if class_w._instance is None :
            INDENT
                class_w._instance = super(class_w, class2).__new__(class2, * args, ** kwargs)
                class_w._instance._sealed = False
            DEDENT
            return class_w._instance
        DEDENT
        def __init__(self, * args, ** kwargs) :
        INDENT
            if self._sealed :
            INDENT
                return
            DEDENT
            super(class_w, self).__init__(* args, ** kwargs)
            self._sealed = True
        DEDENT
    DEDENT
    class_w.__name__ = class_.__name__
    return class_w
DEDENT

def fib(n) :
INDENT
    if n == 2 :
    INDENT
        try :
        INDENT
            fib.two_count += 1
        DEDENT
        except AttributeError :
        INDENT
            fib.two_count = 1
        DEDENT
    DEDENT
    if n == 0 or n == 1 :
    INDENT
        return n
    DEDENT
    else :
    INDENT
        return fib(n - 1) + fib(n - 2)
    DEDENT
DEDENT

    def test_update_slug(self):
        CaseTestModel.objects.update(
            slug=Case(
                When(integer=1, then=Value('1')),
                When(integer=2, then=Value('2')),
                default=Value(''),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '1'), (2, '2'), (3, ''), (2, '2'), (3, ''), (3, ''), (4, '')],
            transform=attrgetter('integer', 'slug')
        )

def window(iterable, n = 2) :
INDENT
    "s -> (s0, ...,s(n-1)), (s1, ...,sn), (s2, ..., s(n+1)), ..."
    iters = tee(iterable, n)
    for i, it in enumerate(iters) :
    INDENT
        consume(it, i)
    DEDENT
    return zip(* iters)
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

def fires(event, before = True) :
INDENT
    if before :
    INDENT
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
    DEDENT
    else :
    INDENT
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
    DEDENT
    return decorator
DEDENT

    def test_update_small_integer(self):
        CaseTestModel.objects.update(
            small_integer=Case(
                When(integer=1, then=1),
                When(integer=2, then=2),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, 1), (2, 2), (3, None), (2, 2), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'small_integer')
        )

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

def is_cgi(self) :
INDENT
    collapsed_path = CGIHTTPServer._url_collapse_path(self.path)
    dir_sep = collapsed_path.find('/', 1)
    head, tail = collapsed_path [: dir_sep], collapsed_path [dir_sep + 1 :]
    if head in self.cgi_directories :
    INDENT
        if not tail.endswith('.html') :
        INDENT
            self.cgi_info = head, tail
            return True
        DEDENT
    DEDENT
    return False
DEDENT

    def test_update_string(self):
        CaseTestModel.objects.filter(string__in=['1', '2']).update(
            string=Case(
                When(integer=1, then=Value('1', output_field=models.CharField())),
                When(integer=2, then=Value('2', output_field=models.CharField())),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(string__in=['1', '2']).order_by('pk'),
            [(1, '1'), (2, '2'), (2, '2')],
            transform=attrgetter('integer', 'string')
        )

def change_keys(obj, convert) :
INDENT
    if isinstance(obj, dict) :
    INDENT
        new = {}
        for k, v in obj.iteritems() :
        INDENT
            new [convert(k)] = change_keys(v, convert)
        DEDENT
    DEDENT
    elif isinstance(obj, list) :
    INDENT
        new = []
        for v in obj :
        INDENT
            new.append(change_keys(v, convert))
        DEDENT
    DEDENT
    else :
    INDENT
        return obj
    DEDENT
    return new
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

def visit_Call(self, node) :
INDENT
    debug("function", node.func.id)
    if node.func.id in functions :
    INDENT
        debug("defined function")
        func_visit(functions [node.func.id], node.args)
        return
    DEDENT
    debug("not defined function", node.func.id)
    generate(node.func.id)
    generate("(")
    sep = ""
    for arg in node.args :
    INDENT
        generate(sep)
        self.visit(arg)
        sep = ","
    DEDENT
    generate(")")
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

def __init__(self, parent) :
INDENT
    self.root = parent
    self.root.geometry('250x150')
    self.root.title("DiscreteMaths_3_1")
    Label_1 = tk.Label(self.root, text = "Input")
    Label_2 = tk.Label(self.root, text = "Output")
    Label_1.grid(row = 0)
    Label_2.grid(row = 1)
    self.inputField = tk.Entry(self.root)
    self.outputField = tk.Entry(self.root)
    self.inputField.grid(row = 0, column = 1)
    self.outputField.grid(row = 1, column = 1)
    self.inputField.bind('<Return>', self.printLine)
DEDENT

def get_list(self, term, offset = 0, limit = DEFAULT_PAGE_SIZE) :
INDENT
    filters = list(
        field.ilike(u'%%%s%%' % term) for field in self._cached_fields
        )
    filters.append(Organisation.org_id == "Google")
    return (
        db.session.query(Product)
        .join(organisation_products_table)
        .join(Organisation)
        .filter(* filters)
        .all())
DEDENT

def prime(n) :
INDENT
    for x in range(2, int(math.sqrt(n)) + 1) :
    INDENT
        if n % x == 0 :
        INDENT
            print n / x
            return prime(n / x)
        DEDENT
    DEDENT
DEDENT

def read_file() :
INDENT
    fname = 'InputFile.bak'
    if os.path.exists(fname) :
    INDENT
        fsize = os.path.getsize(fname)
        with open(fname, 'rb') as fh :
        INDENT
            while fh.tell() < fsize :
            INDENT
                item = cPickle.load(fh)
                for k, v in item.iteritems() :
                INDENT
                    print v [0], "\t", v [1], "\t", k
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    else :
    INDENT
        item_name = {}
    DEDENT
DEDENT

    def test_update_text(self):
        CaseTestModel.objects.update(
            text=Case(
                When(integer=1, then=Value('1')),
                When(integer=2, then=Value('2')),
                default=Value(''),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, '1'), (2, '2'), (3, ''), (2, '2'), (3, ''), (3, ''), (4, '')],
            transform=attrgetter('integer', 'text')
        )

def window(iterable, n) :
INDENT
    els = tee(iterable, n)
    for i, el in enumerate(els) :
    INDENT
        for _ in xrange(i) :
        INDENT
            next(el, None)
        DEDENT
    DEDENT
    return izip(* els)
DEDENT

def plotPerfect(df, spline) :
INDENT
    ax = df.plot()
    if not spline :
    INDENT
        ax.set_frame_on(False)
    DEDENT
    return ax
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

def unique_file(input_filename, output_filename) :
INDENT
    with open(input_filename) as file :
    INDENT
        contents = file.read()
        word_set = set(contents.split())
    DEDENT
    with open(output_filename, "w+") as output_file :
    INDENT
        for word in word_set :
        INDENT
            output_file.write(word + '\n')
        DEDENT
    DEDENT
    print ("Done")
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

def long_substr(strings) :
INDENT
    substr = ""
    if not strings :
    INDENT
        return substr
    DEDENT
    reference = shortest_of(strings)
    length = len(reference)
    for i in xrange(length) :
    INDENT
        for j in xrange(i + len(substr) + 1, length + 1) :
        INDENT
            candidate = reference [i : j]
            if all(candidate in text for text in strings) :
            INDENT
                substr = candidate
            DEDENT
        DEDENT
    DEDENT
    return substr
DEDENT

    def test_update_time(self):
        CaseTestModel.objects.update(
            time=Case(
                # fails on sqlite if output_field is not set explicitly on all
                # Values containing times
                When(integer=1, then=Value(time(1), output_field=models.TimeField())),
                When(integer=2, then=Value(time(2), output_field=models.TimeField())),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, time(1)), (2, time(2)), (3, None), (2, time(2)), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'time')
        )

def distance_from_zero(n) :
INDENT
    try :
    INDENT
        return abs(float(n))
    DEDENT
    except ValueError :
    INDENT
        return "That is not an integer or float!"
    DEDENT
DEDENT

def upgrade() :
INDENT
    op.create_table('client_credential',
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
    client_credential = sa.sql.table('client_credential',
        sa.Column('client_id', sa.Integer, nullable = False),
        sa.Column('is_active', sa.Boolean, nullable = False, default = True),
        sa.Column('key', sa.String(22), nullable = False, default = True),
        sa.Column('secret', sa.String(22), nullable = False, default = True),
        sa.Column('created_at', sa.DateTime, nullable = False, default = sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable = False, default = sa.func.now()),
        )
    conn = op.get_bind()
    res = conn.execute("select secret, key, id from client")
    results = res.fetchall()
    clients = [{'secret' : r [0], 'key' : r [1], 'is_active' : True, 'client_id' : r [2], 'created_at' : datetime.datetime.now(), 'updated_at' : datetime.datetime.now()} for r in results]
    op.bulk_insert(client_credential, clients)
    op.drop_column(u'client', u'secret')
    op.drop_column(u'client', u'key')
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

def remove_adjacent(nums) :
INDENT
    result = []
    for num in nums :
    INDENT
        if len(result) == 0 or num ! = result [- 1] :
        INDENT
            result.append(num)
        DEDENT
    DEDENT
    return result
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

def Run(self) :
INDENT
    self.time0 = time.clock()
    try :
    INDENT
        source = open(self.src, 'rb')
        import os
        (st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime) = os.stat(self.src)
        num_blocks = st_size / self.block_size
        current_block = 0
        self.JobBeginning(num_blocks)
        dest = open(self.dest, 'wb')
        while 1 :
        INDENT
            copy_buffer = source.read(self.block_size)
            if copy_buffer :
            INDENT
                dest.write(copy_buffer)
                current_block += 1
                self.JobProgress(current_block)
                self.PossibleStoppingPoint()
            DEDENT
            else :
            INDENT
                break
            DEDENT
        DEDENT
        source.close()
        dest.close()
    DEDENT
    except InterruptedException :
    INDENT
        dest.close()
        os.unlink(self.dest)
        print "canceled, dest deleted!"
    DEDENT
    self.JobFinished()
DEDENT

def reverseParentheses(s) :
INDENT
    if '(' in s :
    INDENT
        posopen = s.find('(')
        s = s [: posopen] + reverseParentheses(s [posopen + 1 :])
        posclose = s.find(')', posopen + 1)
        s = s [: posopen] + s [posopen : posclose] [: : - 1] + s [posclose + 1 :]
    DEDENT
    return s
DEDENT

    def test_update_url(self):
        CaseTestModel.objects.update(
            url=Case(
                When(integer=1, then=Value('http://1.example.com/')),
                When(integer=2, then=Value('http://2.example.com/')),
                default=Value(''),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [
                (1, 'http://1.example.com/'), (2, 'http://2.example.com/'), (3, ''), (2, 'http://2.example.com/'),
                (3, ''), (3, ''), (4, '')
            ],
            transform=attrgetter('integer', 'url')
        )

def breakdown(li) :
INDENT
    result = []
    for i in range(len(li) - 1, - 1, - 1) :
    INDENT
        result.append(li [: i + 1])
    DEDENT
    return result
DEDENT

def scraper(pageNum) :
INDENT
    while pageNum < SOME_TARGET_VALUE :
    INDENT
        req = Request("http://www.someurl.com/Search/page=" + str(pageNum) + "&facet_Category=20", headers = {"User-Agent" : "Mozilla/5.0"})
        html = urlopen(req).read()
        bsObj = BeautifulSoup(html)
        for result in bsObj.select("h2 a") :
        INDENT
            print (result ["href"])
        DEDENT
        pageNum += 1
    DEDENT
DEDENT

def decorate(function) :
INDENT
    def wrap_function(* args, ** kwargs) :
    INDENT
        str = 'Hello!'
        args.insert(1, str)
        return function(* args, ** kwargs)
    DEDENT
    return wrap_function
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

    def test_update_uuid(self):
        CaseTestModel.objects.update(
            uuid=Case(
                # fails on sqlite if output_field is not set explicitly on all
                # Values containing UUIDs
                When(integer=1, then=Value(
                    UUID('11111111111111111111111111111111'),
                    output_field=models.UUIDField(),
                )),
                When(integer=2, then=Value(
                    UUID('22222222222222222222222222222222'),
                    output_field=models.UUIDField(),
                )),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [
                (1, UUID('11111111111111111111111111111111')),
                (2, UUID('22222222222222222222222222222222')),
                (3, None),
                (2, UUID('22222222222222222222222222222222')),
                (3, None),
                (3, None),
                (4, None),
            ],
            transform=attrgetter('integer', 'uuid')
        )

def formatTime(self, record, datefmt = None) :
INDENT
    ct = self.converter(record.created)
    if datefmt :
    INDENT
        s = time.strftime(datefmt, ct)
    DEDENT
    else :
    INDENT
        t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
        s = "%s.%03d" % (t, record.msecs)
    DEDENT
    return s
DEDENT

def linear_merge(list1, list2) :
INDENT
    list1 = iter(list1)
    list2 = iter(list2)
    value1 = next(list1)
    value2 = next(list2)
    while True :
    INDENT
        if value1 < = value2 :
        INDENT
            yield value1
            try :
            INDENT
                value1 = next(list1)
            DEDENT
            except StopIteration :
            INDENT
                yield value2
                while True :
                INDENT
                    yield next(list2)
                DEDENT
            DEDENT
        DEDENT
        else :
        INDENT
            yield value2
            try :
            INDENT
                value2 = next(list2)
            DEDENT
            except StopIteration :
            INDENT
                yield value1
                while True :
                INDENT
                    yield next(list1)
                DEDENT
            DEDENT
        DEDENT
    DEDENT
DEDENT

def find_neighbors(tess) :
INDENT
    neighbors = defaultdict(set)
    for simplex in tess.simplices :
    INDENT
        for idx in simplex :
        INDENT
            other = set(simplex)
            other.remove(idx)
            neighbors [idx] = neighbors [idx].union(other)
        DEDENT
    DEDENT
    return neighbors
DEDENT

def file_filter(name) :
INDENT
    lst = []
    idtile = None
    for line in file(name, mode = "r") :
    INDENT
        element = line.split()
        if idtile is None :
        INDENT
            idtile = (int(element [0]), int(element [1]))
        DEDENT
        if (int(element [0]), int(element [1])) == idtile :
        INDENT
            lst.append(element [2 :])
            dy, dx = int(element [0]), int(element [1])
        DEDENT
        else :
        INDENT
            yield lst, dx, dy
            lst = []
            idtile = None
        DEDENT
    DEDENT
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

    def test_update_fk(self):
        obj1, obj2 = CaseTestModel.objects.all()[:2]

        CaseTestModel.objects.update(
            fk=Case(
                When(integer=1, then=obj1.pk),
                When(integer=2, then=obj2.pk),
            ),
        )
        self.assertQuerysetEqual(
            CaseTestModel.objects.all().order_by('pk'),
            [(1, obj1.pk), (2, obj2.pk), (3, None), (2, obj2.pk), (3, None), (3, None), (4, None)],
            transform=attrgetter('integer', 'fk_id')
        )

def distance_from_zero(n) :
INDENT
    try :
    INDENT
        return abs(float(n))
    DEDENT
    except ValueError :
    INDENT
        return "That is not an integer or float!"
    DEDENT
DEDENT

def window(iterable, n = 2) :
INDENT
    "s -> (s0, ...,s(n-1)), (s1, ...,sn), (s2, ..., s(n+1)), ..."
    iters = tee(iterable, n)
    for i, it in enumerate(iters) :
    INDENT
        consume(it, i)
    DEDENT
    return zip(* iters)
DEDENT

def __init__(self, parent, id, title) :
INDENT
    wx.Frame.__init__(self, parent, id, title)
    vbox = wx.BoxSizer(wx.VERTICAL)
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    button = wx.Button(self, wx.ID_OK, "GoTo Blue Panel")
    self.Bind(wx.EVT_BUTTON, self.OnButton, button)
    hbox.Add(button, 0, wx.ALL, 5)
    self.nb = MyFlatNotebook(self)
    vbox.Add(hbox, 0, wx.EXPAND)
    vbox.Add(self.nb, 1, wx.EXPAND)
    self.SetSizer(vbox)
DEDENT

def to_bool(value) :
INDENT
    if type(value) == type('') :
    INDENT
        if value.lower() in ("yes", "y", "true", "t", "1") :
        INDENT
            return True
        DEDENT
        if value.lower() in ("no", "n", "false", "f", "0", "") :
        INDENT
            return False
        DEDENT
        raise Exception('Invalid value for boolean conversion: ' + value)
    DEDENT
    return bool(value)
DEDENT

    def test_lookup_in_condition(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                test=Case(
                    When(integer__lt=2, then=Value('less than 2')),
                    When(integer__gt=2, then=Value('greater than 2')),
                    default=Value('equal to 2'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [
                (1, 'less than 2'), (2, 'equal to 2'), (3, 'greater than 2'), (2, 'equal to 2'), (3, 'greater than 2'),
                (3, 'greater than 2'), (4, 'greater than 2')
            ],
            transform=attrgetter('integer', 'test')
        )

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

def fib(n) :
INDENT
    a, b = 0, 1
    for _ in xrange(n) :
    INDENT
        yield a
        a, b = b, a + b
    DEDENT
DEDENT

def treeToList(root, order = Order.INORDER) :
INDENT
    ret = list()
    def inorder_traversal(node) :
    INDENT
        if node is not None :
        INDENT
            inorder_traversal(node.right)
            ret.append(node.data)
            inorder_traversal(node.down)
        DEDENT
    DEDENT
    def preorder_traversal(node) :
    INDENT
        if node is not None :
        INDENT
            ret.append(node.data)
            preorder_traversal(node.right)
            preorder_traversal(node.down)
        DEDENT
    DEDENT
    def postorder_traversal(node) :
    INDENT
        if node is not None :
        INDENT
            postorder_traversal(node.right)
            postorder_traversal(node.down)
            ret.append(node.data)
        DEDENT
    DEDENT
    if order == Order.PREORDER :
    INDENT
        preorder_traversal(node)
    DEDENT
    elif order == Order.INORDER :
    INDENT
        inorder_traversal(node)
    DEDENT
    else :
    INDENT
        postorder_traversal(node)
    DEDENT
    return ret
DEDENT

def morse(s) :
INDENT
    outputs = ''
    for item in s :
    INDENT
        outputs += morsecode.get(item, item)
    DEDENT
    return outputs
DEDENT

    def test_lookup_different_fields(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                test=Case(
                    When(integer=2, integer2=3, then=Value('when')),
                    default=Value('default'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [
                (1, 1, 'default'), (2, 3, 'when'), (3, 4, 'default'), (2, 2, 'default'), (3, 4, 'default'),
                (3, 3, 'default'), (4, 5, 'default')
            ],
            transform=attrgetter('integer', 'integer2', 'test')
        )

def _compute_pos_order_total(self) :
INDENT
    for partner in self :
    INDENT
        total = 0.0
        for order in partner.pos_order_ids :
        INDENT
            total += order.amount_total
        DEDENT
        partner.pos_order_total = total
    DEDENT
DEDENT

def find_items_within(l1, l2, dist) :
INDENT
    l1.sort()
    l2.sort()
    b = 0
    e = 0
    ans = []
    for a in l1 :
    INDENT
        while b < len(l2) and a - l2 [b] > dist :
        INDENT
            b += 1
        DEDENT
        while e < len(l2) and l2 [e] - a < = dist :
        INDENT
            e += 1
        DEDENT
        ans.extend([(a, x) for x in l2 [b : e]])
    DEDENT
    return ans
DEDENT

def longestSubstringFinder(string1, string2) :
INDENT
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1) :
    INDENT
        match = ""
        for j in range(len2) :
        INDENT
            if (i + j < len1 and string1 [i + j] == string2 [j]) :
            INDENT
                match += string2 [j]
            DEDENT
            else :
            INDENT
                if (len(match) > len(answer)) : answer = match
                match = ""
            DEDENT
        DEDENT
    DEDENT
    return answer
DEDENT

def moto_boto() :
INDENT
    @ mock_s3
    def boto_resource() :
    INDENT
        res = boto3.resource('s3')
        res.create_bucket(Bucket = BUCKET)
        return res
    DEDENT
    return boto_resource
DEDENT

def device_id_replace(filepath) :
INDENT
    original_id = input("What device ID are you needing to replace?")
    new_id = input("What is the new device ID?")
    with open(filepath, 'r+') as devicetxt :
    INDENT
        contents = devicetxt.readlines()
        for line_i, line in enumerate(contents) :
        INDENT
            if original_id in line :
            INDENT
                contents [line_i] = line.replace(original_id, new_id)
            DEDENT
        DEDENT
        devicetxt.truncate(0)
        devicetxt.seek(0)
        devicetxt.writelines(contents)
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

def package_contents(package_name) :
INDENT
    spec = importlib.util.find_spec(package_name)
    if spec is None :
    INDENT
        return set()
    DEDENT
    pathname = Path(spec.origin).parent
    ret = set()
    with os.scandir(pathname) as entries :
    INDENT
        for entry in entries :
        INDENT
            if entry.name.startswith('__') :
            INDENT
                continue
            DEDENT
            current = '.'.join((package_name, entry.name.partition('.') [0]))
            if entry.is_file() :
            INDENT
                if entry.name.endswith(MODULE_EXTENSIONS) :
                INDENT
                    ret.add(current)
                DEDENT
            DEDENT
            elif entry.is_dir() :
            INDENT
                ret.add(current)
                ret |= package_contents(current)
            DEDENT
        DEDENT
    DEDENT
    return ret
DEDENT

    def test_combined_q_object(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.annotate(
                test=Case(
                    When(Q(integer=2) | Q(integer2=3), then=Value('when')),
                    default=Value('default'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [
                (1, 1, 'default'), (2, 3, 'when'), (3, 4, 'default'), (2, 2, 'when'), (3, 4, 'default'),
                (3, 3, 'when'), (4, 5, 'default')
            ],
            transform=attrgetter('integer', 'integer2', 'test')
        )

def validate(func) :
INDENT
    def wrapped(self, * args, ** kwargs) :
    INDENT
        self.valid = True
        func(self, * args, ** kwargs)
    DEDENT
    return wrapped
DEDENT

def find_mount_point(path) :
INDENT
    path = os.path.abspath(path)
    orig_dev = os.stat(path).st_dev
    while path ! = '/' :
    INDENT
        dir = os.path.dirname(path)
        if os.stat(dir).st_dev ! = orig_dev :
        INDENT
            break
        DEDENT
        path = dir
    DEDENT
    return path
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

def toc() :
INDENT
    import time
    if 'startTime_for_tictoc' in globals() :
    INDENT
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    DEDENT
    else :
    INDENT
        print "Toc: start time not set"
    DEDENT
DEDENT

def emit(self, record) :
INDENT
    myrecord = copy.copy(record)
    levelno = myrecord.levelno
    if (levelno > = 50) :
    INDENT
        color = '\x1b[31m'
    DEDENT
    elif (levelno > = 40) :
    INDENT
        color = '\x1b[31m'
    DEDENT
    elif (levelno > = 30) :
    INDENT
        color = '\x1b[33m'
    DEDENT
    elif (levelno > = 20) :
    INDENT
        color = '\x1b[32m'
    DEDENT
    elif (levelno > = 10) :
    INDENT
        color = '\x1b[35m'
    DEDENT
    else :
    INDENT
        color = '\x1b[0m'
    DEDENT
    myrecord.msg = color + str(myrecord.msg) + '\x1b[0m'
    logging.StreamHandler.emit(self, myrecord)
DEDENT

    def test_order_by_conditional_implicit(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer__lte=2).annotate(test=Case(
                When(integer=1, then=2),
                When(integer=2, then=1),
                default=3,
                output_field=models.IntegerField(),
            )).order_by('test', 'pk'),
            [(2, 1), (2, 1), (1, 2)],
            transform=attrgetter('integer', 'test')
        )

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

def replace_runs(a, search, run_length, replace = 2) :
INDENT
    a_copy = a.copy()
    for i, row in enumerate(a) :
    INDENT
        runs = []
        current_run = []
        for j, val in enumerate(row) :
        INDENT
            if val == search :
            INDENT
                current_run.append(j)
            DEDENT
            else :
            INDENT
                if len(current_run) > = run_length or j == len(row) - 1 :
                INDENT
                    runs.append(current_run)
                DEDENT
                current_run = []
            DEDENT
        DEDENT
        if len(current_run) > = run_length or j == len(row) - 1 :
        INDENT
            runs.append(current_run)
        DEDENT
        for run in runs :
        INDENT
            for col in run :
            INDENT
                a_copy [i] [col] = replace
            DEDENT
        DEDENT
    DEDENT
    return a_copy
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

def is_member(x) :
INDENT
    a = [1, 5, 3, 9, 4, 100]
    for i in a :
    INDENT
        if i == x :
        INDENT
            return "True"
        DEDENT
    DEDENT
    return "False"
DEDENT

    def test_order_by_conditional_explicit(self):
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(integer__lte=2).annotate(test=Case(
                When(integer=1, then=2),
                When(integer=2, then=1),
                default=3,
                output_field=models.IntegerField(),
            )).order_by(F('test').asc(), 'pk'),
            [(2, 1), (2, 1), (1, 2)],
            transform=attrgetter('integer', 'test')
        )

def to_int(bin) :
INDENT
    n = 0
    for i, b in enumerate(reversed(bin)) :
    INDENT
        if b == '1' :
        INDENT
            if i ! = (len(bin) - 1) :
            INDENT
                n += 2 ** i
            DEDENT
            else :
            INDENT
                n -= 2 ** i
            DEDENT
        DEDENT
    DEDENT
    return n
DEDENT

def __init__(self, queue, endcommand, * args) :
INDENT
    QtGui.QMainWindow.__init__(self, * args)
    self.setWindowTitle('Arduino Serial Demo')
    self.queue = queue
    self.editor = QtGui.QTextEdit(self)
    self.setCentralWidget(self.editor)
    self.endcommand = endcommand
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

def read_logfile(master_log, linecount = 1) :
INDENT
    lastmatches = deque(maxlen = linecount)
    for line in master_log :
    INDENT
        if '[76:Health]:' in line :
        INDENT
            lastmatches.append(line)
        DEDENT
    DEDENT
    for line in lastmatches :
    INDENT
        print line
    DEDENT
DEDENT

def myfunc(orientation, l, w) :
INDENT
    if 1 < = orientation < = 8 :
    INDENT
        a = (- w, - l, - w, - l, w, l, w, l) [orientation - 1]
        b = (l, w, - l, - w) [(orientation - 1) % 4]
    DEDENT
    return a, b
DEDENT

    def test_join_promotion(self):
        o = CaseTestModel.objects.create(integer=1, integer2=1, string='1')
        # Testing that:
        # 1. There isn't any object on the remote side of the fk_rel
        #    relation. If the query used inner joins, then the join to fk_rel
        #    would remove o from the results. So, in effect we are testing that
        #    we are promoting the fk_rel join to a left outer join here.
        # 2. The default value of 3 is generated for the case expression.
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(pk=o.pk).annotate(
                foo=Case(
                    When(fk_rel__pk=1, then=2),
                    default=3,
                    output_field=models.IntegerField()
                ),
            ),
            [(o, 3)],
            lambda x: (x, x.foo)
        )
        # Now 2 should be generated, as the fk_rel is null.
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(pk=o.pk).annotate(
                foo=Case(
                    When(fk_rel__isnull=True, then=2),
                    default=3,
                    output_field=models.IntegerField()
                ),
            ),
            [(o, 2)],
            lambda x: (x, x.foo)
        )

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

def square(x = None) :
INDENT
    if x is None :
    INDENT
        print "you have not entered x"
    DEDENT
    else :
    INDENT
        y = x ** 2
        return y
    DEDENT
DEDENT

def request(flow) :
INDENT
    if flow.request.pretty_host.endswith("mydomain.com") :
    INDENT
        mitmproxy.ctx.log(flow.request.path)
        method = flow.request.path.split('/') [3].split('?') [0]
        flow.request.host = "newsite.mydomain.com"
        flow.request.port = 8181
        flow.request.scheme = 'http'
        if method == 'getjson' :
        INDENT
            flow.request.path = flow.request.path.replace(method, "getxml")
        DEDENT
        flow.request.headers ["Host"] = "newsite.mydomain.com"
    DEDENT
DEDENT

def main() :
INDENT
    pygame.init()
    white = (255, 255, 255)
    red = (255, 0, 0)
    gameDisplay = pygame.display.set_mode((600, 800))
    gameExit = False
    x = 0
    y = 0
    w = 25
    h = 25
    sobj = shape(white, 0, 0, 25, 25)
    sobj.draw_rect(gameDisplay)
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

    def test_join_promotion_multiple_annotations(self):
        o = CaseTestModel.objects.create(integer=1, integer2=1, string='1')
        # Testing that:
        # 1. There isn't any object on the remote side of the fk_rel
        #    relation. If the query used inner joins, then the join to fk_rel
        #    would remove o from the results. So, in effect we are testing that
        #    we are promoting the fk_rel join to a left outer join here.
        # 2. The default value of 3 is generated for the case expression.
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(pk=o.pk).annotate(
                foo=Case(
                    When(fk_rel__pk=1, then=2),
                    default=3,
                    output_field=models.IntegerField()
                ),
                bar=Case(
                    When(fk_rel__pk=1, then=4),
                    default=5,
                    output_field=models.IntegerField()
                ),
            ),
            [(o, 3, 5)],
            lambda x: (x, x.foo, x.bar)
        )
        # Now 2 should be generated, as the fk_rel is null.
        self.assertQuerysetEqual(
            CaseTestModel.objects.filter(pk=o.pk).annotate(
                foo=Case(
                    When(fk_rel__isnull=True, then=2),
                    default=3,
                    output_field=models.IntegerField()
                ),
                bar=Case(
                    When(fk_rel__isnull=True, then=4),
                    default=5,
                    output_field=models.IntegerField()
                ),
            ),
            [(o, 2, 4)],
            lambda x: (x, x.foo, x.bar)
        )

def get_icon_path(extension, size = 32) :
INDENT
    type_, encoding = mimetypes.guess_type('x.' + extension)
    if type_ :
    INDENT
        icon = gio.content_type_get_icon(type_)
        theme = gtk.icon_theme_get_default()
        info = theme.choose_icon(icon.get_names(), size, 0)
        if info :
        INDENT
            return info.get_filename()
        DEDENT
    DEDENT
DEDENT

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

def decrypt(key, encoded) :
INDENT
    padded_key = key.ljust(KEY_SIZE, '\0')
    ciphertext = base64.b64decode(encoded)
    r = rijndael.rijndael(padded_key, BLOCK_SIZE)
    padded_text = ''
    for start in range(0, len(ciphertext), BLOCK_SIZE) :
    INDENT
        padded_text += r.decrypt(ciphertext [start : start + BLOCK_SIZE])
    DEDENT
    plaintext = padded_text.split('\x00', 1) [0]
    return plaintext
DEDENT

def get_word_len_dict(text) :
INDENT
    result_dict = defaultdict(set)
    for word in text.split() :
    INDENT
        result_dict [str(len(word))].add(word)
    DEDENT
    return result_dict
DEDENT

def __iter__(self) :
INDENT
    for child in self.l :
    INDENT
        for item in child :
        INDENT
            yield item
        DEDENT
    DEDENT
    yield self
DEDENT

def search(self, st) :
INDENT
    if self.value == st :
    INDENT
        return True
    DEDENT
    for child in self.children :
    INDENT
        if child.search(st) :
        INDENT
            return True
        DEDENT
    DEDENT
    return False
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

    def test_m2m_exclude(self):
        CaseTestModel.objects.create(integer=10, integer2=1, string='1')
        qs = CaseTestModel.objects.values_list('id', 'integer').annotate(
            cnt=models.Sum(
                Case(When(~Q(fk_rel__integer=1), then=1), default=2),
                output_field=models.IntegerField()
            ),
        ).order_by('integer')
        # The first o has 2 as its fk_rel__integer=1, thus it hits the
        # default=2 case. The other ones have 2 as the result as they have 2
        # fk_rel objects, except for integer=4 and integer=10 (created above).
        # The integer=4 case has one integer, thus the result is 1, and
        # integer=10 doesn't have any and this too generates 1 (instead of 0)
        # as ~Q() also matches nulls.
        self.assertQuerysetEqual(
            qs,
            [(1, 2), (2, 2), (2, 2), (3, 2), (3, 2), (3, 2), (4, 1), (10, 1)],
            lambda x: x[1:]
        )

def __init__(self, * args, ** kwargs) :
INDENT
    QtWidgets.QScrollBar.__init__(self, * args, ** kwargs)
    self.baseSheet = '''
            QScrollBar {{
                width: 45px;
                margin: 45px 0 45px 0;
                background: #32CC99;
            }}
            QScrollBar::handle {{
                border: 10px solid grey;
                background: white;
                min-height: 10px;
            }}
            QScrollBar::add-line:vertical {{
                border: 2px solid grey;
                background: none;
                height: 45px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }}
            QScrollBar::sub-line:vertical {{
                border: 2px solid grey;
                background: none;
                height: 45px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }}
            QScrollBar::up-arrow:vertical {{
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {upArrow}
            }}
            QScrollBar::down-arrow:vertical {{
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {downArrow}
            }}
            QScrollBar::left-arrow:vertical {{
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {leftArrow}
            }}
            QScrollBar::right-arrow:vertical {{
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                {rightArrow}
            }}
            '''
    self.arrowNormal = '''
                border-top: 5px solid lightgray;
                border-left: 5px solid lightgray;
                border-right: 5px solid gray;
                border-bottom: 5px solid gray;
            '''
    self.arrowPressed = '''
                border: 5px solid darkgray;
            '''
    self.setStyleSheet(self.baseSheet.format(
            upArrow = self.arrowNormal,
            downArrow = self.arrowNormal,
            leftArrow = self.arrowNormal,
            rightArrow = self.arrowNormal))
DEDENT

def acquire_data(list_or_filename) :
INDENT
    if isinstance(list_or_filename, str) :
    INDENT
        with open(list_or_filename, "r") as f :
        INDENT
            return acquire_data_from_file(f)
        DEDENT
    DEDENT
    else :
    INDENT
        return acquire_data_from_list(list_or_filename)
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

def timeout(max_timeout) :
INDENT
    def timeout_decorator(item) :
    INDENT
        @ functools.wraps(item)
        def func_wrapper(* args, ** kwargs) :
        INDENT
            pool = multiprocessing.pool.ThreadPool(processes = 1)
            async_result = pool.apply_async(item, args, kwargs)
            return async_result.get(max_timeout)
        DEDENT
        return func_wrapper
    DEDENT
    return timeout_decorator
DEDENT

    def test_m2m_reuse(self):
        CaseTestModel.objects.create(integer=10, integer2=1, string='1')
        # Need to use values before annotate so that Oracle will not group
        # by fields it isn't capable of grouping by.
        qs = CaseTestModel.objects.values_list('id', 'integer').annotate(
            cnt=models.Sum(
                Case(When(~Q(fk_rel__integer=1), then=1), default=2),
                output_field=models.IntegerField()
            ),
        ).annotate(
            cnt2=models.Sum(
                Case(When(~Q(fk_rel__integer=1), then=1), default=2),
                output_field=models.IntegerField()
            ),
        ).order_by('integer')
        self.assertEqual(str(qs.query).count(' JOIN '), 1)
        self.assertQuerysetEqual(
            qs,
            [(1, 2, 2), (2, 2, 2), (2, 2, 2), (3, 2, 2), (3, 2, 2), (3, 2, 2), (4, 1, 1), (10, 1, 1)],
            lambda x: x[1:]
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

def flat_sum(q) :
INDENT
    global total
    if not q :
    INDENT
        return
    DEDENT
    if isinstance(q, list) :
    INDENT
        if not isinstance(q [0], list) and not isinstance(q [0], str) :
        INDENT
            total += q [0]
        DEDENT
        else :
        INDENT
            flat_sum(q [0])
        DEDENT
        flat_sum(q [1 :])
    DEDENT
    else :
    INDENT
        if not isinstance(q, str) :
        INDENT
            total += q
        DEDENT
    DEDENT
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

def add(self, value) :
INDENT
    if not self.root :
    INDENT
        self.root = Node(value)
    DEDENT
    else :
    INDENT
        self._add(self.root, value)
    DEDENT
DEDENT

def update_position(self) :
INDENT
    self.set_rotation(0)
    self.set_va(self.__Va)
    self.set_ha(self.__Ha)
    self.set_position(self.__Position)
    ax = self.axes
    xy = self.__Position
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    figW, figH = ax.get_figure().get_size_inches()
    _, _, w, h = ax.get_position().bounds
    aspect = ((figW * w) / (figH * h)) * (ylim [1] - ylim [0]) / (xlim [1] - xlim [0])
    renderer = ax.figure.canvas.get_renderer()
    bbox1 = self.get_window_extent(renderer = renderer)
    bbox1d = ax.transData.inverted().transform(bbox1)
    width = bbox1d [1, 0] - bbox1d [0, 0]
    height = bbox1d [1, 1] - bbox1d [0, 1]
    self.set_va('center')
    self.set_ha('center')
    bbox2 = self.get_window_extent(renderer = renderer)
    bbox2d = ax.transData.inverted().transform(bbox2)
    dr = np.array(bbox2d [0] - bbox1d [0])
    rad = np.deg2rad(self.__Rotation)
    rot_mat = np.array([
            [math.cos(rad), math.sin(rad) * aspect],
            [- math.sin(rad) / aspect, math.cos(rad)]])
    drp = np.dot(dr, rot_mat)
    self.set_position((xy [0] - drp [0], xy [1] - drp [1]))
    self.set_rotation(self.__Rotation)
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

class CaseDocumentationExamples(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            name='Jane Doe',
            account_type=Client.REGULAR,
            registered_on=date.today() - timedelta(days=36),
        )
        Client.objects.create(
            name='James Smith',
            account_type=Client.GOLD,
            registered_on=date.today() - timedelta(days=5),
        )
        Client.objects.create(
            name='Jack Black',
            account_type=Client.PLATINUM,
            registered_on=date.today() - timedelta(days=10 * 365),
        )

def display_list(A, B) :
INDENT
    data = [("01", "02", "03", "04", "05", "06", "07"),
        ("08", "09", "10", "11", "12", "13", "14"),
        ("15", "16", "17", "18", "19", "20", "21")]
    result = []
    for sublist in data :
    INDENT
        tmp_result = []
        for element in sublist :
        INDENT
            value = int(element)
            if value == A :
            INDENT
                tmp_result.append("A")
            DEDENT
            elif value == B :
            INDENT
                tmp_result.append("B")
            DEDENT
            else :
            INDENT
                tmp_result.append(element)
            DEDENT
        DEDENT
        result.append(tuple(tmp_result))
    DEDENT
    return result
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
        elif isinstance(value, list) :
        INDENT
            l = []
            for v in value :
            INDENT
                if isinstance(v, list) or isinstance(v, dict) :
                INDENT
                    l.append(FakeSudsNode(v))
                DEDENT
                else :
                INDENT
                    l.append(v)
                DEDENT
            DEDENT
            setattr(self, key, l)
        DEDENT
        else :
        INDENT
            setattr(self, key, value)
        DEDENT
    DEDENT
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

def brute_force(length, check_callback, guess = "") :
INDENT
    if check_callback(guess) :
    INDENT
        return guess
    DEDENT
    elif len(guess) == length :
    INDENT
        return None
    DEDENT
    for char in chars :
    INDENT
        retval = brute_force(length, check_callback, guess = guess + char)
        if retval is not None :
        INDENT
            return retval
        DEDENT
    DEDENT
    return None
DEDENT

    def test_simple_example(self):
        self.assertQuerysetEqual(
            Client.objects.annotate(
                discount=Case(
                    When(account_type=Client.GOLD, then=Value('5%')),
                    When(account_type=Client.PLATINUM, then=Value('10%')),
                    default=Value('0%'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [('Jane Doe', '0%'), ('James Smith', '5%'), ('Jack Black', '10%')],
            transform=attrgetter('name', 'discount')
        )

def window(iterable, n = 2) :
INDENT
    "s -> (s0, ...,s(n-1)), (s1, ...,sn), (s2, ..., s(n+1)), ..."
    iters = tee(iterable, n)
    for i, it in enumerate(iters) :
    INDENT
        consume(it, i)
    DEDENT
    return zip(* iters)
DEDENT

def release(self) :
INDENT
    if self.released :
    INDENT
        return False
    DEDENT
    for sig in self.signals :
    INDENT
        signal.signal(sig, self.original_handlers [sig])
    DEDENT
    self.released = True
    return True
DEDENT

def Problem4() :
INDENT
    y = 100
    a = []
    x1 = []
    y1 = []
    while y < 1000 :
    INDENT
        y = y + 1
        x = 100
        while x < 1000 :
        INDENT
            z = x * y
            if str(z) == str(z) [: : - 1] :
            INDENT
                a.append(z)
            DEDENT
            x = x + 1
        DEDENT
    DEDENT
    a.sort()
    print (a)
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

    def test_lookup_example(self):
        a_month_ago = date.today() - timedelta(days=30)
        a_year_ago = date.today() - timedelta(days=365)
        self.assertQuerysetEqual(
            Client.objects.annotate(
                discount=Case(
                    When(registered_on__lte=a_year_ago, then=Value('10%')),
                    When(registered_on__lte=a_month_ago, then=Value('5%')),
                    default=Value('0%'),
                    output_field=models.CharField(),
                ),
            ).order_by('pk'),
            [('Jane Doe', '5%'), ('James Smith', '0%'), ('Jack Black', '10%')],
            transform=attrgetter('name', 'discount')
        )

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

def R(A) :
INDENT
    z = {}
    for i in r :
    INDENT
        if 0 == A [i] : h = dict((A [j] * (j / 9 == i / 9 or j % 9 == i % 9 or j / 27 == i / 27 and j % 9 / 3 == i % 9 / 3), 1) for j in r); z [9 - len(h)] = h, i
    DEDENT
    for l in sorted(z) :
    INDENT
        h, i = z [l]
        for j in r [1 : 10] :
        INDENT
            if (j in h) - 1 :
            INDENT
                A [i] = j
                if R(A) : return A
            DEDENT
        DEDENT
        A [i] = 0; return []
    DEDENT
    return A
DEDENT

    def test_conditional_update_example(self):
        a_month_ago = date.today() - timedelta(days=30)
        a_year_ago = date.today() - timedelta(days=365)
        Client.objects.update(
            account_type=Case(
                When(registered_on__lte=a_year_ago, then=Value(Client.PLATINUM)),
                When(registered_on__lte=a_month_ago, then=Value(Client.GOLD)),
                default=Value(Client.REGULAR),
            ),
        )
        self.assertQuerysetEqual(
            Client.objects.all().order_by('pk'),
            [('Jane Doe', 'G'), ('James Smith', 'R'), ('Jack Black', 'P')],
            transform=attrgetter('name', 'account_type')
        )

def after_request(response) :
INDENT
    diff = time.time() - g.start
    if (response.response) :
    INDENT
        response.response [0] = response.response [0].replace('__EXECUTION_TIME__', str(diff))
    DEDENT
    return response
DEDENT

def permutation(flag, k = 1) :
INDENT
    N = len(flag)
    for i in xrange(0, N) :
    INDENT
        if flag [i] ! = 0 :
        INDENT
            continue
        DEDENT
        flag [i] = k
        if k == N :
        INDENT
            print flag
        DEDENT
        permutation(flag, k + 1)
        flag [i] = 0
    DEDENT
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

def punk(string) :
INDENT
    letters = ('Z', 'z')
    zCount = 0
    for char in string :
    INDENT
        if char in letters :
        INDENT
            zCount += 1
        DEDENT
    DEDENT
    return 1 if zCount > = 3 else 0
DEDENT

    def test_conditional_aggregation_example(self):
        Client.objects.create(
            name='Jean Grey',
            account_type=Client.REGULAR,
            registered_on=date.today(),
        )
        Client.objects.create(
            name='James Bond',
            account_type=Client.PLATINUM,
            registered_on=date.today(),
        )
        Client.objects.create(
            name='Jane Porter',
            account_type=Client.PLATINUM,
            registered_on=date.today(),
        )
        self.assertEqual(
            Client.objects.aggregate(
                regular=models.Count('pk', filter=Q(account_type=Client.REGULAR)),
                gold=models.Count('pk', filter=Q(account_type=Client.GOLD)),
                platinum=models.Count('pk', filter=Q(account_type=Client.PLATINUM)),
            ),
            {'regular': 2, 'gold': 1, 'platinum': 3}
        )
        # This was the example before the filter argument was added.
        self.assertEqual(
            Client.objects.aggregate(
                regular=models.Sum(Case(
                    When(account_type=Client.REGULAR, then=1),
                    output_field=models.IntegerField(),
                )),
                gold=models.Sum(Case(
                    When(account_type=Client.GOLD, then=1),
                    output_field=models.IntegerField(),
                )),
                platinum=models.Sum(Case(
                    When(account_type=Client.PLATINUM, then=1),
                    output_field=models.IntegerField(),
                )),
            ),
            {'regular': 2, 'gold': 1, 'platinum': 3}
        )

def main() :
INDENT
    @ clazzRef
    def BarOverride(self) :
    INDENT
        print "Hello, world! I'm a %s but this method is from class %s!" % (type(self), clazz)
        super(clazz, self).FooMethod()
    DEDENT
    derived_type = type('Derived', (FooClass,), {'FooMethod' : BarOverride})
    instance = derived_type()
    instance.FooMethod()
    class derivedDerived(derived_type) :
    INDENT
        def FooMethod(self) :
        INDENT
            print 'I inherit from derived.'
            super(derivedDerived, self).FooMethod()
        DEDENT
    DEDENT
    instance = derivedDerived()
    instance.FooMethod()
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

def rev(s) :
INDENT
    l = len(s)
    for i, j in zip(range(l - 1, 0, - 1), range(l / / 2)) :
    INDENT
        s [i], s [j] = s [j], s [i]
    DEDENT
    return s
DEDENT

    def test_filter_example(self):
        a_month_ago = date.today() - timedelta(days=30)
        a_year_ago = date.today() - timedelta(days=365)
        self.assertQuerysetEqual(
            Client.objects.filter(
                registered_on__lte=Case(
                    When(account_type=Client.GOLD, then=a_month_ago),
                    When(account_type=Client.PLATINUM, then=a_year_ago),
                ),
            ),
            [('Jack Black', 'P')],
            transform=attrgetter('name', 'account_type')
        )

def addition() :
INDENT
    total = 0
    while True :
    INDENT
        total += int(input())
        if input() == "exit" :
        INDENT
            break
        DEDENT
    DEDENT
    print (total)
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

    def test_hash(self):
        expression_1 = Case(
            When(account_type__in=[Client.REGULAR, Client.GOLD], then=1),
            default=2,
            output_field=models.IntegerField(),
        )
        expression_2 = Case(
            When(account_type__in=(Client.REGULAR, Client.GOLD), then=1),
            default=2,
            output_field=models.IntegerField(),
        )
        expression_3 = Case(When(account_type__in=[Client.REGULAR, Client.GOLD], then=1), default=2)
        expression_4 = Case(When(account_type__in=[Client.PLATINUM, Client.GOLD], then=2), default=1)
        self.assertEqual(hash(expression_1), hash(expression_2))
        self.assertNotEqual(hash(expression_2), hash(expression_3))
        self.assertNotEqual(hash(expression_1), hash(expression_4))
        self.assertNotEqual(hash(expression_3), hash(expression_4))


def memoize(fn) :
INDENT
    get = [lambda key : (False, None)]
    def vset(args) :
    INDENT
        value = fn(* args)
        oldget = get [0]
        def newget(key) :
        INDENT
            if args == key :
            INDENT
                return (True, value)
            DEDENT
            return oldget(key)
        DEDENT
        get [0] = newget
        return value
    DEDENT
    def mfun(* args) :
    INDENT
        found, value = get [0](args)
        if found :
        INDENT
            return value
        DEDENT
        return vset(args)
    DEDENT
    return mfun
DEDENT

def __init__(self, maxlen, items = None) :
INDENT
    self._maxlen = maxlen
    self.d = OrderedDict()
    if items :
    INDENT
        for k, v in items :
        INDENT
            self [k] = v
        DEDENT
    DEDENT
DEDENT

def time_limit(seconds, msg = '') :
INDENT
    timer = threading.Timer(seconds, lambda : _thread.interrupt_main())
    timer.start()
    try :
    INDENT
        yield
    DEDENT
    except KeyboardInterrupt :
    INDENT
        raise TimeoutException("Timed out for operation {}".format(msg))
    DEDENT
    finally :
    INDENT
        timer.cancel()
    DEDENT
DEDENT

def select_weighted(d) :
INDENT
    offset = random.randint(0, sum(d.itervalues()) - 1)
    for k, v in d.iteritems() :
    INDENT
        if offset < v :
        INDENT
            return k
        DEDENT
        offset -= v
    DEDENT
DEDENT

def download_file(url) :
INDENT
    local_filename = url.split('/') [- 1]
    with requests.get(url, stream = True) as r :
    INDENT
        with open(local_filename, 'wb') as f :
        INDENT
            for chunk in r.iter_content(chunk_size = 8192) :
            INDENT
                if chunk :
                INDENT
                    f.write(chunk)
                DEDENT
            DEDENT
        DEDENT
    DEDENT
    return local_filename
DEDENT

def create_response(self, request, data, response_class = HttpResponse, ** response_kwargs) :
INDENT
    stripped_data = data.get('objects') or data
    desired_format = self.determine_format(request)
    serialized = self.serialize(request, stripped_data, desired_format)
    response = response_class(content = serialized,
        content_type = build_content_type(desired_format),
        ** response_kwargs)
    for name, value in data.get('meta', {}).items() :
    INDENT
        response [name] = str(value)
    DEDENT
    return response
DEDENT

class CaseWhenTests(SimpleTestCase):
    def test_only_when_arguments(self):
        msg = 'Positional arguments must all be When objects.'
        with self.assertRaisesMessage(TypeError, msg):
            Case(When(Q(pk__in=[])), object())

def getVerb() :
INDENT
    correctAnswers = 0
    for level in (level1, level2) :
    INDENT
        level_name, choices = level [0], level [1 :]
        random.shuffle(choices)
        for choice in choices :
        INDENT
            prefix, suffix = choice.split(' ', 2)
            print (prefix, blanks, level_name)
            ans = raw_input('Answer: ')
            while True :
            INDENT
                if ans == suffix :
                INDENT
                    correctAnswers += 1
                    print ("Nice one!")
                    print (correctAnswers)
                    break
                DEDENT
                else :
                INDENT
                    print ("Bad luck!")
                    ans = raw_input('Try again: ')
                DEDENT
            DEDENT
        DEDENT
    DEDENT
DEDENT

def to_string(my_list) :
INDENT
    result = ''
    last = len(my_list) - 1
    for pos, elem in enumerate(my_list) :
    INDENT
        result += str(elem)
        if pos ! = last :
        INDENT
            result += ', '
        DEDENT
    DEDENT
    return result
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

    def test_invalid_when_constructor_args(self):
        msg = (
            'When() supports a Q object, a boolean expression, or lookups as '
            'a condition.'
        )
        with self.assertRaisesMessage(TypeError, msg):
            When(condition=object())
        with self.assertRaisesMessage(TypeError, msg):
            When(condition=Value(1, output_field=models.IntegerField()))
        with self.assertRaisesMessage(TypeError, msg):
            When()

def __init__(self) :
INDENT
    self.button = gtk.Button()
    self.hbox = gtk.HBox()
    self.hbox.pack_start(self.button, False)
    self.button.set_image(self.OPEN_IMAGE)
    self.button.connect('clicked', self.the_method, "plop")
    self.toggled = True
DEDENT

def merge_lists(head1, head2) :
INDENT
    if head1 is None :
    INDENT
        return head2
    DEDENT
    if head2 is None :
    INDENT
        return head1
    DEDENT
    s = t = node()
    while not (head1 is None or head2 is None) :
    INDENT
        if head1.value < head2.value :
        INDENT
            c = head1
            head1 = head1.next
        DEDENT
        else :
        INDENT
            c = head2
            head2 = head2.next
        DEDENT
        t.next = c
        t = t.next
    DEDENT
    t.next = head1 or head2
    return s.next
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

    def test_empty_q_object(self):
        msg = "An empty Q() can't be used as a When() condition."
        with self.assertRaisesMessage(ValueError, msg):
            When(Q(), then=Value(True))
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

def meta_redirect(content) :
INDENT
    root = soupparser.fromstring(content)
    result_url = root.xpath('//meta[@http-equiv="refresh"]/@content')
    if result_url :
    INDENT
        result_url = str(result_url [0])
        urls = result_url.split('URL=') if len(result_url.split('url=')) < 2 else result_url.split('url=')
        url = urls [1] if len(urls) > = 2 else None
    DEDENT
    else :
    INDENT
        return None
    DEDENT
    return url
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
    return re.sub("&#?\w+;", fixup, text)
DEDENT

def __init__(self, parent) :
INDENT
    wx.Frame.__init__(self, parent, - 1, "Reference Frame", size = (300, 300))
    panel = wx.Panel(self)
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.btn = wx.Button(panel, - 1, "open frame")
    self.Bind(wx.EVT_BUTTON, self.OnOpenFrame, id = self.btn.GetId())
    sizer.Add(self.btn)
    text = "This is a line.\n" * 100
    txtCtrl = wx.TextCtrl(panel, - 1, text, style = wx.TE_MULTILINE,
        size = (200, 200))
    sizer.Add(txtCtrl)
    panel.SetSizer(sizer)
    self.Centre()
    self.Show()
DEDENT
































































































































































































































































































































































































































































