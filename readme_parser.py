import sys
import re
import urllib.request

arg = sys.argv[1]
fp = urllib.request.urlopen("https://projecteuler.net/problem=" + arg)
text = fp.read().decode("utf8")

ex = re.compile(r'<div class="problem_content".*>((\n|.)+?)<div .*?class="noprint">')

match = re.findall(ex, text)[0][0]
ex = re.compile(r"<.*?>")
res = re.sub(r"<.*?>", "", match)

res = re.sub(r"\r", "", res)
 
print("# Task "+ arg + "\n" + res)
