# https://github.com/ziishaned/learn-regex/blob/master/translations/README-ru.md

import re
# флаги при компиляции
# rename = re.compile(r"\w+@\w+(?:\.\w+)?")                             # компилируем выражение перед использованием
# print(rename.findall("nuke@ukrnet"))
# print(rename.findall("nuke@ukr.net"))
# -------------------------------------------
# rename = re.compile(r"\w+[.]\w+")                                     # компилируем выражение перед использованием
# print(rename.findall("nukeukr.net dsfgvd. dfd dfvdsv.dfdgadfgv"))
# -------------------------------------------
# rename = re.compile(r"n\w*[.]\w+")                                      # компилируем выражение перед использованием
# print(rename.findall("nkr.net"))
# -------------------------------------------
# a = re.compile(r"""\d + # the integral part
#                \.       # the decimal point
#                \d*      # some fractional digits""", re.X)              # флаг re.X добавляет коментарии
# b = re.compile(r"\d+\.\d*")
# print(a.findall("441.60"))
# print(b.findall("441.60"))


# ==========================================================
# sub
# print(re.sub(r"(\w+).(\w+)", r"\2-\1", "qqq.XXX ppp.WER"))                      # sub заменяет первое слово(\w+) на второе - первое -> XXX-qqq WER-ppp
# print(re.sub(r"(?P<one>\w+).(?P<two>\w+)", r"\g<two>-\g<one>", "qqq.XXX ppp.WER"))   # XXX-qqq WER-ppp


# ==========================================================

# groupdict служит для того чтобы сослаться на именованные групы "?P<one>, ?P<two>"
res = re.search(r"((?P<one>A+)\s*(?P<two>B+))", "qweAAA BBB sljfv jsdfv A BBB AA")          
print(res.group())                                                                          # AAA BBB
print(res.groupdict())                                                                      # {'gro': 'AAA'}
print(res.groupdict()["one"])                                                               # AAA









