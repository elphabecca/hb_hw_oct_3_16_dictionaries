"""
Prints out all the melons in our inventory
"""

from melons import melon_info


def print_melon(melon_name):
    """ Prints details on a melon given the melon name.

    As of 10/3/16, details inclue seedlessness, price, flesh_color, weight, rind_color.
    """

    melon_name = melon_name.title()

    add_dict = {
        "price" : None,
        "seedless" : None,
        "flesh_color" : None,
        "weight" : None,
        "rind_color" : None
    }

    if melon_name in melon_info.keys():
        print melon_name.upper()
        for category, detail in melon_info[melon_name].items():
            print "    %s : %s" % (category, detail)

    else:
        melon_info[melon_name] = add_dict
        print "***New Melon Added: %s***" % (melon_name.upper())
        for category, detail in melon_info[melon_name].items():
            print "    %s : %s" % (category, detail)





