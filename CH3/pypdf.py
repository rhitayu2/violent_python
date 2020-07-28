#!/usr/bin/env python3

import PyPDF2
from PyPDF2 import PdfFileReader

def printMeta(filename):
    pdfFile = PdfFileReader(open(filename, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print(f"[*] PDF Metadata for: {filename}")
    for metaItem in docInfo:
        print(f"[+] {metaItem} : {docInfo[metaItem]}")

def main():
    filename = "/home/norman/Desktop/ANONOPS_The_Press_Release.pdf"
    printMeta(filename)

if __name__ == '__main__':
    main()