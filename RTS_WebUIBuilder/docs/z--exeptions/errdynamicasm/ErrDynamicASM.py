from RTS_Documentations.doclayout import DocLayout

def ErrDynamicASM():
    layout = DocLayout(path="/docs/rts_webuibuilder/exeptions/errdynamicasm")
    container = layout.container
    topbox = layout.topbox
    container.title.displaytext = "Exceptions > ErrDynamicASM"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addCodeBlock("methods",'''# page.py
from RTS_WebUIBuilder import RDocument
                        
def page():
    dom = RDocument(documentRoute="/page", static=False) # note that static is here set to FALSE
                        
    dom.asm() # therefor having this line will raise the ErrDynamicASM exception
    # to fix this, remove the asm() method and leave it "open ended" due to its dynamic nature.''')
