from RTS_Documentations.doclayout import DocLayout


def Static():
    layout = DocLayout(path="/docs/rts_webuibuilder/rdocument/static")
    container = layout.container
    topbox = layout.topbox


    container.title.displaytext = "RDocument > Static pages"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addText("RDocument.py",'''Static documents are usefull if you are planning to display content that does not change during runtime.

For example, a static document could be a simple about page, a contact page, login screen etc.
$red$Keep in mind;: Static documents should not be handled by a custom handler and should be made accessible to automounted of the webserver instead.
More about this can be found under the topic $orange$Automounter; in the section $orange$Mounting of Static pages;.''')

    layout.addCodeBlock("initdynamic", '''# page.py
                        
# Simple example of how to create a DYNAMIC document 
from RTS_WebUIBuilder import RDocument
                        
def page():
    dom = RDocument(documentRoute="/page")
                        
    # The documents content goes here
    
    dom.asm()       
''')

    layout.addText("asm", "Static documents $yellow$need to end; with a $yellow$dom.asm(); call.")