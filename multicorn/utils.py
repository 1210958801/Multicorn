# -*- coding: utf-8 -*-
# Copyright © 2008-2011 Kozea
# This file is part of Multicorn, licensed under a 3-clause BSD license.


# If pygment installed use colorize
try:
    from pygments.console import colorize
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.lexers import JavascriptLexer
    from pygments.lexers import SqlLexer
    from pygments.formatters import TerminalFormatter

    def print_py(py):
        print(highlight(py,
                  PythonLexer(),
                  TerminalFormatter(bg="dark")))

    def print_js(js):
        print(highlight(js,
                  JavascriptLexer(),
                  TerminalFormatter(bg="dark")))

    def print_sql(sql):
        print(highlight(sql,
                  SqlLexer(),
                  TerminalFormatter(bg="dark")))

except ImportError:
    colorize = lambda x, y: y

    def print_py(py):
        print(py)
    print_js = print_py
    print_sql = print_py

try:
    str.isidentifier
except AttributeError:
    # Python 2
    import re
    # http://docs.python.org/py3k/reference/lexical_analysis.html#identifiers
    # the uppercase and lowercase letters A through Z, the underscore _
    # and, except for the first character, the digits 0 through 9.
    _identifiers_re = re.compile('^[a-zA-Z_][a-zA-Z_0-9]*$')

    def isidentifier(string):
        return _identifiers_re.match(string) is not None
else:
    # Python 3
    def isidentifier(string):
        return string.isidentifier()
