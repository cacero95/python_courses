from django import template

register = template.Library()
@register.filter(name="hello")
def hello(value):
    print(value)
    name = 'the name is too long' if len(value) > 8 else f'{value}'
    print(name)
    return f"<h2 style='background:green;color:white';>{name}</h2>"