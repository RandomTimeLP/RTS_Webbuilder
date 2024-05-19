from RTS_WebUIBuilder import RDocument, RWebserver, RLabel
from RTS_WebUIBuilder.presets.Button1 import Button1

webs = RWebserver(host='0.0.0.0',port=80)

def main(webs):
    print("Starting Webserver on port ", webs.port)

    dom = RDocument(documentRoute="/killme")

    dom.body.title = RLabel()
    dom.body.title.displaytext = "Kill me already!"
    dom.asm()

webs.run(main, webs=webs)

