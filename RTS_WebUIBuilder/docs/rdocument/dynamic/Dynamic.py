from RTS_Documentations.doclayout import DocLayout


def Dynamic():
    layout = DocLayout(path="/docs/rts_webuibuilder/rdocument/dynamic")
    container = layout.container
    topbox = layout.topbox


    container.title.displaytext = "RDocument > Dynamic pages"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addText("RDocument.py",'''Dynamic documents are usefull if you are planning to display content in different languages or things like warehouse stock or other content that changes a lot during runtime.

$red$Keep in mind; that dynamic documents that contain $yellow$user specific content; should be handled $yellow$by a custom handler; and $yellow$not be automounted; to the webserver.
More about this can be found under the topic $orange$Automounter;.''')

    layout.addCodeBlock("initdynamic", '''# page.py
                        
# Simple example of how to create a DYNAMIC document 
from RTS_WebUIBuilder import RDocument
                        
def page():
    dom = RDocument(documentRoute="/page", static=False)
                        
    # The documents content goes here
    
    # no need to call dom.asm() here        
''')

    layout.addText("asm", '''Dynamic documents $yellow$can not need; to end with a $yellow$dom.asm(); call.
If you do, you will get the error $red$ErrDynamicASM;.''')
    