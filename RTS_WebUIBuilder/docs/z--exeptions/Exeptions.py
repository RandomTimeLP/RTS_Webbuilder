from RTS_Documentations.doclayout import DocLayout

def Exeptions():
    layout = DocLayout(path="/docs/rts_webuibuilder/exeptions")
    container = layout.container
    topbox = layout.topbox
    container.title.displaytext = "Common Exeptions"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addCodeBlock("methods",'''# Exeptions overview
ErrDynamicASM()               # raised in RDocument > Dynamic
ErrStaticCompile()               # raised in RDocument > Static
ErrHeadOrBodyOverwritten()  # (ErrHOBOw) raised in RDocument().asm() and RDocument().compileDocument()
ErrReservedPath()               # raised in RDocument() ''')
