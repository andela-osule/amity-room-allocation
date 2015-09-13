def flatten(args):
    """This function flattens a nested list.
    """
    if isinstance(args, list):
        return [item for arg in args for item in flatten(arg)]
    else:
        return [args]


def  get_parent(arg):
    """Return parent class of the arg
    """
    return arg.__class__.__base__
