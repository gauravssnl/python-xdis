# (C) Copyright 2017 by Rocky Bernstein
import inspect
class Code3:
    """Class for a Python3 code object used when a Python interpreter less than 3 is
    working on Python3 bytecode
    """
    def __init__(self, co_argcount, co_kwonlyargcount, co_nlocals,
                 co_stacksize, co_flags, co_code,
                 co_consts, co_names, co_varnames, co_filename, co_name,
                 co_firstlineno, co_lnotab, co_freevars, co_cellvars):
        self.co_argcount = co_argcount
        self.co_kwonlyargcount = co_kwonlyargcount
        self.co_nlocals = co_nlocals
        self.co_stacksize = co_stacksize
        self.co_flags = co_flags
        # FIXME: should we enforce co_flags to be bytes rather than str?
        self.co_code = co_code
        self.co_consts = co_consts
        self.co_names = co_names
        self.co_varnames = co_varnames
        self.co_filename = co_filename
        self.co_name = co_name
        self.co_firstlineno = co_firstlineno
        # FIXME: should we enforce co_lnotab to be bytes rather than str?
        self.co_lnotab = co_lnotab
        self.co_freevars = co_freevars
        self.co_cellvars = co_cellvars

class Code2:
    """Class for a Python2 code object used when a Python 3 interpreter is
    working on Python2 bytecode
    """
    def __init__(self, co_argcount, co_kwonlyargcount, co_nlocals, co_stacksize,
                 co_flags, co_code,
                 co_consts, co_names, co_varnames, co_filename, co_name,
                 co_firstlineno, co_lnotab, co_freevars, co_cellvars):
        self.co_argcount = co_argcount
        # Note: There is no kwonlyargcount in Python2
        self.co_kwonlyargcount = co_kwonlyargcount
        self.co_nlocals = co_nlocals
        self.co_stacksize = co_stacksize
        self.co_flags = co_flags
        # FIXME: should we enforce co_code to be str rather than bytes?
        self.co_code = co_code
        self.co_consts = co_consts
        self.co_names = co_names
        self.co_varnames = co_varnames
        self.co_filename = co_filename
        self.co_name = co_name
        self.co_firstlineno = co_firstlineno
        # FIXME: should we enforce co_lnotab to be str rather than bytes?
        self.co_lnotab = co_lnotab
        self.co_freevars = co_freevars
        self.co_cellvars = co_cellvars

def iscode(obj):
    """A replacement for inspect.iscode() which we can't used because we may be
    using a different version of Python than the version of Python used
    in creating the byte-compiled objects. Here, the code types may mismatch.
    """
    return inspect.iscode(obj) or isinstance(obj, Code3) or isinstance(obj, Code2)

def code_has_star_arg(code):
    """Return True iff
    the code object has a variable positional parameter (*args-like)"""
    return (code.co_flags & 4) != 0

def code_has_star_star_arg(code):
    """Return True iff
    The code object has a variable keyword parameter (**kwargs-like)."""
    return (code.co_flags & 8) != 0
