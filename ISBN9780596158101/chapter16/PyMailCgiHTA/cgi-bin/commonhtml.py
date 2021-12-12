#!/usr/bin/env python3

# Example 16-14
# Defines functions that dump raw CGI environment information to the browser 
# (dumpstatepage), and that wrap calls to functions that print status messages 
# so that their output isn't added to the HTML stream (runsilent)
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-07

"""
################################################################################
generate standard page header, list, and footer HTML; isolates HTML generation 
related details in this file; text printed here goes over asocket to the client, 
to create parts of a new web page in the web browser; uses one print per line, 
instead of string blocks; uses urllib to escape params in URL links auto from a 
dict, but cgi.escape to put them in HTML hidden fields; some tools here may be 
useful outside pymailcgi; could also return the HTML generated here instead of 
printing it, so it could be included in other pages; could also structure as a 
single CGI script that gets and tests a next action name as a hidden form field; 
caveat: this system works, but wa largely written during a two-hour layover at 
the Chicago O'Hare airport: there is much room for improvement and optimization;
################################################################################
"""

import cgi, urllib.parse, sys, os

# 3.0: Python 3.1 has issues printing some decoded str as text to stdout
import builtins
bstdout = open(sys.stdout.fileno(), 'wb')
tab = ' ' * 2
def print(*args, end='\n'):
    try:
        builtins.print(*args, end=end)
        sys.stdout.flush()
    except:
        for arg in args:
            bstdout.write(str(arg).encode('utf-8'))
        if end: bstdout.write(end.encode('utf-8'))
        bstdout.flush()

sys.stderr = sys.stdout             # show error messages in browser
from externs import mailconfig      # from a package somewhere on server
from externs import mailtools       # need parser for header decoding
parser = mailtools.MailParser()     # one per process in this module

# my cgi address root
# urlroot = 'http://starship.python.net/~lutz/PyMailCgi/'
# urlroot = 'http://localhost:8000/cgi-bin'

urlroot = ''    # use minimal, relative paths

def pageheader(app='PyMailCGI', color='#FFFFFF', kind='main', info=''):
    print('Content-type: text/html\n')
    print('<html>\n', tab, '<head>\n', tab*2, 
          '<title>%s: %s page (PP4E)</title>\n' % (app, kind))
    print(tab*2, '<script>\n', 
          tab*3, 'function emlOpen(lnk, idx) { \n', 
          tab*4, 'document.getElementById("emlFrm").src = lnk;\n',
          tab*4, 'var tbl = document.getElementById("emlList");\n;',
          tab*4, 'for (var i = 0; i < tbl.rows.length; i++) {\n',
          tab*5, 'tbl.rows[i].cells[0].style.background="white";\n',
          tab*4, '}\n',
          tab*4, 'tbl.rows[idx].cells[0].style.background="orange";\n',
          tab*3, '}\n',
          tab*3, 'function emlAction() {\n', 
          tab*4, 'if (document.getElementById("action").value == "Delete") {\n', 
          tab*5, 'var tbl = parent.document.getElementById("emlList"), mnum;\n', 
          tab*5, 'for (var i = 0; i < tbl.rows.length; i++) {\n',
          tab*6, 'if (tbl.rows[i].cells[0].style.background=="orange") {\n',
          tab*7, 'tbl.deleteRow(i);\n',
          tab*6, '}\n',
          tab*6, 'mnum = tbl.rows[i].id.split("?")[1].split("&")[0];\n',
          tab*6, 'tbl.rows[i].id = tbl.rows[i].id.replace(mnum, "mnum=" + (i + 1));\n',
          tab*5, '}\n',
          tab*4, '}\n',
          tab*4, 'document.getElementById("vfrm").submit();\n',
          tab*3, '}\n',
          tab*2, '</script>')
    print(tab*2, '<style>\n',tab*3, 'table, td {\n', tab*4, 'font-size: 10pt;\n', 
          tab*4, 'vertical-align: top;\n', tab*4, 'border-collapse: collapse;\n', 
          tab*4, 'padding:0px;\n', tab*3, '}\n', tab*2, '</style>',
          tab, '</head>')
    print(tab, '<body bgcolor="%s">\n'% color)

def pagefooter(root='pymailcgi.html'):
    print(tab*2, '</p>\n', tab*2, '<hr />\n', tab, '</body>\n','</html>')

def formatlink(cgiurl, parmdict):
    """
    make "%url?key=val&key=val" query link from a dictionary;
    escapes str() of all key and val with %xx, changes ' ' to +
    note that URL escapes are different from HTML (cgi.escape)
    """
    parmtext = urllib.parse.urlencode(parmdict)     # calls parse.quote_plus
    return '%s?%s' % (cgiurl, parmtext)                # urllib does all the work

def pagelistsimple(linklist):                       # showlist in a table
    print(tab*2, '<ol>')
    for (text,cgiurl, parmdict) in linklist:
        link = formatlink(cgiurl, parmdict)
        text = cgi.escape(text)
        print(tab*3, '<li>\n', tab*4,'<a href="%s">\n' % link, tab*5, '%s\n' % text, 
              tab*4, '</a>\n', tab*3, '</li>')
    print(tab*2, '</ol>')

def pagelisttable(linklist):                        # show list in a table
    print(tab*3,'<table border="0" cellpadding="0" width="100%" height="100%">\n',
          tab*4, '<tr>\n', tab*5, '<td width="200">\n', 
          tab*6, '<table id="emlList" border>') 
    for (text, cgiurl, parmdict) in linklist:
        link = formatlink(cgiurl, parmdict)
        text = cgi.escape(text)
        sbj, adr, dt = text.split('|') 
        print(tab*7, '<tr id="%s" onclick="emlOpen(id, rowIndex)">\n'% link, 
              tab*8, '<td>\n', 
              tab*9, '%s<br />\n' % dt, 
              tab*9, '%s<br />\n' % sbj, 
              tab*9, '%s<br />\n' % adr, 
              tab*8, '</td>\n', 
              tab*7, '</tr>' )
    print(tab*6, '</table>\n', tab*5, '</td>')
    print(tab*5, '<td>\n', tab*6, '<iframe id="emlFrm" width="100%" height="100%" ',
          'src="javascript: document.write(\'Hello PyMailCGI World!<br />',
          '<br />Click on a link in the list on the left to View the email.\');" />',
          tab*5, '</td>\n', tab*4, '<tr>\n', tab*3, '</table>')

def listpage(linkslist, kind='selection list'):
    pageheader(kind=kind)
    pagelisttable(linkslist)            # [('text', 'cgiurl', {'parm': 'value'})]
    pagefooter()

def messagearea(headers, text, extra=''):               # extra for readonly
    addrhdrs = ('From', 'To', 'Cc', 'Bcc')              # decode names only
    print(tab*3, '<p>\n', tab*4, '<table border cellpadding="3" width="100%">')
    for hdr in ('From', 'To', 'Cc', 'Subject'):
        rawhdr = headers.get(hdr, '?')
        if hdr not in addrhdrs:
            dechdr = parser.decodeHeader(rawhdr)        # 3.0: decode for display
        else:                                           # encoded on sends
            dechdr = parser.decodeAddrHeader(rawhdr)    #email names only
        val = cgi.escape(dechdr, quote=1)
        print(tab*5, '<tr>\n', tab*6, '<th align="right">\n', tab*7, '%s\n' % hdr, 
              tab*6, '</th>')
        print(tab*6, '<td>\n', tab*7, '<input type="text" name="%s" value="%s" '
              % (hdr, val), '%s size="60" />\n'  % extra, tab*6, '</td>\n', 
              tab*5, '</tr>')
    print(tab*5, '<tr>', tab*6, '<td colspan="2">\n', )
    if extra == 'readonly':
        print(tab*7, '<span>\n', tab*8,
              '%s\n' % (text.replace('\n', '<br />') or '?'), tab*7, '</span>\n',
              tab*7, '<textarea name="text" style="display:none;">',
              '%s\n' % (cgi.escape(text) or '?'), tab*7, '</textarea>')
    else:
        print(tab*7, '<textarea name="text" cols="80" rows="10" %s>'
              % extra, '%s\n' % (cgi.escape(text) or '?'), tab*7, '</textarea>')
    print(tab*6, '</td>\n', tab*5, '</tr>\n', tab*4, '</table>')# if has </>s

def viewattachmentlinks(partnames):
    """
    create hyperlinks to locally saved part/attachment files when clicked, user's 
    web browser will handle opening 
    assumes just one user, only valid while viewing 1 msg
    """
    print(tab*2, '<hr />\n', tab*2, '<table border cellpadding="3">\n', tab*3,
          '<tr>\n', tab*4, '<th>\n', tab*5, 'Parts:\n', tab*4, '</th>')
    for filename in partnames:
        basename = os.path.basename(filename)
        filename = filename.replace('\\', '/')      # Windows hack
        print(tab*4, '<td>\n', tab*5, '<a href="../%s">\n'  
              % filename, tab*6, '%s\n' % basename, tab*5, '</a>\n', tab*4, 
              '</td>')
    print(tab*3, '</tr>\n', tab*2, '</table>\n', tab*2, '<hr />')

def viewpage(msgnum, headers, text, form, parts=[]):
    """
    on View + select (generated link click)
    very subtle thing: at this point, pswd was URL encoded in the link, and then
    unencoded by CGI input parser; it'sbeing embedded in HTML here, so we use 
    cgi.escape; this usually sends nonprintable chars in the hidden field's HTML, 
    but works on ie and ns anyhow:
    in url: ?user=lutz&mnum=3&pswd=%8cg%c2P%1e%f0%5b%c5J%1c%f3&...
    in html: <input type=hidden name=pswd value="...nonprintables...">
    could urllib.parse.quote html field here too, but must urllib.parse.unquote 
    in next script (which precludes passing the inputs in a URL instead of the 
    form); cal also fall back on numeric string fmt in secret.py
    """
    pageheader(kind='View')
    user, pswd, site = list(map(cgi.escape, getstandardpopfields(form)))
    print(tab*2, '<form id="vfrm" method="post" action="%sonViewPageAction.py">' 
          % urlroot)
    print(tab*3, '<input type="hidden" name="mnum" value="%s" />' % msgnum)
    print(tab*3, '<input type="hidden" name="user" value="%s" />'   # from page|url
          % user) 
    print(tab*3, '<input type="hidden" name="site" value="%s" />'   # for deletes
          % site)
    print(tab*3, '<input type="hidden" name="pswd" value="%s" />'   # pswd encoded
          % pswd)
    if form['lpop'].value == 'on':
        print(tab*3, '<input type="hidden" name="dellist" value="%s" />'  
              % headers.get('File'))
    messagearea(headers, text, 'readonly')
    if parts: viewattachmentlinks(parts)
    
    # onViewPageAction.quotetext needs date passed in page
    print(tab*3, '<input type="hidden" name="Date" value="%s" />' % 
          headers.get('Date', '?'))
    print(tab*3, '<table>\n', tab*4, '<tr>\n', tab*5, '<th align="right">\n',
          tab*6, 'Action:\n', tab*5, '</th>')
    print(tab*5, '<td>\n', tab*6, '<select id="action" name="action">')
    print(tab*7, '<option value="Reply">\n', tab*8, 'Reply\n', tab*7, '</option>\n', 
          tab*7,'<option value="Forward">\n', tab*8, 'Forward\n', tab*7, '</option>\n', 
          tab*7,'<option value="Delete">\n', tab*8, 'Delete\n', tab*7, '</option>\n',  
          tab*6,'</select>')
    print(tab*6, '<input type="button" onclick="emlAction()" value="Next" />\n', 
          tab*5, '</td>\n', tab*4, '</tr>')
    print(tab*3, '</table>\n', tab*2, '</form>')    # no reset needed here
    pagefooter()

def sendattachmentwidgets(maxattach=3):
    print(tab*2, '<p>\n', tab*3, '<b>Attach:</b>\n', tab*3, '<br />')
    for i in range(1, maxattach+1):
        print(tab*3, '<input size="80" type="file" name="attach%d" />\n' % i,
              tab*3, '<br />')
    print(tab*2, '</p>')

def editpage(kind, headers={}, text=''):
    # on Send, View+select+Reply, View+select+Fwd
    pageheader(kind=kind)
    print(tab*2, '<p>\n', tab*3, '<form enctype="multipart/form-data" ', 
          'method="post"', end=' ')
    print('action="%sonEditPageSend.py">' % urlroot)
    if mailconfig.mysignature:
        text = '\n%s\n%s' % (mailconfig.mysignature, text)
    messagearea(headers, text)
    sendattachmentwidgets()
    print(tab*4, '<input type="submit" value="Send" />')
    print(tab*4, '<input type="reset" value="Reset" />')
    print(tab*3, '</form>\n', tab*2, '</p>')
    pagefooter()
    
def errorpage(message, stacktrace=True):
    pageheader(kind='Error')                    # was sys.exc_type/exc_value
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(tab*2, '<h2>Error Description</h2>\n', tab*2, '<p>\n', tab*3, 
          message, '\n', tab*2, '</p>')
    print(tab*2, '<h2>Python Exception</h2>\n', tab*2, '<p>\n', tab*3,
          cgi.escape(str(exc_type)), '\n', tab*2, '</p>')
    print(tab*2, '<h2>Exception details</h2>\n', tab*2, '<p>\n', tab*3,
          cgi.escape(str(exc_value)), '\n', tab*2, '</p>')
    if stacktrace:
        print(tab*2, '<h2>Exception traceback</h2>\n',tab*2, '<p>\n', tab*3,
              '<pre>\n', tab*4, end='')
        import traceback
        traceback.print_tb(exc_tb, None, sys.stdout)
        print(tab*3, '</pre>')
    pagefooter()

def confirmationpage(kind):
    pageheader(kind='Confirmation')
    msg = """Click a button above to either Send another or View a list of emails
    <br /><br />If the email list is currently displayed, select an item in the 
    list to download and view that email
    """
    print(tab*2, '<h2>%s operation was successful</h2>' % kind)
    print(tab*2, '<p>\n', tab*3, msg,
          tab*2, '</p>')
    pagefooter()

def getfield(form, field, default=''):
    # emulate dictionary get method
    return (field in form and form[field].value) or default

def getstandardpopfields(form):
    """
    fields can arrive missing or '' or with a real value hardcoded in a URL; 
    default to mailconfig settings
    """
    return (getfield(form, 'user', mailconfig.popusername),
            getfield(form, 'pswd', '?'),
            getfield(form, 'site', mailconfig.popservername))

def getstandardsmtpfields(form):
    return getfield(form, 'site', mailconfig.smtpservername)

def runsilent(func, args):
    """
    run a function without writing stdout
    ex: supress print's in imported tools ales they go to the client/browser
    """
    class Silent:
        def write(self, line): pass
    save_stdout = sys.stdout
    sys.stdout = Silent()               # send print to dummy object
    try:                                # which has a write method
        result = func(*args)            # try to return func result
    finally:                            # but always restore stdout
        sys.stdout = save_stdout
    return result

def dumpstatepage(exhaustive=0):
    """
    for debugging: call me at top of a CGI to generate a new page with CGI state 
    details
    """
    if exhaustive:
        cgi.test()                      # show page with form, environ, etc.
    else:
        pageheader(kind='state dump')
        form = cgi.FieldStorage()       # show just form fields names/values
        cgi.print_form(form)
        pagefooter()
    sys.exit()

def selftest(showastable=False):        # make phony web page
    links = [                           # [(text, url, {parms})]
        ('text1', urlroot + 'page1.cgi', {'a': 1}),
        ('text2', urlroot + 'page1.cgi', {'a': 2, 'b': '3'}),
        ('text3', urlroot + 'page2.cgi', {'x': 'a b', 'y': 'a<b&c', 'z':'?'}),
        ('te<>4', urlroot + 'page2.cgi', {'<x>': '', 'y': '<a>', 'z': None})]
    pageheader(kind='View')
    if showastable:
        pagelisttable(links)
    else:
        pagelistsimple(links)
    pagefooter()

if __name__ == '__main__':              # when run, not imported
    selftest(len(sys.argv) > 1)         # HTML goes to stdout