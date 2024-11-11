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

# @register.filter
# def ind(data,fc):
#     return data.index(fc)

@register.filter
def ind(data,fc,si):
    try:
        return data.index(fc,si)
    except ValueError:
        return -1  # or any fallback value


@register.simple_tag
def my_tag(value, arg1, arg2):
    # Process value, arg1, and arg2 as needed
    return f"{value} - {arg1} - {arg2}"


#Getting Index of string's substring from perticular index to perticular index
@register.filter
def my_filter(value, args):
    # Split the arguments by comma
    a1=''
    a2=0
    a3=0
    if len(args)==3:
        a1,a3=args.split(',')
    else:
        a1,a2,a3 = args.split(',')
    # Perform any operation using `value`, `arg1`, and `arg2`
    if (a1)=="":
        return -1
    elif (a2)==0:
        return value.index(a1,0,int(a3))
    elif (a3)==0:
        return value.index(a1,int(a2))
    else:
        return value.index(a1,int(a2),int(a3))
    

@register.filter
def find(value, args):
    if(args in value):
        return value.index(args)
    else:
        return -1
