from nose.tools import assert_equal
from dissect.model.entity.module import Module
from dissect.model.entity.function import Function

@then(u'the modules aa, ab, ba, bb are identified as such')
def step_impl(context):
    module_names = _get_entity_names(context.entities, Module)
    assert_equal(module_names, set(['aa', 'ab', 'ba', 'bb']))

@then(u'the functions aa_func, ab_func, ba_func, bb_func are identified as such')
def step_impl(context):
    function_names = _get_entity_names(context.entities, Function)
    assert_equal(function_names, set(['aa_func', 'ab_func', 'ba_func', 'bb_func']))

def _get_entity_names(entities, entity_type):
    entity_names = set()
    for entity in (x for x in entities if isinstance(x, entity_type)):
        entity_names.add(entity.name)
    return entity_names
