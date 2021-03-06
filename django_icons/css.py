from collections import OrderedDict


def _merge_css_item(item):
    """
    Process arguments
    """
    # Recurse lists and tuples to combine into single list
    if isinstance(item, (list, tuple)):
        return _merge_css_list(*item)
    # Cast to string, be sure to cast falsy values to ''
    item = "{}".format(item) if item else ""
    # Return as a list
    return [item]


def _merge_css_list(*args):
    """
    Iterate over all arguments
    """
    css_list = []
    for a in args:
        css_list += _merge_css_item(a)
    return css_list


def merge_css_list(*args):
    """
    Takes a series of strings and lists and combines them into a single list of unique CSS classes.
    Removes duplicates. Gives precedence to first class encountered.
    """
    # Combine args into a single list
    css_list = _merge_css_list(*args)
    # There may be strings with multiple classes in the array, so combine the values into a string ...
    css_string = " ".join(css_list)
    # ... and split the string back to a list, also takes care of all whitespace, including tabs and newlines
    css_list = css_string.split()
    # Remove empty values from the list
    css_list = filter(None, css_list)
    # Remove duplicates, see https://stackoverflow.com/questions/480214/
    css_list = list(OrderedDict.fromkeys(css_list))
    # Return the list
    return css_list


def merge_css_text(*args):
    """
    Takes a series of strings and lists and combines them into one space separated string of unique CSS classes.
    Removes duplicates. Gives precedence to first class encountered.
    """
    return " ".join(merge_css_list(*args))
