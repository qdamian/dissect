from nose.tools import assert_equal
from dissect.model.entity.module import Module
from dissect.model.entity.function import Function
from dissect.model.entity.function_call import FunctionCall

@then(u'the modules aa, ab, ba, bb are identified as such')
def step_impl(context):
    assert_equal(
        set(e.name for e in context.entities if isinstance(e, Module)),
        set(['aa', 'ab', 'ba', 'bb'])
    )

@then(u'the functions aa_func, ab_func, ba_func, bb_func are identified as such')
def step_impl(context):
    assert_equal(
        set(e.name for e in context.entities if isinstance(e, Function)),
        set(['aa_func', 'ab_func', 'ba_func', 'bb_func'])
    )

@then(u'the function calls aa_func, ab_func, ba_func, bb_func are identified as such')
def step_impl(context):
    assert_equal(
        set(e.function.name for e in context.entities if isinstance(e, FunctionCall)),
        set(['aa_func', 'ab_func', 'ba_func', 'bb_func'])
    )
