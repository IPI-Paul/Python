# Classes representing groups and articles.
# Author: David Wrag, Paul I Ighofose
# Last modified: 2019-03-09

import os, os.path, time, warnings, cgi

import settings, message, lockfile

# we use tempnam safely.
warnings.filterwarnings('ignore', 'tempnam', RuntimeWarning, 'group')
unicode = type('')

class OpenRange:
    """An OpenRange object contains everything."""
    def __init__(self):
        pass

    def __contains__(self, num):
        return True

class Range:
    """A Range object contains numbers in a given range."""
    
    def __init__(self, lo=None, hi=None):
        self.lo = lo
        self.hi = hi

    def __contains__(self, num):
        return (self.lo is None or num >= self.lo) and (self.hi is None or num <= self.hi)

def isdigit(c):
    """Return true if the given character is a digit."""
    return c >= '0' and c <= '9'

def saferemove(path):
    """Remove a file which does not necessarily exist."""
    try:
        os.remove(path)
    except:
        pass

class NoSuchGroupError(Exception):
    """An Exception indicating that the specified group did not exist."""
    pass

class GroupAlreadyExistsError(Exception):
    """An Exception indicating that a group with the specified name already exists"""
    pass

def group_path(group_name):
    """The proper path name for the directory of the named group."""
    return "%s/%s" % (settings.groups_dir, group_name)

class Group:
    """A NNTP group, and its associated feed information."""
    
    def __init__(self, name, path=None, config=None):
        """Load the group with the given name."""
        if path is None:
            path = group_path('/'.join(name.split('.')))

        if not os.path.isdir(path):
            raise NoSuchGroupError(name)

        self.name = name
        self.path = path

        if config is None:
            config = self.load_eval("config", {})

        self.config = config
        self.lockfile = lockfile.LockFile(self.group_file("lock"))

    def group_file(self, fname):
        """Return the path name for the given file in the group's
        directory."""
        return os.path.join(self.path, fname)

    def load_eval(self, fname, otherwise=None):
        """Load and evaluate a file from the group's directory."""
        path = self.group_file(fname)
        if not os.path.exists(path):
            return otherwise
        
        # f = file(path)
        f = open(path, 'r') 
        expr = f.read()
        f.close()
        return eval(expr)

    def reload_config(self):
        """Reload the group's configuration data.

        The configuration data is loaded when the Group object is
        constructed.  But if it may have changed, this function can be
        used to reload it."""
        self.config = self.load_eval("config", {})

    def save_config(self):
        """Save the group's configuration data."""
        self.save("config", repr(self.config))

    def save(self, fname, val):
        """Save a value into a file in the group's directory."""
        path = self.group_file(fname)
        tmppath = path + ".new"
        f = file(tmppath, "w")
        f.write(val)
        f.close()
        os.rename(tmppath, path)

    def saferemove(self, fname):
        """Remove a file in the group's directory.

        It is not an error if the file does not exist."""
        saferemove(self.group_file(fname))

    def ready_to_check(self, t):
        """Do we need to poll the group's feed at time t?"""
        polled_at = self.config.get("lastpolled", 0)
        failed_at = self.config.get("last_failed_poll", 0)
        interval = self.config.get("interval", settings.feed_poll_interval)

        if failed_at > polled_at:
            next_poll = failed_at + min(interval,
                                    60 << self.config.get("failed_polls", 0))
        else:
            next_poll = polled_at + interval

        return t >= next_poll

    def article_range(self):
        """Determine a (lowest article number, highest article number,
        article count) triple for the group."""
        lowest = self.config.get('next_article_number', 1)
        highest = lowest - 1
        count = 0

        for f in os.listdir(self.path):
            if isdigit(f[0]):
                f = int(f)
                count += 1
                if f < lowest:
                    lowest = f
                if f > highest:
                    highest = f

        return (lowest, highest, count)

    def article(self, num):
        """Fetch an Article object for the given article number.

        Returns None if the article does not exist."""
        entry = self.load_eval(str(num))
        if entry is not None:
            return Article(self, num, entry)
        else:
            return None

    def save_article(self, artnum, entry):
        self.save(str(artnum), repr(entry))

    def delete_article(self, artnum):
        self.saferemove(str(artnum))
    
    def article_file(self, artnum):
        return self.group_file(str(artnum))
    
    def article_numbers(self, range=OpenRange()):
        """Generate the article numbers of articles in the group,
        within the given range."""
        for f in os.listdir(self.path):
            if isdigit(f[0]):
                f = int(f)
                if f in range:
                    yield f

    def articles(self, range=OpenRange()):
        """Return all articles in the group, in article number order."""
        return [self.article(n) for n in sorted(self.article_numbers(range))]

    def next_article_number(self):
        """Produce an article number for the next new article,
        updating the group configuration held within this object."""
        num = self.config.get('next_article_number')
        if num is None:
            num = self.article_range()[1] + 1
        else:
            # just in case...
            while os.path.exists(self.group_file(str(num))):
                num += 1

        self.config['next_article_number'] = num + 1
        return num

    def delete(self):
        # First lock the group, so we know no other processes are
        # accessing it except to lock.
        self.lockfile.lock()

        # Now rename the group directory, because deletion is not
        # atomic but renaming is.
        path = os.tempnam(settings.groups_dir, ".deleting.")
        try:
            os.rename(self.path, path)
        except:
            lock.unlock()
            raise

        # Now delete
        remove_r(path)

def remove_r(d):
    for f in os.listdir(d):
        f = os.path.join(d, f)
        if os.path.isdir(f):
            remove_r(f)
        else:
            os.remove(f)
    os.rmdir(d)

class NewGroup(Group):
    """A NNTP group in the process of creation."""

    def __init__(self, name, config):
        """Create a new group with the given name and config"""
        path = os.tempnam(settings.groups_dir, ".new.")
        os.mkdir(path)
        Group.__init__(self, name, path, config)
        self.save_config()

    def create(self):
        lock = lockfile.LockFile(os.path.join(settings.groups_dir,
                                              ".rename." + self.name))
        try:
            lock.lock()
            path = group_path(self.name)
            if os.path.exists(path):
                raise GroupAlreadyExistsError(name)
    
            os.rename(self.path, path)
            self.path = path
        finally:
            lock.unlock()

def groups():
    """Return a sequence of all available groups."""
    return [Group(d) for d in os.listdir(settings.groups_dir)
            if not d.startswith(".")
            and os.path.isdir(group_path(d))]

def decode_implicit_utf8(s):
    if type(s) is not unicode:
        s = s.decode('utf-8')
    return s

def encode_email_header(name, email="unknown@unknown"):
    """Produce a properly encoded string with the given name and email
    address for use in an article header."""
    return '%s <%s>' % tuple(message.encode_header_word(decode_implicit_utf8(s))
                             for s in [name, email])

def to_html(detail, para=False):
    """Convert a detail-dict produced by the UFP into HTML."""
    type = detail['type']
    if type == 'text/plain':
        html = cgi.escape(detail['value'])
        if para:
            return '<p>%s</p>' % html
        else:
            return html
    else:
        # maybe do something smarter for application/xhtml+xml?
        return detail['value']

class Article:
    """An NNTP article corresponding to a feed entry."""
    
    def __init__(self, group, num, entry):
        self.group = group
        self.num = num
        self.entry = entry

    def same_entry(self, entry):
        """Is the given entry unchanged compared to the entry of this
        article?"""
        def clean(e):
            if 'feed_updated_parsed' in e:
                e = dict(e)
                del e['feed_updated_parsed']
                
            return e

        return clean(self.entry) == clean(entry)

    def number(self):
        """Return the article number."""
        return self.num

    def message_id(self):
        """Return the message-id of this article."""
        return "<%s@%s>" % (self.entry['message_id'], self.group.name)

    def subject(self):
        """Return the subject header value of this article."""
        if 'title_detail' in self.entry:
            # XXX should strip HTML
            return self.entry['title_detail']['value']
        else:
            # XXX do something smarter here?
            return ""

    def content(self):
        """Return a detail-dict with the main content of the feed entry."""
        if 'content' in self.entry:
            return self.entry['content'][0]
        elif 'summary_detail' in self.entry:
            return self.entry['summary_detail']
        else:
            return {'value':'', 'type':'text/plain'}

    def render_body(self):
        """Return a detail-dict to form the body of the article."""
        if 'link' not in self.entry:
            # without a link, plain text entries can be passed through
            c = self.content()
            if c['type'] == 'text/plain':
                return c

        # result is going to be HTML
        res = to_html(self.content(), para=True)
        if 'link' in self.entry:
            link = self.entry['link']
            caption = self.entry.get('title_detail')
            if not (caption and caption['value']):
                caption = {'value':link, 'type':'text/plain'}
            res = "<h1><a href='%s'>%s</a></h1>\n%s" % (link, to_html(caption),
                                                        res)

        return {'value':res, 'type':'text/html'}

    def author(self):
        """Construct an author header value for the article."""
        for d in [self.entry, self.group.config]:
            if 'author_detail' in d:
                ad = d['author_detail']
                if 'name' in ad and 'email' in ad:
                    return encode_email_header(ad['name'], ad['email'])
                elif 'name' in ad:
                    return encode_email_header(ad['name'])
                elif 'email' in ad:
                    return message.encode_header_word(ad['email'])
            elif 'author' in d:
                return encode_email_header(d['author'])

        if 'title' in self.group.config:
            return encode_email_header(self.group.config['title'])
                                
        return 'Unknown <unknown@unknown>'

    def date(self):
        """Construct a date header value for the article."""
        t = self.entry.get('updated_parsed')
        if not t:
            t = self.entry.get('published_parsed')
        if not t:
            t = self.entry.get('feed_updated_parsed')
        return time.strftime("%d %b %Y %H:%M:%S %z", t)

    def make_message(self):
        """Construct the NNTP article."""
        
        # we don't know lines and bytes, but NNTP clients seem to
        # tolerate it when those fields are missing
        msg = message.Message()
        msg['From'] = self.author()
        msg['Newsgroups'] = self.group.name
        msg['Date'] = self.date()
        msg['Subject'] = self.subject()
        msg['Message-ID'] = self.message_id()
        msg['Path'] = 'pnntprss'

        body = self.render_body()
        msg.set_body(body['value'], body['type'])
        
        return msg
