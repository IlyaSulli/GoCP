import datetime

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings
from django.views.generic.base import View

from .models import Artist, Author, Book, Page


@override_settings(ROOT_URLCONF='generic_views.urls')
class ListViewTests(TestCase):

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

def listComp(listA, listB) :
INDENT
    Awins = 0
    Aties = 0
    Alosses = 0
    for i in range(0, whatever) :
    INDENT
        random.shuffle(listA)
        random.shuffle(listB)
        for j in range(0, len(listA)) :
        INDENT
            if A [j] > B [j] :
            INDENT
                Awins += 1
            DEDENT
            elif A [j] == B [j] :
            INDENT
                Aties += 1
            DEDENT
            elif A [j] < B [j] :
            INDENT
                Alosses += 1
            DEDENT
        DEDENT
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

    def test_items(self):
        res = self.client.get('/list/dict/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/list.html')
        self.assertEqual(res.context['object_list'][0]['first'], 'John')

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

def stemming(verb) :
INDENT
    suffix = ["ing", "ed", "es", "s"]
    for i in suffix :
    INDENT
        verb = verb.replace(i, "")
    DEDENT
    return verb
DEDENT

    def test_queryset(self):
        res = self.client.get('/list/authors/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertIsInstance(res.context['view'], View)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertIsNone(res.context['paginator'])
        self.assertIsNone(res.context['page_obj'])
        self.assertFalse(res.context['is_paginated'])

def get_images(query, num_turn) :
INDENT
    image_urls = []
    s = requests.session()
    s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"})
    URL = "https://www.google.dk/search"
    for x in range(0, num_turn) :
    INDENT
        start = x * 100
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
        for img in re.findall(r'imgurl=(.*?(?:&|\.(?:jpg|gif|png|jpeg)))', request.text, re.I) :
        INDENT
            image_urls.append(img)
        DEDENT
    DEDENT
    return image_urls
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

    def test_paginated_queryset(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(len(res.context['object_list']), 30)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertTrue(res.context['is_paginated'])
        self.assertEqual(res.context['page_obj'].number, 1)
        self.assertEqual(res.context['paginator'].num_pages, 4)
        self.assertEqual(res.context['author_list'][0].name, 'Author 00')
        self.assertEqual(list(res.context['author_list'])[-1].name, 'Author 29')

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

def checkfortie() :
INDENT
    for row in board :
    INDENT
        for square in row :
        INDENT
            if square == 0 :
            INDENT
                return False
            DEDENT
        DEDENT
    DEDENT
    return True
DEDENT

def normalize(df) :
INDENT
    result = df.copy()
    for feature_name in df.columns :
    INDENT
        max_value = df [feature_name].max()
        min_value = df [feature_name].min()
        result [feature_name] = (df [feature_name] - min_value) / (max_value - min_value)
    DEDENT
    return result
DEDENT

def request(context, flow) :
INDENT
    if flow.request.host == 'google.com' :
    INDENT
        flow.reply(HTTPResponse('HTTP/1.1', 302, 'Found',
                Headers(Location = 'http://stackoverflow.com/',
                    Content_Length = '0'),
                b''))
    DEDENT
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

    def test_paginated_queryset_shortdata(self):
        # Short datasets also result in a paginated view.
        res = self.client.get('/list/authors/paginated/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertEqual(res.context['page_obj'].number, 1)
        self.assertEqual(res.context['paginator'].num_pages, 1)
        self.assertFalse(res.context['is_paginated'])

def accept(func_or_mimetype = None) :
INDENT
    mimetype = 'text/html'
    class Accept(object) :
    INDENT
        def __init__(self, func) :
        INDENT
            self.default_mimetype = mimetype
            self.accept_handlers = {mimetype : func}
            functools.update_wrapper(self, func)
        DEDENT
        def __call__(self, * args, ** kwargs) :
        INDENT
            default = self.default_mimetype
            mimetypes = request.accept_mimetypes
            best = mimetypes.best_match(self.accept_handlers.keys(), default)
            if best ! = default and mimetypes [best] == mimetypes [default] :
            INDENT
                best = default
            DEDENT
            return self.accept_handlers [best](* args, ** kwargs)
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
    DEDENT
    if callable(func_or_mimetype) :
    INDENT
        return Accept(func_or_mimetype)
    DEDENT
    if func_or_mimetype is not None :
    INDENT
        mimetype = func_or_mimetype
    DEDENT
    return Accept
DEDENT

def __getitem__(self, key) :
INDENT
    if isinstance(key, slice) :
    INDENT
        return [self [ii] for ii in xrange(* key.indices(len(self)))]
    DEDENT
    elif isinstance(key, int) :
    INDENT
        if key < 0 :
        INDENT
            key += len(self)
        DEDENT
        if key < 0 or key > = len(self) :
        INDENT
            raise IndexError, "The index (%d) is out of range." % key
        DEDENT
        return self.getData(key)
    DEDENT
    else :
    INDENT
        raise TypeError, "Invalid argument type."
    DEDENT
DEDENT

def two_powers(n) :
INDENT
    m = 1
    while n > = m :
    INDENT
        if n & m :
        INDENT
            yield m
        DEDENT
        m <<= 1
    DEDENT
DEDENT

def singleton(cls) :
INDENT
    instances = {}
    def getinstance(anyArgs = None) :
    INDENT
        if cls not in instances :
        INDENT
            instances [cls] = cls(anyArgs)
            return instances [cls]
        DEDENT
    DEDENT
    return getinstance
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

def __setattr__(self, attribute, value) :
INDENT
    if not attribute in self.__class__.__allowed_attr :
    INDENT
        raise AttributeError
    DEDENT
    else :
    INDENT
        super().__setattr__(attribute, value)
    DEDENT
DEDENT

    def test_paginated_get_page_by_query_string(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/', {'page': '2'})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(len(res.context['object_list']), 30)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertEqual(res.context['author_list'][0].name, 'Author 30')
        self.assertEqual(res.context['page_obj'].number, 2)

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

def json_scan(json_obj, key) :
INDENT
    result = None
    for element in json_obj :
    INDENT
        if str(element) == key :
        INDENT
            result = json_obj [element]
        DEDENT
        else :
        INDENT
            if type(json_obj [element]) == DictType :
            INDENT
                result = json_scan(json_obj [element], key)
            DEDENT
            elif type(json_obj [element]) == ListType :
            INDENT
                result = json_scan(element, key)
            DEDENT
        DEDENT
    DEDENT
    return result
DEDENT

def __exit__(self, exception_type, exception_value, traceback) :
INDENT
    self.restore_logger('', logging.getLogger())
    for name, logger in logging.Logger.manager.loggerDict.items() :
    INDENT
        self.restore_logger(name, logger)
    DEDENT
DEDENT

def __init__(self) :
INDENT
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()
    self.widthScreen = screen.width
    self.heightScreen = screen.height
    self.xDisplay = int(self.widthScreen / 2 - self.widthDisplay / 2)
    self.yDisplay = int(self.heightScreen / 2 - self.heightDiplay / 2)
    self.Display = pyglet.window.Window(width = self.widthDisplay, height = self.heightDiplay, caption = self.title, resizable = False)
    self.Display.set_location(self.xDisplay, self.yDisplay)
    pyglet.app.run()
DEDENT

    def test_paginated_get_last_page_by_query_string(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/', {'page': 'last'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['object_list']), 10)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertEqual(res.context['author_list'][0].name, 'Author 90')
        self.assertEqual(res.context['page_obj'].number, 4)

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

def self_reference(cls, array, index) :
INDENT
    if not isinstance(array, tuple) :
    INDENT
        raise TypeError('array must be a tuple')
    DEDENT
    if not isinstance(index, int) :
    INDENT
        raise TypeError('index must be an int')
    DEDENT
    if not 0 < = index < len(array) :
    INDENT
        raise ValueError('index is out of range')
    DEDENT
    GIL.acquire()
    try :
    INDENT
        obj = ctypes.py_object(array)
        ob_refcnt = ctypes.cast(id(array), ob_refcnt_p).contents.value
        for _ in range(ob_refcnt - 1) :
        INDENT
            Ref.dec(obj)
        DEDENT
        if cls.setitem(obj, ctypes.c_ssize_t(index), obj) :
        INDENT
            raise SystemError('PyTuple_SetItem was not successful')
        DEDENT
        for _ in range(ob_refcnt) :
        INDENT
            Ref.inc(obj)
        DEDENT
    DEDENT
    finally :
    INDENT
        GIL.release()
    DEDENT
DEDENT

def mail(to, subject, text, attach) :
INDENT
    if not isinstance(to, list) :
    INDENT
        to = [to]
    DEDENT
    if not isinstance(attach, list) :
    INDENT
        attach = [attach]
    DEDENT
    gmail_user = 'username@gmail.com'
    gmail_pwd = "password"
    msg = MIMEMultipart()
    msg ['From'] = gmail_user
    msg ['To'] = ", ".join(to)
    msg ['Subject'] = subject
    msg.attach(MIMEText(text))
    for file in attach :
    INDENT
        print file
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
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

def default(obj) :
INDENT
    if type(obj).__module__ == np.__name__ :
    INDENT
        if isinstance(obj, np.ndarray) :
        INDENT
            return obj.tolist()
        DEDENT
        else :
        INDENT
            return obj.item()
        DEDENT
    DEDENT
    raise TypeError('Unknown type:', type(obj))
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

def file_store(filename) :
INDENT
    def store(items) :
    INDENT
        with open(filename, 'w') as output :
        INDENT
            results = []
            for item in items :
            INDENT
                write_result(item, result, output)
                result.append(item)
            DEDENT
        DEDENT
        return results
    DEDENT
    return store
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

    def test_paginated_get_page_by_urlvar(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/3/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(len(res.context['object_list']), 30)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertEqual(res.context['author_list'][0].name, 'Author 60')
        self.assertEqual(res.context['page_obj'].number, 3)

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

def running_average(data, windowSize) :
INDENT
    dShape = np.shape(data)
    raOut = np.zeros(dShape)
    if len(dShape) == 1 :
    INDENT
        for row, avg in average_iterator(data, windowSize) :
        INDENT
            raOut [row] = avg
        DEDENT
    DEDENT
    else :
    INDENT
        for col in xrange(dShape [1]) :
        INDENT
            for row, avg in average_iterator(data [:, col], windowSize) :
            INDENT
                raOut [row, col] = avg
            DEDENT
        DEDENT
    DEDENT
    return raOut
DEDENT

    def test_paginated_page_out_of_range(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/42/')
        self.assertEqual(res.status_code, 404)

def square(x) :
INDENT
    try :
    INDENT
        y = [e ** 2 for e in x]
    DEDENT
    except TypeError :
    INDENT
        y = x ** 2
    DEDENT
    return y
DEDENT

def func() :
INDENT
    sql = " select some rows "
    dbconn = "connect and open to dtabase code"
    n = 0
    ret = execute(sql, n)
    while ret is not None :
    INDENT
        yield ret
        n += 1
        ret = execute(sql, n)
    DEDENT
    dbclose()
DEDENT

def random_grid(file) :
INDENT
    grid = []
    num_rows = raw_input("How many raws would you like in your grid? ")
    num_columns = raw_input("How many columns would you like in your grid? ")
    min_range = raw_input("What is the minimum number you would like in your grid? ")
    max_range = raw_input("what is the maximum number you would like in your grid? ")
    for row in range(int(num_rows)) :
    INDENT
        grid.append([])
        for column in range(int(num_columns)) :
        INDENT
            grid [row].append(random.randint((int(min_range)), (int(max_range))))
        DEDENT
    DEDENT
    for row in grid :
    INDENT
        x = (' '.join([str(x) for x in row]))
        print x
        with open(r"test.txt", 'a') as text_file :
        INDENT
            text_file.write(x)
            text_file.write("\n")
        DEDENT
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

def numpy_ewma(data, window) :
INDENT
    returnArray = np.empty((data.shape [0]))
    returnArray.fill(np.nan)
    e = data [0]
    alpha = 2 / float(window + 1)
    for s in range(data.shape [0]) :
    INDENT
        e = ((data [s] - e) * alpha) + e
        returnArray [s] = e
    DEDENT
    return returnArray
DEDENT

    def test_paginated_invalid_page(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/?page=frog')
        self.assertEqual(res.status_code, 404)

def __init__(self, parent = None) :
INDENT
    super(Test, self).__init__(parent)
    self.pushButton = QtGui.QPushButton('I am in Test widget')
    layout = QtGui.QHBoxLayout()
    layout.addWidget(self.pushButton)
    self.setLayout(layout)
DEDENT

def get_user_attributes(cls) :
INDENT
    boring = dir(type('dummy', (object,), {}))
    attrs = {}
    bases = reversed(inspect.getmro(cls))
    for base in bases :
    INDENT
        if hasattr(base, '__dict__') :
        INDENT
            attrs.update(base.__dict__)
        DEDENT
        elif hasattr(base, '__slots__') :
        INDENT
            if hasattr(base, base.__slots__ [0]) :
            INDENT
                for item in base.__slots__ :
                INDENT
                    attrs [item] = getattr(base, item)
                DEDENT
            DEDENT
            else :
            INDENT
                attrs [base.__slots__] = getattr(base, base.__slots__)
            DEDENT
        DEDENT
    DEDENT
    for key in boring :
    INDENT
        del attrs ['key']
    DEDENT
    return attrs
DEDENT

def test2() :
INDENT
    import json
    import time
    time_start = time.time()
    with open('data.csv', 'rb') as f :
    INDENT
        data = f.read()
    DEDENT
    data = '[[[' + ']],[['.join(data.splitlines()).replace('\t', '],[') + ']]]'
    all_point_sets = [Point(* xy) for row in json.loads(data) for xy in zip(* row)]
    time_end = time.time()
    print "total time: ", (time_end - time_start)
DEDENT

def __call__(self, new) :
INDENT
    params = self.immutable_params
    def __set_if_unset__(self, name, value) :
    INDENT
        if name in self.__dict__ :
        INDENT
            raise Exception("Attribute %s has already been set" % name)
        DEDENT
        if not name in params :
        INDENT
            raise Exception("Cannot create atribute %s" % name)
        DEDENT
        self.__dict__ [name] = value;
    DEDENT
    def __new__(cls, * args, ** kws) :
    INDENT
        cls.__setattr__ = __set_if_unset__
        return super(cls.__class__, cls).__new__(cls, * args, ** kws)
    DEDENT
    return __new__
DEDENT

    def test_paginated_custom_paginator_class(self):
        self._make_authors(7)
        res = self.client.get('/list/authors/paginated/custom_class/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['paginator'].num_pages, 1)
        # Custom pagination allows for 2 orphans on a page size of 5
        self.assertEqual(len(res.context['object_list']), 7)

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

def fdec(func) :
INDENT
    def f(* args, ** kwargs) :
    INDENT
        assert (args [argnum] % 2 == 0)
        return func(* args, ** kwargs)
    DEDENT
    return f
DEDENT

def overload(self, * types) :
INDENT
    def wrapper(f) :
    INDENT
        for type_seq in types :
        INDENT
            if type(type_seq) == tuple :
            INDENT
                type_seq = tuple(type_seq)
            DEDENT
            else :
            INDENT
                type_seq = (type_seq,)
            DEDENT
            self.map [type_seq] = f
        DEDENT
        return self
    DEDENT
    return wrapper
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

    def test_paginated_custom_page_kwarg(self):
        self._make_authors(100)
        res = self.client.get('/list/authors/paginated/custom_page_kwarg/', {'pagina': '2'})
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')
        self.assertEqual(len(res.context['object_list']), 30)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertEqual(res.context['author_list'][0].name, 'Author 30')
        self.assertEqual(res.context['page_obj'].number, 2)

def shiftedColorMap(cmap, start = 0, midpoint = 0.5, stop = 1.0, name = 'shiftedcmap') :
INDENT
    cdict = {
        'red' : [],
        'green' : [],
        'blue' : [],
        'alpha' : []}
    reg_index = np.linspace(start, stop, 257)
    shift_index = np.hstack([
            np.linspace(0.0, midpoint, 128, endpoint = False),
            np.linspace(midpoint, 1.0, 129, endpoint = True)])
    for ri, si in zip(reg_index, shift_index) :
    INDENT
        r, g, b, a = cmap(ri)
        cdict ['red'].append((si, r, r))
        cdict ['green'].append((si, g, g))
        cdict ['blue'].append((si, b, b))
        cdict ['alpha'].append((si, a, a))
    DEDENT
    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap = newcmap)
    return newcmap
DEDENT

def addToInventory(inventory, addedItems) :
INDENT
    for item in addedItems :
    INDENT
        inventory.setdefault(item, 0)
        inventory [item] = inventory [item] + 1
    DEDENT
    return (inventory)
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

def is_sequence_same(l1, l2) :
INDENT
    if l1 == l2 :
    INDENT
        return True
    DEDENT
    if set(l1) ! = set(l2) or len(l1) ! = len(l2) :
    INDENT
        return False
    DEDENT
    d2 = deque(l2)
    for i in range(len(l2)) :
    INDENT
        if l1 == list(d2) :
        INDENT
            return True
        DEDENT
        d2.rotate()
    DEDENT
    return False
DEDENT

def test_foo() :
INDENT
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout) :
    INDENT
        foo()
    DEDENT
    output = temp_stdout.getvalue().strip()
    assert output == 'hello world!'
DEDENT

    def test_paginated_custom_paginator_constructor(self):
        self._make_authors(7)
        res = self.client.get('/list/authors/paginated/custom_constructor/')
        self.assertEqual(res.status_code, 200)
        # Custom pagination allows for 2 orphans on a page size of 5
        self.assertEqual(len(res.context['object_list']), 7)

def validator(test) :
INDENT
    def wrap(func) :
    INDENT
        def wrapped(* args, ** kwargs) :
        INDENT
            result = func(* args, ** kwargs)
            if test(result) :
            INDENT
                return result
            DEDENT
            return None
        DEDENT
        return wrapped
    DEDENT
    return wrap
DEDENT

def update(self, instance, validated_data) :
INDENT
    user_data = validated_data.pop('user', None)
    for attr, value in user_data.items() :
    INDENT
        setattr(instance.user, attr, value)
    DEDENT
    for attr, value in validated_data.items() :
    INDENT
        setattr(instance, attr, value)
    DEDENT
    instance.save()
    return instance
DEDENT

def package_contents(package_name) :
INDENT
    file, pathname, description = imp.find_module(package_name)
    if file :
    INDENT
        raise ImportError('Not a package: %r', package_name)
    DEDENT
    return set([os.path.splitext(module) [0] for module in os.listdir(pathname)
            if module.endswith(MODULE_EXTENSIONS)])
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

    def test_paginated_orphaned_queryset(self):
        self._make_authors(92)
        res = self.client.get('/list/authors/paginated-orphaned/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['page_obj'].number, 1)
        res = self.client.get(
            '/list/authors/paginated-orphaned/', {'page': 'last'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['page_obj'].number, 3)
        res = self.client.get(
            '/list/authors/paginated-orphaned/', {'page': '3'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['page_obj'].number, 3)
        res = self.client.get(
            '/list/authors/paginated-orphaned/', {'page': '4'})
        self.assertEqual(res.status_code, 404)

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

def html_to_text(html) :
INDENT
    parser = _HTMLToText()
    try :
    INDENT
        parser.feed(html)
        parser.close()
    DEDENT
    except HTMLParseError :
    INDENT
        pass
    DEDENT
    return parser.get_text()
DEDENT

def factorial(n) :
INDENT
    num = 1
    while n > = 1 :
    INDENT
        num = num * n
        n = n - 1
    DEDENT
    return num
DEDENT

    def test_paginated_non_queryset(self):
        res = self.client.get('/list/dict/paginated/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['object_list']), 1)

def _extract_links(self, response_text, response_url, response_encoding, base_url = None) :
INDENT
    if base_url is None :
    INDENT
        base_url = urljoin(response_url, self.base_url) if self.base_url else response_url
    DEDENT
    clean_url = lambda u : urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))
    clean_text = lambda t : replace_escape_chars(remove_tags(t.decode(response_encoding))).strip()
    links_text = linkre.findall(response_text)
    urlstext = set([(clean_url(url), clean_text(text)) for url, _, text in links_text])
    return [Link(url, text) for url, text in urlstext]
DEDENT

def print_checked_items(self) :
INDENT
    path = "/home/test1/checked.txt"
    mode = QtCore.QFile.Append if self.isWritten else QtCore.QFile.WriteOnly
    if len(self.items) > 0 :
    INDENT
        file = QtCore.QFile(path)
        if file.open(mode) :
        INDENT
            for item in self.items :
            INDENT
                print ('%s' % item.text())
                file.write(item.text() + "\n")
            DEDENT
        DEDENT
        file.close()
    DEDENT
    print ("print checked items executed")
DEDENT

def count_chars(p) :
INDENT
    d = collections.defaultdict(int)
    for letter in open(p).read() :
    INDENT
        d [letter] += 1
    DEDENT
    return d
DEDENT

def Problem4() :
INDENT
    y = 909
    a = []
    b = []
    x1 = []
    y1 = []
    while y < 1000 :
    INDENT
        x = 100
        while x < 1000 :
        INDENT
            z = x * y
            if str(z) == str(z) [: : - 1] :
            INDENT
                a.append(z)
                x1.append(x)
                y1.append(y)
            DEDENT
            else :
            INDENT
                b.append(z)
            DEDENT
            x = x + 1
        DEDENT
        y = y + 1
    DEDENT
    print (a)
    print (x1)
    print (y1)
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

def __add__(self, num) :
INDENT
    if isinstance(num, Time) :
    INDENT
        num = timeToInt(num)
    DEDENT
    elif not isinstance(num, int) :
    INDENT
        raise TypeError, 'num should be an integer or Time instance'
    DEDENT
    return intToTime(timeToInt(self) + num)
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

    def test_verbose_name(self):
        res = self.client.get('/list/artists/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'generic_views/list.html')
        self.assertEqual(list(res.context['object_list']), list(Artist.objects.all()))
        self.assertIs(res.context['artist_list'], res.context['object_list'])
        self.assertIsNone(res.context['paginator'])
        self.assertIsNone(res.context['page_obj'])
        self.assertFalse(res.context['is_paginated'])

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

def main() :
INDENT
    t = np.linspace(0, 6 * np.pi, 100)
    x = np.sin(t)
    condition = x > 0
    regions = contiguous_regions(condition)
    lengths = regions [:, 1] - regions [:, 0]
    for reg, length in zip(regions, lengths) :
    INDENT
        print 'Condition was True for {0} seconds'.format(length)
        print '    From time {0}s to {1}s'.format(* reg)
    DEDENT
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

def __new__(mcs, name, bases, dict) :
INDENT
    def make_binary_op(op) :
    INDENT
        fn = lambda self, other : self.__op__(op, other)
        fn.__name__ = op
        return fn
    DEDENT
    for opname in mcs.__binary_ops :
    INDENT
        for op in ('__%s__', '__r%s__') :
        INDENT
            op %= opname
            if op in dict :
            INDENT
                continue
            DEDENT
            dict [op] = make_binary_op(op)
        DEDENT
    DEDENT
    def make_unary_op(op) :
    INDENT
        fn = lambda self : self.__op__(op, None)
        fn.__name__ = op
        return fn
    DEDENT
    for opname in mcs.__unary_ops :
    INDENT
        op = '__%s__' % opname
        if op in dict :
        INDENT
            continue
        DEDENT
        dict [op] = make_unary_op(op)
    DEDENT
    return type.__new__(mcs, name, bases, dict)
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

def fib() :
INDENT
    a, b = 0, 1
    while True :
    INDENT
        yield a
        a, b = b, a + b
    DEDENT
DEDENT

    def test_allow_empty_false(self):
        res = self.client.get('/list/authors/notempty/')
        self.assertEqual(res.status_code, 200)
        Author.objects.all().delete()
        res = self.client.get('/list/authors/notempty/')
        self.assertEqual(res.status_code, 404)

def intersect(haystack, needle) :
INDENT
    while needle :
    INDENT
        pos = haystack.find(needle)
        if pos > = 0 :
        INDENT
            return list(needle)
        DEDENT
        needle = needle [: - 1]
    DEDENT
    return []
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

def morse(s) :
INDENT
    morsecode = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....", 'i' : "..", 'j' : ".---", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z' : "--.."}
    f = ""
    for i in s :
    INDENT
        if not i == ' ' :
        INDENT
            f += morsecode [i]
        DEDENT
        else :
        INDENT
            f += ' '
        DEDENT
    DEDENT
    return f
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

def __new__(cls, name, bases, attrs) :
INDENT
    funcs = [t for t in dir(UnderTest) if t [0] == 'f']
    def doTest(t) :
    INDENT
        def f(slf) :
        INDENT
            ut = UnderTest()
            getattr(ut, t)(3)
        DEDENT
        return f
    DEDENT
    for f in funcs :
    INDENT
        attrs ['test_gen_' + f] = doTest(f)
    DEDENT
    return type.__new__(cls, name, bases, attrs)
DEDENT

    def test_template_name(self):
        res = self.client.get('/list/authors/template_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertTemplateUsed(res, 'generic_views/list.html')

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

def eval_expr(cls, expr, subs) :
INDENT
    '''IMPORTANT: this is class method, overload it with @classmethod!
        Evaluate an expression given in the expr string.
        :param expr: str. String expression.
        :param subs: dict. Dictionary with values to substitute.
        :returns: Evaluated expression result.
        '''
DEDENT

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

def match_class(target) :
INDENT
    target = target.split()
    def do_match(tag) :
    INDENT
        try :
        INDENT
            classes = dict(tag.attrs) ["class"]
        DEDENT
        except KeyError :
        INDENT
            classes = ""
        DEDENT
        classes = classes.split()
        return all(c in classes for c in target)
    DEDENT
    return do_match
DEDENT

    def test_template_name_suffix(self):
        res = self.client.get('/list/authors/template_name_suffix/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertTemplateUsed(res, 'generic_views/author_objects.html')

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

def run(self) :
INDENT
    print '>>>> skip body by not yielding (does not work)'
    with self.drivercontext(self.driverfactory) as driver :
    INDENT
        self.dostuff(driver)
    DEDENT
DEDENT

    def test_context_object_name(self):
        res = self.client.get('/list/authors/context_object_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertNotIn('authors', res.context)
        self.assertIs(res.context['author_list'], res.context['object_list'])
        self.assertTemplateUsed(res, 'generic_views/author_list.html')

def ordinal(num) :
INDENT
    ldig = num % 10
    l2dig = (num / / 10) % 10
    if l2dig == 1 :
    INDENT
        suffix = 'th'
    DEDENT
    elif ldig == 1 :
    INDENT
        suffix = 'st'
    DEDENT
    elif ldig == 2 :
    INDENT
        suffix = 'nd'
    DEDENT
    elif ldig == 3 :
    INDENT
        suffix = 'rd'
    DEDENT
    else :
    INDENT
        suffix = 'th'
    DEDENT
    return '%d%s' % (num, suffix)
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

def do_GET(self) :
INDENT
    path = self.path
    self.uri = path.split("/") [1 :]
    actions = {
        "folder" : self.folder,
        }
    resource = self.uri [0]
    if not resource :
    INDENT
        return self.get_static_content()
    DEDENT
    action = actions.get(resource)
    if action :
    INDENT
        print "action from looking up '%s' is:" % resource, action
        return self.wfile.write(action())
    DEDENT
    SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
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

def linspace(start, stop, n) :
INDENT
    if n == 1 :
    INDENT
        yield stop
        return
    DEDENT
    h = (stop - start) / (n - 1)
    for i in range(n) :
    INDENT
        yield start + h * i
    DEDENT
DEDENT

def recursive_add(s) :
INDENT
    if s :
    INDENT
        return s [0] ** 2 + recursive_add(s [1 :])
    DEDENT
    else :
    INDENT
        return 0
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

    def test_duplicate_context_object_name(self):
        res = self.client.get('/list/authors/dupe_context_object_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context['object_list']), list(Author.objects.all()))
        self.assertNotIn('authors', res.context)
        self.assertNotIn('author_list', res.context)
        self.assertTemplateUsed(res, 'generic_views/author_list.html')

def __init__(self, aName, aCmd, logFileName = '', outFileName = '') :
INDENT
    baseFormatter = logging.Formatter("%(asctime)s \t %(levelname)s \t %(name)s:%(module)s:%(lineno)d \t %(message)s")
    errorFormatter = logging.Formatter(LOG_IDENTIFIER + "%(asctime)s \t %(levelname)s \t %(name)s:%(module)s:%(lineno)d \t %(message)s")
    if logFileName :
    INDENT
        fl = logging.FileHandler("%s.log" % aName)
    DEDENT
    else :
    INDENT
        fl = logging.FileHandler("%s.log" % aName, 'w')
    DEDENT
    fl.setLevel(logging.DEBUG)
    fl.setFormatter(baseFormatter)
    if outFileName :
    INDENT
        teeFile = PyExec.SuperTee("%s_out.log" % aName)
    DEDENT
    else :
    INDENT
        teeFile = PyExec.SuperTee("%s_out.log" % aName, 'w')
    DEDENT
    fl_out = logging.StreamHandler(teeFile)
    fl_out.setLevel(logging.CRITICAL)
    fl_out.setFormatter(errorFormatter)
    self.log = logging.getLogger('pyExec_main')
    log = self.log
    log.addHandler(fl)
    log.addHandler(fl_out)
    print "Test print statement."
    log.setLevel(logging.DEBUG)
    log.info("Starting %s", ME)
    log.critical("Critical.")
    try :
    INDENT
        raise Exception('Exception test.')
    DEDENT
    except Exception, e :
    INDENT
        log.exception(str(e))
    DEDENT
    a = 2 / 0
DEDENT

def backspace(self) :
INDENT
    self.current = self.current [0 : len(self.current) - 1]
    if self.current == "" :
    INDENT
        self.new_num = True
        self.current = "0"
    DEDENT
    self.dsiplay(self.current)
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

def handle_request(req) :
INDENT
    for i, h in enumerate(handlers) :
    INDENT
        if h [1].handles(req) :
        INDENT
            h [0] += 1
            for j in reversed(range(i + 1)) :
            INDENT
                if handlers [j] [0] < = h [0] :
                INDENT
                    break
                DEDENT
            DEDENT
            if j < i :
            INDENT
                handlers [j + 1 : i + 1] = handlers [j : i]
                handlers [j] = h
            DEDENT
            break
        DEDENT
    DEDENT
    else :
    INDENT
        return None
    DEDENT
    return h [1]
DEDENT

def __setattr__(self, name, value) :
INDENT
    if name == "_locked" :
    INDENT
        object.__setattr__(self, name, value)
        return
    DEDENT
    if hasattr(self, "_locked") :
    INDENT
        if not self._locked or hasattr(self, name) :
        INDENT
            object.__setattr__(self, name, value)
        DEDENT
        else :
        INDENT
            raise NameError("Not allowed to create new attribute {} in locked object".format(name))
        DEDENT
    DEDENT
    else :
    INDENT
        object.__setattr__(self, name, value)
    DEDENT
DEDENT

def myfun(my_list, n, par1 = '') :
INDENT
    if par1 == '' :
    INDENT
        outer = range(n)
    DEDENT
    else :
    INDENT
        outer = (i for i in range(n) if my_fun2(i, n) == par1)
    DEDENT
    return [[my_fun2(i, j) for j in range(n)] for i in outer]
DEDENT

    def test_missing_items(self):
        msg = (
            'AuthorList is missing a QuerySet. Define AuthorList.model, '
            'AuthorList.queryset, or override AuthorList.get_queryset().'
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/list/authors/invalid/')

def nostdout() :
INDENT
    '''Prevent print to stdout, but if there was an error then catch it and
    print the output before raising the error.'''
    saved_stdout = sys.stdout
    sys.stdout = cStringIO.StringIO()
    try :
    INDENT
        yield
    DEDENT
    except Exception :
    INDENT
        saved_output = sys.stdout
        sys.stdout = saved_stdout
        print saved_output.getvalue()
        raise
    DEDENT
    sys.stdout = saved_stdout
DEDENT

def enter(self) :
INDENT
    print (self.welcome)
    while (input(self.question + ' ') ! = self.answer) : pass
    if not self.connected : return
    print ('\nWhither goest thou?')
    for i, scene in enumerate(self.connected) :
    INDENT
        print ('{}: {}'.format(i, scene.name))
    DEDENT
    while True :
    INDENT
        try :
        INDENT
            i = int(input('? '))
            return self.connected [i]
        DEDENT
        except ValueError :
        INDENT
            print ('I understand thee not.')
        DEDENT
        except IndexError :
        INDENT
            print ('I understand thee not.')
        DEDENT
    DEDENT
DEDENT

def decode(number, base) :
INDENT
    try :
    INDENT
        int(base)
    DEDENT
    except ValueError :
    INDENT
        raise ValueError('decode(value,base): base must be in base10')
    DEDENT
    else :
    INDENT
        base = int(base)
    DEDENT
    number = str(number)
    if base < 2 :
    INDENT
        base = 2
    DEDENT
    if base > 62 :
    INDENT
        base = 62
    DEDENT
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    final = 0
    if number.startswith("-") :
    INDENT
        neg = True
        number = list(number)
        del (number [0])
        temp = number
        number = ""
        for x in temp :
        INDENT
            number = "{}{}".format(number, x)
        DEDENT
    DEDENT
    else :
    INDENT
        neg = False
    DEDENT
    loc = len(number) - 1
    number = str(number)
    for x in number :
    INDENT
        if numbers.index(x) > base :
        INDENT
            raise ValueError('{} is out of base{} range'.format(x, str(base)))
        DEDENT
        final = final + (numbers.index(x) * (base ** loc))
        loc = loc - 1
    DEDENT
    if neg :
    INDENT
        return - final
    DEDENT
    else :
    INDENT
        return final
    DEDENT
DEDENT

def is_valid_hostname(hostname) :
INDENT
    if hostname [- 1] == "." :
    INDENT
        hostname = hostname [: - 1]
    DEDENT
    if len(hostname) > 253 :
    INDENT
        return False
    DEDENT
    labels = hostname.split(".")
    if re.match(r"[0-9]+$", labels [- 1]) :
    INDENT
        return False
    DEDENT
    allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(label) for label in labels)
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

def runthis(stringinput) :
INDENT
    if isinstance(stringinput, list) :
    INDENT
        for t in stringinput :
        INDENT
            t = t.upper()
        DEDENT
    DEDENT
    elif isinstance(stringinput, basestring) :
    INDENT
        t = t.upper()
    DEDENT
    else :
    INDENT
        raise Exception("Unknown type.")
    DEDENT
DEDENT

    def test_invalid_get_queryset(self):
        msg = (
            "AuthorListGetQuerysetReturnsNone requires either a 'template_name' "
            "attribute or a get_queryset() method that returns a QuerySet."
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            self.client.get('/list/authors/get_queryset/')

def CalcSomething() :
INDENT
    cache = {}
    def CalcSomething(a) :
    INDENT
        if cache.has_key(a) :
        INDENT
            return cache [a]
        DEDENT
        cache [a] = ReallyCalc(a)
        return cache [a]
    DEDENT
    return CalcSomething
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

    def test_paginated_list_view_does_not_load_entire_table(self):
        # Regression test for #17535
        self._make_authors(3)
        # 1 query for authors
        with self.assertNumQueries(1):
            self.client.get('/list/authors/notempty/')
        # same as above + 1 query to test if authors exist + 1 query for pagination
        with self.assertNumQueries(3):
            self.client.get('/list/authors/notempty/paginated/')

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

def scale_bar(ax, length = None, location = (0.5, 0.05), linewidth = 3) :
INDENT
    llx0, llx1, lly0, lly1 = ax.get_extent(ccrs.PlateCarree())
    sbllx = (llx1 + llx0) / 2
    sblly = lly0 + (lly1 - lly0) * location [1]
    tmc = ccrs.TransverseMercator(sbllx, sblly)
    x0, x1, y0, y1 = ax.get_extent(tmc)
    sbx = x0 + (x1 - x0) * location [0]
    sby = y0 + (y1 - y0) * location [1]
    if not length :
    INDENT
        length = (x1 - x0) / 5000
        ndim = int(np.floor(np.log10(length)))
        length = round(length, - ndim)
        def scale_number(x) :
        INDENT
            if str(x) [0] in ['1', '2', '5'] : return int(x)
            else : return scale_number(x - 10 ** ndim)
        DEDENT
        length = scale_number(length)
    DEDENT
    bar_xs = [sbx - length * 500, sbx + length * 500]
    ax.plot(bar_xs, [sby, sby], transform = tmc, color = 'k', linewidth = linewidth)
    ax.text(sbx, sby, str(length) + ' km', transform = tmc,
        horizontalalignment = 'center', verticalalignment = 'bottom')
DEDENT

def getPrimes(n) :
INDENT
    i = 2
    while i < n :
    INDENT
        prime = True
        for a in xrange(2, i) :
        INDENT
            if i % a == 0 :
            INDENT
                prime = False
                break
            DEDENT
        DEDENT
        if prime :
        INDENT
            yield i
        DEDENT
        i += 1
    DEDENT
DEDENT

def __init__(self, year = None, month = None,
day = None, weekday = None,
hour = None, minute = None,
second = None) :
INDENT
    loc = locals()
    loc.pop("self")
    self.at = dict((k, v) for k, v in loc.iteritems() if v ! = None)
DEDENT

def bfs(graph, start, end) :
INDENT
    queue = []
    queue.append([start])
    while queue :
    INDENT
        path = queue.pop(0)
        node = path [- 1]
        if node == end :
        INDENT
            return path
        DEDENT
        for adjacent in graph.get(node, []) :
        INDENT
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
        DEDENT
    DEDENT
DEDENT

def longest(word) :
INDENT
    begin = 0
    end = 0
    longest = (0, 0)
    for i in xrange(len(word)) :
    INDENT
        try :
        INDENT
            j = word.index(word [i], begin, end)
            if end - begin > = longest [1] - longest [0] :
            INDENT
                longest = (begin, end)
            DEDENT
            begin = j + 1
            if begin == end :
            INDENT
                end += 1
            DEDENT
        DEDENT
        except :
        INDENT
            end = i + 1
        DEDENT
    DEDENT
    end = i + 1
    if end - begin > = longest [1] - longest [0] :
    INDENT
        longest = (begin, end)
    DEDENT
    return word [slice(* longest)]
DEDENT

    def test_explicitly_ordered_list_view(self):
        Book.objects.create(name="Zebras for Dummies", pages=800, pubdate=datetime.date(2006, 9, 1))
        res = self.client.get('/list/books/sorted/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object_list'][0].name, '2066')
        self.assertEqual(res.context['object_list'][1].name, 'Dreaming in Code')
        self.assertEqual(res.context['object_list'][2].name, 'Zebras for Dummies')

        res = self.client.get('/list/books/sortedbypagesandnamedec/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['object_list'][0].name, 'Dreaming in Code')
        self.assertEqual(res.context['object_list'][1].name, 'Zebras for Dummies')
        self.assertEqual(res.context['object_list'][2].name, '2066')

def readParag(filename) :
INDENT
    with open(filename) as f :
    INDENT
        while True :
        INDENT
            paras = itertools.takewhile(lambda l : l.strip(), f)
            test, paras = itertools.tee(paras)
            test.next()
            yield (l.strip() for l in paras)
        DEDENT
    DEDENT
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

def transitive_closure(a) :
INDENT
    closure = set()
    for x, _ in a :
    INDENT
        closure |= set((x, y) for y in dfs(x, a))
    DEDENT
    return closure
DEDENT

def __setattr__(self, attribute, value) :
INDENT
    if not attribute in self.__class__.__allowed_attr :
    INDENT
        raise AttributeError
    DEDENT
    else :
    INDENT
        super().__setattr__(attribute, value)
    DEDENT
DEDENT

    @override_settings(DEBUG=True)
    def test_paginated_list_view_returns_useful_message_on_invalid_page(self):
        # test for #19240
        # tests that source exception's message is included in page
        self._make_authors(1)
        res = self.client.get('/list/authors/paginated/2/')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.context.get('reason'), "Invalid page (2): That page contains no results")

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

def __init__(self, some_var) :
INDENT
    QtCore.QObject.__init__(self, parent = None)
    self.some_var = some_var
    self.queue = mp.Queue()
    self.process = mp.Process(
        target = workermodule.some_complex_processing,
        args = (self.queue,))
DEDENT

    def _make_authors(self, n):
        Author.objects.all().delete()
        for i in range(n):
            Author.objects.create(name='Author %02i' % i, slug='a%s' % i)
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

def get_file_list(directory = os.getcwd()) :
INDENT
    def file_list(directory, files) :
    INDENT
        for i in os.listdir(directory) :
        INDENT
            if os.path.isdir(i) :
            INDENT
                file_list(i, files)
                continue
            DEDENT
            files.append(i)
        DEDENT
        return files
    DEDENT
    return file_list(directory, [])
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

def summary(xs) :
INDENT
    for item in xs :
    INDENT
        try :
        INDENT
            yield sum(i ** 2 for i in item)
        DEDENT
        except ValueError :
        INDENT
            yield 0
        DEDENT
    DEDENT
DEDENT

def translate_non_alphanumerics(to_translate, translate_to = '_') :
INDENT
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
    translate_table = string.maketrans(not_letters_or_digits,
        translate_to
        * len(not_letters_or_digits))
    translate_table = translate_table.decode("latin-1")
    return to_translate.translate(translate_table)
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









































































































































