from ipywidgets import HTML
import jinja2
import os
import html
import mimetypes
import base64
from pathlib import Path

script = os.path.realpath(__file__)
code_basedir = os.path.dirname(script)

class InProcess(HTML):
    def __init__(self, caption):
        super().__init__(
            '''
            <!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            .loader {
              border: 16px solid #f3f3f3;
              border-radius: 50%;
              border-top: 16px solid #50ae55;
              width: 120px;
              height: 120px;
              -webkit-animation: spin 2s linear infinite; /* Safari */
              animation: spin 2s linear infinite;
            }

            /* Safari */
            @-webkit-keyframes spin {
              0% { -webkit-transform: rotate(0deg); }
              100% { -webkit-transform: rotate(360deg); }
            }

            @keyframes spin {
              0% { transform: rotate(0deg); }
              100% { transform: rotate(360deg); }
            }
            </style>
            </head>
            <body>

            <h3>
            ''' +
            caption +
            '''
            </h3>

            <div class="loader"></div>

            </body>
            </html>
            ''')


def inline_base64(filename):
    mimetype = mimetypes.guess_type(filename)
    return "data:" + mimetype[0] + ";base64," + base64.b64encode(Path(filename).read_bytes()).decode('ascii')


def escape_js_multiline(s):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.
    """
    s = s.replace('"', '\\"')
    s = s.replace('\n', "\\n")
    return s

def local_text(filename):
    with open(filename, "r") as f:
        return f.read()


def osmd_score(musicxml):
    templateLoader = jinja2.FileSystemLoader(searchpath=os.path.sep.join((code_basedir, ".")))
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("osmd.html")
    return OSMD(template.render({
        'inline_xml': lambda: escape_js_multiline(musicxml)
    }))


def osmd_score_from_file(xml_file_name, absolute=False):
    if not absolute:
        xml_file_name = os.path.sep.join((code_basedir, xml_file_name))
    return OSMD(osmd_score(local_text(xml_file_name)))


class OSMD(HTML):
    def __init__(self, musicXML):
        super().__init__(
            '<iframe srcdoc="' +
            html.escape(musicXML) +
            '" height=900 width=1000></iframe>')

