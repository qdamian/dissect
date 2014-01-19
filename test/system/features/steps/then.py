from nose.tools import *
from dissect.model.entity.module import Module
from dissect.model.entity.function import Function
from dissect.model.entity.function_call import FunctionCall
from dissect.model.entity.thread import Thread

@then(u'the modules main, aa, ab, ba, bb are identified as such')
def step_impl(context):
    assert_equal(
        set(e.name for e in context.entities if isinstance(e, Module)),
        set(['main', 'aa', 'ab', 'ba', 'bb'])
    )

@then(u'the functions main, aa_func, ab_func, ba_func, bb_func are identified as such')
def step_impl(context):
    assert_equal(
        set(e.name for e in context.entities if isinstance(e, Function)),
        set(['main', 'aa_func', 'ab_func', 'ba_func', 'bb_func'])
    )

@then(u'the function calls main, aa_func, ab_func, ba_func, bb_func are identified as such')
def step_impl(context):
    assert_equal(
        set(e.function.name for e in context.entities if isinstance(e, FunctionCall)),
        set(['main', 'aa_func', 'ab_func', 'ba_func', 'bb_func'])
    )

@then(u'the MainThread and four other threads are identified as such')
def step_imp(context):
    thread_name = [e.name for e in context.entities if isinstance(e, Thread)]
    print thread_name
    assert_true(all(['Thread' in name for name in thread_name]))
    assert_equal(len(thread_name), 5)
