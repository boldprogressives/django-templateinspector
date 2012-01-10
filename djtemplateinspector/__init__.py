from django.template import Context

def get_variables(template):
    """
    Returns an ordered list of variable names in the given Template,
    by monkeypatching Django template internals to maintain a list
    of all variables that it attempted to resolve in the template.
    """

    from django.template.base import FilterExpression
    original_resolve = FilterExpression.resolve
    found_vars = []
    
    def resolve_and_catch(self, context, ignore_failures=False):
        if hasattr(self.var, 'var'):
            found_vars.append(self.var.var)
        else:
            found_vars.append(self.var)
        return original_resolve(self, context, 
                                ignore_failures=ignore_failures)
    FilterExpression.resolve = resolve_and_catch

    try:
        _ = template.render(Context({}))
    finally:
        FilterExpression.resolve = original_resolve

    variables = set(found_vars)
    return list(variables)

if __name__ == '__main__':
    from django.template import Template
    test = Template("""
Welcome, {{ user.username }}!

{% if can_view_stuff %}
{{ stuff }}
{% else %}
{{ no_stuff }}
{% endif %}

{% for i in foo %}
{{ bar }}
{% endfor %}
""")
    print get_variables(test)
