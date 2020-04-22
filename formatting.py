import math


message_template = """Hello {name},
Thank for joining {website}. We are very
happy to have you with us.
"""

def format_msg(my_name="Sam", my_website="kk.tech"):
    msg = message_template.format(name=my_name, website=my_website)
    return msg
