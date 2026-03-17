from django.db import models

try:
    from PIL import Image
except ImportError:
    Image = None


class CaseTestModel(models.Model):
    integer = models.IntegerField()
    integer2 = models.IntegerField(null=True)
    string = models.CharField(max_length=100, default='')

    big_integer = models.BigIntegerField(null=True)
    binary = models.BinaryField(default=b'')
    boolean = models.BooleanField(default=False)
    date = models.DateField(null=True, db_column='date_field')
    date_time = models.DateTimeField(null=True)
    decimal = models.DecimalField(max_digits=2, decimal_places=1, null=True, db_column='decimal_field')
    duration = models.DurationField(null=True)
    email = models.EmailField(default='')
    file = models.FileField(null=True, db_column='file_field')
    file_path = models.FilePathField(null=True)
    float = models.FloatField(null=True, db_column='float_field')
    if Image:
        image = models.ImageField(null=True)
    generic_ip_address = models.GenericIPAddressField(null=True)
    null_boolean = models.BooleanField(null=True)
    null_boolean_old = models.NullBooleanField()
    positive_integer = models.PositiveIntegerField(null=True)
    positive_small_integer = models.PositiveSmallIntegerField(null=True)
    slug = models.SlugField(default='')
    small_integer = models.SmallIntegerField(null=True)
    text = models.TextField(default='')
    time = models.TimeField(null=True, db_column='time_field')
    url = models.URLField(default='')
    uuid = models.UUIDField(null=True)
    fk = models.ForeignKey('self', models.CASCADE, null=True)

    def __str__(self):
        return "%i, %s" % (self.integer, self.string)


def __eq__(self, other) :
INDENT
    if self is other :
    INDENT
        return True
    DEDENT
    if isinstance(self, type(other)) :
    INDENT
        return self._data == other._data
    DEDENT
    else :
    INDENT
        return NotImplemented
    DEDENT
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

def main() :
INDENT
    game_display = pygame.display.set_mode((600, 800))
    shape = Shape(WHITE, 0, 0, 25, 25)
    shape2 = Shape(pygame.Color('sienna1'), 100, 100, 25, 25)
    clock = pygame.time.Clock()
    game_exit = False
    while not game_exit :
    INDENT
        for event in pygame.event.get() :
        INDENT
            if event.type == pygame.QUIT :
            INDENT
                game_exit = True
            DEDENT
        DEDENT
        game_display.fill((40, 40, 40))
        shape.draw(game_display)
        shape2.draw(game_display)
        pygame.display.update()
        clock.tick(60)
    DEDENT
DEDENT

class O2OCaseTestModel(models.Model):
    o2o = models.OneToOneField(CaseTestModel, models.CASCADE, related_name='o2o_rel')
    integer = models.IntegerField()

    def __str__(self):
        return "%i, %s" % (self.id, self.o2o)


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

def getIsland(request) :
INDENT
    island = cache.get("island_" + request.user)
    if island == None :
    INDENT
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
        cache.set("island_" + request.user, island, 60)
    DEDENT
    return island
DEDENT

def parse(self, response) :
INDENT
    log.msg("Begin Parsing", level = log.INFO)
    log.msg("Response from: %s" % response.url, level = log.INFO)
    hxs = HtmlXPathSelector(response)
    sites = hxs.select("//*[@id='moduleData8460']")
    items = response.meta ['items']
    for site in sites :
    INDENT
        item = MlboddsItem()
        item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
        item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text()').extract()
        items.append(item)
    DEDENT
    if self.other_urls :
    INDENT
        return Request(self.other_urls.pop(0), meta = {'items' : items})
    DEDENT
    return items
DEDENT

def transpose(matrix) :
INDENT
    n = 0
    li = []
    while n < (len(matrix)) :
    INDENT
        for sets in matrix :
        INDENT
            li.append(sets [0])
        DEDENT
        n += 1
        print (len(matrix))
    DEDENT
    return li
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

class FKCaseTestModel(models.Model):
    fk = models.ForeignKey(CaseTestModel, models.CASCADE, related_name='fk_rel')
    integer = models.IntegerField()

    def __str__(self):
        return "%i, %s" % (self.id, self.fk)


def __getitem__(self, key) :
INDENT
    c = self.cache [key]
    n = datetime.now()
    if (n - c ['timestamp']) < c ['expireTime'] or not self.processExpires :
    INDENT
        return c ['data']
    DEDENT
    del self.cache [key]
    if self.dbg :
    INDENT
        print "DataCache: Key %s expired" % repr(key)
    DEDENT
    raise KeyExpiredError(key)
DEDENT

def getVerb() :
INDENT
    level1 = ["(manger)", "je mange", "tu manges", "il mange", "elle mange", "nous mangeons", "vous mangez", "ils mangent", "elles mangent"]
    level2 = ["(boire)", "je bois", "tu bois", "il boit", "elle boit", "nous buvons", "vous buvez", "ils boivent", "elles boivent"]
    blanks = '_' * 8
    correctAnswers = 0
    randomElement = random.choice(level1)
    print (randomElement.split() [0], blanks, level1 [0])
    ans = input()
    while True :
    INDENT
        if ans == randomElement.split() [1] :
        INDENT
            correctAnswers += 1
            print ("Nice one!")
            print (correctAnswers)
        DEDENT
        else :
        INDENT
            print ("Bad luck!")
        DEDENT
        ans = input()
    DEDENT
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

def backtrack(res, temp, nums, start) :
INDENT
    res.append([])
    for i in temp :
    INDENT
        res [- 1].append(i);
    DEDENT
    for i in range(start, len(nums)) :
    INDENT
        temp.append(nums [i])
        backtrack(res, temp, nums, i + 1)
        temp.pop()
    DEDENT
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

def listFunc(List) :
INDENT
    if len(List) == 0 : return ''
    if len(List) == 1 : return List [0]
    value = List [0]
    for item in List [1 : - 1] :
    INDENT
        value = value + ', ' + item
    DEDENT
    return value + ', and ' + List [- 1]
DEDENT

class Client(models.Model):
    REGULAR = 'R'
    GOLD = 'G'
    PLATINUM = 'P'
    ACCOUNT_TYPE_CHOICES = (
        (REGULAR, 'Regular'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    )
    name = models.CharField(max_length=50)
    registered_on = models.DateField()
    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=REGULAR,
    )

    def __str__(self):
        return self.name
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

def main() :
INDENT
    q = Queue()
    p1 = Process(target = f1, args = (q,))
    p1.start()
    p2 = Process(target = f2, args = (q,))
    p2.start()
    while True :
    INDENT
        try :
        INDENT
            print q.get()
        DEDENT
        except :
        INDENT
            break
        DEDENT
    DEDENT
DEDENT

def SumOdds(x, y) :
INDENT
    count = 0
    for i in range(x, y) :
    INDENT
        if (int(i % 2 == 1)) :
        INDENT
            count = count + i
        DEDENT
    DEDENT
    if (x % 2 == 0) :
    INDENT
        count = count + x
    DEDENT
    if (y % 2 == 0) :
    INDENT
        count = count + 7
    DEDENT
    print (count)
DEDENT

def second_smallest(ls) :
INDENT
    level = len(getouterframes(currentframe(1)))
    if len(ls) < 2 :
    INDENT
        return None
    DEDENT
    if len(ls) == 2 :
    INDENT
        if level == 1 :
        INDENT
            return max(ls)
        DEDENT
        else :
        INDENT
            return min(ls), max(ls)
        DEDENT
    DEDENT
    else :
    INDENT
        m, n = second_smallest(ls [1 :])
        if ls [0] < = m :
        INDENT
            n = m
            m = ls [0]
        DEDENT
        elif ls [0] < n :
        INDENT
            n = ls [0]
        DEDENT
        if level == 1 :
        INDENT
            return n
        DEDENT
        return m, n
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

def __init__(self, key, value = None) :
INDENT
    if not Master.init_OK :
    INDENT
        raise Exception('Direct call to Master() is not allowed')
    DEDENT
    Master.init_OK = False
    self.key = key
    self.value = value
    Master.existent [key] = self
DEDENT

























