from django import template

register = template.Library()

@register.filter()
def runtimeToHour(value):
    return f"{value//60}h {int(value-((value//60)*60))}m"

@register.filter()
def castList(value):
    return f"{value[0].name} ..."
