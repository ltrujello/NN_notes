#!/usr/bin/env python3
import re
import textwrap
from tikzpy import TikzPicture
tex_contents = ""

python_stmt = re.compile("(\\\\begin{python}([\s\S]*?)\\\\end{python})")


def convert_python_to_tikz_code(contents):
    tikz = TikzPicture()
    # de-indent the code
    contents = textwrap.dedent(contents)
    print(contents) 
    exec(contents, locals())
    return tikz.code()

with open("nn_notes.tex") as f:
   contents = f.read()

c = re.finditer(python_stmt, contents)
new_contents = []
ind = 0
for obj in c:
    python_code = obj.group(2)
    start_ind = obj.start()
    end_ind = obj.end()

    new_contents.append(contents[ind:start_ind])
    tikz_code = convert_python_to_tikz_code(python_code)
    new_contents.append(tikz_code)
    ind = end_ind
new_contents.append(contents[ind:])

new_file = "".join(new_contents)
with open("nn_notes_raw.tex", "w") as f:
    f.write(new_file)

