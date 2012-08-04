import re
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template import Library

register = Library()


@register.filter()
def obfuscate_email(email, autoescape=None):
    """
    Given a string representing an email address,
        returns a mailto link with rot13 JavaScript obfuscation.

    Accepts an optional argument to use as the link text;
        otherwise uses the email address itself.
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    email = re.sub('@', '\\\\100', re.sub('\.', '\\\\056',
                                          esc(email))).encode('rot13')

    rotten_link = """
    <script type="text/javascript">document.write \
    ("%s".replace(/[a-zA-Z]/g, \
    function(c){return String.fromCharCode((c<="Z"?90:122)>=\
    (c=c.charCodeAt(0)+13)?c:c-26);}));</script>""" % (email)

    return mark_safe(rotten_link)
obfuscate_email.needs_autoescape = True
