# Copyright (c) 2023 Florian Matter <flmt@mailbox.org>
# Licensed under the MIT License, see below

# The file you want to modify.
TARGET = "path/to/my_lexicon.lift"
# The string to be added to a path.
PREFIX = "/path/to/my/audio/"

from bs4 import BeautifulSoup
with open(TARGET) as fp:
    soup = BeautifulSoup(fp, "xml")
for media in soup.find_all("media"):
    if "href" in media.attrs:
        old = media["href"]
        if PREFIX not in old:
            new = PREFIX + old
            print(f"Changing {old} to:\n{new}")
            media["href"] = new
with open(TARGET, "w") as f:
    f.write(str(soup))

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.