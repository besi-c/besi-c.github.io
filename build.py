#!/bin/python3
# Build site from templates
import os, sys, shutil, toml, sass
from jinja2 import Template, Environment, FileSystemLoader

HOME_DIR = os.getcwd()
TEMPLATES_DIR = "templates"
STYLE_DIR = "style"

LAYOUT_FILE = ".layout.toml"

JINJA_ENV = Environment(loader = FileSystemLoader(["/", os.path.join(HOME_DIR, TEMPLATES_DIR)]))


class Content:
    src = ""
    target = ""
    edit_time = 0

    def __init__(self, src, target):
        self.src = src
        self.target = target
        self.edit_time = os.stat(src).st_mtime
    def updated(self):
        ret = False
        if self.edit_time != os.stat(self.src).st_mtime:
            ret = True
        self.edit_time = os.stat(self.src).st_mtime
        return ret
    def build(self):
        shutil.copy(self.src, self.target)
        print("cp: {} -> {}".format(self.src, self.target))

class Page(Content):
    def build(self):
        try:
            target_file = open(self.target, 'w')
        except:
            try:
                target_file = open(self.target, 'x')
            except:
                os.makedirs(os.path.dirname(self.target))
                target_file = open(self.target, 'x')

        template = JINJA_ENV.get_template(self.src)
        target_file.write(template.render())
        target_file.close()
        print("jinja: {} -> {}".format(self.src, self.target))

class Sass(Content):
    def build(self):
        try:
            target_file = open(self.target, "w")
        except:
            target_file = open(self.target, "x")
        try:
            target_file.write(sass.compile(filename=self.src))
        except Exception as e:
            print(e)
        target_file.close()
        print("sass: {} -> {}".format(self.src, self.target))



with open(LAYOUT_FILE, 'r') as f:
    layout = toml.load(f)

all_content = set()
if "pages" in layout:
    template_dir = os.path.join(HOME_DIR, TEMPLATES_DIR)
    for page in layout["pages"]:
        src_path = os.path.join(template_dir, page["src"])
        target_path = os.path.join(HOME_DIR, page["target"])
        all_content.add(Page(src_path, target_path))
else:
    print("Error: 'pages' missing")
    sys.exit(1)
if "sass" in layout:
    style_dir = os.path.join(HOME_DIR, STYLE_DIR)
    for s in layout["sass"]:
        src_path = os.path.join(style_dir, s["src"])
        target_path = os.path.join(style_dir, s["target"])
        all_content.add(Sass(src_path, target_path))
else:
    print("Error: 'sass' missing")
    sys.exit(1)


for c in all_content:
    c.build()

if "watch" in sys.argv:
    while True:
        for c in all_content:
            if c.updated():
                c.build()
