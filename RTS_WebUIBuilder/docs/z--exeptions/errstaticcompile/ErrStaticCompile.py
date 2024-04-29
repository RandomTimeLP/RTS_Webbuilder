from RTS_Documentations.doclayout import DocLayout

def ErrStaticCompile():
    layout = DocLayout(path="/docs/rts_webuibuilder/exeptions/errstaticcompile")
    container = layout.container
    topbox = layout.topbox
    container.title.displaytext = "Exceptions > ErrStaticCompile"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addCodeBlock("methods",'''# page.py
from RTS_WebUIBuilder import RDocument
                        
def page():
    dom = RDocument(documentRoute="/page", static=True) # note that static is here set to TRUE
                        
    dom.compileDocument() # therefor having this line will raise the Err^StaticCompile exception
    # to fix this, remove the compileDocument() method and "close" the document with an asm() call instead.''')
