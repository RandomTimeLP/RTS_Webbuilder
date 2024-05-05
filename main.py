from RTS_WebUIBuilder import RDocument, RWebserver, RLabel

webs = RWebserver(host='0.0.0.0',port=8080)

def main(webs):
    print("Starting Webserver on port ", webs.port)

    dom = RDocument(documentRoute="/killme")

    dom.body.title = RLabel()
    dom.body.title.displaytext = "Kill me already!"
    dom.asm()

webs.run(main, webs=webs)

