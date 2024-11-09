from django import template as t

register=t.Library()

def swap(data):
    return data.swapcase()

register.filter('Swapping',swap)

@register.filter
def length(data):
    return len(data)

@register.filter
def rev(data):
    return "".join(list(data)[::-1])

@register.filter
def ind(data,fc,sr,si):
    return data.index(fc,sr,si)