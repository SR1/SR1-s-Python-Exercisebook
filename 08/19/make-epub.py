#!/usr/bin/python
#@coding=utf-8
#@Author: SR1
#@Date: 2013-08-19

import os

class epub_builder:
    def __init__(self, build_path):
        '''build the basic content & directory of an epub book'''
        self.work_path = build_path
        self.epub_dir = "%s/%s" % (self.work_path,"book")
        self.epub_dir_META = "%s/%s" % (self.epub_dir,"META-INF")
        self.epub_dir_OPS = "%s/%s" % (self.epub_dir,"OPS")
        self.__build_framework()

    def __build_framework(self):
        '''build the basic content & directory of an epub book'''
        # build the directory of an epub book
        if not os.path.exists(self.epub_dir):
            os.mkdir(self.epub_dir)
        # build META-INF directory of book
        if not os.path.exists(self.epub_dir_META):
            os.mkdir(self.epub_dir_META)
        # build OPS directory of book
        if not os.path.exists(self.epub_dir_OPS):
            os.mkdir(self.epub_dir_OPS)
        mimetype_content = 'application/epub+zip'
        mime = open("%s/%s" % (self.epub_dir,'mimetype'),'w')
        mime.write(mimetype_content)
        mime.close()
        
        container_content = '<?xml version="1.0" encoding="UTF-8" ?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n    <rootfiles>\n        <rootfile full-path="OPS/fb.opf" media-type="application/oebps-package+xml"/>\n    </rootfiles>\n</container>'
        container = open("%s/%s" % (self.epub_dir_META,'container.xml'),'w')
        container.write(container_content)
        container.close()

    def make_book(self):
        zip_command = "zip -qr %s %s" % (os.sep.join((self.work_path, 'book.epub')), self.epub_dir)
        if os.system(zip_command) == 0:
            print zip_command
            print 'build epub book successfully'
            return True
        else:
            print 'build epub book failed'
            return False

work_path = os.getcwd()
book = epub_builder(work_path)
book.make_book()

