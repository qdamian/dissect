import subprocess
import dissect

@when(u'I run dissect on it')
def step_impl(context):
    context.entities = []
    dissect.run(context.program_path, context.entities.append)
