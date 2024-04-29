from RTS_Documentations.doclayout import DocLayout

def ErrHOBOw():
    layout = DocLayout(path="/docs/rts_webuibuilder/exeptions/errheadorbodyoverwritten")
    container = layout.container
    topbox = layout.topbox
    container.title.displaytext = "Exceptions > ErrHeadOrBodyOverwritten"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addCodeBlock("methods",'''# page.py
from RTS_WebUIBuilder import RDocument , RBox , RLable
from .predefinedRBody import predefinedRBody
                        
def page():
    dom = RDocument(documentRoute="/page") 
                        
    dom.body = RBox() # this will raise the ErrHeadOrBodyOverwritten
    
    dom.head = RLable() # this will also raise the ErrHeadOrBodyOverwritten

    # to fix this just access head and body right a way like this 
    body = dom.body
    body.box = RBox() 
    
    # or this works as well
    
    dom.body.box = RBox()
    
    # or asuming you already have an element that is an instance of RBody you can do this
    dom.body = predefinedRBody # this will not raise the exception 
                        
    # same goes for head with its respective methods
    # ...
                        
    dom.asm()''')

    layout.addCodeBlock("predefinedRBody",'''# predefinedRBody.py
from RTS_WebUIBuilder import RBody , RLabel

class predefinedRBody(RBody):
    def __init__(self):
        self.lable = RLabel() 
        #...
''',filt=True)


