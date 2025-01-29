
def format_name(fname, lname):
    """Sample doc String
    Can also be used in multiple lines """
    upper_fname = fname.title()
    lower_lname = lname.title()
    return f"{upper_fname} {lower_lname}"

print(format_name("niikwartei","quartey"))