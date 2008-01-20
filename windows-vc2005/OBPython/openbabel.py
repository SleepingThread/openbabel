# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _openbabel
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _openbabel.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _openbabel.PySwigIterator_value(*args)
    def incr(*args): return _openbabel.PySwigIterator_incr(*args)
    def decr(*args): return _openbabel.PySwigIterator_decr(*args)
    def distance(*args): return _openbabel.PySwigIterator_distance(*args)
    def equal(*args): return _openbabel.PySwigIterator_equal(*args)
    def copy(*args): return _openbabel.PySwigIterator_copy(*args)
    def next(*args): return _openbabel.PySwigIterator_next(*args)
    def previous(*args): return _openbabel.PySwigIterator_previous(*args)
    def advance(*args): return _openbabel.PySwigIterator_advance(*args)
    def __eq__(*args): return _openbabel.PySwigIterator___eq__(*args)
    def __ne__(*args): return _openbabel.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _openbabel.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _openbabel.PySwigIterator___isub__(*args)
    def __add__(*args): return _openbabel.PySwigIterator___add__(*args)
    def __sub__(*args): return _openbabel.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _openbabel.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class vectorInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorInt, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorInt_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorInt___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorInt___len__(*args)
    def pop(*args): return _openbabel.vectorInt_pop(*args)
    def __getslice__(*args): return _openbabel.vectorInt___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorInt___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorInt___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorInt___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorInt___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorInt___setitem__(*args)
    def append(*args): return _openbabel.vectorInt_append(*args)
    def empty(*args): return _openbabel.vectorInt_empty(*args)
    def size(*args): return _openbabel.vectorInt_size(*args)
    def clear(*args): return _openbabel.vectorInt_clear(*args)
    def swap(*args): return _openbabel.vectorInt_swap(*args)
    def get_allocator(*args): return _openbabel.vectorInt_get_allocator(*args)
    def begin(*args): return _openbabel.vectorInt_begin(*args)
    def end(*args): return _openbabel.vectorInt_end(*args)
    def rbegin(*args): return _openbabel.vectorInt_rbegin(*args)
    def rend(*args): return _openbabel.vectorInt_rend(*args)
    def pop_back(*args): return _openbabel.vectorInt_pop_back(*args)
    def erase(*args): return _openbabel.vectorInt_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorInt(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorInt_push_back(*args)
    def front(*args): return _openbabel.vectorInt_front(*args)
    def back(*args): return _openbabel.vectorInt_back(*args)
    def assign(*args): return _openbabel.vectorInt_assign(*args)
    def resize(*args): return _openbabel.vectorInt_resize(*args)
    def insert(*args): return _openbabel.vectorInt_insert(*args)
    def reserve(*args): return _openbabel.vectorInt_reserve(*args)
    def capacity(*args): return _openbabel.vectorInt_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorInt
    __del__ = lambda self : None;
vectorInt_swigregister = _openbabel.vectorInt_swigregister
vectorInt_swigregister(vectorInt)

class vectorUnsignedInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorUnsignedInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorUnsignedInt, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorUnsignedInt_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorUnsignedInt___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorUnsignedInt___len__(*args)
    def pop(*args): return _openbabel.vectorUnsignedInt_pop(*args)
    def __getslice__(*args): return _openbabel.vectorUnsignedInt___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorUnsignedInt___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorUnsignedInt___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorUnsignedInt___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorUnsignedInt___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorUnsignedInt___setitem__(*args)
    def append(*args): return _openbabel.vectorUnsignedInt_append(*args)
    def empty(*args): return _openbabel.vectorUnsignedInt_empty(*args)
    def size(*args): return _openbabel.vectorUnsignedInt_size(*args)
    def clear(*args): return _openbabel.vectorUnsignedInt_clear(*args)
    def swap(*args): return _openbabel.vectorUnsignedInt_swap(*args)
    def get_allocator(*args): return _openbabel.vectorUnsignedInt_get_allocator(*args)
    def begin(*args): return _openbabel.vectorUnsignedInt_begin(*args)
    def end(*args): return _openbabel.vectorUnsignedInt_end(*args)
    def rbegin(*args): return _openbabel.vectorUnsignedInt_rbegin(*args)
    def rend(*args): return _openbabel.vectorUnsignedInt_rend(*args)
    def pop_back(*args): return _openbabel.vectorUnsignedInt_pop_back(*args)
    def erase(*args): return _openbabel.vectorUnsignedInt_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorUnsignedInt(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorUnsignedInt_push_back(*args)
    def front(*args): return _openbabel.vectorUnsignedInt_front(*args)
    def back(*args): return _openbabel.vectorUnsignedInt_back(*args)
    def assign(*args): return _openbabel.vectorUnsignedInt_assign(*args)
    def resize(*args): return _openbabel.vectorUnsignedInt_resize(*args)
    def insert(*args): return _openbabel.vectorUnsignedInt_insert(*args)
    def reserve(*args): return _openbabel.vectorUnsignedInt_reserve(*args)
    def capacity(*args): return _openbabel.vectorUnsignedInt_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorUnsignedInt
    __del__ = lambda self : None;
vectorUnsignedInt_swigregister = _openbabel.vectorUnsignedInt_swigregister
vectorUnsignedInt_swigregister(vectorUnsignedInt)

class vvInt(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vvInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vvInt, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vvInt_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vvInt___nonzero__(*args)
    def __len__(*args): return _openbabel.vvInt___len__(*args)
    def pop(*args): return _openbabel.vvInt_pop(*args)
    def __getslice__(*args): return _openbabel.vvInt___getslice__(*args)
    def __setslice__(*args): return _openbabel.vvInt___setslice__(*args)
    def __delslice__(*args): return _openbabel.vvInt___delslice__(*args)
    def __delitem__(*args): return _openbabel.vvInt___delitem__(*args)
    def __getitem__(*args): return _openbabel.vvInt___getitem__(*args)
    def __setitem__(*args): return _openbabel.vvInt___setitem__(*args)
    def append(*args): return _openbabel.vvInt_append(*args)
    def empty(*args): return _openbabel.vvInt_empty(*args)
    def size(*args): return _openbabel.vvInt_size(*args)
    def clear(*args): return _openbabel.vvInt_clear(*args)
    def swap(*args): return _openbabel.vvInt_swap(*args)
    def get_allocator(*args): return _openbabel.vvInt_get_allocator(*args)
    def begin(*args): return _openbabel.vvInt_begin(*args)
    def end(*args): return _openbabel.vvInt_end(*args)
    def rbegin(*args): return _openbabel.vvInt_rbegin(*args)
    def rend(*args): return _openbabel.vvInt_rend(*args)
    def pop_back(*args): return _openbabel.vvInt_pop_back(*args)
    def erase(*args): return _openbabel.vvInt_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vvInt(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vvInt_push_back(*args)
    def front(*args): return _openbabel.vvInt_front(*args)
    def back(*args): return _openbabel.vvInt_back(*args)
    def assign(*args): return _openbabel.vvInt_assign(*args)
    def resize(*args): return _openbabel.vvInt_resize(*args)
    def insert(*args): return _openbabel.vvInt_insert(*args)
    def reserve(*args): return _openbabel.vvInt_reserve(*args)
    def capacity(*args): return _openbabel.vvInt_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vvInt
    __del__ = lambda self : None;
vvInt_swigregister = _openbabel.vvInt_swigregister
vvInt_swigregister(vvInt)

class vectorDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorDouble, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorDouble_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorDouble___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorDouble___len__(*args)
    def pop(*args): return _openbabel.vectorDouble_pop(*args)
    def __getslice__(*args): return _openbabel.vectorDouble___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorDouble___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorDouble___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorDouble___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorDouble___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorDouble___setitem__(*args)
    def append(*args): return _openbabel.vectorDouble_append(*args)
    def empty(*args): return _openbabel.vectorDouble_empty(*args)
    def size(*args): return _openbabel.vectorDouble_size(*args)
    def clear(*args): return _openbabel.vectorDouble_clear(*args)
    def swap(*args): return _openbabel.vectorDouble_swap(*args)
    def get_allocator(*args): return _openbabel.vectorDouble_get_allocator(*args)
    def begin(*args): return _openbabel.vectorDouble_begin(*args)
    def end(*args): return _openbabel.vectorDouble_end(*args)
    def rbegin(*args): return _openbabel.vectorDouble_rbegin(*args)
    def rend(*args): return _openbabel.vectorDouble_rend(*args)
    def pop_back(*args): return _openbabel.vectorDouble_pop_back(*args)
    def erase(*args): return _openbabel.vectorDouble_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorDouble_push_back(*args)
    def front(*args): return _openbabel.vectorDouble_front(*args)
    def back(*args): return _openbabel.vectorDouble_back(*args)
    def assign(*args): return _openbabel.vectorDouble_assign(*args)
    def resize(*args): return _openbabel.vectorDouble_resize(*args)
    def insert(*args): return _openbabel.vectorDouble_insert(*args)
    def reserve(*args): return _openbabel.vectorDouble_reserve(*args)
    def capacity(*args): return _openbabel.vectorDouble_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorDouble
    __del__ = lambda self : None;
vectorDouble_swigregister = _openbabel.vectorDouble_swigregister
vectorDouble_swigregister(vectorDouble)

class vectorString(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorString, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorString, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorString_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorString___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorString___len__(*args)
    def pop(*args): return _openbabel.vectorString_pop(*args)
    def __getslice__(*args): return _openbabel.vectorString___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorString___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorString___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorString___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorString___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorString___setitem__(*args)
    def append(*args): return _openbabel.vectorString_append(*args)
    def empty(*args): return _openbabel.vectorString_empty(*args)
    def size(*args): return _openbabel.vectorString_size(*args)
    def clear(*args): return _openbabel.vectorString_clear(*args)
    def swap(*args): return _openbabel.vectorString_swap(*args)
    def get_allocator(*args): return _openbabel.vectorString_get_allocator(*args)
    def begin(*args): return _openbabel.vectorString_begin(*args)
    def end(*args): return _openbabel.vectorString_end(*args)
    def rbegin(*args): return _openbabel.vectorString_rbegin(*args)
    def rend(*args): return _openbabel.vectorString_rend(*args)
    def pop_back(*args): return _openbabel.vectorString_pop_back(*args)
    def erase(*args): return _openbabel.vectorString_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorString(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorString_push_back(*args)
    def front(*args): return _openbabel.vectorString_front(*args)
    def back(*args): return _openbabel.vectorString_back(*args)
    def assign(*args): return _openbabel.vectorString_assign(*args)
    def resize(*args): return _openbabel.vectorString_resize(*args)
    def insert(*args): return _openbabel.vectorString_insert(*args)
    def reserve(*args): return _openbabel.vectorString_reserve(*args)
    def capacity(*args): return _openbabel.vectorString_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorString
    __del__ = lambda self : None;
vectorString_swigregister = _openbabel.vectorString_swigregister
vectorString_swigregister(vectorString)

class vVector3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vVector3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vVector3, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vVector3_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vVector3___nonzero__(*args)
    def __len__(*args): return _openbabel.vVector3___len__(*args)
    def pop(*args): return _openbabel.vVector3_pop(*args)
    def __getslice__(*args): return _openbabel.vVector3___getslice__(*args)
    def __setslice__(*args): return _openbabel.vVector3___setslice__(*args)
    def __delslice__(*args): return _openbabel.vVector3___delslice__(*args)
    def __delitem__(*args): return _openbabel.vVector3___delitem__(*args)
    def __getitem__(*args): return _openbabel.vVector3___getitem__(*args)
    def __setitem__(*args): return _openbabel.vVector3___setitem__(*args)
    def append(*args): return _openbabel.vVector3_append(*args)
    def empty(*args): return _openbabel.vVector3_empty(*args)
    def size(*args): return _openbabel.vVector3_size(*args)
    def clear(*args): return _openbabel.vVector3_clear(*args)
    def swap(*args): return _openbabel.vVector3_swap(*args)
    def get_allocator(*args): return _openbabel.vVector3_get_allocator(*args)
    def begin(*args): return _openbabel.vVector3_begin(*args)
    def end(*args): return _openbabel.vVector3_end(*args)
    def rbegin(*args): return _openbabel.vVector3_rbegin(*args)
    def rend(*args): return _openbabel.vVector3_rend(*args)
    def pop_back(*args): return _openbabel.vVector3_pop_back(*args)
    def erase(*args): return _openbabel.vVector3_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vVector3(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vVector3_push_back(*args)
    def front(*args): return _openbabel.vVector3_front(*args)
    def back(*args): return _openbabel.vVector3_back(*args)
    def assign(*args): return _openbabel.vVector3_assign(*args)
    def resize(*args): return _openbabel.vVector3_resize(*args)
    def insert(*args): return _openbabel.vVector3_insert(*args)
    def reserve(*args): return _openbabel.vVector3_reserve(*args)
    def capacity(*args): return _openbabel.vVector3_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vVector3
    __del__ = lambda self : None;
vVector3_swigregister = _openbabel.vVector3_swigregister
vVector3_swigregister(vVector3)

class vectorMol(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorMol, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorMol, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorMol_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorMol___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorMol___len__(*args)
    def pop(*args): return _openbabel.vectorMol_pop(*args)
    def __getslice__(*args): return _openbabel.vectorMol___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorMol___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorMol___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorMol___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorMol___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorMol___setitem__(*args)
    def append(*args): return _openbabel.vectorMol_append(*args)
    def empty(*args): return _openbabel.vectorMol_empty(*args)
    def size(*args): return _openbabel.vectorMol_size(*args)
    def clear(*args): return _openbabel.vectorMol_clear(*args)
    def swap(*args): return _openbabel.vectorMol_swap(*args)
    def get_allocator(*args): return _openbabel.vectorMol_get_allocator(*args)
    def begin(*args): return _openbabel.vectorMol_begin(*args)
    def end(*args): return _openbabel.vectorMol_end(*args)
    def rbegin(*args): return _openbabel.vectorMol_rbegin(*args)
    def rend(*args): return _openbabel.vectorMol_rend(*args)
    def pop_back(*args): return _openbabel.vectorMol_pop_back(*args)
    def erase(*args): return _openbabel.vectorMol_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorMol(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorMol_push_back(*args)
    def front(*args): return _openbabel.vectorMol_front(*args)
    def back(*args): return _openbabel.vectorMol_back(*args)
    def assign(*args): return _openbabel.vectorMol_assign(*args)
    def resize(*args): return _openbabel.vectorMol_resize(*args)
    def insert(*args): return _openbabel.vectorMol_insert(*args)
    def reserve(*args): return _openbabel.vectorMol_reserve(*args)
    def capacity(*args): return _openbabel.vectorMol_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorMol
    __del__ = lambda self : None;
vectorMol_swigregister = _openbabel.vectorMol_swigregister
vectorMol_swigregister(vectorMol)

class vectorBond(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorBond, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorBond, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorBond_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorBond___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorBond___len__(*args)
    def pop(*args): return _openbabel.vectorBond_pop(*args)
    def __getslice__(*args): return _openbabel.vectorBond___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorBond___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorBond___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorBond___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorBond___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorBond___setitem__(*args)
    def append(*args): return _openbabel.vectorBond_append(*args)
    def empty(*args): return _openbabel.vectorBond_empty(*args)
    def size(*args): return _openbabel.vectorBond_size(*args)
    def clear(*args): return _openbabel.vectorBond_clear(*args)
    def swap(*args): return _openbabel.vectorBond_swap(*args)
    def get_allocator(*args): return _openbabel.vectorBond_get_allocator(*args)
    def begin(*args): return _openbabel.vectorBond_begin(*args)
    def end(*args): return _openbabel.vectorBond_end(*args)
    def rbegin(*args): return _openbabel.vectorBond_rbegin(*args)
    def rend(*args): return _openbabel.vectorBond_rend(*args)
    def pop_back(*args): return _openbabel.vectorBond_pop_back(*args)
    def erase(*args): return _openbabel.vectorBond_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorBond(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorBond_push_back(*args)
    def front(*args): return _openbabel.vectorBond_front(*args)
    def back(*args): return _openbabel.vectorBond_back(*args)
    def assign(*args): return _openbabel.vectorBond_assign(*args)
    def resize(*args): return _openbabel.vectorBond_resize(*args)
    def insert(*args): return _openbabel.vectorBond_insert(*args)
    def reserve(*args): return _openbabel.vectorBond_reserve(*args)
    def capacity(*args): return _openbabel.vectorBond_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorBond
    __del__ = lambda self : None;
vectorBond_swigregister = _openbabel.vectorBond_swigregister
vectorBond_swigregister(vectorBond)

class vectorResidue(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorResidue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorResidue, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorResidue_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorResidue___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorResidue___len__(*args)
    def pop(*args): return _openbabel.vectorResidue_pop(*args)
    def __getslice__(*args): return _openbabel.vectorResidue___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorResidue___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorResidue___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorResidue___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorResidue___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorResidue___setitem__(*args)
    def append(*args): return _openbabel.vectorResidue_append(*args)
    def empty(*args): return _openbabel.vectorResidue_empty(*args)
    def size(*args): return _openbabel.vectorResidue_size(*args)
    def clear(*args): return _openbabel.vectorResidue_clear(*args)
    def swap(*args): return _openbabel.vectorResidue_swap(*args)
    def get_allocator(*args): return _openbabel.vectorResidue_get_allocator(*args)
    def begin(*args): return _openbabel.vectorResidue_begin(*args)
    def end(*args): return _openbabel.vectorResidue_end(*args)
    def rbegin(*args): return _openbabel.vectorResidue_rbegin(*args)
    def rend(*args): return _openbabel.vectorResidue_rend(*args)
    def pop_back(*args): return _openbabel.vectorResidue_pop_back(*args)
    def erase(*args): return _openbabel.vectorResidue_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorResidue(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorResidue_push_back(*args)
    def front(*args): return _openbabel.vectorResidue_front(*args)
    def back(*args): return _openbabel.vectorResidue_back(*args)
    def assign(*args): return _openbabel.vectorResidue_assign(*args)
    def resize(*args): return _openbabel.vectorResidue_resize(*args)
    def insert(*args): return _openbabel.vectorResidue_insert(*args)
    def reserve(*args): return _openbabel.vectorResidue_reserve(*args)
    def capacity(*args): return _openbabel.vectorResidue_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorResidue
    __del__ = lambda self : None;
vectorResidue_swigregister = _openbabel.vectorResidue_swigregister
vectorResidue_swigregister(vectorResidue)

class vectorRing(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorRing, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorRing, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorRing_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorRing___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorRing___len__(*args)
    def pop(*args): return _openbabel.vectorRing_pop(*args)
    def __getslice__(*args): return _openbabel.vectorRing___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorRing___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorRing___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorRing___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorRing___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorRing___setitem__(*args)
    def append(*args): return _openbabel.vectorRing_append(*args)
    def empty(*args): return _openbabel.vectorRing_empty(*args)
    def size(*args): return _openbabel.vectorRing_size(*args)
    def clear(*args): return _openbabel.vectorRing_clear(*args)
    def swap(*args): return _openbabel.vectorRing_swap(*args)
    def get_allocator(*args): return _openbabel.vectorRing_get_allocator(*args)
    def begin(*args): return _openbabel.vectorRing_begin(*args)
    def end(*args): return _openbabel.vectorRing_end(*args)
    def rbegin(*args): return _openbabel.vectorRing_rbegin(*args)
    def rend(*args): return _openbabel.vectorRing_rend(*args)
    def pop_back(*args): return _openbabel.vectorRing_pop_back(*args)
    def erase(*args): return _openbabel.vectorRing_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorRing(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorRing_push_back(*args)
    def front(*args): return _openbabel.vectorRing_front(*args)
    def back(*args): return _openbabel.vectorRing_back(*args)
    def assign(*args): return _openbabel.vectorRing_assign(*args)
    def resize(*args): return _openbabel.vectorRing_resize(*args)
    def insert(*args): return _openbabel.vectorRing_insert(*args)
    def reserve(*args): return _openbabel.vectorRing_reserve(*args)
    def capacity(*args): return _openbabel.vectorRing_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorRing
    __del__ = lambda self : None;
vectorRing_swigregister = _openbabel.vectorRing_swigregister
vectorRing_swigregister(vectorRing)

class vectorpRing(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorpRing, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorpRing, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorpRing_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorpRing___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorpRing___len__(*args)
    def pop(*args): return _openbabel.vectorpRing_pop(*args)
    def __getslice__(*args): return _openbabel.vectorpRing___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorpRing___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorpRing___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorpRing___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorpRing___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorpRing___setitem__(*args)
    def append(*args): return _openbabel.vectorpRing_append(*args)
    def empty(*args): return _openbabel.vectorpRing_empty(*args)
    def size(*args): return _openbabel.vectorpRing_size(*args)
    def clear(*args): return _openbabel.vectorpRing_clear(*args)
    def swap(*args): return _openbabel.vectorpRing_swap(*args)
    def get_allocator(*args): return _openbabel.vectorpRing_get_allocator(*args)
    def begin(*args): return _openbabel.vectorpRing_begin(*args)
    def end(*args): return _openbabel.vectorpRing_end(*args)
    def rbegin(*args): return _openbabel.vectorpRing_rbegin(*args)
    def rend(*args): return _openbabel.vectorpRing_rend(*args)
    def pop_back(*args): return _openbabel.vectorpRing_pop_back(*args)
    def erase(*args): return _openbabel.vectorpRing_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorpRing(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorpRing_push_back(*args)
    def front(*args): return _openbabel.vectorpRing_front(*args)
    def back(*args): return _openbabel.vectorpRing_back(*args)
    def assign(*args): return _openbabel.vectorpRing_assign(*args)
    def resize(*args): return _openbabel.vectorpRing_resize(*args)
    def insert(*args): return _openbabel.vectorpRing_insert(*args)
    def reserve(*args): return _openbabel.vectorpRing_reserve(*args)
    def capacity(*args): return _openbabel.vectorpRing_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorpRing
    __del__ = lambda self : None;
vectorpRing_swigregister = _openbabel.vectorpRing_swigregister
vectorpRing_swigregister(vectorpRing)

class vectorData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorData, name)
    __repr__ = _swig_repr
    def iterator(*args): return _openbabel.vectorData_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _openbabel.vectorData___nonzero__(*args)
    def __len__(*args): return _openbabel.vectorData___len__(*args)
    def pop(*args): return _openbabel.vectorData_pop(*args)
    def __getslice__(*args): return _openbabel.vectorData___getslice__(*args)
    def __setslice__(*args): return _openbabel.vectorData___setslice__(*args)
    def __delslice__(*args): return _openbabel.vectorData___delslice__(*args)
    def __delitem__(*args): return _openbabel.vectorData___delitem__(*args)
    def __getitem__(*args): return _openbabel.vectorData___getitem__(*args)
    def __setitem__(*args): return _openbabel.vectorData___setitem__(*args)
    def append(*args): return _openbabel.vectorData_append(*args)
    def empty(*args): return _openbabel.vectorData_empty(*args)
    def size(*args): return _openbabel.vectorData_size(*args)
    def clear(*args): return _openbabel.vectorData_clear(*args)
    def swap(*args): return _openbabel.vectorData_swap(*args)
    def get_allocator(*args): return _openbabel.vectorData_get_allocator(*args)
    def begin(*args): return _openbabel.vectorData_begin(*args)
    def end(*args): return _openbabel.vectorData_end(*args)
    def rbegin(*args): return _openbabel.vectorData_rbegin(*args)
    def rend(*args): return _openbabel.vectorData_rend(*args)
    def pop_back(*args): return _openbabel.vectorData_pop_back(*args)
    def erase(*args): return _openbabel.vectorData_erase(*args)
    def __init__(self, *args): 
        this = _openbabel.new_vectorData(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _openbabel.vectorData_push_back(*args)
    def front(*args): return _openbabel.vectorData_front(*args)
    def back(*args): return _openbabel.vectorData_back(*args)
    def assign(*args): return _openbabel.vectorData_assign(*args)
    def resize(*args): return _openbabel.vectorData_resize(*args)
    def insert(*args): return _openbabel.vectorData_insert(*args)
    def reserve(*args): return _openbabel.vectorData_reserve(*args)
    def capacity(*args): return _openbabel.vectorData_capacity(*args)
    __swig_destroy__ = _openbabel.delete_vectorData
    __del__ = lambda self : None;
vectorData_swigregister = _openbabel.vectorData_swigregister
vectorData_swigregister(vectorData)

toPairData = _openbabel.toPairData
toUnitCell = _openbabel.toUnitCell
class OBGlobalDataBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBGlobalDataBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBGlobalDataBase, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBGlobalDataBase(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBGlobalDataBase
    __del__ = lambda self : None;
    def Init(*args): return _openbabel.OBGlobalDataBase_Init(*args)
    def GetSize(*args): return _openbabel.OBGlobalDataBase_GetSize(*args)
    def SetReadDirectory(*args): return _openbabel.OBGlobalDataBase_SetReadDirectory(*args)
    def SetEnvironmentVariable(*args): return _openbabel.OBGlobalDataBase_SetEnvironmentVariable(*args)
    def ParseLine(*args): return _openbabel.OBGlobalDataBase_ParseLine(*args)
OBGlobalDataBase_swigregister = _openbabel.OBGlobalDataBase_swigregister
OBGlobalDataBase_swigregister(OBGlobalDataBase)

class OBElement(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBElement, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBElement, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBElement(*args)
        try: self.this.append(this)
        except: self.this = this
    def GetAtomicNum(*args): return _openbabel.OBElement_GetAtomicNum(*args)
    def GetSymbol(*args): return _openbabel.OBElement_GetSymbol(*args)
    def GetCovalentRad(*args): return _openbabel.OBElement_GetCovalentRad(*args)
    def GetVdwRad(*args): return _openbabel.OBElement_GetVdwRad(*args)
    def GetMass(*args): return _openbabel.OBElement_GetMass(*args)
    def GetMaxBonds(*args): return _openbabel.OBElement_GetMaxBonds(*args)
    def GetElectroNeg(*args): return _openbabel.OBElement_GetElectroNeg(*args)
    def GetAllredRochowElectroNeg(*args): return _openbabel.OBElement_GetAllredRochowElectroNeg(*args)
    def GetIonization(*args): return _openbabel.OBElement_GetIonization(*args)
    def GetElectronAffinity(*args): return _openbabel.OBElement_GetElectronAffinity(*args)
    def GetName(*args): return _openbabel.OBElement_GetName(*args)
    def GetRed(*args): return _openbabel.OBElement_GetRed(*args)
    def GetGreen(*args): return _openbabel.OBElement_GetGreen(*args)
    def GetBlue(*args): return _openbabel.OBElement_GetBlue(*args)
    __swig_destroy__ = _openbabel.delete_OBElement
    __del__ = lambda self : None;
OBElement_swigregister = _openbabel.OBElement_swigregister
OBElement_swigregister(OBElement)

class OBElementTable(OBGlobalDataBase):
    __swig_setmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBElementTable, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBElementTable, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBElementTable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBElementTable
    __del__ = lambda self : None;
    def ParseLine(*args): return _openbabel.OBElementTable_ParseLine(*args)
    def GetNumberOfElements(*args): return _openbabel.OBElementTable_GetNumberOfElements(*args)
    def GetSize(*args): return _openbabel.OBElementTable_GetSize(*args)
    def GetAtomicNum(*args): return _openbabel.OBElementTable_GetAtomicNum(*args)
    def GetSymbol(*args): return _openbabel.OBElementTable_GetSymbol(*args)
    def GetVdwRad(*args): return _openbabel.OBElementTable_GetVdwRad(*args)
    def GetCovalentRad(*args): return _openbabel.OBElementTable_GetCovalentRad(*args)
    def GetMass(*args): return _openbabel.OBElementTable_GetMass(*args)
    def CorrectedBondRad(*args): return _openbabel.OBElementTable_CorrectedBondRad(*args)
    def CorrectedVdwRad(*args): return _openbabel.OBElementTable_CorrectedVdwRad(*args)
    def GetMaxBonds(*args): return _openbabel.OBElementTable_GetMaxBonds(*args)
    def GetElectroNeg(*args): return _openbabel.OBElementTable_GetElectroNeg(*args)
    def GetAllredRochowElectroNeg(*args): return _openbabel.OBElementTable_GetAllredRochowElectroNeg(*args)
    def GetIonization(*args): return _openbabel.OBElementTable_GetIonization(*args)
    def GetElectronAffinity(*args): return _openbabel.OBElementTable_GetElectronAffinity(*args)
    def GetRGB(*args): return _openbabel.OBElementTable_GetRGB(*args)
    def GetName(*args): return _openbabel.OBElementTable_GetName(*args)
OBElementTable_swigregister = _openbabel.OBElementTable_swigregister
OBElementTable_swigregister(OBElementTable)

class OBIsotopeTable(OBGlobalDataBase):
    __swig_setmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBIsotopeTable, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBIsotopeTable, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBIsotopeTable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBIsotopeTable
    __del__ = lambda self : None;
    def GetSize(*args): return _openbabel.OBIsotopeTable_GetSize(*args)
    def ParseLine(*args): return _openbabel.OBIsotopeTable_ParseLine(*args)
    def GetExactMass(*args): return _openbabel.OBIsotopeTable_GetExactMass(*args)
OBIsotopeTable_swigregister = _openbabel.OBIsotopeTable_swigregister
OBIsotopeTable_swigregister(OBIsotopeTable)

class OBTypeTable(OBGlobalDataBase):
    __swig_setmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBTypeTable, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBTypeTable, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBTypeTable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBTypeTable
    __del__ = lambda self : None;
    def ParseLine(*args): return _openbabel.OBTypeTable_ParseLine(*args)
    def GetSize(*args): return _openbabel.OBTypeTable_GetSize(*args)
    def SetFromType(*args): return _openbabel.OBTypeTable_SetFromType(*args)
    def SetToType(*args): return _openbabel.OBTypeTable_SetToType(*args)
    def Translate(*args): return _openbabel.OBTypeTable_Translate(*args)
    def GetFromType(*args): return _openbabel.OBTypeTable_GetFromType(*args)
    def GetToType(*args): return _openbabel.OBTypeTable_GetToType(*args)
OBTypeTable_swigregister = _openbabel.OBTypeTable_swigregister
OBTypeTable_swigregister(OBTypeTable)

class OBResidueData(OBGlobalDataBase):
    __swig_setmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBResidueData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGlobalDataBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBResidueData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBResidueData(*args)
        try: self.this.append(this)
        except: self.this = this
    def ParseLine(*args): return _openbabel.OBResidueData_ParseLine(*args)
    def GetSize(*args): return _openbabel.OBResidueData_GetSize(*args)
    def SetResName(*args): return _openbabel.OBResidueData_SetResName(*args)
    def LookupBO(*args): return _openbabel.OBResidueData_LookupBO(*args)
    def LookupType(*args): return _openbabel.OBResidueData_LookupType(*args)
    def AssignBonds(*args): return _openbabel.OBResidueData_AssignBonds(*args)
    __swig_destroy__ = _openbabel.delete_OBResidueData
    __del__ = lambda self : None;
OBResidueData_swigregister = _openbabel.OBResidueData_swigregister
OBResidueData_swigregister(OBResidueData)

class DoubleType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleType, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hi"] = _openbabel.DoubleType_hi_set
    __swig_getmethods__["hi"] = _openbabel.DoubleType_hi_get
    if _newclass:hi = _swig_property(_openbabel.DoubleType_hi_get, _openbabel.DoubleType_hi_set)
    __swig_setmethods__["lo"] = _openbabel.DoubleType_lo_set
    __swig_getmethods__["lo"] = _openbabel.DoubleType_lo_get
    if _newclass:lo = _swig_property(_openbabel.DoubleType_lo_get, _openbabel.DoubleType_lo_set)
    def __init__(self, *args): 
        this = _openbabel.new_DoubleType(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_DoubleType
    __del__ = lambda self : None;
DoubleType_swigregister = _openbabel.DoubleType_swigregister
DoubleType_swigregister(DoubleType)

DoubleMultiply = _openbabel.DoubleMultiply
DoubleAdd = _openbabel.DoubleAdd
DoubleModulus = _openbabel.DoubleModulus
class OBRandom(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRandom, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBRandom, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBRandom(*args)
        try: self.this.append(this)
        except: self.this = this
    def Seed(*args): return _openbabel.OBRandom_Seed(*args)
    def TimeSeed(*args): return _openbabel.OBRandom_TimeSeed(*args)
    def NextInt(*args): return _openbabel.OBRandom_NextInt(*args)
    def NextFloat(*args): return _openbabel.OBRandom_NextFloat(*args)
    __swig_destroy__ = _openbabel.delete_OBRandom
    __del__ = lambda self : None;
OBRandom_swigregister = _openbabel.OBRandom_swigregister
OBRandom_swigregister(OBRandom)

M_PI = _openbabel.M_PI
class OBStopwatch(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBStopwatch, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBStopwatch, name)
    __repr__ = _swig_repr
    def Start(*args): return _openbabel.OBStopwatch_Start(*args)
    def Lap(*args): return _openbabel.OBStopwatch_Lap(*args)
    def Elapsed(*args): return _openbabel.OBStopwatch_Elapsed(*args)
    def __init__(self, *args): 
        this = _openbabel.new_OBStopwatch(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBStopwatch
    __del__ = lambda self : None;
OBStopwatch_swigregister = _openbabel.OBStopwatch_swigregister
OBStopwatch_swigregister(OBStopwatch)

class OBSqrtTbl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSqrtTbl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBSqrtTbl, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBSqrtTbl(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBSqrtTbl
    __del__ = lambda self : None;
    def Sqrt(*args): return _openbabel.OBSqrtTbl_Sqrt(*args)
    def Init(*args): return _openbabel.OBSqrtTbl_Init(*args)
OBSqrtTbl_swigregister = _openbabel.OBSqrtTbl_swigregister
OBSqrtTbl_swigregister(OBSqrtTbl)

RAD_TO_DEG = _openbabel.RAD_TO_DEG
DEG_TO_RAD = _openbabel.DEG_TO_RAD
class vector3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector3, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_vector3(*args)
        try: self.this.append(this)
        except: self.this = this
    def Set(*args): return _openbabel.vector3_Set(*args)
    def SetX(*args): return _openbabel.vector3_SetX(*args)
    def SetY(*args): return _openbabel.vector3_SetY(*args)
    def SetZ(*args): return _openbabel.vector3_SetZ(*args)
    def Get(*args): return _openbabel.vector3_Get(*args)
    def AsArray(*args): return _openbabel.vector3_AsArray(*args)
    def __iadd__(*args): return _openbabel.vector3___iadd__(*args)
    def __isub__(*args): return _openbabel.vector3___isub__(*args)
    def __idiv__(*args): return _openbabel.vector3___idiv__(*args)
    def __imul__(*args): return _openbabel.vector3___imul__(*args)
    def randomUnitVector(*args): return _openbabel.vector3_randomUnitVector(*args)
    def normalize(*args): return _openbabel.vector3_normalize(*args)
    def CanBeNormalized(*args): return _openbabel.vector3_CanBeNormalized(*args)
    def length_2(*args): return _openbabel.vector3_length_2(*args)
    def length(*args): return _openbabel.vector3_length(*args)
    def x(*args): return _openbabel.vector3_x(*args)
    def y(*args): return _openbabel.vector3_y(*args)
    def z(*args): return _openbabel.vector3_z(*args)
    def __eq__(*args): return _openbabel.vector3___eq__(*args)
    def __ne__(*args): return _openbabel.vector3___ne__(*args)
    def IsApprox(*args): return _openbabel.vector3_IsApprox(*args)
    def distSq(*args): return _openbabel.vector3_distSq(*args)
    def createOrthoVector(*args): return _openbabel.vector3_createOrthoVector(*args)
    __swig_destroy__ = _openbabel.delete_vector3
    __del__ = lambda self : None;
vector3_swigregister = _openbabel.vector3_swigregister
vector3_swigregister(vector3)

__lshift__ = _openbabel.__lshift__
__add__ = _openbabel.__add__
__div__ = _openbabel.__div__
dot = _openbabel.dot
cross = _openbabel.cross
vectorAngle = _openbabel.vectorAngle
CalcTorsionAngle = _openbabel.CalcTorsionAngle
Point2Plane = _openbabel.Point2Plane
Point2PlaneAngle = _openbabel.Point2PlaneAngle
UndefinedData = _openbabel.UndefinedData
PairData = _openbabel.PairData
EnergyData = _openbabel.EnergyData
CommentData = _openbabel.CommentData
ConformerData = _openbabel.ConformerData
ExternalBondData = _openbabel.ExternalBondData
RotamerList = _openbabel.RotamerList
VirtualBondData = _openbabel.VirtualBondData
RingData = _openbabel.RingData
TorsionData = _openbabel.TorsionData
AngleData = _openbabel.AngleData
SerialNums = _openbabel.SerialNums
UnitCell = _openbabel.UnitCell
SpinData = _openbabel.SpinData
ChargeData = _openbabel.ChargeData
SymmetryData = _openbabel.SymmetryData
ChiralData = _openbabel.ChiralData
OccupationData = _openbabel.OccupationData
DensityData = _openbabel.DensityData
ElectronicData = _openbabel.ElectronicData
VibrationData = _openbabel.VibrationData
RotationData = _openbabel.RotationData
NuclearData = _openbabel.NuclearData
SetData = _openbabel.SetData
GridData = _openbabel.GridData
VectorData = _openbabel.VectorData
CustomData0 = _openbabel.CustomData0
CustomData1 = _openbabel.CustomData1
CustomData2 = _openbabel.CustomData2
CustomData3 = _openbabel.CustomData3
CustomData4 = _openbabel.CustomData4
CustomData5 = _openbabel.CustomData5
CustomData6 = _openbabel.CustomData6
CustomData7 = _openbabel.CustomData7
CustomData8 = _openbabel.CustomData8
CustomData9 = _openbabel.CustomData9
CustomData10 = _openbabel.CustomData10
CustomData11 = _openbabel.CustomData11
CustomData12 = _openbabel.CustomData12
CustomData13 = _openbabel.CustomData13
CustomData14 = _openbabel.CustomData14
CustomData15 = _openbabel.CustomData15
any = _openbabel.any
fileformatInput = _openbabel.fileformatInput
userInput = _openbabel.userInput
perceived = _openbabel.perceived
external = _openbabel.external
class OBGenericData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBGenericData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBGenericData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBGenericData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBGenericData_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBGenericData
    __del__ = lambda self : None;
    def SetAttribute(*args): return _openbabel.OBGenericData_SetAttribute(*args)
    def SetOrigin(*args): return _openbabel.OBGenericData_SetOrigin(*args)
    def GetAttribute(*args): return _openbabel.OBGenericData_GetAttribute(*args)
    def GetDataType(*args): return _openbabel.OBGenericData_GetDataType(*args)
    def GetValue(*args): return _openbabel.OBGenericData_GetValue(*args)
    def GetOrigin(*args): return _openbabel.OBGenericData_GetOrigin(*args)
OBGenericData_swigregister = _openbabel.OBGenericData_swigregister
OBGenericData_swigregister(OBGenericData)
__sub__ = _openbabel.__sub__
__mul__ = _openbabel.__mul__
cvar = _openbabel.cvar
VZero = cvar.VZero
VX = cvar.VX
VY = cvar.VY
VZ = cvar.VZ

class OBBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBBase, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _openbabel.delete_OBBase
    __del__ = lambda self : None;
    def Clear(*args): return _openbabel.OBBase_Clear(*args)
    def DoTransformations(*args): return _openbabel.OBBase_DoTransformations(*args)
    __swig_getmethods__["ClassDescription"] = lambda x: _openbabel.OBBase_ClassDescription
    if _newclass:ClassDescription = staticmethod(_openbabel.OBBase_ClassDescription)
    def HasData(*args): return _openbabel.OBBase_HasData(*args)
    def DeleteData(*args): return _openbabel.OBBase_DeleteData(*args)
    def SetData(*args): return _openbabel.OBBase_SetData(*args)
    def DataSize(*args): return _openbabel.OBBase_DataSize(*args)
    def GetData(*args): return _openbabel.OBBase_GetData(*args)
    def BeginData(*args): return _openbabel.OBBase_BeginData(*args)
    def EndData(*args): return _openbabel.OBBase_EndData(*args)
    def __init__(self, *args): 
        this = _openbabel.new_OBBase(*args)
        try: self.this.append(this)
        except: self.this = this
OBBase_swigregister = _openbabel.OBBase_swigregister
OBBase_swigregister(OBBase)
OBBase_ClassDescription = _openbabel.OBBase_ClassDescription

class OBCommentData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBCommentData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBCommentData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBCommentData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBCommentData_Clone(*args)
    def SetData(*args): return _openbabel.OBCommentData_SetData(*args)
    def GetData(*args): return _openbabel.OBCommentData_GetData(*args)
    def GetValue(*args): return _openbabel.OBCommentData_GetValue(*args)
    __swig_destroy__ = _openbabel.delete_OBCommentData
    __del__ = lambda self : None;
OBCommentData_swigregister = _openbabel.OBCommentData_swigregister
OBCommentData_swigregister(OBCommentData)

class OBExternalBond(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBExternalBond, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBExternalBond, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBExternalBond(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBExternalBond
    __del__ = lambda self : None;
    def GetIdx(*args): return _openbabel.OBExternalBond_GetIdx(*args)
    def GetAtom(*args): return _openbabel.OBExternalBond_GetAtom(*args)
    def GetBond(*args): return _openbabel.OBExternalBond_GetBond(*args)
    def SetIdx(*args): return _openbabel.OBExternalBond_SetIdx(*args)
    def SetAtom(*args): return _openbabel.OBExternalBond_SetAtom(*args)
    def SetBond(*args): return _openbabel.OBExternalBond_SetBond(*args)
OBExternalBond_swigregister = _openbabel.OBExternalBond_swigregister
OBExternalBond_swigregister(OBExternalBond)

class OBExternalBondData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBExternalBondData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBExternalBondData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBExternalBondData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBExternalBondData_Clone(*args)
    def SetData(*args): return _openbabel.OBExternalBondData_SetData(*args)
    def GetData(*args): return _openbabel.OBExternalBondData_GetData(*args)
    __swig_destroy__ = _openbabel.delete_OBExternalBondData
    __del__ = lambda self : None;
OBExternalBondData_swigregister = _openbabel.OBExternalBondData_swigregister
OBExternalBondData_swigregister(OBExternalBondData)

class OBPairData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBPairData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBPairData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBPairData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBPairData_Clone(*args)
    def SetValue(*args): return _openbabel.OBPairData_SetValue(*args)
    def GetValue(*args): return _openbabel.OBPairData_GetValue(*args)
    __swig_destroy__ = _openbabel.delete_OBPairData
    __del__ = lambda self : None;
OBPairData_swigregister = _openbabel.OBPairData_swigregister
OBPairData_swigregister(OBPairData)

class OBSetData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSetData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBSetData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBSetData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBSetData_Clone(*args)
    def AddData(*args): return _openbabel.OBSetData_AddData(*args)
    def SetData(*args): return _openbabel.OBSetData_SetData(*args)
    def GetData(*args): return _openbabel.OBSetData_GetData(*args)
    def GetBegin(*args): return _openbabel.OBSetData_GetBegin(*args)
    def GetEnd(*args): return _openbabel.OBSetData_GetEnd(*args)
    def DeleteData(*args): return _openbabel.OBSetData_DeleteData(*args)
    __swig_destroy__ = _openbabel.delete_OBSetData
    __del__ = lambda self : None;
OBSetData_swigregister = _openbabel.OBSetData_swigregister
OBSetData_swigregister(OBSetData)

class OBVirtualBond(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBVirtualBond, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBVirtualBond, name)
    __repr__ = _swig_repr
    def Clone(*args): return _openbabel.OBVirtualBond_Clone(*args)
    def __init__(self, *args): 
        this = _openbabel.new_OBVirtualBond(*args)
        try: self.this.append(this)
        except: self.this = this
    def GetBgn(*args): return _openbabel.OBVirtualBond_GetBgn(*args)
    def GetEnd(*args): return _openbabel.OBVirtualBond_GetEnd(*args)
    def GetOrder(*args): return _openbabel.OBVirtualBond_GetOrder(*args)
    def GetStereo(*args): return _openbabel.OBVirtualBond_GetStereo(*args)
    __swig_destroy__ = _openbabel.delete_OBVirtualBond
    __del__ = lambda self : None;
OBVirtualBond_swigregister = _openbabel.OBVirtualBond_swigregister
OBVirtualBond_swigregister(OBVirtualBond)

class OBRingData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRingData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBRingData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBRingData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBRingData_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBRingData
    __del__ = lambda self : None;
    def SetData(*args): return _openbabel.OBRingData_SetData(*args)
    def PushBack(*args): return _openbabel.OBRingData_PushBack(*args)
    def GetData(*args): return _openbabel.OBRingData_GetData(*args)
    def BeginRings(*args): return _openbabel.OBRingData_BeginRings(*args)
    def EndRings(*args): return _openbabel.OBRingData_EndRings(*args)
    def BeginRing(*args): return _openbabel.OBRingData_BeginRing(*args)
    def NextRing(*args): return _openbabel.OBRingData_NextRing(*args)
OBRingData_swigregister = _openbabel.OBRingData_swigregister
OBRingData_swigregister(OBRingData)

class OBUnitCell(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBUnitCell, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBUnitCell, name)
    __repr__ = _swig_repr
    Undefined = _openbabel.OBUnitCell_Undefined
    Triclinic = _openbabel.OBUnitCell_Triclinic
    Monoclinic = _openbabel.OBUnitCell_Monoclinic
    Orthorhombic = _openbabel.OBUnitCell_Orthorhombic
    Tetragonal = _openbabel.OBUnitCell_Tetragonal
    Rhombohedral = _openbabel.OBUnitCell_Rhombohedral
    Hexagonal = _openbabel.OBUnitCell_Hexagonal
    Cubic = _openbabel.OBUnitCell_Cubic
    def __init__(self, *args): 
        this = _openbabel.new_OBUnitCell(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBUnitCell_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBUnitCell
    __del__ = lambda self : None;
    def SetData(*args): return _openbabel.OBUnitCell_SetData(*args)
    def SetOffset(*args): return _openbabel.OBUnitCell_SetOffset(*args)
    def SetSpaceGroup(*args): return _openbabel.OBUnitCell_SetSpaceGroup(*args)
    def SetLatticeType(*args): return _openbabel.OBUnitCell_SetLatticeType(*args)
    def GetA(*args): return _openbabel.OBUnitCell_GetA(*args)
    def GetB(*args): return _openbabel.OBUnitCell_GetB(*args)
    def GetC(*args): return _openbabel.OBUnitCell_GetC(*args)
    def GetAlpha(*args): return _openbabel.OBUnitCell_GetAlpha(*args)
    def GetBeta(*args): return _openbabel.OBUnitCell_GetBeta(*args)
    def GetGamma(*args): return _openbabel.OBUnitCell_GetGamma(*args)
    def GetOffset(*args): return _openbabel.OBUnitCell_GetOffset(*args)
    def GetSpaceGroup(*args): return _openbabel.OBUnitCell_GetSpaceGroup(*args)
    def GetSpaceGroupName(*args): return _openbabel.OBUnitCell_GetSpaceGroupName(*args)
    def GetLatticeType(*args): return _openbabel.OBUnitCell_GetLatticeType(*args)
    def GetCellVectors(*args): return _openbabel.OBUnitCell_GetCellVectors(*args)
    def GetCellMatrix(*args): return _openbabel.OBUnitCell_GetCellMatrix(*args)
    def GetOrthoMatrix(*args): return _openbabel.OBUnitCell_GetOrthoMatrix(*args)
    def GetFractionalMatrix(*args): return _openbabel.OBUnitCell_GetFractionalMatrix(*args)
    def GetSpaceGroupNumber(*args): return _openbabel.OBUnitCell_GetSpaceGroupNumber(*args)
    def GetCellVolume(*args): return _openbabel.OBUnitCell_GetCellVolume(*args)
OBUnitCell_swigregister = _openbabel.OBUnitCell_swigregister
OBUnitCell_swigregister(OBUnitCell)

class OBConformerData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBConformerData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBConformerData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBConformerData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBConformerData_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBConformerData
    __del__ = lambda self : None;
    def SetDimension(*args): return _openbabel.OBConformerData_SetDimension(*args)
    def SetEnergies(*args): return _openbabel.OBConformerData_SetEnergies(*args)
    def SetForces(*args): return _openbabel.OBConformerData_SetForces(*args)
    def SetVelocities(*args): return _openbabel.OBConformerData_SetVelocities(*args)
    def SetDisplacements(*args): return _openbabel.OBConformerData_SetDisplacements(*args)
    def SetData(*args): return _openbabel.OBConformerData_SetData(*args)
    def GetDimension(*args): return _openbabel.OBConformerData_GetDimension(*args)
    def GetEnergies(*args): return _openbabel.OBConformerData_GetEnergies(*args)
    def GetForces(*args): return _openbabel.OBConformerData_GetForces(*args)
    def GetVelocities(*args): return _openbabel.OBConformerData_GetVelocities(*args)
    def GetDisplacements(*args): return _openbabel.OBConformerData_GetDisplacements(*args)
    def GetData(*args): return _openbabel.OBConformerData_GetData(*args)
OBConformerData_swigregister = _openbabel.OBConformerData_swigregister
OBConformerData_swigregister(OBConformerData)

class OBSymmetryData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSymmetryData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBSymmetryData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBSymmetryData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBSymmetryData_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBSymmetryData
    __del__ = lambda self : None;
    def SetData(*args): return _openbabel.OBSymmetryData_SetData(*args)
    def SetPointGroup(*args): return _openbabel.OBSymmetryData_SetPointGroup(*args)
    def SetSpaceGroup(*args): return _openbabel.OBSymmetryData_SetSpaceGroup(*args)
    def GetPointGroup(*args): return _openbabel.OBSymmetryData_GetPointGroup(*args)
    def GetSpaceGroup(*args): return _openbabel.OBSymmetryData_GetSpaceGroup(*args)
OBSymmetryData_swigregister = _openbabel.OBSymmetryData_swigregister
OBSymmetryData_swigregister(OBSymmetryData)

class OBTorsion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBTorsion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBTorsion, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBTorsion(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBTorsion
    __del__ = lambda self : None;
    def Clear(*args): return _openbabel.OBTorsion_Clear(*args)
    def Empty(*args): return _openbabel.OBTorsion_Empty(*args)
    def AddTorsion(*args): return _openbabel.OBTorsion_AddTorsion(*args)
    def SetAngle(*args): return _openbabel.OBTorsion_SetAngle(*args)
    def SetData(*args): return _openbabel.OBTorsion_SetData(*args)
    def GetAngle(*args): return _openbabel.OBTorsion_GetAngle(*args)
    def GetBondIdx(*args): return _openbabel.OBTorsion_GetBondIdx(*args)
    def GetSize(*args): return _openbabel.OBTorsion_GetSize(*args)
    def GetBC(*args): return _openbabel.OBTorsion_GetBC(*args)
    def GetADs(*args): return _openbabel.OBTorsion_GetADs(*args)
    def IsProtonRotor(*args): return _openbabel.OBTorsion_IsProtonRotor(*args)
OBTorsion_swigregister = _openbabel.OBTorsion_swigregister
OBTorsion_swigregister(OBTorsion)

class OBTorsionData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBTorsionData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBTorsionData, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Clone(*args): return _openbabel.OBTorsionData_Clone(*args)
    def Clear(*args): return _openbabel.OBTorsionData_Clear(*args)
    def GetData(*args): return _openbabel.OBTorsionData_GetData(*args)
    def GetSize(*args): return _openbabel.OBTorsionData_GetSize(*args)
    def SetData(*args): return _openbabel.OBTorsionData_SetData(*args)
    def FillTorsionArray(*args): return _openbabel.OBTorsionData_FillTorsionArray(*args)
    __swig_destroy__ = _openbabel.delete_OBTorsionData
    __del__ = lambda self : None;
OBTorsionData_swigregister = _openbabel.OBTorsionData_swigregister
OBTorsionData_swigregister(OBTorsionData)

class OBAngle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBAngle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBAngle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBAngle(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBAngle
    __del__ = lambda self : None;
    def __eq__(*args): return _openbabel.OBAngle___eq__(*args)
    def Clear(*args): return _openbabel.OBAngle_Clear(*args)
    def GetAngle(*args): return _openbabel.OBAngle_GetAngle(*args)
    def SetAngle(*args): return _openbabel.OBAngle_SetAngle(*args)
    def SetAtoms(*args): return _openbabel.OBAngle_SetAtoms(*args)
OBAngle_swigregister = _openbabel.OBAngle_swigregister
OBAngle_swigregister(OBAngle)

class OBAngleData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBAngleData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBAngleData, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Clone(*args): return _openbabel.OBAngleData_Clone(*args)
    def Clear(*args): return _openbabel.OBAngleData_Clear(*args)
    def FillAngleArray(*args): return _openbabel.OBAngleData_FillAngleArray(*args)
    def SetData(*args): return _openbabel.OBAngleData_SetData(*args)
    def GetSize(*args): return _openbabel.OBAngleData_GetSize(*args)
    __swig_destroy__ = _openbabel.delete_OBAngleData
    __del__ = lambda self : None;
OBAngleData_swigregister = _openbabel.OBAngleData_swigregister
OBAngleData_swigregister(OBAngleData)

output = _openbabel.output
input = _openbabel.input
calcvolume = _openbabel.calcvolume
class OBChiralData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBChiralData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBChiralData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBChiralData(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBChiralData_Clone(*args)
    __swig_destroy__ = _openbabel.delete_OBChiralData
    __del__ = lambda self : None;
    def Clear(*args): return _openbabel.OBChiralData_Clear(*args)
    def GetAtom4Refs(*args): return _openbabel.OBChiralData_GetAtom4Refs(*args)
    def GetAtomRef(*args): return _openbabel.OBChiralData_GetAtomRef(*args)
    def SetAtom4Refs(*args): return _openbabel.OBChiralData_SetAtom4Refs(*args)
    def AddAtomRef(*args): return _openbabel.OBChiralData_AddAtomRef(*args)
    def GetSize(*args): return _openbabel.OBChiralData_GetSize(*args)
OBChiralData_swigregister = _openbabel.OBChiralData_swigregister
OBChiralData_swigregister(OBChiralData)

class OBSerialNums(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSerialNums, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBSerialNums, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBSerialNums(*args)
        try: self.this.append(this)
        except: self.this = this
    def Clone(*args): return _openbabel.OBSerialNums_Clone(*args)
    def GetData(*args): return _openbabel.OBSerialNums_GetData(*args)
    def SetData(*args): return _openbabel.OBSerialNums_SetData(*args)
    __swig_destroy__ = _openbabel.delete_OBSerialNums
    __del__ = lambda self : None;
OBSerialNums_swigregister = _openbabel.OBSerialNums_swigregister
OBSerialNums_swigregister(OBSerialNums)

class OBVibrationData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBVibrationData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBVibrationData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBVibrationData(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBVibrationData
    __del__ = lambda self : None;
    def Clone(*args): return _openbabel.OBVibrationData_Clone(*args)
    def SetData(*args): return _openbabel.OBVibrationData_SetData(*args)
    def GetLx(*args): return _openbabel.OBVibrationData_GetLx(*args)
    def GetFrequencies(*args): return _openbabel.OBVibrationData_GetFrequencies(*args)
    def GetIntensities(*args): return _openbabel.OBVibrationData_GetIntensities(*args)
    def GetNumberOfFrequencies(*args): return _openbabel.OBVibrationData_GetNumberOfFrequencies(*args)
OBVibrationData_swigregister = _openbabel.OBVibrationData_swigregister
OBVibrationData_swigregister(OBVibrationData)

class OBRotationData(OBGenericData):
    __swig_setmethods__ = {}
    for _s in [OBGenericData]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRotationData, name, value)
    __swig_getmethods__ = {}
    for _s in [OBGenericData]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBRotationData, name)
    __repr__ = _swig_repr
    UNKNOWN = _openbabel.OBRotationData_UNKNOWN
    ASYMMETRIC = _openbabel.OBRotationData_ASYMMETRIC
    SYMMETRIC = _openbabel.OBRotationData_SYMMETRIC
    LINEAR = _openbabel.OBRotationData_LINEAR
    def __init__(self, *args): 
        this = _openbabel.new_OBRotationData(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBRotationData
    __del__ = lambda self : None;
    def Clone(*args): return _openbabel.OBRotationData_Clone(*args)
    def SetData(*args): return _openbabel.OBRotationData_SetData(*args)
    def GetRotConsts(*args): return _openbabel.OBRotationData_GetRotConsts(*args)
    def GetSymmetryNumber(*args): return _openbabel.OBRotationData_GetSymmetryNumber(*args)
    def GetRotorType(*args): return _openbabel.OBRotationData_GetRotorType(*args)
OBRotationData_swigregister = _openbabel.OBRotationData_swigregister
OBRotationData_swigregister(OBRotationData)

class CharPtrLess(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CharPtrLess, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CharPtrLess, name)
    __repr__ = _swig_repr
    def __call__(*args): return _openbabel.CharPtrLess___call__(*args)
    def __init__(self, *args): 
        this = _openbabel.new_CharPtrLess(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_CharPtrLess
    __del__ = lambda self : None;
CharPtrLess_swigregister = _openbabel.CharPtrLess_swigregister
CharPtrLess_swigregister(CharPtrLess)

class OBPlugin(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBPlugin, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBPlugin, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _openbabel.delete_OBPlugin
    __del__ = lambda self : None;
    def Description(*args): return _openbabel.OBPlugin_Description(*args)
    def Display(*args): return _openbabel.OBPlugin_Display(*args)
    def MakeInstance(*args): return _openbabel.OBPlugin_MakeInstance(*args)
    __swig_getmethods__["GetPlugin"] = lambda x: _openbabel.OBPlugin_GetPlugin
    if _newclass:GetPlugin = staticmethod(_openbabel.OBPlugin_GetPlugin)
    def GetID(*args): return _openbabel.OBPlugin_GetID(*args)
    __swig_getmethods__["ListAsVector"] = lambda x: _openbabel.OBPlugin_ListAsVector
    if _newclass:ListAsVector = staticmethod(_openbabel.OBPlugin_ListAsVector)
    __swig_getmethods__["List"] = lambda x: _openbabel.OBPlugin_List
    if _newclass:List = staticmethod(_openbabel.OBPlugin_List)
    __swig_getmethods__["ListAsString"] = lambda x: _openbabel.OBPlugin_ListAsString
    if _newclass:ListAsString = staticmethod(_openbabel.OBPlugin_ListAsString)
    __swig_getmethods__["FirstLine"] = lambda x: _openbabel.OBPlugin_FirstLine
    if _newclass:FirstLine = staticmethod(_openbabel.OBPlugin_FirstLine)
    __swig_getmethods__["Begin"] = lambda x: _openbabel.OBPlugin_Begin
    if _newclass:Begin = staticmethod(_openbabel.OBPlugin_Begin)
    __swig_getmethods__["End"] = lambda x: _openbabel.OBPlugin_End
    if _newclass:End = staticmethod(_openbabel.OBPlugin_End)
    def GetMap(*args): return _openbabel.OBPlugin_GetMap(*args)
OBPlugin_swigregister = _openbabel.OBPlugin_swigregister
OBPlugin_swigregister(OBPlugin)
OBPlugin_GetPlugin = _openbabel.OBPlugin_GetPlugin
OBPlugin_ListAsVector = _openbabel.OBPlugin_ListAsVector
OBPlugin_List = _openbabel.OBPlugin_List
OBPlugin_ListAsString = _openbabel.OBPlugin_ListAsString
OBPlugin_FirstLine = _openbabel.OBPlugin_FirstLine
OBPlugin_Begin = _openbabel.OBPlugin_Begin
OBPlugin_End = _openbabel.OBPlugin_End

obError = _openbabel.obError
obWarning = _openbabel.obWarning
obInfo = _openbabel.obInfo
obAuditMsg = _openbabel.obAuditMsg
obDebug = _openbabel.obDebug
class OBError(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBError(*args)
        try: self.this.append(this)
        except: self.this = this
    def message(*args): return _openbabel.OBError_message(*args)
    def GetMethod(*args): return _openbabel.OBError_GetMethod(*args)
    def GetError(*args): return _openbabel.OBError_GetError(*args)
    def GetExplanation(*args): return _openbabel.OBError_GetExplanation(*args)
    def GetPossibleCause(*args): return _openbabel.OBError_GetPossibleCause(*args)
    def GetSuggestedRemedy(*args): return _openbabel.OBError_GetSuggestedRemedy(*args)
    def GetLevel(*args): return _openbabel.OBError_GetLevel(*args)
    __swig_destroy__ = _openbabel.delete_OBError
    __del__ = lambda self : None;
OBError_swigregister = _openbabel.OBError_swigregister
OBError_swigregister(OBError)

class OBMessageHandler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBMessageHandler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBMessageHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBMessageHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBMessageHandler
    __del__ = lambda self : None;
    def ThrowError(*args): return _openbabel.OBMessageHandler_ThrowError(*args)
    def GetMessagesOfLevel(*args): return _openbabel.OBMessageHandler_GetMessagesOfLevel(*args)
    def StartLogging(*args): return _openbabel.OBMessageHandler_StartLogging(*args)
    def StopLogging(*args): return _openbabel.OBMessageHandler_StopLogging(*args)
    def SetMaxLogEntries(*args): return _openbabel.OBMessageHandler_SetMaxLogEntries(*args)
    def GetMaxLogEntries(*args): return _openbabel.OBMessageHandler_GetMaxLogEntries(*args)
    def ClearLog(*args): return _openbabel.OBMessageHandler_ClearLog(*args)
    def SetOutputLevel(*args): return _openbabel.OBMessageHandler_SetOutputLevel(*args)
    def GetOutputLevel(*args): return _openbabel.OBMessageHandler_GetOutputLevel(*args)
    def SetOutputStream(*args): return _openbabel.OBMessageHandler_SetOutputStream(*args)
    def GetOutputStream(*args): return _openbabel.OBMessageHandler_GetOutputStream(*args)
    def StartErrorWrap(*args): return _openbabel.OBMessageHandler_StartErrorWrap(*args)
    def StopErrorWrap(*args): return _openbabel.OBMessageHandler_StopErrorWrap(*args)
    def GetErrorMessageCount(*args): return _openbabel.OBMessageHandler_GetErrorMessageCount(*args)
    def GetWarningMessageCount(*args): return _openbabel.OBMessageHandler_GetWarningMessageCount(*args)
    def GetInfoMessageCount(*args): return _openbabel.OBMessageHandler_GetInfoMessageCount(*args)
    def GetAuditMessageCount(*args): return _openbabel.OBMessageHandler_GetAuditMessageCount(*args)
    def GetDebugMessageCount(*args): return _openbabel.OBMessageHandler_GetDebugMessageCount(*args)
    def GetMessageSummary(*args): return _openbabel.OBMessageHandler_GetMessageSummary(*args)
OBMessageHandler_swigregister = _openbabel.OBMessageHandler_swigregister
OBMessageHandler_swigregister(OBMessageHandler)

class obLogBuf(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, obLogBuf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, obLogBuf, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _openbabel.delete_obLogBuf
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _openbabel.new_obLogBuf(*args)
        try: self.this.append(this)
        except: self.this = this
obLogBuf_swigregister = _openbabel.obLogBuf_swigregister
obLogBuf_swigregister(obLogBuf)

NOTREADABLE = _openbabel.NOTREADABLE
READONEONLY = _openbabel.READONEONLY
READBINARY = _openbabel.READBINARY
ZEROATOMSOK = _openbabel.ZEROATOMSOK
NOTWRITABLE = _openbabel.NOTWRITABLE
WRITEONEONLY = _openbabel.WRITEONEONLY
WRITEBINARY = _openbabel.WRITEBINARY
READXML = _openbabel.READXML
DEFAULTFORMAT = _openbabel.DEFAULTFORMAT
class OBFormat(OBPlugin):
    __swig_setmethods__ = {}
    for _s in [OBPlugin]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFormat, name, value)
    __swig_getmethods__ = {}
    for _s in [OBPlugin]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBFormat, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["Default"] = lambda x: _openbabel.OBFormat_Default
    if _newclass:Default = staticmethod(_openbabel.OBFormat_Default)
    __swig_getmethods__["FindType"] = lambda x: _openbabel.OBFormat_FindType
    if _newclass:FindType = staticmethod(_openbabel.OBFormat_FindType)
    def TypeID(*args): return _openbabel.OBFormat_TypeID(*args)
    def ReadMolecule(*args): return _openbabel.OBFormat_ReadMolecule(*args)
    def ReadChemObject(*args): return _openbabel.OBFormat_ReadChemObject(*args)
    def WriteMolecule(*args): return _openbabel.OBFormat_WriteMolecule(*args)
    def WriteChemObject(*args): return _openbabel.OBFormat_WriteChemObject(*args)
    def Description(*args): return _openbabel.OBFormat_Description(*args)
    def TargetClassDescription(*args): return _openbabel.OBFormat_TargetClassDescription(*args)
    def GetType(*args): return _openbabel.OBFormat_GetType(*args)
    def SpecificationURL(*args): return _openbabel.OBFormat_SpecificationURL(*args)
    def GetMIMEType(*args): return _openbabel.OBFormat_GetMIMEType(*args)
    def Flags(*args): return _openbabel.OBFormat_Flags(*args)
    def SkipObjects(*args): return _openbabel.OBFormat_SkipObjects(*args)
    def MakeNewInstance(*args): return _openbabel.OBFormat_MakeNewInstance(*args)
    def RegisterFormat(*args): return _openbabel.OBFormat_RegisterFormat(*args)
    def Display(*args): return _openbabel.OBFormat_Display(*args)
    __swig_getmethods__["FormatFromMIME"] = lambda x: _openbabel.OBFormat_FormatFromMIME
    if _newclass:FormatFromMIME = staticmethod(_openbabel.OBFormat_FormatFromMIME)
    __swig_destroy__ = _openbabel.delete_OBFormat
    __del__ = lambda self : None;
OBFormat_swigregister = _openbabel.OBFormat_swigregister
OBFormat_swigregister(OBFormat)
OBFormat_Default = _openbabel.OBFormat_Default
OBFormat_FindType = _openbabel.OBFormat_FindType
OBFormat_FormatFromMIME = _openbabel.OBFormat_FormatFromMIME

class OBConversion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBConversion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBConversion, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBConversion(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBConversion
    __del__ = lambda self : None;
    __swig_getmethods__["RegisterFormat"] = lambda x: _openbabel.OBConversion_RegisterFormat
    if _newclass:RegisterFormat = staticmethod(_openbabel.OBConversion_RegisterFormat)
    __swig_getmethods__["FindFormat"] = lambda x: _openbabel.OBConversion_FindFormat
    if _newclass:FindFormat = staticmethod(_openbabel.OBConversion_FindFormat)
    __swig_getmethods__["FormatFromExt"] = lambda x: _openbabel.OBConversion_FormatFromExt
    if _newclass:FormatFromExt = staticmethod(_openbabel.OBConversion_FormatFromExt)
    __swig_getmethods__["FormatFromMIME"] = lambda x: _openbabel.OBConversion_FormatFromMIME
    if _newclass:FormatFromMIME = staticmethod(_openbabel.OBConversion_FormatFromMIME)
    __swig_getmethods__["Description"] = lambda x: _openbabel.OBConversion_Description
    if _newclass:Description = staticmethod(_openbabel.OBConversion_Description)
    def GetInStream(*args): return _openbabel.OBConversion_GetInStream(*args)
    def GetOutStream(*args): return _openbabel.OBConversion_GetOutStream(*args)
    def SetInStream(*args): return _openbabel.OBConversion_SetInStream(*args)
    def SetOutStream(*args): return _openbabel.OBConversion_SetOutStream(*args)
    def SetInAndOutFormats(*args): return _openbabel.OBConversion_SetInAndOutFormats(*args)
    def SetInFormat(*args): return _openbabel.OBConversion_SetInFormat(*args)
    def SetOutFormat(*args): return _openbabel.OBConversion_SetOutFormat(*args)
    def GetInFormat(*args): return _openbabel.OBConversion_GetInFormat(*args)
    def GetOutFormat(*args): return _openbabel.OBConversion_GetOutFormat(*args)
    def GetInFilename(*args): return _openbabel.OBConversion_GetInFilename(*args)
    def GetInPos(*args): return _openbabel.OBConversion_GetInPos(*args)
    def GetInLen(*args): return _openbabel.OBConversion_GetInLen(*args)
    def GetTitle(*args): return _openbabel.OBConversion_GetTitle(*args)
    def GetAuxConv(*args): return _openbabel.OBConversion_GetAuxConv(*args)
    def SetAuxConv(*args): return _openbabel.OBConversion_SetAuxConv(*args)
    INOPTIONS = _openbabel.OBConversion_INOPTIONS
    OUTOPTIONS = _openbabel.OBConversion_OUTOPTIONS
    GENOPTIONS = _openbabel.OBConversion_GENOPTIONS
    ALL = _openbabel.OBConversion_ALL
    def IsOption(*args): return _openbabel.OBConversion_IsOption(*args)
    def GetOptions(*args): return _openbabel.OBConversion_GetOptions(*args)
    def AddOption(*args): return _openbabel.OBConversion_AddOption(*args)
    def RemoveOption(*args): return _openbabel.OBConversion_RemoveOption(*args)
    def SetOptions(*args): return _openbabel.OBConversion_SetOptions(*args)
    __swig_getmethods__["RegisterOptionParam"] = lambda x: _openbabel.OBConversion_RegisterOptionParam
    if _newclass:RegisterOptionParam = staticmethod(_openbabel.OBConversion_RegisterOptionParam)
    __swig_getmethods__["GetOptionParams"] = lambda x: _openbabel.OBConversion_GetOptionParams
    if _newclass:GetOptionParams = staticmethod(_openbabel.OBConversion_GetOptionParams)
    def CopyOptions(*args): return _openbabel.OBConversion_CopyOptions(*args)
    def GetSupportedInputFormat(*args): return _openbabel.OBConversion_GetSupportedInputFormat(*args)
    def GetSupportedOutputFormat(*args): return _openbabel.OBConversion_GetSupportedOutputFormat(*args)
    def Convert(*args): return _openbabel.OBConversion_Convert(*args)
    def FullConvert(*args): return _openbabel.OBConversion_FullConvert(*args)
    def AddChemObject(*args): return _openbabel.OBConversion_AddChemObject(*args)
    def GetChemObject(*args): return _openbabel.OBConversion_GetChemObject(*args)
    def IsLast(*args): return _openbabel.OBConversion_IsLast(*args)
    def IsFirstInput(*args): return _openbabel.OBConversion_IsFirstInput(*args)
    def SetFirstInput(*args): return _openbabel.OBConversion_SetFirstInput(*args)
    def GetOutputIndex(*args): return _openbabel.OBConversion_GetOutputIndex(*args)
    def SetOutputIndex(*args): return _openbabel.OBConversion_SetOutputIndex(*args)
    def SetMoreFilesToCome(*args): return _openbabel.OBConversion_SetMoreFilesToCome(*args)
    def SetOneObjectOnly(*args): return _openbabel.OBConversion_SetOneObjectOnly(*args)
    def SetLast(*args): return _openbabel.OBConversion_SetLast(*args)
    def IsLastFile(*args): return _openbabel.OBConversion_IsLastFile(*args)
    __swig_getmethods__["GetDefaultFormat"] = lambda x: _openbabel.OBConversion_GetDefaultFormat
    if _newclass:GetDefaultFormat = staticmethod(_openbabel.OBConversion_GetDefaultFormat)
    def Write(*args): return _openbabel.OBConversion_Write(*args)
    def WriteString(*args): return _openbabel.OBConversion_WriteString(*args)
    def WriteFile(*args): return _openbabel.OBConversion_WriteFile(*args)
    def CloseOutFile(*args): return _openbabel.OBConversion_CloseOutFile(*args)
    def Read(*args): return _openbabel.OBConversion_Read(*args)
    def ReadString(*args): return _openbabel.OBConversion_ReadString(*args)
    def ReadFile(*args): return _openbabel.OBConversion_ReadFile(*args)
    def ReportNumberConverted(*args): return _openbabel.OBConversion_ReportNumberConverted(*args)
OBConversion_swigregister = _openbabel.OBConversion_swigregister
OBConversion_swigregister(OBConversion)
OBConversion_RegisterFormat = _openbabel.OBConversion_RegisterFormat
OBConversion_FindFormat = _openbabel.OBConversion_FindFormat
OBConversion_FormatFromExt = _openbabel.OBConversion_FormatFromExt
OBConversion_FormatFromMIME = _openbabel.OBConversion_FormatFromMIME
OBConversion_Description = _openbabel.OBConversion_Description
OBConversion_RegisterOptionParam = _openbabel.OBConversion_RegisterOptionParam
OBConversion_GetOptionParams = _openbabel.OBConversion_GetOptionParams
OBConversion_GetDefaultFormat = _openbabel.OBConversion_GetDefaultFormat

class OBResidue(OBBase):
    __swig_setmethods__ = {}
    for _s in [OBBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBResidue, name, value)
    __swig_getmethods__ = {}
    for _s in [OBBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBResidue, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBResidue(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBResidue
    __del__ = lambda self : None;
    def AddAtom(*args): return _openbabel.OBResidue_AddAtom(*args)
    def InsertAtom(*args): return _openbabel.OBResidue_InsertAtom(*args)
    def RemoveAtom(*args): return _openbabel.OBResidue_RemoveAtom(*args)
    def Clear(*args): return _openbabel.OBResidue_Clear(*args)
    def SetName(*args): return _openbabel.OBResidue_SetName(*args)
    def SetNum(*args): return _openbabel.OBResidue_SetNum(*args)
    def SetChain(*args): return _openbabel.OBResidue_SetChain(*args)
    def SetChainNum(*args): return _openbabel.OBResidue_SetChainNum(*args)
    def SetIdx(*args): return _openbabel.OBResidue_SetIdx(*args)
    def SetAtomID(*args): return _openbabel.OBResidue_SetAtomID(*args)
    def SetHetAtom(*args): return _openbabel.OBResidue_SetHetAtom(*args)
    def SetSerialNum(*args): return _openbabel.OBResidue_SetSerialNum(*args)
    def GetName(*args): return _openbabel.OBResidue_GetName(*args)
    def GetNum(*args): return _openbabel.OBResidue_GetNum(*args)
    def GetNumString(*args): return _openbabel.OBResidue_GetNumString(*args)
    def GetNumAtoms(*args): return _openbabel.OBResidue_GetNumAtoms(*args)
    def GetChain(*args): return _openbabel.OBResidue_GetChain(*args)
    def GetChainNum(*args): return _openbabel.OBResidue_GetChainNum(*args)
    def GetIdx(*args): return _openbabel.OBResidue_GetIdx(*args)
    def GetResKey(*args): return _openbabel.OBResidue_GetResKey(*args)
    def GetAtoms(*args): return _openbabel.OBResidue_GetAtoms(*args)
    def GetBonds(*args): return _openbabel.OBResidue_GetBonds(*args)
    def GetAtomID(*args): return _openbabel.OBResidue_GetAtomID(*args)
    def GetSerialNum(*args): return _openbabel.OBResidue_GetSerialNum(*args)
    def GetAminoAcidProperty(*args): return _openbabel.OBResidue_GetAminoAcidProperty(*args)
    def GetAtomProperty(*args): return _openbabel.OBResidue_GetAtomProperty(*args)
    def GetResidueProperty(*args): return _openbabel.OBResidue_GetResidueProperty(*args)
    def IsHetAtom(*args): return _openbabel.OBResidue_IsHetAtom(*args)
    def IsResidueType(*args): return _openbabel.OBResidue_IsResidueType(*args)
    def BeginAtoms(*args): return _openbabel.OBResidue_BeginAtoms(*args)
    def EndAtoms(*args): return _openbabel.OBResidue_EndAtoms(*args)
    def BeginAtom(*args): return _openbabel.OBResidue_BeginAtom(*args)
    def NextAtom(*args): return _openbabel.OBResidue_NextAtom(*args)
OBResidue_swigregister = _openbabel.OBResidue_swigregister
OBResidue_swigregister(OBResidue)

MAXSETNO = _openbabel.MAXSETNO
MAXELEM = _openbabel.MAXELEM
MINELEM = _openbabel.MINELEM
MAXRES = _openbabel.MAXRES
MINRES = _openbabel.MINRES
AA_ALA = _openbabel.AA_ALA
AA_GLY = _openbabel.AA_GLY
AA_LEU = _openbabel.AA_LEU
AA_SER = _openbabel.AA_SER
AA_VAL = _openbabel.AA_VAL
AA_THR = _openbabel.AA_THR
AA_LYS = _openbabel.AA_LYS
AA_ASP = _openbabel.AA_ASP
AA_ILE = _openbabel.AA_ILE
AA_ASN = _openbabel.AA_ASN
AA_GLU = _openbabel.AA_GLU
AA_PRO = _openbabel.AA_PRO
AA_ARG = _openbabel.AA_ARG
AA_PHE = _openbabel.AA_PHE
AA_GLN = _openbabel.AA_GLN
AA_TYR = _openbabel.AA_TYR
AA_HIS = _openbabel.AA_HIS
AA_CYS = _openbabel.AA_CYS
AA_MET = _openbabel.AA_MET
AA_TRP = _openbabel.AA_TRP
ACIDIC = _openbabel.ACIDIC
ACYCLIC = _openbabel.ACYCLIC
ALIPHATIC = _openbabel.ALIPHATIC
AROMATIC = _openbabel.AROMATIC
BASIC = _openbabel.BASIC
BURIED = _openbabel.BURIED
CHARGED = _openbabel.CHARGED
CYCLIC = _openbabel.CYCLIC
HYDROPHOBIC = _openbabel.HYDROPHOBIC
LARGE = _openbabel.LARGE
MEDIUM = _openbabel.MEDIUM
NEGATIVE = _openbabel.NEGATIVE
NEUTRAL = _openbabel.NEUTRAL
POLAR = _openbabel.POLAR
POSITIVE = _openbabel.POSITIVE
SMALL = _openbabel.SMALL
SURFACE = _openbabel.SURFACE
ALPHA_CARBON = _openbabel.ALPHA_CARBON
AMINO_BACKBONE = _openbabel.AMINO_BACKBONE
BACKBONE = _openbabel.BACKBONE
CYSTEINE_SULPHUR = _openbabel.CYSTEINE_SULPHUR
LIGAND = _openbabel.LIGAND
NUCLEIC_BACKBONE = _openbabel.NUCLEIC_BACKBONE
SHAPELY_BACKBONE = _openbabel.SHAPELY_BACKBONE
SHAPELY_SPECIAL = _openbabel.SHAPELY_SPECIAL
SIDECHAIN = _openbabel.SIDECHAIN
SUGAR_PHOSPHATE = _openbabel.SUGAR_PHOSPHATE
ALA = _openbabel.ALA
GLY = _openbabel.GLY
LEU = _openbabel.LEU
SER = _openbabel.SER
VAL = _openbabel.VAL
THR = _openbabel.THR
LYS = _openbabel.LYS
ASP = _openbabel.ASP
ILE = _openbabel.ILE
ASN = _openbabel.ASN
GLU = _openbabel.GLU
PRO = _openbabel.PRO
ARG = _openbabel.ARG
PHE = _openbabel.PHE
GLN = _openbabel.GLN
TYR = _openbabel.TYR
HIS = _openbabel.HIS
CYS = _openbabel.CYS
MET = _openbabel.MET
TRP = _openbabel.TRP
ASX = _openbabel.ASX
GLX = _openbabel.GLX
PCA = _openbabel.PCA
HYP = _openbabel.HYP
A = _openbabel.A
C = _openbabel.C
G = _openbabel.G
T = _openbabel.T
U = _openbabel.U
UPLUS = _openbabel.UPLUS
I = _openbabel.I
_1MA = _openbabel._1MA
_5MC = _openbabel._5MC
OMC = _openbabel.OMC
_1MG = _openbabel._1MG
_2MG = _openbabel._2MG
M2G = _openbabel.M2G
_7MG = _openbabel._7MG
OMG = _openbabel.OMG
YG = _openbabel.YG
H2U = _openbabel.H2U
_5MU = _openbabel._5MU
PSU = _openbabel.PSU
UNK = _openbabel.UNK
ACE = _openbabel.ACE
FOR = _openbabel.FOR
HOH = _openbabel.HOH
DOD = _openbabel.DOD
SO4 = _openbabel.SO4
PO4 = _openbabel.PO4
NAD = _openbabel.NAD
COA = _openbabel.COA
NAP = _openbabel.NAP
NDP = _openbabel.NDP
AMINO = _openbabel.AMINO
AMINO_NUCLEO = _openbabel.AMINO_NUCLEO
COENZYME = _openbabel.COENZYME
ION = _openbabel.ION
NUCLEO = _openbabel.NUCLEO
PROTEIN = _openbabel.PROTEIN
PURINE = _openbabel.PURINE
PYRIMIDINE = _openbabel.PYRIMIDINE
SOLVENT = _openbabel.SOLVENT
WATER = _openbabel.WATER
class OBInternalCoord(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBInternalCoord, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBInternalCoord, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_a"] = _openbabel.OBInternalCoord__a_set
    __swig_getmethods__["_a"] = _openbabel.OBInternalCoord__a_get
    if _newclass:_a = _swig_property(_openbabel.OBInternalCoord__a_get, _openbabel.OBInternalCoord__a_set)
    __swig_setmethods__["_b"] = _openbabel.OBInternalCoord__b_set
    __swig_getmethods__["_b"] = _openbabel.OBInternalCoord__b_get
    if _newclass:_b = _swig_property(_openbabel.OBInternalCoord__b_get, _openbabel.OBInternalCoord__b_set)
    __swig_setmethods__["_c"] = _openbabel.OBInternalCoord__c_set
    __swig_getmethods__["_c"] = _openbabel.OBInternalCoord__c_get
    if _newclass:_c = _swig_property(_openbabel.OBInternalCoord__c_get, _openbabel.OBInternalCoord__c_set)
    __swig_setmethods__["_dst"] = _openbabel.OBInternalCoord__dst_set
    __swig_getmethods__["_dst"] = _openbabel.OBInternalCoord__dst_get
    if _newclass:_dst = _swig_property(_openbabel.OBInternalCoord__dst_get, _openbabel.OBInternalCoord__dst_set)
    __swig_setmethods__["_ang"] = _openbabel.OBInternalCoord__ang_set
    __swig_getmethods__["_ang"] = _openbabel.OBInternalCoord__ang_get
    if _newclass:_ang = _swig_property(_openbabel.OBInternalCoord__ang_get, _openbabel.OBInternalCoord__ang_set)
    __swig_setmethods__["_tor"] = _openbabel.OBInternalCoord__tor_set
    __swig_getmethods__["_tor"] = _openbabel.OBInternalCoord__tor_get
    if _newclass:_tor = _swig_property(_openbabel.OBInternalCoord__tor_get, _openbabel.OBInternalCoord__tor_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBInternalCoord(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBInternalCoord
    __del__ = lambda self : None;
OBInternalCoord_swigregister = _openbabel.OBInternalCoord_swigregister
OBInternalCoord_swigregister(OBInternalCoord)

OB_4RING_ATOM = _openbabel.OB_4RING_ATOM
OB_3RING_ATOM = _openbabel.OB_3RING_ATOM
OB_AROMATIC_ATOM = _openbabel.OB_AROMATIC_ATOM
OB_RING_ATOM = _openbabel.OB_RING_ATOM
OB_CSTEREO_ATOM = _openbabel.OB_CSTEREO_ATOM
OB_ACSTEREO_ATOM = _openbabel.OB_ACSTEREO_ATOM
OB_DONOR_ATOM = _openbabel.OB_DONOR_ATOM
OB_ACCEPTOR_ATOM = _openbabel.OB_ACCEPTOR_ATOM
OB_CHIRAL_ATOM = _openbabel.OB_CHIRAL_ATOM
OB_POS_CHIRAL_ATOM = _openbabel.OB_POS_CHIRAL_ATOM
OB_NEG_CHIRAL_ATOM = _openbabel.OB_NEG_CHIRAL_ATOM
OB_ATOM_HAS_NO_H = _openbabel.OB_ATOM_HAS_NO_H
OB_ATOM_NOT_H_DEFICIENT = _openbabel.OB_ATOM_NOT_H_DEFICIENT
class OBAtom(OBBase):
    __swig_setmethods__ = {}
    for _s in [OBBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBAtom, name, value)
    __swig_getmethods__ = {}
    for _s in [OBBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBAtom, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Visit"] = _openbabel.OBAtom_Visit_set
    __swig_getmethods__["Visit"] = _openbabel.OBAtom_Visit_get
    if _newclass:Visit = _swig_property(_openbabel.OBAtom_Visit_get, _openbabel.OBAtom_Visit_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBAtom(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBAtom
    __del__ = lambda self : None;
    def Clear(*args): return _openbabel.OBAtom_Clear(*args)
    def SetIdx(*args): return _openbabel.OBAtom_SetIdx(*args)
    def SetHyb(*args): return _openbabel.OBAtom_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel.OBAtom_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel.OBAtom_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel.OBAtom_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel.OBAtom_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel.OBAtom_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel.OBAtom_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel.OBAtom_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel.OBAtom_SetType(*args)
    def SetPartialCharge(*args): return _openbabel.OBAtom_SetPartialCharge(*args)
    def SetCoordPtr(*args): return _openbabel.OBAtom_SetCoordPtr(*args)
    def SetVector(*args): return _openbabel.OBAtom_SetVector(*args)
    def SetResidue(*args): return _openbabel.OBAtom_SetResidue(*args)
    def SetParent(*args): return _openbabel.OBAtom_SetParent(*args)
    def SetAromatic(*args): return _openbabel.OBAtom_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel.OBAtom_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel.OBAtom_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel.OBAtom_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel.OBAtom_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel.OBAtom_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel.OBAtom_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel.OBAtom_SetInRing(*args)
    def SetChiral(*args): return _openbabel.OBAtom_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel.OBAtom_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel.OBAtom_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel.OBAtom_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel.OBAtom_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel.OBAtom_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel.OBAtom_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel.OBAtom_GetExactMass(*args)
    def GetIdx(*args): return _openbabel.OBAtom_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel.OBAtom_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel.OBAtom_GetCIdx(*args)
    def GetValence(*args): return _openbabel.OBAtom_GetValence(*args)
    def GetHyb(*args): return _openbabel.OBAtom_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel.OBAtom_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel.OBAtom_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel.OBAtom_GetHeteroValence(*args)
    def GetType(*args): return _openbabel.OBAtom_GetType(*args)
    def GetX(*args): return _openbabel.OBAtom_GetX(*args)
    def GetY(*args): return _openbabel.OBAtom_GetY(*args)
    def GetZ(*args): return _openbabel.OBAtom_GetZ(*args)
    def x(*args): return _openbabel.OBAtom_x(*args)
    def y(*args): return _openbabel.OBAtom_y(*args)
    def z(*args): return _openbabel.OBAtom_z(*args)
    def GetCoordinate(*args): return _openbabel.OBAtom_GetCoordinate(*args)
    def GetVector(*args): return _openbabel.OBAtom_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel.OBAtom_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel.OBAtom_GetResidue(*args)
    def GetParent(*args): return _openbabel.OBAtom_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel.OBAtom_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel.OBAtom_GetBond(*args)
    def GetNextAtom(*args): return _openbabel.OBAtom_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel.OBAtom_BeginBonds(*args)
    def EndBonds(*args): return _openbabel.OBAtom_EndBonds(*args)
    def BeginBond(*args): return _openbabel.OBAtom_BeginBond(*args)
    def NextBond(*args): return _openbabel.OBAtom_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel.OBAtom_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel.OBAtom_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel.OBAtom_GetDistance(*args)
    def GetAngle(*args): return _openbabel.OBAtom_GetAngle(*args)
    def NewResidue(*args): return _openbabel.OBAtom_NewResidue(*args)
    def AddResidue(*args): return _openbabel.OBAtom_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel.OBAtom_DeleteResidue(*args)
    def AddBond(*args): return _openbabel.OBAtom_AddBond(*args)
    def InsertBond(*args): return _openbabel.OBAtom_InsertBond(*args)
    def DeleteBond(*args): return _openbabel.OBAtom_DeleteBond(*args)
    def ClearBond(*args): return _openbabel.OBAtom_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel.OBAtom_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel.OBAtom_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel.OBAtom_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel.OBAtom_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel.OBAtom_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel.OBAtom_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel.OBAtom_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel.OBAtom_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel.OBAtom_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel.OBAtom_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel.OBAtom_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel.OBAtom_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel.OBAtom_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel.OBAtom_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel.OBAtom_BOSum(*args)
    def KBOSum(*args): return _openbabel.OBAtom_KBOSum(*args)
    def HasResidue(*args): return _openbabel.OBAtom_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel.OBAtom_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel.OBAtom_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel.OBAtom_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel.OBAtom_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel.OBAtom_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel.OBAtom_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel.OBAtom_IsAromatic(*args)
    def IsInRing(*args): return _openbabel.OBAtom_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel.OBAtom_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel.OBAtom_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel.OBAtom_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel.OBAtom_IsConnected(*args)
    def IsOneThree(*args): return _openbabel.OBAtom_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel.OBAtom_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel.OBAtom_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel.OBAtom_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel.OBAtom_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel.OBAtom_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel.OBAtom_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel.OBAtom_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel.OBAtom_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel.OBAtom_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel.OBAtom_IsChiral(*args)
    def IsAxial(*args): return _openbabel.OBAtom_IsAxial(*args)
    def IsClockwise(*args): return _openbabel.OBAtom_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel.OBAtom_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel.OBAtom_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel.OBAtom_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel.OBAtom_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel.OBAtom_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel.OBAtom_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel.OBAtom_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel.OBAtom_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel.OBAtom_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel.OBAtom_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel.OBAtom_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel.OBAtom_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel.OBAtom_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel.OBAtom_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel.OBAtom_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel.OBAtom_MatchesSMARTS(*args)
OBAtom_swigregister = _openbabel.OBAtom_swigregister
OBAtom_swigregister(OBAtom)

OB_AROMATIC_BOND = _openbabel.OB_AROMATIC_BOND
OB_WEDGE_BOND = _openbabel.OB_WEDGE_BOND
OB_HASH_BOND = _openbabel.OB_HASH_BOND
OB_RING_BOND = _openbabel.OB_RING_BOND
OB_TORUP_BOND = _openbabel.OB_TORUP_BOND
OB_TORDOWN_BOND = _openbabel.OB_TORDOWN_BOND
OB_KSINGLE_BOND = _openbabel.OB_KSINGLE_BOND
OB_KDOUBLE_BOND = _openbabel.OB_KDOUBLE_BOND
OB_KTRIPLE_BOND = _openbabel.OB_KTRIPLE_BOND
OB_CLOSURE_BOND = _openbabel.OB_CLOSURE_BOND
class OBBond(OBBase):
    __swig_setmethods__ = {}
    for _s in [OBBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBBond, name, value)
    __swig_getmethods__ = {}
    for _s in [OBBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBBond, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Visit"] = _openbabel.OBBond_Visit_set
    __swig_getmethods__["Visit"] = _openbabel.OBBond_Visit_get
    if _newclass:Visit = _swig_property(_openbabel.OBBond_Visit_get, _openbabel.OBBond_Visit_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBBond(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBBond
    __del__ = lambda self : None;
    def SetIdx(*args): return _openbabel.OBBond_SetIdx(*args)
    def SetBO(*args): return _openbabel.OBBond_SetBO(*args)
    def SetBondOrder(*args): return _openbabel.OBBond_SetBondOrder(*args)
    def SetBegin(*args): return _openbabel.OBBond_SetBegin(*args)
    def SetEnd(*args): return _openbabel.OBBond_SetEnd(*args)
    def SetParent(*args): return _openbabel.OBBond_SetParent(*args)
    def SetLength(*args): return _openbabel.OBBond_SetLength(*args)
    def Set(*args): return _openbabel.OBBond_Set(*args)
    def SetKSingle(*args): return _openbabel.OBBond_SetKSingle(*args)
    def SetKDouble(*args): return _openbabel.OBBond_SetKDouble(*args)
    def SetKTriple(*args): return _openbabel.OBBond_SetKTriple(*args)
    def SetAromatic(*args): return _openbabel.OBBond_SetAromatic(*args)
    def SetHash(*args): return _openbabel.OBBond_SetHash(*args)
    def SetWedge(*args): return _openbabel.OBBond_SetWedge(*args)
    def SetUp(*args): return _openbabel.OBBond_SetUp(*args)
    def SetDown(*args): return _openbabel.OBBond_SetDown(*args)
    def SetInRing(*args): return _openbabel.OBBond_SetInRing(*args)
    def SetClosure(*args): return _openbabel.OBBond_SetClosure(*args)
    def UnsetHash(*args): return _openbabel.OBBond_UnsetHash(*args)
    def UnsetWedge(*args): return _openbabel.OBBond_UnsetWedge(*args)
    def UnsetUp(*args): return _openbabel.OBBond_UnsetUp(*args)
    def UnsetDown(*args): return _openbabel.OBBond_UnsetDown(*args)
    def UnsetAromatic(*args): return _openbabel.OBBond_UnsetAromatic(*args)
    def UnsetKekule(*args): return _openbabel.OBBond_UnsetKekule(*args)
    def GetIdx(*args): return _openbabel.OBBond_GetIdx(*args)
    def GetBO(*args): return _openbabel.OBBond_GetBO(*args)
    def GetBondOrder(*args): return _openbabel.OBBond_GetBondOrder(*args)
    def GetFlags(*args): return _openbabel.OBBond_GetFlags(*args)
    def GetBeginAtomIdx(*args): return _openbabel.OBBond_GetBeginAtomIdx(*args)
    def GetEndAtomIdx(*args): return _openbabel.OBBond_GetEndAtomIdx(*args)
    def GetBeginAtom(*args): return _openbabel.OBBond_GetBeginAtom(*args)
    def GetEndAtom(*args): return _openbabel.OBBond_GetEndAtom(*args)
    def GetNbrAtom(*args): return _openbabel.OBBond_GetNbrAtom(*args)
    def GetParent(*args): return _openbabel.OBBond_GetParent(*args)
    def GetEquibLength(*args): return _openbabel.OBBond_GetEquibLength(*args)
    def GetLength(*args): return _openbabel.OBBond_GetLength(*args)
    def GetNbrAtomIdx(*args): return _openbabel.OBBond_GetNbrAtomIdx(*args)
    def IsAromatic(*args): return _openbabel.OBBond_IsAromatic(*args)
    def IsInRing(*args): return _openbabel.OBBond_IsInRing(*args)
    def IsRotor(*args): return _openbabel.OBBond_IsRotor(*args)
    def IsAmide(*args): return _openbabel.OBBond_IsAmide(*args)
    def IsPrimaryAmide(*args): return _openbabel.OBBond_IsPrimaryAmide(*args)
    def IsSecondaryAmide(*args): return _openbabel.OBBond_IsSecondaryAmide(*args)
    def IsEster(*args): return _openbabel.OBBond_IsEster(*args)
    def IsCarbonyl(*args): return _openbabel.OBBond_IsCarbonyl(*args)
    def IsSingle(*args): return _openbabel.OBBond_IsSingle(*args)
    def IsDouble(*args): return _openbabel.OBBond_IsDouble(*args)
    def IsTriple(*args): return _openbabel.OBBond_IsTriple(*args)
    def IsKSingle(*args): return _openbabel.OBBond_IsKSingle(*args)
    def IsKDouble(*args): return _openbabel.OBBond_IsKDouble(*args)
    def IsKTriple(*args): return _openbabel.OBBond_IsKTriple(*args)
    def IsClosure(*args): return _openbabel.OBBond_IsClosure(*args)
    def IsUp(*args): return _openbabel.OBBond_IsUp(*args)
    def IsDown(*args): return _openbabel.OBBond_IsDown(*args)
    def IsWedge(*args): return _openbabel.OBBond_IsWedge(*args)
    def IsHash(*args): return _openbabel.OBBond_IsHash(*args)
    def IsDoubleBondGeometry(*args): return _openbabel.OBBond_IsDoubleBondGeometry(*args)
OBBond_swigregister = _openbabel.OBBond_swigregister
OBBond_swigregister(OBBond)

OB_SSSR_MOL = _openbabel.OB_SSSR_MOL
OB_RINGFLAGS_MOL = _openbabel.OB_RINGFLAGS_MOL
OB_AROMATIC_MOL = _openbabel.OB_AROMATIC_MOL
OB_ATOMTYPES_MOL = _openbabel.OB_ATOMTYPES_MOL
OB_CHIRALITY_MOL = _openbabel.OB_CHIRALITY_MOL
OB_PCHARGE_MOL = _openbabel.OB_PCHARGE_MOL
OB_HYBRID_MOL = _openbabel.OB_HYBRID_MOL
OB_IMPVAL_MOL = _openbabel.OB_IMPVAL_MOL
OB_KEKULE_MOL = _openbabel.OB_KEKULE_MOL
OB_CLOSURE_MOL = _openbabel.OB_CLOSURE_MOL
OB_H_ADDED_MOL = _openbabel.OB_H_ADDED_MOL
OB_PH_CORRECTED_MOL = _openbabel.OB_PH_CORRECTED_MOL
OB_AROM_CORRECTED_MOL = _openbabel.OB_AROM_CORRECTED_MOL
OB_CHAINS_MOL = _openbabel.OB_CHAINS_MOL
OB_TCHARGE_MOL = _openbabel.OB_TCHARGE_MOL
OB_TSPIN_MOL = _openbabel.OB_TSPIN_MOL
OB_RINGTYPES_MOL = _openbabel.OB_RINGTYPES_MOL
OB_CURRENT_CONFORMER = _openbabel.OB_CURRENT_CONFORMER
class OBMol(OBBase):
    __swig_setmethods__ = {}
    for _s in [OBBase]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBMol, name, value)
    __swig_getmethods__ = {}
    for _s in [OBBase]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBMol, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBMol(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBMol
    __del__ = lambda self : None;
    def __iadd__(*args): return _openbabel.OBMol___iadd__(*args)
    def ReserveAtoms(*args): return _openbabel.OBMol_ReserveAtoms(*args)
    def CreateAtom(*args): return _openbabel.OBMol_CreateAtom(*args)
    def CreateBond(*args): return _openbabel.OBMol_CreateBond(*args)
    def CreateResidue(*args): return _openbabel.OBMol_CreateResidue(*args)
    def DestroyAtom(*args): return _openbabel.OBMol_DestroyAtom(*args)
    def DestroyBond(*args): return _openbabel.OBMol_DestroyBond(*args)
    def DestroyResidue(*args): return _openbabel.OBMol_DestroyResidue(*args)
    def AddAtom(*args): return _openbabel.OBMol_AddAtom(*args)
    def InsertAtom(*args): return _openbabel.OBMol_InsertAtom(*args)
    def AddBond(*args): return _openbabel.OBMol_AddBond(*args)
    def AddResidue(*args): return _openbabel.OBMol_AddResidue(*args)
    def NewAtom(*args): return _openbabel.OBMol_NewAtom(*args)
    def NewBond(*args): return _openbabel.OBMol_NewBond(*args)
    def NewResidue(*args): return _openbabel.OBMol_NewResidue(*args)
    def DeleteAtom(*args): return _openbabel.OBMol_DeleteAtom(*args)
    def DeleteBond(*args): return _openbabel.OBMol_DeleteBond(*args)
    def DeleteResidue(*args): return _openbabel.OBMol_DeleteResidue(*args)
    def BeginModify(*args): return _openbabel.OBMol_BeginModify(*args)
    def EndModify(*args): return _openbabel.OBMol_EndModify(*args)
    def GetMod(*args): return _openbabel.OBMol_GetMod(*args)
    def IncrementMod(*args): return _openbabel.OBMol_IncrementMod(*args)
    def DecrementMod(*args): return _openbabel.OBMol_DecrementMod(*args)
    def GetFlags(*args): return _openbabel.OBMol_GetFlags(*args)
    def GetTitle(*args): return _openbabel.OBMol_GetTitle(*args)
    def NumAtoms(*args): return _openbabel.OBMol_NumAtoms(*args)
    def NumBonds(*args): return _openbabel.OBMol_NumBonds(*args)
    def NumHvyAtoms(*args): return _openbabel.OBMol_NumHvyAtoms(*args)
    def NumResidues(*args): return _openbabel.OBMol_NumResidues(*args)
    def NumRotors(*args): return _openbabel.OBMol_NumRotors(*args)
    def GetAtom(*args): return _openbabel.OBMol_GetAtom(*args)
    def GetFirstAtom(*args): return _openbabel.OBMol_GetFirstAtom(*args)
    def GetBond(*args): return _openbabel.OBMol_GetBond(*args)
    def GetResidue(*args): return _openbabel.OBMol_GetResidue(*args)
    def GetInternalCoord(*args): return _openbabel.OBMol_GetInternalCoord(*args)
    def GetTorsion(*args): return _openbabel.OBMol_GetTorsion(*args)
    def GetAngle(*args): return _openbabel.OBMol_GetAngle(*args)
    def GetFormula(*args): return _openbabel.OBMol_GetFormula(*args)
    def GetSpacedFormula(*args): return _openbabel.OBMol_GetSpacedFormula(*args)
    def GetMolWt(*args): return _openbabel.OBMol_GetMolWt(*args)
    def GetExactMass(*args): return _openbabel.OBMol_GetExactMass(*args)
    def GetTotalCharge(*args): return _openbabel.OBMol_GetTotalCharge(*args)
    def GetTotalSpinMultiplicity(*args): return _openbabel.OBMol_GetTotalSpinMultiplicity(*args)
    def GetDimension(*args): return _openbabel.OBMol_GetDimension(*args)
    def GetCoordinates(*args): return _openbabel.OBMol_GetCoordinates(*args)
    def GetSSSR(*args): return _openbabel.OBMol_GetSSSR(*args)
    def AutomaticFormalCharge(*args): return _openbabel.OBMol_AutomaticFormalCharge(*args)
    def AutomaticPartialCharge(*args): return _openbabel.OBMol_AutomaticPartialCharge(*args)
    def SetTitle(*args): return _openbabel.OBMol_SetTitle(*args)
    def SetFormula(*args): return _openbabel.OBMol_SetFormula(*args)
    def SetEnergy(*args): return _openbabel.OBMol_SetEnergy(*args)
    def SetDimension(*args): return _openbabel.OBMol_SetDimension(*args)
    def SetTotalCharge(*args): return _openbabel.OBMol_SetTotalCharge(*args)
    def SetTotalSpinMultiplicity(*args): return _openbabel.OBMol_SetTotalSpinMultiplicity(*args)
    def SetInternalCoord(*args): return _openbabel.OBMol_SetInternalCoord(*args)
    def SetAutomaticFormalCharge(*args): return _openbabel.OBMol_SetAutomaticFormalCharge(*args)
    def SetAutomaticPartialCharge(*args): return _openbabel.OBMol_SetAutomaticPartialCharge(*args)
    def SetAromaticPerceived(*args): return _openbabel.OBMol_SetAromaticPerceived(*args)
    def SetSSSRPerceived(*args): return _openbabel.OBMol_SetSSSRPerceived(*args)
    def SetRingAtomsAndBondsPerceived(*args): return _openbabel.OBMol_SetRingAtomsAndBondsPerceived(*args)
    def SetAtomTypesPerceived(*args): return _openbabel.OBMol_SetAtomTypesPerceived(*args)
    def SetRingTypesPerceived(*args): return _openbabel.OBMol_SetRingTypesPerceived(*args)
    def SetChainsPerceived(*args): return _openbabel.OBMol_SetChainsPerceived(*args)
    def SetChiralityPerceived(*args): return _openbabel.OBMol_SetChiralityPerceived(*args)
    def SetPartialChargesPerceived(*args): return _openbabel.OBMol_SetPartialChargesPerceived(*args)
    def SetHybridizationPerceived(*args): return _openbabel.OBMol_SetHybridizationPerceived(*args)
    def SetImplicitValencePerceived(*args): return _openbabel.OBMol_SetImplicitValencePerceived(*args)
    def SetKekulePerceived(*args): return _openbabel.OBMol_SetKekulePerceived(*args)
    def SetClosureBondsPerceived(*args): return _openbabel.OBMol_SetClosureBondsPerceived(*args)
    def SetHydrogensAdded(*args): return _openbabel.OBMol_SetHydrogensAdded(*args)
    def SetCorrectedForPH(*args): return _openbabel.OBMol_SetCorrectedForPH(*args)
    def SetAromaticCorrected(*args): return _openbabel.OBMol_SetAromaticCorrected(*args)
    def SetSpinMultiplicityAssigned(*args): return _openbabel.OBMol_SetSpinMultiplicityAssigned(*args)
    def SetFlags(*args): return _openbabel.OBMol_SetFlags(*args)
    def UnsetAromaticPerceived(*args): return _openbabel.OBMol_UnsetAromaticPerceived(*args)
    def UnsetRingTypesPerceived(*args): return _openbabel.OBMol_UnsetRingTypesPerceived(*args)
    def UnsetPartialChargesPerceived(*args): return _openbabel.OBMol_UnsetPartialChargesPerceived(*args)
    def UnsetImplicitValencePerceived(*args): return _openbabel.OBMol_UnsetImplicitValencePerceived(*args)
    def UnsetHydrogensAdded(*args): return _openbabel.OBMol_UnsetHydrogensAdded(*args)
    def UnsetFlag(*args): return _openbabel.OBMol_UnsetFlag(*args)
    def DoTransformations(*args): return _openbabel.OBMol_DoTransformations(*args)
    __swig_getmethods__["ClassDescription"] = lambda x: _openbabel.OBMol_ClassDescription
    if _newclass:ClassDescription = staticmethod(_openbabel.OBMol_ClassDescription)
    def Clear(*args): return _openbabel.OBMol_Clear(*args)
    def RenumberAtoms(*args): return _openbabel.OBMol_RenumberAtoms(*args)
    def SetCoordinates(*args): return _openbabel.OBMol_SetCoordinates(*args)
    def ToInertialFrame(*args): return _openbabel.OBMol_ToInertialFrame(*args)
    def Translate(*args): return _openbabel.OBMol_Translate(*args)
    def Rotate(*args): return _openbabel.OBMol_Rotate(*args)
    def Kekulize(*args): return _openbabel.OBMol_Kekulize(*args)
    def PerceiveKekuleBonds(*args): return _openbabel.OBMol_PerceiveKekuleBonds(*args)
    def NewPerceiveKekuleBonds(*args): return _openbabel.OBMol_NewPerceiveKekuleBonds(*args)
    def DeleteHydrogens(*args): return _openbabel.OBMol_DeleteHydrogens(*args)
    def DeleteNonPolarHydrogens(*args): return _openbabel.OBMol_DeleteNonPolarHydrogens(*args)
    def DeleteHydrogen(*args): return _openbabel.OBMol_DeleteHydrogen(*args)
    def AddHydrogens(*args): return _openbabel.OBMol_AddHydrogens(*args)
    def AddPolarHydrogens(*args): return _openbabel.OBMol_AddPolarHydrogens(*args)
    def StripSalts(*args): return _openbabel.OBMol_StripSalts(*args)
    def Separate(*args): return _openbabel.OBMol_Separate(*args)
    def ConvertDativeBonds(*args): return _openbabel.OBMol_ConvertDativeBonds(*args)
    def CorrectForPH(*args): return _openbabel.OBMol_CorrectForPH(*args)
    def AssignSpinMultiplicity(*args): return _openbabel.OBMol_AssignSpinMultiplicity(*args)
    def Center(*args): return _openbabel.OBMol_Center(*args)
    def SetTorsion(*args): return _openbabel.OBMol_SetTorsion(*args)
    def FindSSSR(*args): return _openbabel.OBMol_FindSSSR(*args)
    def FindRingAtomsAndBonds(*args): return _openbabel.OBMol_FindRingAtomsAndBonds(*args)
    def FindChiralCenters(*args): return _openbabel.OBMol_FindChiralCenters(*args)
    def FindChildren(*args): return _openbabel.OBMol_FindChildren(*args)
    def FindLargestFragment(*args): return _openbabel.OBMol_FindLargestFragment(*args)
    def ContigFragList(*args): return _openbabel.OBMol_ContigFragList(*args)
    def Align(*args): return _openbabel.OBMol_Align(*args)
    def ConnectTheDots(*args): return _openbabel.OBMol_ConnectTheDots(*args)
    def PerceiveBondOrders(*args): return _openbabel.OBMol_PerceiveBondOrders(*args)
    def FindAngles(*args): return _openbabel.OBMol_FindAngles(*args)
    def FindTorsions(*args): return _openbabel.OBMol_FindTorsions(*args)
    def GetGTDVector(*args): return _openbabel.OBMol_GetGTDVector(*args)
    def GetGIVector(*args): return _openbabel.OBMol_GetGIVector(*args)
    def GetGIDVector(*args): return _openbabel.OBMol_GetGIDVector(*args)
    def Has2D(*args): return _openbabel.OBMol_Has2D(*args)
    def Has3D(*args): return _openbabel.OBMol_Has3D(*args)
    def HasNonZeroCoords(*args): return _openbabel.OBMol_HasNonZeroCoords(*args)
    def HasAromaticPerceived(*args): return _openbabel.OBMol_HasAromaticPerceived(*args)
    def HasSSSRPerceived(*args): return _openbabel.OBMol_HasSSSRPerceived(*args)
    def HasRingAtomsAndBondsPerceived(*args): return _openbabel.OBMol_HasRingAtomsAndBondsPerceived(*args)
    def HasAtomTypesPerceived(*args): return _openbabel.OBMol_HasAtomTypesPerceived(*args)
    def HasRingTypesPerceived(*args): return _openbabel.OBMol_HasRingTypesPerceived(*args)
    def HasChiralityPerceived(*args): return _openbabel.OBMol_HasChiralityPerceived(*args)
    def HasPartialChargesPerceived(*args): return _openbabel.OBMol_HasPartialChargesPerceived(*args)
    def HasHybridizationPerceived(*args): return _openbabel.OBMol_HasHybridizationPerceived(*args)
    def HasImplicitValencePerceived(*args): return _openbabel.OBMol_HasImplicitValencePerceived(*args)
    def HasKekulePerceived(*args): return _openbabel.OBMol_HasKekulePerceived(*args)
    def HasClosureBondsPerceived(*args): return _openbabel.OBMol_HasClosureBondsPerceived(*args)
    def HasChainsPerceived(*args): return _openbabel.OBMol_HasChainsPerceived(*args)
    def HasHydrogensAdded(*args): return _openbabel.OBMol_HasHydrogensAdded(*args)
    def HasAromaticCorrected(*args): return _openbabel.OBMol_HasAromaticCorrected(*args)
    def IsCorrectedForPH(*args): return _openbabel.OBMol_IsCorrectedForPH(*args)
    def HasSpinMultiplicityAssigned(*args): return _openbabel.OBMol_HasSpinMultiplicityAssigned(*args)
    def IsChiral(*args): return _openbabel.OBMol_IsChiral(*args)
    def Empty(*args): return _openbabel.OBMol_Empty(*args)
    def NumConformers(*args): return _openbabel.OBMol_NumConformers(*args)
    def SetConformers(*args): return _openbabel.OBMol_SetConformers(*args)
    def AddConformer(*args): return _openbabel.OBMol_AddConformer(*args)
    def SetConformer(*args): return _openbabel.OBMol_SetConformer(*args)
    def CopyConformer(*args): return _openbabel.OBMol_CopyConformer(*args)
    def DeleteConformer(*args): return _openbabel.OBMol_DeleteConformer(*args)
    def GetConformer(*args): return _openbabel.OBMol_GetConformer(*args)
    def SetEnergies(*args): return _openbabel.OBMol_SetEnergies(*args)
    def GetEnergies(*args): return _openbabel.OBMol_GetEnergies(*args)
    def GetEnergy(*args): return _openbabel.OBMol_GetEnergy(*args)
    def BeginConformer(*args): return _openbabel.OBMol_BeginConformer(*args)
    def NextConformer(*args): return _openbabel.OBMol_NextConformer(*args)
    def GetConformers(*args): return _openbabel.OBMol_GetConformers(*args)
    def BeginAtoms(*args): return _openbabel.OBMol_BeginAtoms(*args)
    def EndAtoms(*args): return _openbabel.OBMol_EndAtoms(*args)
    def BeginBonds(*args): return _openbabel.OBMol_BeginBonds(*args)
    def EndBonds(*args): return _openbabel.OBMol_EndBonds(*args)
    def BeginResidues(*args): return _openbabel.OBMol_BeginResidues(*args)
    def EndResidues(*args): return _openbabel.OBMol_EndResidues(*args)
    def BeginAtom(*args): return _openbabel.OBMol_BeginAtom(*args)
    def NextAtom(*args): return _openbabel.OBMol_NextAtom(*args)
    def BeginBond(*args): return _openbabel.OBMol_BeginBond(*args)
    def NextBond(*args): return _openbabel.OBMol_NextBond(*args)
    def BeginResidue(*args): return _openbabel.OBMol_BeginResidue(*args)
    def NextResidue(*args): return _openbabel.OBMol_NextResidue(*args)
    def BeginInternalCoord(*args): return _openbabel.OBMol_BeginInternalCoord(*args)
    def NextInternalCoord(*args): return _openbabel.OBMol_NextInternalCoord(*args)
OBMol_swigregister = _openbabel.OBMol_swigregister
OBMol_swigregister(OBMol)
OBMol_ClassDescription = _openbabel.OBMol_ClassDescription

CartesianToInternal = _openbabel.CartesianToInternal
InternalToCartesian = _openbabel.InternalToCartesian
NewExtension = _openbabel.NewExtension
BUFF_SIZE = _openbabel.BUFF_SIZE
get_rmat = _openbabel.get_rmat
ob_make_rmat = _openbabel.ob_make_rmat
qtrfit = _openbabel.qtrfit
superimpose = _openbabel.superimpose
class OBRing(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRing, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBRing, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_path"] = _openbabel.OBRing__path_set
    __swig_getmethods__["_path"] = _openbabel.OBRing__path_get
    if _newclass:_path = _swig_property(_openbabel.OBRing__path_get, _openbabel.OBRing__path_set)
    __swig_setmethods__["_pathset"] = _openbabel.OBRing__pathset_set
    __swig_getmethods__["_pathset"] = _openbabel.OBRing__pathset_get
    if _newclass:_pathset = _swig_property(_openbabel.OBRing__pathset_get, _openbabel.OBRing__pathset_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBRing(*args)
        try: self.this.append(this)
        except: self.this = this
    def Size(*args): return _openbabel.OBRing_Size(*args)
    def PathSize(*args): return _openbabel.OBRing_PathSize(*args)
    def IsAromatic(*args): return _openbabel.OBRing_IsAromatic(*args)
    def SetType(*args): return _openbabel.OBRing_SetType(*args)
    def GetType(*args): return _openbabel.OBRing_GetType(*args)
    def GetRootAtom(*args): return _openbabel.OBRing_GetRootAtom(*args)
    def IsMember(*args): return _openbabel.OBRing_IsMember(*args)
    def IsInRing(*args): return _openbabel.OBRing_IsInRing(*args)
    def SetParent(*args): return _openbabel.OBRing_SetParent(*args)
    def GetParent(*args): return _openbabel.OBRing_GetParent(*args)
    def findCenterAndNormal(*args): return _openbabel.OBRing_findCenterAndNormal(*args)
    __swig_destroy__ = _openbabel.delete_OBRing
    __del__ = lambda self : None;
OBRing_swigregister = _openbabel.OBRing_swigregister
OBRing_swigregister(OBRing)
ThrowError = _openbabel.ThrowError

CompareRingSize = _openbabel.CompareRingSize
class OBRingSearch(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRingSearch, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBRingSearch, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBRingSearch(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBRingSearch
    __del__ = lambda self : None;
    def SortRings(*args): return _openbabel.OBRingSearch_SortRings(*args)
    def RemoveRedundant(*args): return _openbabel.OBRingSearch_RemoveRedundant(*args)
    def AddRingFromClosure(*args): return _openbabel.OBRingSearch_AddRingFromClosure(*args)
    def SaveUniqueRing(*args): return _openbabel.OBRingSearch_SaveUniqueRing(*args)
    def WriteRings(*args): return _openbabel.OBRingSearch_WriteRings(*args)
    def BeginRings(*args): return _openbabel.OBRingSearch_BeginRings(*args)
    def EndRings(*args): return _openbabel.OBRingSearch_EndRings(*args)
OBRingSearch_swigregister = _openbabel.OBRingSearch_swigregister
OBRingSearch_swigregister(OBRingSearch)

class OBRTree(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBRTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBRTree, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBRTree(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBRTree
    __del__ = lambda self : None;
    def GetAtomIdx(*args): return _openbabel.OBRTree_GetAtomIdx(*args)
    def PathToRoot(*args): return _openbabel.OBRTree_PathToRoot(*args)
OBRTree_swigregister = _openbabel.OBRTree_swigregister
OBRTree_swigregister(OBRTree)

class OBSmartsPattern(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSmartsPattern, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBSmartsPattern, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _openbabel.delete_OBSmartsPattern
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _openbabel.new_OBSmartsPattern(*args)
        try: self.this.append(this)
        except: self.this = this
    def Init(*args): return _openbabel.OBSmartsPattern_Init(*args)
    def GetSMARTS(*args): return _openbabel.OBSmartsPattern_GetSMARTS(*args)
    def Empty(*args): return _openbabel.OBSmartsPattern_Empty(*args)
    def IsValid(*args): return _openbabel.OBSmartsPattern_IsValid(*args)
    def NumAtoms(*args): return _openbabel.OBSmartsPattern_NumAtoms(*args)
    def NumBonds(*args): return _openbabel.OBSmartsPattern_NumBonds(*args)
    def GetBond(*args): return _openbabel.OBSmartsPattern_GetBond(*args)
    def GetAtomicNum(*args): return _openbabel.OBSmartsPattern_GetAtomicNum(*args)
    def GetCharge(*args): return _openbabel.OBSmartsPattern_GetCharge(*args)
    def GetVectorBinding(*args): return _openbabel.OBSmartsPattern_GetVectorBinding(*args)
    def Match(*args): return _openbabel.OBSmartsPattern_Match(*args)
    def RestrictedMatch(*args): return _openbabel.OBSmartsPattern_RestrictedMatch(*args)
    def NumMatches(*args): return _openbabel.OBSmartsPattern_NumMatches(*args)
    def GetMapList(*args): return _openbabel.OBSmartsPattern_GetMapList(*args)
    def BeginMList(*args): return _openbabel.OBSmartsPattern_BeginMList(*args)
    def EndMList(*args): return _openbabel.OBSmartsPattern_EndMList(*args)
    def GetUMapList(*args): return _openbabel.OBSmartsPattern_GetUMapList(*args)
    def WriteMapList(*args): return _openbabel.OBSmartsPattern_WriteMapList(*args)
OBSmartsPattern_swigregister = _openbabel.OBSmartsPattern_swigregister
OBSmartsPattern_swigregister(OBSmartsPattern)

class OBSSMatch(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBSSMatch, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBSSMatch, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBSSMatch(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBSSMatch
    __del__ = lambda self : None;
    def Match(*args): return _openbabel.OBSSMatch_Match(*args)
OBSSMatch_swigregister = _openbabel.OBSSMatch_swigregister
OBSSMatch_swigregister(OBSSMatch)

SmartsLexReplace = _openbabel.SmartsLexReplace
class OBFingerprint(OBPlugin):
    __swig_setmethods__ = {}
    for _s in [OBPlugin]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFingerprint, name, value)
    __swig_getmethods__ = {}
    for _s in [OBPlugin]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBFingerprint, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["Default"] = lambda x: _openbabel.OBFingerprint_Default
    if _newclass:Default = staticmethod(_openbabel.OBFingerprint_Default)
    __swig_getmethods__["FindType"] = lambda x: _openbabel.OBFingerprint_FindType
    if _newclass:FindType = staticmethod(_openbabel.OBFingerprint_FindType)
    def TypeID(*args): return _openbabel.OBFingerprint_TypeID(*args)
    __swig_destroy__ = _openbabel.delete_OBFingerprint
    __del__ = lambda self : None;
    def SetBit(*args): return _openbabel.OBFingerprint_SetBit(*args)
    def GetBit(*args): return _openbabel.OBFingerprint_GetBit(*args)
    def Fold(*args): return _openbabel.OBFingerprint_Fold(*args)
    def GetFingerprint(*args): return _openbabel.OBFingerprint_GetFingerprint(*args)
    FPT_UNIQUEBITS = _openbabel.OBFingerprint_FPT_UNIQUEBITS
    def Flags(*args): return _openbabel.OBFingerprint_Flags(*args)
    def DescribeBits(*args): return _openbabel.OBFingerprint_DescribeBits(*args)
    __swig_getmethods__["Tanimoto"] = lambda x: _openbabel.OBFingerprint_Tanimoto
    if _newclass:Tanimoto = staticmethod(_openbabel.OBFingerprint_Tanimoto)
    __swig_getmethods__["Getbitsperint"] = lambda x: _openbabel.OBFingerprint_Getbitsperint
    if _newclass:Getbitsperint = staticmethod(_openbabel.OBFingerprint_Getbitsperint)
    __swig_getmethods__["FindFingerprint"] = lambda x: _openbabel.OBFingerprint_FindFingerprint
    if _newclass:FindFingerprint = staticmethod(_openbabel.OBFingerprint_FindFingerprint)
OBFingerprint_swigregister = _openbabel.OBFingerprint_swigregister
OBFingerprint_swigregister(OBFingerprint)
OBFingerprint_Default = _openbabel.OBFingerprint_Default
OBFingerprint_FindType = _openbabel.OBFingerprint_FindType
OBFingerprint_Tanimoto = _openbabel.OBFingerprint_Tanimoto
OBFingerprint_Getbitsperint = _openbabel.OBFingerprint_Getbitsperint
OBFingerprint_FindFingerprint = _openbabel.OBFingerprint_FindFingerprint

class FptIndexHeader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FptIndexHeader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FptIndexHeader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["headerlength"] = _openbabel.FptIndexHeader_headerlength_set
    __swig_getmethods__["headerlength"] = _openbabel.FptIndexHeader_headerlength_get
    if _newclass:headerlength = _swig_property(_openbabel.FptIndexHeader_headerlength_get, _openbabel.FptIndexHeader_headerlength_set)
    __swig_setmethods__["nEntries"] = _openbabel.FptIndexHeader_nEntries_set
    __swig_getmethods__["nEntries"] = _openbabel.FptIndexHeader_nEntries_get
    if _newclass:nEntries = _swig_property(_openbabel.FptIndexHeader_nEntries_get, _openbabel.FptIndexHeader_nEntries_set)
    __swig_setmethods__["words"] = _openbabel.FptIndexHeader_words_set
    __swig_getmethods__["words"] = _openbabel.FptIndexHeader_words_get
    if _newclass:words = _swig_property(_openbabel.FptIndexHeader_words_get, _openbabel.FptIndexHeader_words_set)
    __swig_setmethods__["fpid"] = _openbabel.FptIndexHeader_fpid_set
    __swig_getmethods__["fpid"] = _openbabel.FptIndexHeader_fpid_get
    if _newclass:fpid = _swig_property(_openbabel.FptIndexHeader_fpid_get, _openbabel.FptIndexHeader_fpid_set)
    __swig_setmethods__["datafilename"] = _openbabel.FptIndexHeader_datafilename_set
    __swig_getmethods__["datafilename"] = _openbabel.FptIndexHeader_datafilename_get
    if _newclass:datafilename = _swig_property(_openbabel.FptIndexHeader_datafilename_get, _openbabel.FptIndexHeader_datafilename_set)
    def __init__(self, *args): 
        this = _openbabel.new_FptIndexHeader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_FptIndexHeader
    __del__ = lambda self : None;
FptIndexHeader_swigregister = _openbabel.FptIndexHeader_swigregister
FptIndexHeader_swigregister(FptIndexHeader)

class FptIndex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FptIndex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FptIndex, name)
    __repr__ = _swig_repr
    __swig_setmethods__["header"] = _openbabel.FptIndex_header_set
    __swig_getmethods__["header"] = _openbabel.FptIndex_header_get
    if _newclass:header = _swig_property(_openbabel.FptIndex_header_get, _openbabel.FptIndex_header_set)
    __swig_setmethods__["fptdata"] = _openbabel.FptIndex_fptdata_set
    __swig_getmethods__["fptdata"] = _openbabel.FptIndex_fptdata_get
    if _newclass:fptdata = _swig_property(_openbabel.FptIndex_fptdata_get, _openbabel.FptIndex_fptdata_set)
    __swig_setmethods__["seekdata"] = _openbabel.FptIndex_seekdata_set
    __swig_getmethods__["seekdata"] = _openbabel.FptIndex_seekdata_get
    if _newclass:seekdata = _swig_property(_openbabel.FptIndex_seekdata_get, _openbabel.FptIndex_seekdata_set)
    def Read(*args): return _openbabel.FptIndex_Read(*args)
    def CheckFP(*args): return _openbabel.FptIndex_CheckFP(*args)
    def __init__(self, *args): 
        this = _openbabel.new_FptIndex(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_FptIndex
    __del__ = lambda self : None;
FptIndex_swigregister = _openbabel.FptIndex_swigregister
FptIndex_swigregister(FptIndex)

class FastSearch(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FastSearch, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FastSearch, name)
    __repr__ = _swig_repr
    def ReadIndexFile(*args): return _openbabel.FastSearch_ReadIndexFile(*args)
    def ReadIndex(*args): return _openbabel.FastSearch_ReadIndex(*args)
    __swig_destroy__ = _openbabel.delete_FastSearch
    __del__ = lambda self : None;
    def Find(*args): return _openbabel.FastSearch_Find(*args)
    def FindMatch(*args): return _openbabel.FastSearch_FindMatch(*args)
    def FindSimilar(*args): return _openbabel.FastSearch_FindSimilar(*args)
    def GetFingerprint(*args): return _openbabel.FastSearch_GetFingerprint(*args)
    def GetIndexHeader(*args): return _openbabel.FastSearch_GetIndexHeader(*args)
    def __init__(self, *args): 
        this = _openbabel.new_FastSearch(*args)
        try: self.this.append(this)
        except: self.this = this
FastSearch_swigregister = _openbabel.FastSearch_swigregister
FastSearch_swigregister(FastSearch)

class FastSearchIndexer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FastSearchIndexer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FastSearchIndexer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_FastSearchIndexer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_FastSearchIndexer
    __del__ = lambda self : None;
    def Add(*args): return _openbabel.FastSearchIndexer_Add(*args)
FastSearchIndexer_swigregister = _openbabel.FastSearchIndexer_swigregister
FastSearchIndexer_swigregister(FastSearchIndexer)

class OBDescriptor(OBPlugin):
    __swig_setmethods__ = {}
    for _s in [OBPlugin]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBDescriptor, name, value)
    __swig_getmethods__ = {}
    for _s in [OBPlugin]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBDescriptor, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["Default"] = lambda x: _openbabel.OBDescriptor_Default
    if _newclass:Default = staticmethod(_openbabel.OBDescriptor_Default)
    __swig_getmethods__["FindType"] = lambda x: _openbabel.OBDescriptor_FindType
    if _newclass:FindType = staticmethod(_openbabel.OBDescriptor_FindType)
    def TypeID(*args): return _openbabel.OBDescriptor_TypeID(*args)
    def Predict(*args): return _openbabel.OBDescriptor_Predict(*args)
    def PredictAndSave(*args): return _openbabel.OBDescriptor_PredictAndSave(*args)
    def GetStringValue(*args): return _openbabel.OBDescriptor_GetStringValue(*args)
    def Compare(*args): return _openbabel.OBDescriptor_Compare(*args)
    def Display(*args): return _openbabel.OBDescriptor_Display(*args)
    __swig_getmethods__["FilterCompare"] = lambda x: _openbabel.OBDescriptor_FilterCompare
    if _newclass:FilterCompare = staticmethod(_openbabel.OBDescriptor_FilterCompare)
    __swig_getmethods__["AddProperties"] = lambda x: _openbabel.OBDescriptor_AddProperties
    if _newclass:AddProperties = staticmethod(_openbabel.OBDescriptor_AddProperties)
    __swig_getmethods__["DeleteProperties"] = lambda x: _openbabel.OBDescriptor_DeleteProperties
    if _newclass:DeleteProperties = staticmethod(_openbabel.OBDescriptor_DeleteProperties)
    __swig_getmethods__["GetValues"] = lambda x: _openbabel.OBDescriptor_GetValues
    if _newclass:GetValues = staticmethod(_openbabel.OBDescriptor_GetValues)
    __swig_destroy__ = _openbabel.delete_OBDescriptor
    __del__ = lambda self : None;
OBDescriptor_swigregister = _openbabel.OBDescriptor_swigregister
OBDescriptor_swigregister(OBDescriptor)
OBDescriptor_Default = _openbabel.OBDescriptor_Default
OBDescriptor_FindType = _openbabel.OBDescriptor_FindType
OBDescriptor_FilterCompare = _openbabel.OBDescriptor_FilterCompare
OBDescriptor_AddProperties = _openbabel.OBDescriptor_AddProperties
OBDescriptor_DeleteProperties = _openbabel.OBDescriptor_DeleteProperties
OBDescriptor_GetValues = _openbabel.OBDescriptor_GetValues

OBFF_LOGLVL_NONE = _openbabel.OBFF_LOGLVL_NONE
OBFF_LOGLVL_LOW = _openbabel.OBFF_LOGLVL_LOW
OBFF_LOGLVL_MEDIUM = _openbabel.OBFF_LOGLVL_MEDIUM
OBFF_LOGLVL_HIGH = _openbabel.OBFF_LOGLVL_HIGH
OBFF_ENERGY = _openbabel.OBFF_ENERGY
OBFF_EBOND = _openbabel.OBFF_EBOND
OBFF_EANGLE = _openbabel.OBFF_EANGLE
OBFF_ESTRBND = _openbabel.OBFF_ESTRBND
OBFF_ETORSION = _openbabel.OBFF_ETORSION
OBFF_EOOP = _openbabel.OBFF_EOOP
OBFF_EVDW = _openbabel.OBFF_EVDW
OBFF_EELECTROSTATIC = _openbabel.OBFF_EELECTROSTATIC
OBFF_CONST_IGNORE = _openbabel.OBFF_CONST_IGNORE
OBFF_CONST_ATOM = _openbabel.OBFF_CONST_ATOM
OBFF_CONST_ATOM_X = _openbabel.OBFF_CONST_ATOM_X
OBFF_CONST_ATOM_Y = _openbabel.OBFF_CONST_ATOM_Y
OBFF_CONST_ATOM_Z = _openbabel.OBFF_CONST_ATOM_Z
OBFF_CONST_DISTANCE = _openbabel.OBFF_CONST_DISTANCE
OBFF_CONST_ANGLE = _openbabel.OBFF_CONST_ANGLE
OBFF_CONST_TORSION = _openbabel.OBFF_CONST_TORSION
OBFF_NUMERICAL_GRADIENT = _openbabel.OBFF_NUMERICAL_GRADIENT
OBFF_ANALYTICAL_GRADIENT = _openbabel.OBFF_ANALYTICAL_GRADIENT
KCAL_TO_KJ = _openbabel.KCAL_TO_KJ
class OBFFParameter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFFParameter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBFFParameter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["a"] = _openbabel.OBFFParameter_a_set
    __swig_getmethods__["a"] = _openbabel.OBFFParameter_a_get
    if _newclass:a = _swig_property(_openbabel.OBFFParameter_a_get, _openbabel.OBFFParameter_a_set)
    __swig_setmethods__["b"] = _openbabel.OBFFParameter_b_set
    __swig_getmethods__["b"] = _openbabel.OBFFParameter_b_get
    if _newclass:b = _swig_property(_openbabel.OBFFParameter_b_get, _openbabel.OBFFParameter_b_set)
    __swig_setmethods__["c"] = _openbabel.OBFFParameter_c_set
    __swig_getmethods__["c"] = _openbabel.OBFFParameter_c_get
    if _newclass:c = _swig_property(_openbabel.OBFFParameter_c_get, _openbabel.OBFFParameter_c_set)
    __swig_setmethods__["d"] = _openbabel.OBFFParameter_d_set
    __swig_getmethods__["d"] = _openbabel.OBFFParameter_d_get
    if _newclass:d = _swig_property(_openbabel.OBFFParameter_d_get, _openbabel.OBFFParameter_d_set)
    __swig_setmethods__["_a"] = _openbabel.OBFFParameter__a_set
    __swig_getmethods__["_a"] = _openbabel.OBFFParameter__a_get
    if _newclass:_a = _swig_property(_openbabel.OBFFParameter__a_get, _openbabel.OBFFParameter__a_set)
    __swig_setmethods__["_b"] = _openbabel.OBFFParameter__b_set
    __swig_getmethods__["_b"] = _openbabel.OBFFParameter__b_get
    if _newclass:_b = _swig_property(_openbabel.OBFFParameter__b_get, _openbabel.OBFFParameter__b_set)
    __swig_setmethods__["_c"] = _openbabel.OBFFParameter__c_set
    __swig_getmethods__["_c"] = _openbabel.OBFFParameter__c_get
    if _newclass:_c = _swig_property(_openbabel.OBFFParameter__c_get, _openbabel.OBFFParameter__c_set)
    __swig_setmethods__["_d"] = _openbabel.OBFFParameter__d_set
    __swig_getmethods__["_d"] = _openbabel.OBFFParameter__d_get
    if _newclass:_d = _swig_property(_openbabel.OBFFParameter__d_get, _openbabel.OBFFParameter__d_set)
    __swig_setmethods__["_ipar"] = _openbabel.OBFFParameter__ipar_set
    __swig_getmethods__["_ipar"] = _openbabel.OBFFParameter__ipar_get
    if _newclass:_ipar = _swig_property(_openbabel.OBFFParameter__ipar_get, _openbabel.OBFFParameter__ipar_set)
    __swig_setmethods__["_dpar"] = _openbabel.OBFFParameter__dpar_set
    __swig_getmethods__["_dpar"] = _openbabel.OBFFParameter__dpar_get
    if _newclass:_dpar = _swig_property(_openbabel.OBFFParameter__dpar_get, _openbabel.OBFFParameter__dpar_set)
    def clear(*args): return _openbabel.OBFFParameter_clear(*args)
    def __init__(self, *args): 
        this = _openbabel.new_OBFFParameter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBFFParameter
    __del__ = lambda self : None;
OBFFParameter_swigregister = _openbabel.OBFFParameter_swigregister
OBFFParameter_swigregister(OBFFParameter)

class OBFFCalculation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFFCalculation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBFFCalculation, name)
    __repr__ = _swig_repr
    __swig_setmethods__["energy"] = _openbabel.OBFFCalculation_energy_set
    __swig_getmethods__["energy"] = _openbabel.OBFFCalculation_energy_get
    if _newclass:energy = _swig_property(_openbabel.OBFFCalculation_energy_get, _openbabel.OBFFCalculation_energy_set)
    __swig_setmethods__["grada"] = _openbabel.OBFFCalculation_grada_set
    __swig_getmethods__["grada"] = _openbabel.OBFFCalculation_grada_get
    if _newclass:grada = _swig_property(_openbabel.OBFFCalculation_grada_get, _openbabel.OBFFCalculation_grada_set)
    __swig_setmethods__["gradb"] = _openbabel.OBFFCalculation_gradb_set
    __swig_getmethods__["gradb"] = _openbabel.OBFFCalculation_gradb_get
    if _newclass:gradb = _swig_property(_openbabel.OBFFCalculation_gradb_get, _openbabel.OBFFCalculation_gradb_set)
    __swig_setmethods__["gradc"] = _openbabel.OBFFCalculation_gradc_set
    __swig_getmethods__["gradc"] = _openbabel.OBFFCalculation_gradc_get
    if _newclass:gradc = _swig_property(_openbabel.OBFFCalculation_gradc_get, _openbabel.OBFFCalculation_gradc_set)
    __swig_setmethods__["gradd"] = _openbabel.OBFFCalculation_gradd_set
    __swig_getmethods__["gradd"] = _openbabel.OBFFCalculation_gradd_get
    if _newclass:gradd = _swig_property(_openbabel.OBFFCalculation_gradd_get, _openbabel.OBFFCalculation_gradd_set)
    __swig_setmethods__["a"] = _openbabel.OBFFCalculation_a_set
    __swig_getmethods__["a"] = _openbabel.OBFFCalculation_a_get
    if _newclass:a = _swig_property(_openbabel.OBFFCalculation_a_get, _openbabel.OBFFCalculation_a_set)
    __swig_setmethods__["b"] = _openbabel.OBFFCalculation_b_set
    __swig_getmethods__["b"] = _openbabel.OBFFCalculation_b_get
    if _newclass:b = _swig_property(_openbabel.OBFFCalculation_b_get, _openbabel.OBFFCalculation_b_set)
    __swig_setmethods__["c"] = _openbabel.OBFFCalculation_c_set
    __swig_getmethods__["c"] = _openbabel.OBFFCalculation_c_get
    if _newclass:c = _swig_property(_openbabel.OBFFCalculation_c_get, _openbabel.OBFFCalculation_c_set)
    __swig_setmethods__["d"] = _openbabel.OBFFCalculation_d_set
    __swig_getmethods__["d"] = _openbabel.OBFFCalculation_d_get
    if _newclass:d = _swig_property(_openbabel.OBFFCalculation_d_get, _openbabel.OBFFCalculation_d_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBFFCalculation(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBFFCalculation
    __del__ = lambda self : None;
    def Compute(*args): return _openbabel.OBFFCalculation_Compute(*args)
    def GetEnergy(*args): return _openbabel.OBFFCalculation_GetEnergy(*args)
    def GetGradient(*args): return _openbabel.OBFFCalculation_GetGradient(*args)
OBFFCalculation_swigregister = _openbabel.OBFFCalculation_swigregister
OBFFCalculation_swigregister(OBFFCalculation)

class OBFFConstraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFFConstraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBFFConstraint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["factor"] = _openbabel.OBFFConstraint_factor_set
    __swig_getmethods__["factor"] = _openbabel.OBFFConstraint_factor_get
    if _newclass:factor = _swig_property(_openbabel.OBFFConstraint_factor_get, _openbabel.OBFFConstraint_factor_set)
    __swig_setmethods__["constraint_value"] = _openbabel.OBFFConstraint_constraint_value_set
    __swig_getmethods__["constraint_value"] = _openbabel.OBFFConstraint_constraint_value_get
    if _newclass:constraint_value = _swig_property(_openbabel.OBFFConstraint_constraint_value_get, _openbabel.OBFFConstraint_constraint_value_set)
    __swig_setmethods__["rab0"] = _openbabel.OBFFConstraint_rab0_set
    __swig_getmethods__["rab0"] = _openbabel.OBFFConstraint_rab0_get
    if _newclass:rab0 = _swig_property(_openbabel.OBFFConstraint_rab0_get, _openbabel.OBFFConstraint_rab0_set)
    __swig_setmethods__["rbc0"] = _openbabel.OBFFConstraint_rbc0_set
    __swig_getmethods__["rbc0"] = _openbabel.OBFFConstraint_rbc0_get
    if _newclass:rbc0 = _swig_property(_openbabel.OBFFConstraint_rbc0_get, _openbabel.OBFFConstraint_rbc0_set)
    __swig_setmethods__["type"] = _openbabel.OBFFConstraint_type_set
    __swig_getmethods__["type"] = _openbabel.OBFFConstraint_type_get
    if _newclass:type = _swig_property(_openbabel.OBFFConstraint_type_get, _openbabel.OBFFConstraint_type_set)
    __swig_setmethods__["ia"] = _openbabel.OBFFConstraint_ia_set
    __swig_getmethods__["ia"] = _openbabel.OBFFConstraint_ia_get
    if _newclass:ia = _swig_property(_openbabel.OBFFConstraint_ia_get, _openbabel.OBFFConstraint_ia_set)
    __swig_setmethods__["ib"] = _openbabel.OBFFConstraint_ib_set
    __swig_getmethods__["ib"] = _openbabel.OBFFConstraint_ib_get
    if _newclass:ib = _swig_property(_openbabel.OBFFConstraint_ib_get, _openbabel.OBFFConstraint_ib_set)
    __swig_setmethods__["ic"] = _openbabel.OBFFConstraint_ic_set
    __swig_getmethods__["ic"] = _openbabel.OBFFConstraint_ic_get
    if _newclass:ic = _swig_property(_openbabel.OBFFConstraint_ic_get, _openbabel.OBFFConstraint_ic_set)
    __swig_setmethods__["id"] = _openbabel.OBFFConstraint_id_set
    __swig_getmethods__["id"] = _openbabel.OBFFConstraint_id_get
    if _newclass:id = _swig_property(_openbabel.OBFFConstraint_id_get, _openbabel.OBFFConstraint_id_set)
    __swig_setmethods__["a"] = _openbabel.OBFFConstraint_a_set
    __swig_getmethods__["a"] = _openbabel.OBFFConstraint_a_get
    if _newclass:a = _swig_property(_openbabel.OBFFConstraint_a_get, _openbabel.OBFFConstraint_a_set)
    __swig_setmethods__["b"] = _openbabel.OBFFConstraint_b_set
    __swig_getmethods__["b"] = _openbabel.OBFFConstraint_b_get
    if _newclass:b = _swig_property(_openbabel.OBFFConstraint_b_get, _openbabel.OBFFConstraint_b_set)
    __swig_setmethods__["c"] = _openbabel.OBFFConstraint_c_set
    __swig_getmethods__["c"] = _openbabel.OBFFConstraint_c_get
    if _newclass:c = _swig_property(_openbabel.OBFFConstraint_c_get, _openbabel.OBFFConstraint_c_set)
    __swig_setmethods__["d"] = _openbabel.OBFFConstraint_d_set
    __swig_getmethods__["d"] = _openbabel.OBFFConstraint_d_get
    if _newclass:d = _swig_property(_openbabel.OBFFConstraint_d_get, _openbabel.OBFFConstraint_d_set)
    __swig_setmethods__["grada"] = _openbabel.OBFFConstraint_grada_set
    __swig_getmethods__["grada"] = _openbabel.OBFFConstraint_grada_get
    if _newclass:grada = _swig_property(_openbabel.OBFFConstraint_grada_get, _openbabel.OBFFConstraint_grada_set)
    __swig_setmethods__["gradb"] = _openbabel.OBFFConstraint_gradb_set
    __swig_getmethods__["gradb"] = _openbabel.OBFFConstraint_gradb_get
    if _newclass:gradb = _swig_property(_openbabel.OBFFConstraint_gradb_get, _openbabel.OBFFConstraint_gradb_set)
    __swig_setmethods__["gradc"] = _openbabel.OBFFConstraint_gradc_set
    __swig_getmethods__["gradc"] = _openbabel.OBFFConstraint_gradc_get
    if _newclass:gradc = _swig_property(_openbabel.OBFFConstraint_gradc_get, _openbabel.OBFFConstraint_gradc_set)
    __swig_setmethods__["gradd"] = _openbabel.OBFFConstraint_gradd_set
    __swig_getmethods__["gradd"] = _openbabel.OBFFConstraint_gradd_get
    if _newclass:gradd = _swig_property(_openbabel.OBFFConstraint_gradd_get, _openbabel.OBFFConstraint_gradd_set)
    def __init__(self, *args): 
        this = _openbabel.new_OBFFConstraint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBFFConstraint
    __del__ = lambda self : None;
    def GetGradient(*args): return _openbabel.OBFFConstraint_GetGradient(*args)
OBFFConstraint_swigregister = _openbabel.OBFFConstraint_swigregister
OBFFConstraint_swigregister(OBFFConstraint)

class OBFFConstraints(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBFFConstraints, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OBFFConstraints, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_OBFFConstraints(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_OBFFConstraints
    __del__ = lambda self : None;
    def Clear(*args): return _openbabel.OBFFConstraints_Clear(*args)
    def GetConstraintEnergy(*args): return _openbabel.OBFFConstraints_GetConstraintEnergy(*args)
    def GetGradient(*args): return _openbabel.OBFFConstraints_GetGradient(*args)
    def Setup(*args): return _openbabel.OBFFConstraints_Setup(*args)
    def SetFactor(*args): return _openbabel.OBFFConstraints_SetFactor(*args)
    def AddIgnore(*args): return _openbabel.OBFFConstraints_AddIgnore(*args)
    def AddAtomConstraint(*args): return _openbabel.OBFFConstraints_AddAtomConstraint(*args)
    def AddAtomXConstraint(*args): return _openbabel.OBFFConstraints_AddAtomXConstraint(*args)
    def AddAtomYConstraint(*args): return _openbabel.OBFFConstraints_AddAtomYConstraint(*args)
    def AddAtomZConstraint(*args): return _openbabel.OBFFConstraints_AddAtomZConstraint(*args)
    def AddDistanceConstraint(*args): return _openbabel.OBFFConstraints_AddDistanceConstraint(*args)
    def AddAngleConstraint(*args): return _openbabel.OBFFConstraints_AddAngleConstraint(*args)
    def AddTorsionConstraint(*args): return _openbabel.OBFFConstraints_AddTorsionConstraint(*args)
    def DeleteConstraint(*args): return _openbabel.OBFFConstraints_DeleteConstraint(*args)
    def GetFactor(*args): return _openbabel.OBFFConstraints_GetFactor(*args)
    def Size(*args): return _openbabel.OBFFConstraints_Size(*args)
    def GetConstraintType(*args): return _openbabel.OBFFConstraints_GetConstraintType(*args)
    def GetConstraintValue(*args): return _openbabel.OBFFConstraints_GetConstraintValue(*args)
    def GetConstraintAtomA(*args): return _openbabel.OBFFConstraints_GetConstraintAtomA(*args)
    def GetConstraintAtomB(*args): return _openbabel.OBFFConstraints_GetConstraintAtomB(*args)
    def GetConstraintAtomC(*args): return _openbabel.OBFFConstraints_GetConstraintAtomC(*args)
    def GetConstraintAtomD(*args): return _openbabel.OBFFConstraints_GetConstraintAtomD(*args)
    def IsIgnored(*args): return _openbabel.OBFFConstraints_IsIgnored(*args)
    def IsFixed(*args): return _openbabel.OBFFConstraints_IsFixed(*args)
    def IsXFixed(*args): return _openbabel.OBFFConstraints_IsXFixed(*args)
    def IsYFixed(*args): return _openbabel.OBFFConstraints_IsYFixed(*args)
    def IsZFixed(*args): return _openbabel.OBFFConstraints_IsZFixed(*args)
OBFFConstraints_swigregister = _openbabel.OBFFConstraints_swigregister
OBFFConstraints_swigregister(OBFFConstraints)

class OBForceField(OBPlugin):
    __swig_setmethods__ = {}
    for _s in [OBPlugin]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBForceField, name, value)
    __swig_getmethods__ = {}
    for _s in [OBPlugin]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBForceField, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["Default"] = lambda x: _openbabel.OBForceField_Default
    if _newclass:Default = staticmethod(_openbabel.OBForceField_Default)
    __swig_getmethods__["FindType"] = lambda x: _openbabel.OBForceField_FindType
    if _newclass:FindType = staticmethod(_openbabel.OBForceField_FindType)
    def MakeNewInstance(*args): return _openbabel.OBForceField_MakeNewInstance(*args)
    __swig_destroy__ = _openbabel.delete_OBForceField
    __del__ = lambda self : None;
    def TypeID(*args): return _openbabel.OBForceField_TypeID(*args)
    __swig_getmethods__["FindForceField"] = lambda x: _openbabel.OBForceField_FindForceField
    if _newclass:FindForceField = staticmethod(_openbabel.OBForceField_FindForceField)
    def GetUnit(*args): return _openbabel.OBForceField_GetUnit(*args)
    def HasAnalyticalGradients(*args): return _openbabel.OBForceField_HasAnalyticalGradients(*args)
    def Setup(*args): return _openbabel.OBForceField_Setup(*args)
    def ParseParamFile(*args): return _openbabel.OBForceField_ParseParamFile(*args)
    def SetTypes(*args): return _openbabel.OBForceField_SetTypes(*args)
    def SetFormalCharges(*args): return _openbabel.OBForceField_SetFormalCharges(*args)
    def SetPartialCharges(*args): return _openbabel.OBForceField_SetPartialCharges(*args)
    def SetupCalculations(*args): return _openbabel.OBForceField_SetupCalculations(*args)
    def IsSetupNeeded(*args): return _openbabel.OBForceField_IsSetupNeeded(*args)
    def GetCoordinates(*args): return _openbabel.OBForceField_GetCoordinates(*args)
    def UpdateCoordinates(*args): return _openbabel.OBForceField_UpdateCoordinates(*args)
    def GetConformers(*args): return _openbabel.OBForceField_GetConformers(*args)
    def UpdateConformers(*args): return _openbabel.OBForceField_UpdateConformers(*args)
    def SetCoordinates(*args): return _openbabel.OBForceField_SetCoordinates(*args)
    def SetConformers(*args): return _openbabel.OBForceField_SetConformers(*args)
    def Energy(*args): return _openbabel.OBForceField_Energy(*args)
    def E_Bond(*args): return _openbabel.OBForceField_E_Bond(*args)
    def E_Angle(*args): return _openbabel.OBForceField_E_Angle(*args)
    def E_StrBnd(*args): return _openbabel.OBForceField_E_StrBnd(*args)
    def E_Torsion(*args): return _openbabel.OBForceField_E_Torsion(*args)
    def E_OOP(*args): return _openbabel.OBForceField_E_OOP(*args)
    def E_VDW(*args): return _openbabel.OBForceField_E_VDW(*args)
    def E_Electrostatic(*args): return _openbabel.OBForceField_E_Electrostatic(*args)
    def PrintTypes(*args): return _openbabel.OBForceField_PrintTypes(*args)
    def PrintFormalCharges(*args): return _openbabel.OBForceField_PrintFormalCharges(*args)
    def PrintPartialCharges(*args): return _openbabel.OBForceField_PrintPartialCharges(*args)
    def PrintVelocities(*args): return _openbabel.OBForceField_PrintVelocities(*args)
    def SetLogFile(*args): return _openbabel.OBForceField_SetLogFile(*args)
    def SetLogLevel(*args): return _openbabel.OBForceField_SetLogLevel(*args)
    def GetLogLevel(*args): return _openbabel.OBForceField_GetLogLevel(*args)
    def OBFFLog(*args): return _openbabel.OBForceField_OBFFLog(*args)
    def DistanceGeometry(*args): return _openbabel.OBForceField_DistanceGeometry(*args)
    def SystematicRotorSearch(*args): return _openbabel.OBForceField_SystematicRotorSearch(*args)
    def SystematicRotorSearchInitialize(*args): return _openbabel.OBForceField_SystematicRotorSearchInitialize(*args)
    def SystematicRotorSearchNextConformer(*args): return _openbabel.OBForceField_SystematicRotorSearchNextConformer(*args)
    def RandomRotorSearch(*args): return _openbabel.OBForceField_RandomRotorSearch(*args)
    def RandomRotorSearchInitialize(*args): return _openbabel.OBForceField_RandomRotorSearchInitialize(*args)
    def RandomRotorSearchNextConformer(*args): return _openbabel.OBForceField_RandomRotorSearchNextConformer(*args)
    def WeightedRotorSearch(*args): return _openbabel.OBForceField_WeightedRotorSearch(*args)
    def LineSearch(*args): return _openbabel.OBForceField_LineSearch(*args)
    def SteepestDescent(*args): return _openbabel.OBForceField_SteepestDescent(*args)
    def SteepestDescentInitialize(*args): return _openbabel.OBForceField_SteepestDescentInitialize(*args)
    def SteepestDescentTakeNSteps(*args): return _openbabel.OBForceField_SteepestDescentTakeNSteps(*args)
    def ConjugateGradients(*args): return _openbabel.OBForceField_ConjugateGradients(*args)
    def ConjugateGradientsInitialize(*args): return _openbabel.OBForceField_ConjugateGradientsInitialize(*args)
    def ConjugateGradientsTakeNSteps(*args): return _openbabel.OBForceField_ConjugateGradientsTakeNSteps(*args)
    def GenerateVelocities(*args): return _openbabel.OBForceField_GenerateVelocities(*args)
    def CorrectVelocities(*args): return _openbabel.OBForceField_CorrectVelocities(*args)
    def MolecularDynamicsTakeNSteps(*args): return _openbabel.OBForceField_MolecularDynamicsTakeNSteps(*args)
    def GetConstraints(*args): return _openbabel.OBForceField_GetConstraints(*args)
    def SetConstraints(*args): return _openbabel.OBForceField_SetConstraints(*args)
    def DetectExplosion(*args): return _openbabel.OBForceField_DetectExplosion(*args)
    def ValidateLineSearch(*args): return _openbabel.OBForceField_ValidateLineSearch(*args)
    def ValidateSteepestDescent(*args): return _openbabel.OBForceField_ValidateSteepestDescent(*args)
    def ValidateConjugateGradients(*args): return _openbabel.OBForceField_ValidateConjugateGradients(*args)
    def Validate(*args): return _openbabel.OBForceField_Validate(*args)
    def ValidateGradients(*args): return _openbabel.OBForceField_ValidateGradients(*args)
    def ValidateGradientError(*args): return _openbabel.OBForceField_ValidateGradientError(*args)
    __swig_getmethods__["VectorLengthDerivative"] = lambda x: _openbabel.OBForceField_VectorLengthDerivative
    if _newclass:VectorLengthDerivative = staticmethod(_openbabel.OBForceField_VectorLengthDerivative)
    __swig_getmethods__["VectorAngleDerivative"] = lambda x: _openbabel.OBForceField_VectorAngleDerivative
    if _newclass:VectorAngleDerivative = staticmethod(_openbabel.OBForceField_VectorAngleDerivative)
    __swig_getmethods__["VectorOOPDerivative"] = lambda x: _openbabel.OBForceField_VectorOOPDerivative
    if _newclass:VectorOOPDerivative = staticmethod(_openbabel.OBForceField_VectorOOPDerivative)
    __swig_getmethods__["VectorTorsionDerivative"] = lambda x: _openbabel.OBForceField_VectorTorsionDerivative
    if _newclass:VectorTorsionDerivative = staticmethod(_openbabel.OBForceField_VectorTorsionDerivative)
OBForceField_swigregister = _openbabel.OBForceField_swigregister
OBForceField_swigregister(OBForceField)
OBForceField_Default = _openbabel.OBForceField_Default
OBForceField_FindType = _openbabel.OBForceField_FindType
OBForceField_FindForceField = _openbabel.OBForceField_FindForceField
OBForceField_VectorLengthDerivative = _openbabel.OBForceField_VectorLengthDerivative
OBForceField_VectorAngleDerivative = _openbabel.OBForceField_VectorAngleDerivative
OBForceField_VectorOOPDerivative = _openbabel.OBForceField_VectorOOPDerivative
OBForceField_VectorTorsionDerivative = _openbabel.OBForceField_VectorTorsionDerivative

class OBOp(OBPlugin):
    __swig_setmethods__ = {}
    for _s in [OBPlugin]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OBOp, name, value)
    __swig_getmethods__ = {}
    for _s in [OBPlugin]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OBOp, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["Default"] = lambda x: _openbabel.OBOp_Default
    if _newclass:Default = staticmethod(_openbabel.OBOp_Default)
    __swig_getmethods__["FindType"] = lambda x: _openbabel.OBOp_FindType
    if _newclass:FindType = staticmethod(_openbabel.OBOp_FindType)
    def TypeID(*args): return _openbabel.OBOp_TypeID(*args)
    def Do(*args): return _openbabel.OBOp_Do(*args)
    def WorksWith(*args): return _openbabel.OBOp_WorksWith(*args)
    __swig_getmethods__["OpOptions"] = lambda x: _openbabel.OBOp_OpOptions
    if _newclass:OpOptions = staticmethod(_openbabel.OBOp_OpOptions)
    __swig_getmethods__["DoOps"] = lambda x: _openbabel.OBOp_DoOps
    if _newclass:DoOps = staticmethod(_openbabel.OBOp_DoOps)
    __swig_destroy__ = _openbabel.delete_OBOp
    __del__ = lambda self : None;
OBOp_swigregister = _openbabel.OBOp_swigregister
OBOp_swigregister(OBOp)
OBOp_Default = _openbabel.OBOp_Default
OBOp_FindType = _openbabel.OBOp_FindType
OBOp_OpOptions = _openbabel.OBOp_OpOptions
OBOp_DoOps = _openbabel.OBOp_DoOps

class _OBMolAtomIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolAtomIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolAtomIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolAtomIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolAtomIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolAtomIter_good(*args)
    def inc(*args): return _openbabel._OBMolAtomIter_inc(*args)
    def deref(*args): return _openbabel._OBMolAtomIter_deref(*args)
    def __ref__(*args): return _openbabel._OBMolAtomIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBMolAtomIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBMolAtomIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBMolAtomIter_Visit_get, _openbabel._OBMolAtomIter_Visit_set)
    def Clear(*args): return _openbabel._OBMolAtomIter_Clear(*args)
    def SetIdx(*args): return _openbabel._OBMolAtomIter_SetIdx(*args)
    def SetHyb(*args): return _openbabel._OBMolAtomIter_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel._OBMolAtomIter_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel._OBMolAtomIter_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel._OBMolAtomIter_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel._OBMolAtomIter_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel._OBMolAtomIter_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel._OBMolAtomIter_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel._OBMolAtomIter_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel._OBMolAtomIter_SetType(*args)
    def SetPartialCharge(*args): return _openbabel._OBMolAtomIter_SetPartialCharge(*args)
    def SetVector(*args): return _openbabel._OBMolAtomIter_SetVector(*args)
    def SetCoordPtr(*args): return _openbabel._OBMolAtomIter_SetCoordPtr(*args)
    def SetResidue(*args): return _openbabel._OBMolAtomIter_SetResidue(*args)
    def SetParent(*args): return _openbabel._OBMolAtomIter_SetParent(*args)
    def SetAromatic(*args): return _openbabel._OBMolAtomIter_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel._OBMolAtomIter_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel._OBMolAtomIter_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel._OBMolAtomIter_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel._OBMolAtomIter_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel._OBMolAtomIter_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel._OBMolAtomIter_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel._OBMolAtomIter_SetInRing(*args)
    def SetChiral(*args): return _openbabel._OBMolAtomIter_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel._OBMolAtomIter_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel._OBMolAtomIter_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel._OBMolAtomIter_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel._OBMolAtomIter_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel._OBMolAtomIter_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel._OBMolAtomIter_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel._OBMolAtomIter_GetExactMass(*args)
    def GetIdx(*args): return _openbabel._OBMolAtomIter_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel._OBMolAtomIter_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel._OBMolAtomIter_GetCIdx(*args)
    def GetValence(*args): return _openbabel._OBMolAtomIter_GetValence(*args)
    def GetHyb(*args): return _openbabel._OBMolAtomIter_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel._OBMolAtomIter_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel._OBMolAtomIter_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel._OBMolAtomIter_GetHeteroValence(*args)
    def GetType(*args): return _openbabel._OBMolAtomIter_GetType(*args)
    def GetX(*args): return _openbabel._OBMolAtomIter_GetX(*args)
    def GetY(*args): return _openbabel._OBMolAtomIter_GetY(*args)
    def GetZ(*args): return _openbabel._OBMolAtomIter_GetZ(*args)
    def x(*args): return _openbabel._OBMolAtomIter_x(*args)
    def y(*args): return _openbabel._OBMolAtomIter_y(*args)
    def z(*args): return _openbabel._OBMolAtomIter_z(*args)
    def GetCoordinate(*args): return _openbabel._OBMolAtomIter_GetCoordinate(*args)
    def GetVector(*args): return _openbabel._OBMolAtomIter_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel._OBMolAtomIter_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel._OBMolAtomIter_GetResidue(*args)
    def GetParent(*args): return _openbabel._OBMolAtomIter_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel._OBMolAtomIter_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel._OBMolAtomIter_GetBond(*args)
    def GetNextAtom(*args): return _openbabel._OBMolAtomIter_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel._OBMolAtomIter_BeginBonds(*args)
    def EndBonds(*args): return _openbabel._OBMolAtomIter_EndBonds(*args)
    def BeginBond(*args): return _openbabel._OBMolAtomIter_BeginBond(*args)
    def NextBond(*args): return _openbabel._OBMolAtomIter_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel._OBMolAtomIter_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel._OBMolAtomIter_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel._OBMolAtomIter_GetDistance(*args)
    def GetAngle(*args): return _openbabel._OBMolAtomIter_GetAngle(*args)
    def NewResidue(*args): return _openbabel._OBMolAtomIter_NewResidue(*args)
    def AddResidue(*args): return _openbabel._OBMolAtomIter_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel._OBMolAtomIter_DeleteResidue(*args)
    def AddBond(*args): return _openbabel._OBMolAtomIter_AddBond(*args)
    def InsertBond(*args): return _openbabel._OBMolAtomIter_InsertBond(*args)
    def DeleteBond(*args): return _openbabel._OBMolAtomIter_DeleteBond(*args)
    def ClearBond(*args): return _openbabel._OBMolAtomIter_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel._OBMolAtomIter_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel._OBMolAtomIter_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel._OBMolAtomIter_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel._OBMolAtomIter_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel._OBMolAtomIter_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel._OBMolAtomIter_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel._OBMolAtomIter_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel._OBMolAtomIter_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel._OBMolAtomIter_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel._OBMolAtomIter_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel._OBMolAtomIter_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel._OBMolAtomIter_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel._OBMolAtomIter_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel._OBMolAtomIter_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel._OBMolAtomIter_BOSum(*args)
    def KBOSum(*args): return _openbabel._OBMolAtomIter_KBOSum(*args)
    def HasResidue(*args): return _openbabel._OBMolAtomIter_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel._OBMolAtomIter_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel._OBMolAtomIter_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel._OBMolAtomIter_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel._OBMolAtomIter_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel._OBMolAtomIter_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel._OBMolAtomIter_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel._OBMolAtomIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBMolAtomIter_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel._OBMolAtomIter_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel._OBMolAtomIter_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel._OBMolAtomIter_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel._OBMolAtomIter_IsConnected(*args)
    def IsOneThree(*args): return _openbabel._OBMolAtomIter_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel._OBMolAtomIter_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel._OBMolAtomIter_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel._OBMolAtomIter_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel._OBMolAtomIter_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel._OBMolAtomIter_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel._OBMolAtomIter_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel._OBMolAtomIter_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel._OBMolAtomIter_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel._OBMolAtomIter_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel._OBMolAtomIter_IsChiral(*args)
    def IsAxial(*args): return _openbabel._OBMolAtomIter_IsAxial(*args)
    def IsClockwise(*args): return _openbabel._OBMolAtomIter_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel._OBMolAtomIter_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel._OBMolAtomIter_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel._OBMolAtomIter_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel._OBMolAtomIter_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel._OBMolAtomIter_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel._OBMolAtomIter_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel._OBMolAtomIter_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel._OBMolAtomIter_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel._OBMolAtomIter_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel._OBMolAtomIter_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel._OBMolAtomIter_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel._OBMolAtomIter_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel._OBMolAtomIter_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel._OBMolAtomIter_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel._OBMolAtomIter_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel._OBMolAtomIter_MatchesSMARTS(*args)
    def DoTransformations(*args): return _openbabel._OBMolAtomIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBMolAtomIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBMolAtomIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBMolAtomIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBMolAtomIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBMolAtomIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBMolAtomIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBMolAtomIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBMolAtomIter_EndData(*args)
_OBMolAtomIter_swigregister = _openbabel._OBMolAtomIter_swigregister
_OBMolAtomIter_swigregister(_OBMolAtomIter)

class _OBMolAtomDFSIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolAtomDFSIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolAtomDFSIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolAtomDFSIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolAtomDFSIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolAtomDFSIter_good(*args)
    def inc(*args): return _openbabel._OBMolAtomDFSIter_inc(*args)
    def deref(*args): return _openbabel._OBMolAtomDFSIter_deref(*args)
    def __ref__(*args): return _openbabel._OBMolAtomDFSIter___ref__(*args)
    def next(*args): return _openbabel._OBMolAtomDFSIter_next(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBMolAtomDFSIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBMolAtomDFSIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBMolAtomDFSIter_Visit_get, _openbabel._OBMolAtomDFSIter_Visit_set)
    def Clear(*args): return _openbabel._OBMolAtomDFSIter_Clear(*args)
    def SetIdx(*args): return _openbabel._OBMolAtomDFSIter_SetIdx(*args)
    def SetHyb(*args): return _openbabel._OBMolAtomDFSIter_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel._OBMolAtomDFSIter_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel._OBMolAtomDFSIter_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel._OBMolAtomDFSIter_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel._OBMolAtomDFSIter_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel._OBMolAtomDFSIter_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel._OBMolAtomDFSIter_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel._OBMolAtomDFSIter_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel._OBMolAtomDFSIter_SetType(*args)
    def SetPartialCharge(*args): return _openbabel._OBMolAtomDFSIter_SetPartialCharge(*args)
    def SetVector(*args): return _openbabel._OBMolAtomDFSIter_SetVector(*args)
    def SetCoordPtr(*args): return _openbabel._OBMolAtomDFSIter_SetCoordPtr(*args)
    def SetResidue(*args): return _openbabel._OBMolAtomDFSIter_SetResidue(*args)
    def SetParent(*args): return _openbabel._OBMolAtomDFSIter_SetParent(*args)
    def SetAromatic(*args): return _openbabel._OBMolAtomDFSIter_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel._OBMolAtomDFSIter_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel._OBMolAtomDFSIter_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel._OBMolAtomDFSIter_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel._OBMolAtomDFSIter_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel._OBMolAtomDFSIter_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel._OBMolAtomDFSIter_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel._OBMolAtomDFSIter_SetInRing(*args)
    def SetChiral(*args): return _openbabel._OBMolAtomDFSIter_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel._OBMolAtomDFSIter_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel._OBMolAtomDFSIter_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel._OBMolAtomDFSIter_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel._OBMolAtomDFSIter_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel._OBMolAtomDFSIter_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel._OBMolAtomDFSIter_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel._OBMolAtomDFSIter_GetExactMass(*args)
    def GetIdx(*args): return _openbabel._OBMolAtomDFSIter_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel._OBMolAtomDFSIter_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel._OBMolAtomDFSIter_GetCIdx(*args)
    def GetValence(*args): return _openbabel._OBMolAtomDFSIter_GetValence(*args)
    def GetHyb(*args): return _openbabel._OBMolAtomDFSIter_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel._OBMolAtomDFSIter_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel._OBMolAtomDFSIter_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel._OBMolAtomDFSIter_GetHeteroValence(*args)
    def GetType(*args): return _openbabel._OBMolAtomDFSIter_GetType(*args)
    def GetX(*args): return _openbabel._OBMolAtomDFSIter_GetX(*args)
    def GetY(*args): return _openbabel._OBMolAtomDFSIter_GetY(*args)
    def GetZ(*args): return _openbabel._OBMolAtomDFSIter_GetZ(*args)
    def x(*args): return _openbabel._OBMolAtomDFSIter_x(*args)
    def y(*args): return _openbabel._OBMolAtomDFSIter_y(*args)
    def z(*args): return _openbabel._OBMolAtomDFSIter_z(*args)
    def GetCoordinate(*args): return _openbabel._OBMolAtomDFSIter_GetCoordinate(*args)
    def GetVector(*args): return _openbabel._OBMolAtomDFSIter_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel._OBMolAtomDFSIter_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel._OBMolAtomDFSIter_GetResidue(*args)
    def GetParent(*args): return _openbabel._OBMolAtomDFSIter_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel._OBMolAtomDFSIter_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel._OBMolAtomDFSIter_GetBond(*args)
    def GetNextAtom(*args): return _openbabel._OBMolAtomDFSIter_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel._OBMolAtomDFSIter_BeginBonds(*args)
    def EndBonds(*args): return _openbabel._OBMolAtomDFSIter_EndBonds(*args)
    def BeginBond(*args): return _openbabel._OBMolAtomDFSIter_BeginBond(*args)
    def NextBond(*args): return _openbabel._OBMolAtomDFSIter_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel._OBMolAtomDFSIter_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel._OBMolAtomDFSIter_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel._OBMolAtomDFSIter_GetDistance(*args)
    def GetAngle(*args): return _openbabel._OBMolAtomDFSIter_GetAngle(*args)
    def NewResidue(*args): return _openbabel._OBMolAtomDFSIter_NewResidue(*args)
    def AddResidue(*args): return _openbabel._OBMolAtomDFSIter_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel._OBMolAtomDFSIter_DeleteResidue(*args)
    def AddBond(*args): return _openbabel._OBMolAtomDFSIter_AddBond(*args)
    def InsertBond(*args): return _openbabel._OBMolAtomDFSIter_InsertBond(*args)
    def DeleteBond(*args): return _openbabel._OBMolAtomDFSIter_DeleteBond(*args)
    def ClearBond(*args): return _openbabel._OBMolAtomDFSIter_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel._OBMolAtomDFSIter_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel._OBMolAtomDFSIter_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel._OBMolAtomDFSIter_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel._OBMolAtomDFSIter_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel._OBMolAtomDFSIter_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel._OBMolAtomDFSIter_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel._OBMolAtomDFSIter_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel._OBMolAtomDFSIter_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel._OBMolAtomDFSIter_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel._OBMolAtomDFSIter_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel._OBMolAtomDFSIter_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel._OBMolAtomDFSIter_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel._OBMolAtomDFSIter_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel._OBMolAtomDFSIter_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel._OBMolAtomDFSIter_BOSum(*args)
    def KBOSum(*args): return _openbabel._OBMolAtomDFSIter_KBOSum(*args)
    def HasResidue(*args): return _openbabel._OBMolAtomDFSIter_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel._OBMolAtomDFSIter_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel._OBMolAtomDFSIter_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel._OBMolAtomDFSIter_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel._OBMolAtomDFSIter_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel._OBMolAtomDFSIter_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel._OBMolAtomDFSIter_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel._OBMolAtomDFSIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBMolAtomDFSIter_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel._OBMolAtomDFSIter_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel._OBMolAtomDFSIter_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel._OBMolAtomDFSIter_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel._OBMolAtomDFSIter_IsConnected(*args)
    def IsOneThree(*args): return _openbabel._OBMolAtomDFSIter_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel._OBMolAtomDFSIter_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel._OBMolAtomDFSIter_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel._OBMolAtomDFSIter_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel._OBMolAtomDFSIter_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel._OBMolAtomDFSIter_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel._OBMolAtomDFSIter_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel._OBMolAtomDFSIter_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel._OBMolAtomDFSIter_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel._OBMolAtomDFSIter_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel._OBMolAtomDFSIter_IsChiral(*args)
    def IsAxial(*args): return _openbabel._OBMolAtomDFSIter_IsAxial(*args)
    def IsClockwise(*args): return _openbabel._OBMolAtomDFSIter_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel._OBMolAtomDFSIter_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel._OBMolAtomDFSIter_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel._OBMolAtomDFSIter_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel._OBMolAtomDFSIter_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel._OBMolAtomDFSIter_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel._OBMolAtomDFSIter_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel._OBMolAtomDFSIter_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel._OBMolAtomDFSIter_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel._OBMolAtomDFSIter_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel._OBMolAtomDFSIter_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel._OBMolAtomDFSIter_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel._OBMolAtomDFSIter_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel._OBMolAtomDFSIter_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel._OBMolAtomDFSIter_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel._OBMolAtomDFSIter_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel._OBMolAtomDFSIter_MatchesSMARTS(*args)
    def DoTransformations(*args): return _openbabel._OBMolAtomDFSIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBMolAtomDFSIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBMolAtomDFSIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBMolAtomDFSIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBMolAtomDFSIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBMolAtomDFSIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBMolAtomDFSIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBMolAtomDFSIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBMolAtomDFSIter_EndData(*args)
_OBMolAtomDFSIter_swigregister = _openbabel._OBMolAtomDFSIter_swigregister
_OBMolAtomDFSIter_swigregister(_OBMolAtomDFSIter)

class _OBMolAtomBFSIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolAtomBFSIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolAtomBFSIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolAtomBFSIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolAtomBFSIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolAtomBFSIter_good(*args)
    def inc(*args): return _openbabel._OBMolAtomBFSIter_inc(*args)
    def deref(*args): return _openbabel._OBMolAtomBFSIter_deref(*args)
    def __ref__(*args): return _openbabel._OBMolAtomBFSIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBMolAtomBFSIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBMolAtomBFSIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBMolAtomBFSIter_Visit_get, _openbabel._OBMolAtomBFSIter_Visit_set)
    def Clear(*args): return _openbabel._OBMolAtomBFSIter_Clear(*args)
    def SetIdx(*args): return _openbabel._OBMolAtomBFSIter_SetIdx(*args)
    def SetHyb(*args): return _openbabel._OBMolAtomBFSIter_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel._OBMolAtomBFSIter_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel._OBMolAtomBFSIter_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel._OBMolAtomBFSIter_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel._OBMolAtomBFSIter_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel._OBMolAtomBFSIter_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel._OBMolAtomBFSIter_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel._OBMolAtomBFSIter_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel._OBMolAtomBFSIter_SetType(*args)
    def SetPartialCharge(*args): return _openbabel._OBMolAtomBFSIter_SetPartialCharge(*args)
    def SetVector(*args): return _openbabel._OBMolAtomBFSIter_SetVector(*args)
    def SetCoordPtr(*args): return _openbabel._OBMolAtomBFSIter_SetCoordPtr(*args)
    def SetResidue(*args): return _openbabel._OBMolAtomBFSIter_SetResidue(*args)
    def SetParent(*args): return _openbabel._OBMolAtomBFSIter_SetParent(*args)
    def SetAromatic(*args): return _openbabel._OBMolAtomBFSIter_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel._OBMolAtomBFSIter_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel._OBMolAtomBFSIter_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel._OBMolAtomBFSIter_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel._OBMolAtomBFSIter_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel._OBMolAtomBFSIter_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel._OBMolAtomBFSIter_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel._OBMolAtomBFSIter_SetInRing(*args)
    def SetChiral(*args): return _openbabel._OBMolAtomBFSIter_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel._OBMolAtomBFSIter_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel._OBMolAtomBFSIter_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel._OBMolAtomBFSIter_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel._OBMolAtomBFSIter_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel._OBMolAtomBFSIter_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel._OBMolAtomBFSIter_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel._OBMolAtomBFSIter_GetExactMass(*args)
    def GetIdx(*args): return _openbabel._OBMolAtomBFSIter_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel._OBMolAtomBFSIter_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel._OBMolAtomBFSIter_GetCIdx(*args)
    def GetValence(*args): return _openbabel._OBMolAtomBFSIter_GetValence(*args)
    def GetHyb(*args): return _openbabel._OBMolAtomBFSIter_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel._OBMolAtomBFSIter_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel._OBMolAtomBFSIter_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel._OBMolAtomBFSIter_GetHeteroValence(*args)
    def GetType(*args): return _openbabel._OBMolAtomBFSIter_GetType(*args)
    def GetX(*args): return _openbabel._OBMolAtomBFSIter_GetX(*args)
    def GetY(*args): return _openbabel._OBMolAtomBFSIter_GetY(*args)
    def GetZ(*args): return _openbabel._OBMolAtomBFSIter_GetZ(*args)
    def x(*args): return _openbabel._OBMolAtomBFSIter_x(*args)
    def y(*args): return _openbabel._OBMolAtomBFSIter_y(*args)
    def z(*args): return _openbabel._OBMolAtomBFSIter_z(*args)
    def GetCoordinate(*args): return _openbabel._OBMolAtomBFSIter_GetCoordinate(*args)
    def GetVector(*args): return _openbabel._OBMolAtomBFSIter_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel._OBMolAtomBFSIter_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel._OBMolAtomBFSIter_GetResidue(*args)
    def GetParent(*args): return _openbabel._OBMolAtomBFSIter_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel._OBMolAtomBFSIter_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel._OBMolAtomBFSIter_GetBond(*args)
    def GetNextAtom(*args): return _openbabel._OBMolAtomBFSIter_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel._OBMolAtomBFSIter_BeginBonds(*args)
    def EndBonds(*args): return _openbabel._OBMolAtomBFSIter_EndBonds(*args)
    def BeginBond(*args): return _openbabel._OBMolAtomBFSIter_BeginBond(*args)
    def NextBond(*args): return _openbabel._OBMolAtomBFSIter_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel._OBMolAtomBFSIter_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel._OBMolAtomBFSIter_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel._OBMolAtomBFSIter_GetDistance(*args)
    def GetAngle(*args): return _openbabel._OBMolAtomBFSIter_GetAngle(*args)
    def NewResidue(*args): return _openbabel._OBMolAtomBFSIter_NewResidue(*args)
    def AddResidue(*args): return _openbabel._OBMolAtomBFSIter_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel._OBMolAtomBFSIter_DeleteResidue(*args)
    def AddBond(*args): return _openbabel._OBMolAtomBFSIter_AddBond(*args)
    def InsertBond(*args): return _openbabel._OBMolAtomBFSIter_InsertBond(*args)
    def DeleteBond(*args): return _openbabel._OBMolAtomBFSIter_DeleteBond(*args)
    def ClearBond(*args): return _openbabel._OBMolAtomBFSIter_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel._OBMolAtomBFSIter_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel._OBMolAtomBFSIter_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel._OBMolAtomBFSIter_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel._OBMolAtomBFSIter_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel._OBMolAtomBFSIter_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel._OBMolAtomBFSIter_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel._OBMolAtomBFSIter_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel._OBMolAtomBFSIter_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel._OBMolAtomBFSIter_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel._OBMolAtomBFSIter_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel._OBMolAtomBFSIter_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel._OBMolAtomBFSIter_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel._OBMolAtomBFSIter_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel._OBMolAtomBFSIter_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel._OBMolAtomBFSIter_BOSum(*args)
    def KBOSum(*args): return _openbabel._OBMolAtomBFSIter_KBOSum(*args)
    def HasResidue(*args): return _openbabel._OBMolAtomBFSIter_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel._OBMolAtomBFSIter_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel._OBMolAtomBFSIter_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel._OBMolAtomBFSIter_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel._OBMolAtomBFSIter_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel._OBMolAtomBFSIter_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel._OBMolAtomBFSIter_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel._OBMolAtomBFSIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBMolAtomBFSIter_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel._OBMolAtomBFSIter_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel._OBMolAtomBFSIter_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel._OBMolAtomBFSIter_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel._OBMolAtomBFSIter_IsConnected(*args)
    def IsOneThree(*args): return _openbabel._OBMolAtomBFSIter_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel._OBMolAtomBFSIter_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel._OBMolAtomBFSIter_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel._OBMolAtomBFSIter_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel._OBMolAtomBFSIter_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel._OBMolAtomBFSIter_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel._OBMolAtomBFSIter_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel._OBMolAtomBFSIter_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel._OBMolAtomBFSIter_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel._OBMolAtomBFSIter_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel._OBMolAtomBFSIter_IsChiral(*args)
    def IsAxial(*args): return _openbabel._OBMolAtomBFSIter_IsAxial(*args)
    def IsClockwise(*args): return _openbabel._OBMolAtomBFSIter_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel._OBMolAtomBFSIter_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel._OBMolAtomBFSIter_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel._OBMolAtomBFSIter_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel._OBMolAtomBFSIter_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel._OBMolAtomBFSIter_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel._OBMolAtomBFSIter_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel._OBMolAtomBFSIter_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel._OBMolAtomBFSIter_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel._OBMolAtomBFSIter_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel._OBMolAtomBFSIter_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel._OBMolAtomBFSIter_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel._OBMolAtomBFSIter_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel._OBMolAtomBFSIter_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel._OBMolAtomBFSIter_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel._OBMolAtomBFSIter_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel._OBMolAtomBFSIter_MatchesSMARTS(*args)
    def DoTransformations(*args): return _openbabel._OBMolAtomBFSIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBMolAtomBFSIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBMolAtomBFSIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBMolAtomBFSIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBMolAtomBFSIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBMolAtomBFSIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBMolAtomBFSIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBMolAtomBFSIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBMolAtomBFSIter_EndData(*args)
_OBMolAtomBFSIter_swigregister = _openbabel._OBMolAtomBFSIter_swigregister
_OBMolAtomBFSIter_swigregister(_OBMolAtomBFSIter)

class _OBMolBondIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolBondIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolBondIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolBondIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolBondIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolBondIter_good(*args)
    def inc(*args): return _openbabel._OBMolBondIter_inc(*args)
    def deref(*args): return _openbabel._OBMolBondIter_deref(*args)
    def __ref__(*args): return _openbabel._OBMolBondIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBMolBondIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBMolBondIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBMolBondIter_Visit_get, _openbabel._OBMolBondIter_Visit_set)
    def SetIdx(*args): return _openbabel._OBMolBondIter_SetIdx(*args)
    def SetBO(*args): return _openbabel._OBMolBondIter_SetBO(*args)
    def SetBondOrder(*args): return _openbabel._OBMolBondIter_SetBondOrder(*args)
    def SetBegin(*args): return _openbabel._OBMolBondIter_SetBegin(*args)
    def SetEnd(*args): return _openbabel._OBMolBondIter_SetEnd(*args)
    def SetParent(*args): return _openbabel._OBMolBondIter_SetParent(*args)
    def SetLength(*args): return _openbabel._OBMolBondIter_SetLength(*args)
    def Set(*args): return _openbabel._OBMolBondIter_Set(*args)
    def SetKSingle(*args): return _openbabel._OBMolBondIter_SetKSingle(*args)
    def SetKDouble(*args): return _openbabel._OBMolBondIter_SetKDouble(*args)
    def SetKTriple(*args): return _openbabel._OBMolBondIter_SetKTriple(*args)
    def SetAromatic(*args): return _openbabel._OBMolBondIter_SetAromatic(*args)
    def SetHash(*args): return _openbabel._OBMolBondIter_SetHash(*args)
    def SetWedge(*args): return _openbabel._OBMolBondIter_SetWedge(*args)
    def SetUp(*args): return _openbabel._OBMolBondIter_SetUp(*args)
    def SetDown(*args): return _openbabel._OBMolBondIter_SetDown(*args)
    def SetInRing(*args): return _openbabel._OBMolBondIter_SetInRing(*args)
    def SetClosure(*args): return _openbabel._OBMolBondIter_SetClosure(*args)
    def UnsetHash(*args): return _openbabel._OBMolBondIter_UnsetHash(*args)
    def UnsetWedge(*args): return _openbabel._OBMolBondIter_UnsetWedge(*args)
    def UnsetUp(*args): return _openbabel._OBMolBondIter_UnsetUp(*args)
    def UnsetDown(*args): return _openbabel._OBMolBondIter_UnsetDown(*args)
    def UnsetAromatic(*args): return _openbabel._OBMolBondIter_UnsetAromatic(*args)
    def UnsetKekule(*args): return _openbabel._OBMolBondIter_UnsetKekule(*args)
    def GetIdx(*args): return _openbabel._OBMolBondIter_GetIdx(*args)
    def GetBO(*args): return _openbabel._OBMolBondIter_GetBO(*args)
    def GetBondOrder(*args): return _openbabel._OBMolBondIter_GetBondOrder(*args)
    def GetFlags(*args): return _openbabel._OBMolBondIter_GetFlags(*args)
    def GetBeginAtomIdx(*args): return _openbabel._OBMolBondIter_GetBeginAtomIdx(*args)
    def GetEndAtomIdx(*args): return _openbabel._OBMolBondIter_GetEndAtomIdx(*args)
    def GetBeginAtom(*args): return _openbabel._OBMolBondIter_GetBeginAtom(*args)
    def GetEndAtom(*args): return _openbabel._OBMolBondIter_GetEndAtom(*args)
    def GetNbrAtom(*args): return _openbabel._OBMolBondIter_GetNbrAtom(*args)
    def GetParent(*args): return _openbabel._OBMolBondIter_GetParent(*args)
    def GetEquibLength(*args): return _openbabel._OBMolBondIter_GetEquibLength(*args)
    def GetLength(*args): return _openbabel._OBMolBondIter_GetLength(*args)
    def GetNbrAtomIdx(*args): return _openbabel._OBMolBondIter_GetNbrAtomIdx(*args)
    def IsAromatic(*args): return _openbabel._OBMolBondIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBMolBondIter_IsInRing(*args)
    def IsRotor(*args): return _openbabel._OBMolBondIter_IsRotor(*args)
    def IsAmide(*args): return _openbabel._OBMolBondIter_IsAmide(*args)
    def IsPrimaryAmide(*args): return _openbabel._OBMolBondIter_IsPrimaryAmide(*args)
    def IsSecondaryAmide(*args): return _openbabel._OBMolBondIter_IsSecondaryAmide(*args)
    def IsEster(*args): return _openbabel._OBMolBondIter_IsEster(*args)
    def IsCarbonyl(*args): return _openbabel._OBMolBondIter_IsCarbonyl(*args)
    def IsSingle(*args): return _openbabel._OBMolBondIter_IsSingle(*args)
    def IsDouble(*args): return _openbabel._OBMolBondIter_IsDouble(*args)
    def IsTriple(*args): return _openbabel._OBMolBondIter_IsTriple(*args)
    def IsKSingle(*args): return _openbabel._OBMolBondIter_IsKSingle(*args)
    def IsKDouble(*args): return _openbabel._OBMolBondIter_IsKDouble(*args)
    def IsKTriple(*args): return _openbabel._OBMolBondIter_IsKTriple(*args)
    def IsClosure(*args): return _openbabel._OBMolBondIter_IsClosure(*args)
    def IsUp(*args): return _openbabel._OBMolBondIter_IsUp(*args)
    def IsDown(*args): return _openbabel._OBMolBondIter_IsDown(*args)
    def IsWedge(*args): return _openbabel._OBMolBondIter_IsWedge(*args)
    def IsHash(*args): return _openbabel._OBMolBondIter_IsHash(*args)
    def IsDoubleBondGeometry(*args): return _openbabel._OBMolBondIter_IsDoubleBondGeometry(*args)
    def Clear(*args): return _openbabel._OBMolBondIter_Clear(*args)
    def DoTransformations(*args): return _openbabel._OBMolBondIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBMolBondIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBMolBondIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBMolBondIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBMolBondIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBMolBondIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBMolBondIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBMolBondIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBMolBondIter_EndData(*args)
_OBMolBondIter_swigregister = _openbabel._OBMolBondIter_swigregister
_OBMolBondIter_swigregister(_OBMolBondIter)

class _OBAtomAtomIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBAtomAtomIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBAtomAtomIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBAtomAtomIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBAtomAtomIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBAtomAtomIter_good(*args)
    def inc(*args): return _openbabel._OBAtomAtomIter_inc(*args)
    def deref(*args): return _openbabel._OBAtomAtomIter_deref(*args)
    def __ref__(*args): return _openbabel._OBAtomAtomIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBAtomAtomIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBAtomAtomIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBAtomAtomIter_Visit_get, _openbabel._OBAtomAtomIter_Visit_set)
    def Clear(*args): return _openbabel._OBAtomAtomIter_Clear(*args)
    def SetIdx(*args): return _openbabel._OBAtomAtomIter_SetIdx(*args)
    def SetHyb(*args): return _openbabel._OBAtomAtomIter_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel._OBAtomAtomIter_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel._OBAtomAtomIter_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel._OBAtomAtomIter_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel._OBAtomAtomIter_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel._OBAtomAtomIter_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel._OBAtomAtomIter_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel._OBAtomAtomIter_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel._OBAtomAtomIter_SetType(*args)
    def SetPartialCharge(*args): return _openbabel._OBAtomAtomIter_SetPartialCharge(*args)
    def SetVector(*args): return _openbabel._OBAtomAtomIter_SetVector(*args)
    def SetCoordPtr(*args): return _openbabel._OBAtomAtomIter_SetCoordPtr(*args)
    def SetResidue(*args): return _openbabel._OBAtomAtomIter_SetResidue(*args)
    def SetParent(*args): return _openbabel._OBAtomAtomIter_SetParent(*args)
    def SetAromatic(*args): return _openbabel._OBAtomAtomIter_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel._OBAtomAtomIter_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel._OBAtomAtomIter_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel._OBAtomAtomIter_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel._OBAtomAtomIter_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel._OBAtomAtomIter_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel._OBAtomAtomIter_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel._OBAtomAtomIter_SetInRing(*args)
    def SetChiral(*args): return _openbabel._OBAtomAtomIter_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel._OBAtomAtomIter_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel._OBAtomAtomIter_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel._OBAtomAtomIter_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel._OBAtomAtomIter_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel._OBAtomAtomIter_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel._OBAtomAtomIter_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel._OBAtomAtomIter_GetExactMass(*args)
    def GetIdx(*args): return _openbabel._OBAtomAtomIter_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel._OBAtomAtomIter_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel._OBAtomAtomIter_GetCIdx(*args)
    def GetValence(*args): return _openbabel._OBAtomAtomIter_GetValence(*args)
    def GetHyb(*args): return _openbabel._OBAtomAtomIter_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel._OBAtomAtomIter_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel._OBAtomAtomIter_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel._OBAtomAtomIter_GetHeteroValence(*args)
    def GetType(*args): return _openbabel._OBAtomAtomIter_GetType(*args)
    def GetX(*args): return _openbabel._OBAtomAtomIter_GetX(*args)
    def GetY(*args): return _openbabel._OBAtomAtomIter_GetY(*args)
    def GetZ(*args): return _openbabel._OBAtomAtomIter_GetZ(*args)
    def x(*args): return _openbabel._OBAtomAtomIter_x(*args)
    def y(*args): return _openbabel._OBAtomAtomIter_y(*args)
    def z(*args): return _openbabel._OBAtomAtomIter_z(*args)
    def GetCoordinate(*args): return _openbabel._OBAtomAtomIter_GetCoordinate(*args)
    def GetVector(*args): return _openbabel._OBAtomAtomIter_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel._OBAtomAtomIter_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel._OBAtomAtomIter_GetResidue(*args)
    def GetParent(*args): return _openbabel._OBAtomAtomIter_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel._OBAtomAtomIter_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel._OBAtomAtomIter_GetBond(*args)
    def GetNextAtom(*args): return _openbabel._OBAtomAtomIter_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel._OBAtomAtomIter_BeginBonds(*args)
    def EndBonds(*args): return _openbabel._OBAtomAtomIter_EndBonds(*args)
    def BeginBond(*args): return _openbabel._OBAtomAtomIter_BeginBond(*args)
    def NextBond(*args): return _openbabel._OBAtomAtomIter_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel._OBAtomAtomIter_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel._OBAtomAtomIter_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel._OBAtomAtomIter_GetDistance(*args)
    def GetAngle(*args): return _openbabel._OBAtomAtomIter_GetAngle(*args)
    def NewResidue(*args): return _openbabel._OBAtomAtomIter_NewResidue(*args)
    def AddResidue(*args): return _openbabel._OBAtomAtomIter_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel._OBAtomAtomIter_DeleteResidue(*args)
    def AddBond(*args): return _openbabel._OBAtomAtomIter_AddBond(*args)
    def InsertBond(*args): return _openbabel._OBAtomAtomIter_InsertBond(*args)
    def DeleteBond(*args): return _openbabel._OBAtomAtomIter_DeleteBond(*args)
    def ClearBond(*args): return _openbabel._OBAtomAtomIter_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel._OBAtomAtomIter_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel._OBAtomAtomIter_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel._OBAtomAtomIter_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel._OBAtomAtomIter_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel._OBAtomAtomIter_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel._OBAtomAtomIter_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel._OBAtomAtomIter_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel._OBAtomAtomIter_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel._OBAtomAtomIter_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel._OBAtomAtomIter_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel._OBAtomAtomIter_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel._OBAtomAtomIter_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel._OBAtomAtomIter_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel._OBAtomAtomIter_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel._OBAtomAtomIter_BOSum(*args)
    def KBOSum(*args): return _openbabel._OBAtomAtomIter_KBOSum(*args)
    def HasResidue(*args): return _openbabel._OBAtomAtomIter_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel._OBAtomAtomIter_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel._OBAtomAtomIter_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel._OBAtomAtomIter_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel._OBAtomAtomIter_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel._OBAtomAtomIter_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel._OBAtomAtomIter_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel._OBAtomAtomIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBAtomAtomIter_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel._OBAtomAtomIter_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel._OBAtomAtomIter_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel._OBAtomAtomIter_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel._OBAtomAtomIter_IsConnected(*args)
    def IsOneThree(*args): return _openbabel._OBAtomAtomIter_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel._OBAtomAtomIter_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel._OBAtomAtomIter_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel._OBAtomAtomIter_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel._OBAtomAtomIter_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel._OBAtomAtomIter_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel._OBAtomAtomIter_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel._OBAtomAtomIter_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel._OBAtomAtomIter_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel._OBAtomAtomIter_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel._OBAtomAtomIter_IsChiral(*args)
    def IsAxial(*args): return _openbabel._OBAtomAtomIter_IsAxial(*args)
    def IsClockwise(*args): return _openbabel._OBAtomAtomIter_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel._OBAtomAtomIter_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel._OBAtomAtomIter_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel._OBAtomAtomIter_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel._OBAtomAtomIter_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel._OBAtomAtomIter_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel._OBAtomAtomIter_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel._OBAtomAtomIter_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel._OBAtomAtomIter_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel._OBAtomAtomIter_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel._OBAtomAtomIter_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel._OBAtomAtomIter_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel._OBAtomAtomIter_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel._OBAtomAtomIter_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel._OBAtomAtomIter_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel._OBAtomAtomIter_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel._OBAtomAtomIter_MatchesSMARTS(*args)
    def DoTransformations(*args): return _openbabel._OBAtomAtomIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBAtomAtomIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBAtomAtomIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBAtomAtomIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBAtomAtomIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBAtomAtomIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBAtomAtomIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBAtomAtomIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBAtomAtomIter_EndData(*args)
_OBAtomAtomIter_swigregister = _openbabel._OBAtomAtomIter_swigregister
_OBAtomAtomIter_swigregister(_OBAtomAtomIter)

class _OBAtomBondIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBAtomBondIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBAtomBondIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBAtomBondIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBAtomBondIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBAtomBondIter_good(*args)
    def inc(*args): return _openbabel._OBAtomBondIter_inc(*args)
    def deref(*args): return _openbabel._OBAtomBondIter_deref(*args)
    def __ref__(*args): return _openbabel._OBAtomBondIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBAtomBondIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBAtomBondIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBAtomBondIter_Visit_get, _openbabel._OBAtomBondIter_Visit_set)
    def SetIdx(*args): return _openbabel._OBAtomBondIter_SetIdx(*args)
    def SetBO(*args): return _openbabel._OBAtomBondIter_SetBO(*args)
    def SetBondOrder(*args): return _openbabel._OBAtomBondIter_SetBondOrder(*args)
    def SetBegin(*args): return _openbabel._OBAtomBondIter_SetBegin(*args)
    def SetEnd(*args): return _openbabel._OBAtomBondIter_SetEnd(*args)
    def SetParent(*args): return _openbabel._OBAtomBondIter_SetParent(*args)
    def SetLength(*args): return _openbabel._OBAtomBondIter_SetLength(*args)
    def Set(*args): return _openbabel._OBAtomBondIter_Set(*args)
    def SetKSingle(*args): return _openbabel._OBAtomBondIter_SetKSingle(*args)
    def SetKDouble(*args): return _openbabel._OBAtomBondIter_SetKDouble(*args)
    def SetKTriple(*args): return _openbabel._OBAtomBondIter_SetKTriple(*args)
    def SetAromatic(*args): return _openbabel._OBAtomBondIter_SetAromatic(*args)
    def SetHash(*args): return _openbabel._OBAtomBondIter_SetHash(*args)
    def SetWedge(*args): return _openbabel._OBAtomBondIter_SetWedge(*args)
    def SetUp(*args): return _openbabel._OBAtomBondIter_SetUp(*args)
    def SetDown(*args): return _openbabel._OBAtomBondIter_SetDown(*args)
    def SetInRing(*args): return _openbabel._OBAtomBondIter_SetInRing(*args)
    def SetClosure(*args): return _openbabel._OBAtomBondIter_SetClosure(*args)
    def UnsetHash(*args): return _openbabel._OBAtomBondIter_UnsetHash(*args)
    def UnsetWedge(*args): return _openbabel._OBAtomBondIter_UnsetWedge(*args)
    def UnsetUp(*args): return _openbabel._OBAtomBondIter_UnsetUp(*args)
    def UnsetDown(*args): return _openbabel._OBAtomBondIter_UnsetDown(*args)
    def UnsetAromatic(*args): return _openbabel._OBAtomBondIter_UnsetAromatic(*args)
    def UnsetKekule(*args): return _openbabel._OBAtomBondIter_UnsetKekule(*args)
    def GetIdx(*args): return _openbabel._OBAtomBondIter_GetIdx(*args)
    def GetBO(*args): return _openbabel._OBAtomBondIter_GetBO(*args)
    def GetBondOrder(*args): return _openbabel._OBAtomBondIter_GetBondOrder(*args)
    def GetFlags(*args): return _openbabel._OBAtomBondIter_GetFlags(*args)
    def GetBeginAtomIdx(*args): return _openbabel._OBAtomBondIter_GetBeginAtomIdx(*args)
    def GetEndAtomIdx(*args): return _openbabel._OBAtomBondIter_GetEndAtomIdx(*args)
    def GetBeginAtom(*args): return _openbabel._OBAtomBondIter_GetBeginAtom(*args)
    def GetEndAtom(*args): return _openbabel._OBAtomBondIter_GetEndAtom(*args)
    def GetNbrAtom(*args): return _openbabel._OBAtomBondIter_GetNbrAtom(*args)
    def GetParent(*args): return _openbabel._OBAtomBondIter_GetParent(*args)
    def GetEquibLength(*args): return _openbabel._OBAtomBondIter_GetEquibLength(*args)
    def GetLength(*args): return _openbabel._OBAtomBondIter_GetLength(*args)
    def GetNbrAtomIdx(*args): return _openbabel._OBAtomBondIter_GetNbrAtomIdx(*args)
    def IsAromatic(*args): return _openbabel._OBAtomBondIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBAtomBondIter_IsInRing(*args)
    def IsRotor(*args): return _openbabel._OBAtomBondIter_IsRotor(*args)
    def IsAmide(*args): return _openbabel._OBAtomBondIter_IsAmide(*args)
    def IsPrimaryAmide(*args): return _openbabel._OBAtomBondIter_IsPrimaryAmide(*args)
    def IsSecondaryAmide(*args): return _openbabel._OBAtomBondIter_IsSecondaryAmide(*args)
    def IsEster(*args): return _openbabel._OBAtomBondIter_IsEster(*args)
    def IsCarbonyl(*args): return _openbabel._OBAtomBondIter_IsCarbonyl(*args)
    def IsSingle(*args): return _openbabel._OBAtomBondIter_IsSingle(*args)
    def IsDouble(*args): return _openbabel._OBAtomBondIter_IsDouble(*args)
    def IsTriple(*args): return _openbabel._OBAtomBondIter_IsTriple(*args)
    def IsKSingle(*args): return _openbabel._OBAtomBondIter_IsKSingle(*args)
    def IsKDouble(*args): return _openbabel._OBAtomBondIter_IsKDouble(*args)
    def IsKTriple(*args): return _openbabel._OBAtomBondIter_IsKTriple(*args)
    def IsClosure(*args): return _openbabel._OBAtomBondIter_IsClosure(*args)
    def IsUp(*args): return _openbabel._OBAtomBondIter_IsUp(*args)
    def IsDown(*args): return _openbabel._OBAtomBondIter_IsDown(*args)
    def IsWedge(*args): return _openbabel._OBAtomBondIter_IsWedge(*args)
    def IsHash(*args): return _openbabel._OBAtomBondIter_IsHash(*args)
    def IsDoubleBondGeometry(*args): return _openbabel._OBAtomBondIter_IsDoubleBondGeometry(*args)
    def Clear(*args): return _openbabel._OBAtomBondIter_Clear(*args)
    def DoTransformations(*args): return _openbabel._OBAtomBondIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBAtomBondIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBAtomBondIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBAtomBondIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBAtomBondIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBAtomBondIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBAtomBondIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBAtomBondIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBAtomBondIter_EndData(*args)
_OBAtomBondIter_swigregister = _openbabel._OBAtomBondIter_swigregister
_OBAtomBondIter_swigregister(_OBAtomBondIter)

class _OBResidueIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBResidueIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBResidueIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBResidueIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBResidueIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBResidueIter_good(*args)
    def inc(*args): return _openbabel._OBResidueIter_inc(*args)
    def deref(*args): return _openbabel._OBResidueIter_deref(*args)
    def __ref__(*args): return _openbabel._OBResidueIter___ref__(*args)
    def AddAtom(*args): return _openbabel._OBResidueIter_AddAtom(*args)
    def InsertAtom(*args): return _openbabel._OBResidueIter_InsertAtom(*args)
    def RemoveAtom(*args): return _openbabel._OBResidueIter_RemoveAtom(*args)
    def Clear(*args): return _openbabel._OBResidueIter_Clear(*args)
    def SetName(*args): return _openbabel._OBResidueIter_SetName(*args)
    def SetNum(*args): return _openbabel._OBResidueIter_SetNum(*args)
    def SetChain(*args): return _openbabel._OBResidueIter_SetChain(*args)
    def SetChainNum(*args): return _openbabel._OBResidueIter_SetChainNum(*args)
    def SetIdx(*args): return _openbabel._OBResidueIter_SetIdx(*args)
    def SetAtomID(*args): return _openbabel._OBResidueIter_SetAtomID(*args)
    def SetHetAtom(*args): return _openbabel._OBResidueIter_SetHetAtom(*args)
    def SetSerialNum(*args): return _openbabel._OBResidueIter_SetSerialNum(*args)
    def GetName(*args): return _openbabel._OBResidueIter_GetName(*args)
    def GetNum(*args): return _openbabel._OBResidueIter_GetNum(*args)
    def GetNumString(*args): return _openbabel._OBResidueIter_GetNumString(*args)
    def GetNumAtoms(*args): return _openbabel._OBResidueIter_GetNumAtoms(*args)
    def GetChain(*args): return _openbabel._OBResidueIter_GetChain(*args)
    def GetChainNum(*args): return _openbabel._OBResidueIter_GetChainNum(*args)
    def GetIdx(*args): return _openbabel._OBResidueIter_GetIdx(*args)
    def GetResKey(*args): return _openbabel._OBResidueIter_GetResKey(*args)
    def GetAtoms(*args): return _openbabel._OBResidueIter_GetAtoms(*args)
    def GetBonds(*args): return _openbabel._OBResidueIter_GetBonds(*args)
    def GetAtomID(*args): return _openbabel._OBResidueIter_GetAtomID(*args)
    def GetSerialNum(*args): return _openbabel._OBResidueIter_GetSerialNum(*args)
    def GetAminoAcidProperty(*args): return _openbabel._OBResidueIter_GetAminoAcidProperty(*args)
    def GetAtomProperty(*args): return _openbabel._OBResidueIter_GetAtomProperty(*args)
    def GetResidueProperty(*args): return _openbabel._OBResidueIter_GetResidueProperty(*args)
    def IsHetAtom(*args): return _openbabel._OBResidueIter_IsHetAtom(*args)
    def IsResidueType(*args): return _openbabel._OBResidueIter_IsResidueType(*args)
    def BeginAtoms(*args): return _openbabel._OBResidueIter_BeginAtoms(*args)
    def EndAtoms(*args): return _openbabel._OBResidueIter_EndAtoms(*args)
    def BeginAtom(*args): return _openbabel._OBResidueIter_BeginAtom(*args)
    def NextAtom(*args): return _openbabel._OBResidueIter_NextAtom(*args)
    def DoTransformations(*args): return _openbabel._OBResidueIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBResidueIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBResidueIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBResidueIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBResidueIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBResidueIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBResidueIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBResidueIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBResidueIter_EndData(*args)
_OBResidueIter_swigregister = _openbabel._OBResidueIter_swigregister
_OBResidueIter_swigregister(_OBResidueIter)

class _OBResidueAtomIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBResidueAtomIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBResidueAtomIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBResidueAtomIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBResidueAtomIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBResidueAtomIter_good(*args)
    def inc(*args): return _openbabel._OBResidueAtomIter_inc(*args)
    def deref(*args): return _openbabel._OBResidueAtomIter_deref(*args)
    def __ref__(*args): return _openbabel._OBResidueAtomIter___ref__(*args)
    __swig_setmethods__["Visit"] = _openbabel._OBResidueAtomIter_Visit_set
    __swig_getmethods__["Visit"] = _openbabel._OBResidueAtomIter_Visit_get
    if _newclass:Visit = _swig_property(_openbabel._OBResidueAtomIter_Visit_get, _openbabel._OBResidueAtomIter_Visit_set)
    def Clear(*args): return _openbabel._OBResidueAtomIter_Clear(*args)
    def SetIdx(*args): return _openbabel._OBResidueAtomIter_SetIdx(*args)
    def SetHyb(*args): return _openbabel._OBResidueAtomIter_SetHyb(*args)
    def SetAtomicNum(*args): return _openbabel._OBResidueAtomIter_SetAtomicNum(*args)
    def SetIsotope(*args): return _openbabel._OBResidueAtomIter_SetIsotope(*args)
    def SetImplicitValence(*args): return _openbabel._OBResidueAtomIter_SetImplicitValence(*args)
    def IncrementImplicitValence(*args): return _openbabel._OBResidueAtomIter_IncrementImplicitValence(*args)
    def DecrementImplicitValence(*args): return _openbabel._OBResidueAtomIter_DecrementImplicitValence(*args)
    def SetFormalCharge(*args): return _openbabel._OBResidueAtomIter_SetFormalCharge(*args)
    def SetSpinMultiplicity(*args): return _openbabel._OBResidueAtomIter_SetSpinMultiplicity(*args)
    def SetType(*args): return _openbabel._OBResidueAtomIter_SetType(*args)
    def SetPartialCharge(*args): return _openbabel._OBResidueAtomIter_SetPartialCharge(*args)
    def SetVector(*args): return _openbabel._OBResidueAtomIter_SetVector(*args)
    def SetCoordPtr(*args): return _openbabel._OBResidueAtomIter_SetCoordPtr(*args)
    def SetResidue(*args): return _openbabel._OBResidueAtomIter_SetResidue(*args)
    def SetParent(*args): return _openbabel._OBResidueAtomIter_SetParent(*args)
    def SetAromatic(*args): return _openbabel._OBResidueAtomIter_SetAromatic(*args)
    def UnsetAromatic(*args): return _openbabel._OBResidueAtomIter_UnsetAromatic(*args)
    def SetClockwiseStereo(*args): return _openbabel._OBResidueAtomIter_SetClockwiseStereo(*args)
    def SetAntiClockwiseStereo(*args): return _openbabel._OBResidueAtomIter_SetAntiClockwiseStereo(*args)
    def SetPositiveStereo(*args): return _openbabel._OBResidueAtomIter_SetPositiveStereo(*args)
    def SetNegativeStereo(*args): return _openbabel._OBResidueAtomIter_SetNegativeStereo(*args)
    def UnsetStereo(*args): return _openbabel._OBResidueAtomIter_UnsetStereo(*args)
    def SetInRing(*args): return _openbabel._OBResidueAtomIter_SetInRing(*args)
    def SetChiral(*args): return _openbabel._OBResidueAtomIter_SetChiral(*args)
    def ClearCoordPtr(*args): return _openbabel._OBResidueAtomIter_ClearCoordPtr(*args)
    def GetFormalCharge(*args): return _openbabel._OBResidueAtomIter_GetFormalCharge(*args)
    def GetAtomicNum(*args): return _openbabel._OBResidueAtomIter_GetAtomicNum(*args)
    def GetIsotope(*args): return _openbabel._OBResidueAtomIter_GetIsotope(*args)
    def GetSpinMultiplicity(*args): return _openbabel._OBResidueAtomIter_GetSpinMultiplicity(*args)
    def GetAtomicMass(*args): return _openbabel._OBResidueAtomIter_GetAtomicMass(*args)
    def GetExactMass(*args): return _openbabel._OBResidueAtomIter_GetExactMass(*args)
    def GetIdx(*args): return _openbabel._OBResidueAtomIter_GetIdx(*args)
    def GetCoordinateIdx(*args): return _openbabel._OBResidueAtomIter_GetCoordinateIdx(*args)
    def GetCIdx(*args): return _openbabel._OBResidueAtomIter_GetCIdx(*args)
    def GetValence(*args): return _openbabel._OBResidueAtomIter_GetValence(*args)
    def GetHyb(*args): return _openbabel._OBResidueAtomIter_GetHyb(*args)
    def GetImplicitValence(*args): return _openbabel._OBResidueAtomIter_GetImplicitValence(*args)
    def GetHvyValence(*args): return _openbabel._OBResidueAtomIter_GetHvyValence(*args)
    def GetHeteroValence(*args): return _openbabel._OBResidueAtomIter_GetHeteroValence(*args)
    def GetType(*args): return _openbabel._OBResidueAtomIter_GetType(*args)
    def GetX(*args): return _openbabel._OBResidueAtomIter_GetX(*args)
    def GetY(*args): return _openbabel._OBResidueAtomIter_GetY(*args)
    def GetZ(*args): return _openbabel._OBResidueAtomIter_GetZ(*args)
    def x(*args): return _openbabel._OBResidueAtomIter_x(*args)
    def y(*args): return _openbabel._OBResidueAtomIter_y(*args)
    def z(*args): return _openbabel._OBResidueAtomIter_z(*args)
    def GetCoordinate(*args): return _openbabel._OBResidueAtomIter_GetCoordinate(*args)
    def GetVector(*args): return _openbabel._OBResidueAtomIter_GetVector(*args)
    def GetPartialCharge(*args): return _openbabel._OBResidueAtomIter_GetPartialCharge(*args)
    def GetResidue(*args): return _openbabel._OBResidueAtomIter_GetResidue(*args)
    def GetParent(*args): return _openbabel._OBResidueAtomIter_GetParent(*args)
    def GetNewBondVector(*args): return _openbabel._OBResidueAtomIter_GetNewBondVector(*args)
    def GetBond(*args): return _openbabel._OBResidueAtomIter_GetBond(*args)
    def GetNextAtom(*args): return _openbabel._OBResidueAtomIter_GetNextAtom(*args)
    def BeginBonds(*args): return _openbabel._OBResidueAtomIter_BeginBonds(*args)
    def EndBonds(*args): return _openbabel._OBResidueAtomIter_EndBonds(*args)
    def BeginBond(*args): return _openbabel._OBResidueAtomIter_BeginBond(*args)
    def NextBond(*args): return _openbabel._OBResidueAtomIter_NextBond(*args)
    def BeginNbrAtom(*args): return _openbabel._OBResidueAtomIter_BeginNbrAtom(*args)
    def NextNbrAtom(*args): return _openbabel._OBResidueAtomIter_NextNbrAtom(*args)
    def GetDistance(*args): return _openbabel._OBResidueAtomIter_GetDistance(*args)
    def GetAngle(*args): return _openbabel._OBResidueAtomIter_GetAngle(*args)
    def NewResidue(*args): return _openbabel._OBResidueAtomIter_NewResidue(*args)
    def AddResidue(*args): return _openbabel._OBResidueAtomIter_AddResidue(*args)
    def DeleteResidue(*args): return _openbabel._OBResidueAtomIter_DeleteResidue(*args)
    def AddBond(*args): return _openbabel._OBResidueAtomIter_AddBond(*args)
    def InsertBond(*args): return _openbabel._OBResidueAtomIter_InsertBond(*args)
    def DeleteBond(*args): return _openbabel._OBResidueAtomIter_DeleteBond(*args)
    def ClearBond(*args): return _openbabel._OBResidueAtomIter_ClearBond(*args)
    def HtoMethyl(*args): return _openbabel._OBResidueAtomIter_HtoMethyl(*args)
    def SetHybAndGeom(*args): return _openbabel._OBResidueAtomIter_SetHybAndGeom(*args)
    def ForceNoH(*args): return _openbabel._OBResidueAtomIter_ForceNoH(*args)
    def HasNoHForced(*args): return _openbabel._OBResidueAtomIter_HasNoHForced(*args)
    def ForceImplH(*args): return _openbabel._OBResidueAtomIter_ForceImplH(*args)
    def HasImplHForced(*args): return _openbabel._OBResidueAtomIter_HasImplHForced(*args)
    def CountFreeOxygens(*args): return _openbabel._OBResidueAtomIter_CountFreeOxygens(*args)
    def ImplicitHydrogenCount(*args): return _openbabel._OBResidueAtomIter_ImplicitHydrogenCount(*args)
    def ExplicitHydrogenCount(*args): return _openbabel._OBResidueAtomIter_ExplicitHydrogenCount(*args)
    def MemberOfRingCount(*args): return _openbabel._OBResidueAtomIter_MemberOfRingCount(*args)
    def MemberOfRingSize(*args): return _openbabel._OBResidueAtomIter_MemberOfRingSize(*args)
    def CountRingBonds(*args): return _openbabel._OBResidueAtomIter_CountRingBonds(*args)
    def SmallestBondAngle(*args): return _openbabel._OBResidueAtomIter_SmallestBondAngle(*args)
    def AverageBondAngle(*args): return _openbabel._OBResidueAtomIter_AverageBondAngle(*args)
    def BOSum(*args): return _openbabel._OBResidueAtomIter_BOSum(*args)
    def KBOSum(*args): return _openbabel._OBResidueAtomIter_KBOSum(*args)
    def HasResidue(*args): return _openbabel._OBResidueAtomIter_HasResidue(*args)
    def IsHydrogen(*args): return _openbabel._OBResidueAtomIter_IsHydrogen(*args)
    def IsCarbon(*args): return _openbabel._OBResidueAtomIter_IsCarbon(*args)
    def IsNitrogen(*args): return _openbabel._OBResidueAtomIter_IsNitrogen(*args)
    def IsOxygen(*args): return _openbabel._OBResidueAtomIter_IsOxygen(*args)
    def IsSulfur(*args): return _openbabel._OBResidueAtomIter_IsSulfur(*args)
    def IsPhosphorus(*args): return _openbabel._OBResidueAtomIter_IsPhosphorus(*args)
    def IsAromatic(*args): return _openbabel._OBResidueAtomIter_IsAromatic(*args)
    def IsInRing(*args): return _openbabel._OBResidueAtomIter_IsInRing(*args)
    def IsInRingSize(*args): return _openbabel._OBResidueAtomIter_IsInRingSize(*args)
    def IsHeteroatom(*args): return _openbabel._OBResidueAtomIter_IsHeteroatom(*args)
    def IsNotCorH(*args): return _openbabel._OBResidueAtomIter_IsNotCorH(*args)
    def IsConnected(*args): return _openbabel._OBResidueAtomIter_IsConnected(*args)
    def IsOneThree(*args): return _openbabel._OBResidueAtomIter_IsOneThree(*args)
    def IsOneFour(*args): return _openbabel._OBResidueAtomIter_IsOneFour(*args)
    def IsCarboxylOxygen(*args): return _openbabel._OBResidueAtomIter_IsCarboxylOxygen(*args)
    def IsPhosphateOxygen(*args): return _openbabel._OBResidueAtomIter_IsPhosphateOxygen(*args)
    def IsSulfateOxygen(*args): return _openbabel._OBResidueAtomIter_IsSulfateOxygen(*args)
    def IsNitroOxygen(*args): return _openbabel._OBResidueAtomIter_IsNitroOxygen(*args)
    def IsAmideNitrogen(*args): return _openbabel._OBResidueAtomIter_IsAmideNitrogen(*args)
    def IsPolarHydrogen(*args): return _openbabel._OBResidueAtomIter_IsPolarHydrogen(*args)
    def IsNonPolarHydrogen(*args): return _openbabel._OBResidueAtomIter_IsNonPolarHydrogen(*args)
    def IsAromaticNOxide(*args): return _openbabel._OBResidueAtomIter_IsAromaticNOxide(*args)
    def IsChiral(*args): return _openbabel._OBResidueAtomIter_IsChiral(*args)
    def IsAxial(*args): return _openbabel._OBResidueAtomIter_IsAxial(*args)
    def IsClockwise(*args): return _openbabel._OBResidueAtomIter_IsClockwise(*args)
    def IsAntiClockwise(*args): return _openbabel._OBResidueAtomIter_IsAntiClockwise(*args)
    def IsPositiveStereo(*args): return _openbabel._OBResidueAtomIter_IsPositiveStereo(*args)
    def IsNegativeStereo(*args): return _openbabel._OBResidueAtomIter_IsNegativeStereo(*args)
    def HasChiralitySpecified(*args): return _openbabel._OBResidueAtomIter_HasChiralitySpecified(*args)
    def HasChiralVolume(*args): return _openbabel._OBResidueAtomIter_HasChiralVolume(*args)
    def IsHbondAcceptor(*args): return _openbabel._OBResidueAtomIter_IsHbondAcceptor(*args)
    def IsHbondDonor(*args): return _openbabel._OBResidueAtomIter_IsHbondDonor(*args)
    def IsHbondDonorH(*args): return _openbabel._OBResidueAtomIter_IsHbondDonorH(*args)
    def HasAlphaBetaUnsat(*args): return _openbabel._OBResidueAtomIter_HasAlphaBetaUnsat(*args)
    def HasBondOfOrder(*args): return _openbabel._OBResidueAtomIter_HasBondOfOrder(*args)
    def CountBondsOfOrder(*args): return _openbabel._OBResidueAtomIter_CountBondsOfOrder(*args)
    def HasNonSingleBond(*args): return _openbabel._OBResidueAtomIter_HasNonSingleBond(*args)
    def HasSingleBond(*args): return _openbabel._OBResidueAtomIter_HasSingleBond(*args)
    def HasDoubleBond(*args): return _openbabel._OBResidueAtomIter_HasDoubleBond(*args)
    def HasAromaticBond(*args): return _openbabel._OBResidueAtomIter_HasAromaticBond(*args)
    def MatchesSMARTS(*args): return _openbabel._OBResidueAtomIter_MatchesSMARTS(*args)
    def DoTransformations(*args): return _openbabel._OBResidueAtomIter_DoTransformations(*args)
    def ClassDescription(*args): return _openbabel._OBResidueAtomIter_ClassDescription(*args)
    def HasData(*args): return _openbabel._OBResidueAtomIter_HasData(*args)
    def DeleteData(*args): return _openbabel._OBResidueAtomIter_DeleteData(*args)
    def SetData(*args): return _openbabel._OBResidueAtomIter_SetData(*args)
    def DataSize(*args): return _openbabel._OBResidueAtomIter_DataSize(*args)
    def GetData(*args): return _openbabel._OBResidueAtomIter_GetData(*args)
    def BeginData(*args): return _openbabel._OBResidueAtomIter_BeginData(*args)
    def EndData(*args): return _openbabel._OBResidueAtomIter_EndData(*args)
_OBResidueAtomIter_swigregister = _openbabel._OBResidueAtomIter_swigregister
_OBResidueAtomIter_swigregister(_OBResidueAtomIter)

class _OBMolAngleIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolAngleIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolAngleIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolAngleIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolAngleIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolAngleIter_good(*args)
    def inc(*args): return _openbabel._OBMolAngleIter_inc(*args)
    def __ref__(*args): return _openbabel._OBMolAngleIter___ref__(*args)
_OBMolAngleIter_swigregister = _openbabel._OBMolAngleIter_swigregister
_OBMolAngleIter_swigregister(_OBMolAngleIter)

class _OBMolTorsionIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolTorsionIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolTorsionIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolTorsionIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolTorsionIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolTorsionIter_good(*args)
    def inc(*args): return _openbabel._OBMolTorsionIter_inc(*args)
    def __ref__(*args): return _openbabel._OBMolTorsionIter___ref__(*args)
_OBMolTorsionIter_swigregister = _openbabel._OBMolTorsionIter_swigregister
_OBMolTorsionIter_swigregister(_OBMolTorsionIter)

class _OBMolPairIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolPairIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolPairIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolPairIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolPairIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolPairIter_good(*args)
    def inc(*args): return _openbabel._OBMolPairIter_inc(*args)
    def __ref__(*args): return _openbabel._OBMolPairIter___ref__(*args)
_OBMolPairIter_swigregister = _openbabel._OBMolPairIter_swigregister
_OBMolPairIter_swigregister(_OBMolPairIter)

class _OBMolRingIter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _OBMolRingIter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _OBMolRingIter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new__OBMolRingIter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete__OBMolRingIter
    __del__ = lambda self : None;
    def good(*args): return _openbabel._OBMolRingIter_good(*args)
    def inc(*args): return _openbabel._OBMolRingIter_inc(*args)
    def deref(*args): return _openbabel._OBMolRingIter_deref(*args)
    def __ref__(*args): return _openbabel._OBMolRingIter___ref__(*args)
    __swig_setmethods__["_path"] = _openbabel._OBMolRingIter__path_set
    __swig_getmethods__["_path"] = _openbabel._OBMolRingIter__path_get
    if _newclass:_path = _swig_property(_openbabel._OBMolRingIter__path_get, _openbabel._OBMolRingIter__path_set)
    __swig_setmethods__["_pathset"] = _openbabel._OBMolRingIter__pathset_set
    __swig_getmethods__["_pathset"] = _openbabel._OBMolRingIter__pathset_get
    if _newclass:_pathset = _swig_property(_openbabel._OBMolRingIter__pathset_get, _openbabel._OBMolRingIter__pathset_set)
    def Size(*args): return _openbabel._OBMolRingIter_Size(*args)
    def PathSize(*args): return _openbabel._OBMolRingIter_PathSize(*args)
    def IsAromatic(*args): return _openbabel._OBMolRingIter_IsAromatic(*args)
    def SetType(*args): return _openbabel._OBMolRingIter_SetType(*args)
    def GetType(*args): return _openbabel._OBMolRingIter_GetType(*args)
    def GetRootAtom(*args): return _openbabel._OBMolRingIter_GetRootAtom(*args)
    def IsMember(*args): return _openbabel._OBMolRingIter_IsMember(*args)
    def IsInRing(*args): return _openbabel._OBMolRingIter_IsInRing(*args)
    def SetParent(*args): return _openbabel._OBMolRingIter_SetParent(*args)
    def GetParent(*args): return _openbabel._OBMolRingIter_GetParent(*args)
    def findCenterAndNormal(*args): return _openbabel._OBMolRingIter_findCenterAndNormal(*args)
_OBMolRingIter_swigregister = _openbabel._OBMolRingIter_swigregister
_OBMolRingIter_swigregister(_OBMolRingIter)

class OBIter(object):
    OBiterator = None # This is defined by the subclasses

    def __init__(self, *params):
        self.iter = self.OBiterator(*params)
        self.finished = False

    def __iter__(self):
        return self

    def next(self):
        if not self.finished:
            b = self.iter.deref()
            self.iter.inc()
            if not self.iter.good():
                # There is nothing left to iterate over
                self.finished = True
            return b
        else:
            raise StopIteration

class OBAtomAtomIter(OBIter):
    """Iterator over the atoms attached to an atom."""
    OBiterator = _OBAtomAtomIter
class OBAtomBondIter(OBIter):
    """Iterator over the bonds attached to an atom."""
    OBiterator = _OBAtomBondIter
class OBMolAngleIter(OBIter):
    """Iterator over the angles in a molecule."""
    OBiterator = _OBMolAngleIter
class OBMolAtomIter(OBIter):
    """Iterator over the atoms in a molecule."""
    OBiterator = _OBMolAtomIter
class OBMolAtomBFSIter(OBIter):
    """Iterator over the atoms in a molecule in a breadth-first manner."""
    OBiterator = _OBMolAtomBFSIter
class OBMolAtomDFSIter(OBIter):
    """Iterator over the atoms in a molecule in a depth-first manner."""
    OBiterator = _OBMolAtomDFSIter
class OBMolBondIter(OBIter):
    """Iterator over the bonds in a molecule."""
    OBiterator = _OBMolBondIter
class OBMolPairIter(OBIter):
    """Iterator over pairs of atoms in a molecule."""
    OBiterator = _OBMolPairIter
class OBMolRingIter(OBIter):
    """Iterator over the rings in a molecule."""
    OBiterator = _OBMolRingIter
class OBMolTorsionIter(OBIter):
    """Iterator over the torsion angles in a molecule."""
    OBiterator = _OBMolTorsionIter
class OBResidueIter(OBIter):
    """Iterator over the residues in a molecule."""
    OBiterator = _OBResidueIter
class OBResidueAtomIter(OBIter):
    """Iterator over the atoms in a residue."""
    OBiterator = _OBResidueAtomIter

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _openbabel.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openbabel.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _openbabel.doubleArray___getitem__(*args)
    def __setitem__(*args): return _openbabel.doubleArray___setitem__(*args)
    def cast(*args): return _openbabel.doubleArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _openbabel.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_openbabel.doubleArray_frompointer)
doubleArray_swigregister = _openbabel.doubleArray_swigregister
doubleArray_swigregister(doubleArray)
doubleArray_frompointer = _openbabel.doubleArray_frompointer

def double_array(mylist):
    """Create a C array of doubles from a list."""
    c = doubleArray(len(mylist))
    for i,v in enumerate(mylist):
        c[i] = v
    return c



