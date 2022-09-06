#! /usr/bin/env python
# Объединяет файлы по списку, добавляет закладки.
# Параметры вызова:
# pdf-unite имя_итогового_файла список_файлов
# Также записывает meta-данные:
#               автор: имя пользователя;
# заголовок документа: имя директории с файлами
import argparse
import os
import pikepdf

parser = argparse.ArgumentParser()
# Добавляем необходимые нам ключи.
parser.add_argument('fileNameOutput', nargs=1, type=str)
parser.add_argument('fileList', nargs='+', type=str)
options = parser.parse_args()
fileNameOutput = os.path.splitext(options.fileNameOutput[0])[0] + ".pdf"\
    if not os.path.splitext(options.fileNameOutput[0])[1]\
    else options.fileNameOutput[0]
fileList = list(filter(lambda file_ext: file_ext.endswith('.pdf'),
                       options.fileList))
pdf = pikepdf.Pdf.new()
pageCount = 0
with pdf.open_outline() as outline:
    for file in fileList:
        filesPdf = pikepdf.Pdf.open(file)
        pageName = os.path.splitext(os.path.basename(file))[0]
        bookmark = pikepdf.OutlineItem(pageName, pageCount)
        outline.root.append(bookmark)
        pageCount += len(filesPdf.pages)
        pdf.pages.extend(filesPdf.pages)
with pdf.open_metadata() as records:
    records['dc:title'] = os.path.basename(os.path.dirname(fileList[0]))
    records['dc:creator'] = [os.getlogin()]
    records['xmp:CreatorTool'] = 'PDF Unite 0.1'
pdf.save(fileNameOutput)
