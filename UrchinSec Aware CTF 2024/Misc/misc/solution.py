#!/usr/bin/env python3

from pdfquery import PDFQuery
from pdfquery.cache import FileCache
import inspect
import json
from PIL import Image, ImageDraw

pdf = PDFQuery("./Etiquette_Book.pdf", parse_tree_cacher=FileCache("/tmp/"))
pdf.load()
elements = pdf.pq("LTLine")
xMax = 645
yMax = 534
im = Image.new("RGBA", (xMax, yMax + 1), (0, 0, 0, 255))
draw = ImageDraw.Draw(im)

p = elements[0].getparent().getparent().getparent().getparent().getparent()
pixel = 1
pages = []
for i, e in enumerate(elements):
    p = e.getparent().getparent().getparent().getparent().getparent()
    idx = int(p.attrib["page_index"])
    count = 1 + (idx - len(pages))
    if count > 0:
        for _ in range(count):
            pages.append([])

    pages[idx].append(e)

for i, lines in enumerate(pages):
    if len(lines) != 2:
        continue

    top = lines[0]
    bottom = lines[1]

    topPts = json.loads(top.attrib["pts"])
    botPts = json.loads(bottom.attrib["pts"])

    topPts[0][1] = yMax - topPts[0][1]
    topPts[1][1] = yMax - topPts[1][1]

    botPts[0][1] = yMax - botPts[0][1]
    botPts[1][1] = yMax - botPts[1][1]

    pts = [topPts[0], topPts[1], botPts[0], botPts[1]]
    pts.sort(key=lambda x: x[1])

    print(pts)
    print((pixel, pts[1][1], pixel, pts[2][1]))
    draw.line((pixel, pts[1][1], pixel, pts[2][1]), fill="white", width=1)
    pixel += 1


draw.line((0, 0, xMax, 0), fill="red", width=1)
draw.line((xMax, 0, xMax, yMax), fill="red", width=1)
draw.line((0, yMax, xMax, yMax), fill="red", width=1)
draw.line((0, 0, 0, yMax), fill="red", width=1)
print(xMax, yMax, len(elements))
im.save("lines.png")
