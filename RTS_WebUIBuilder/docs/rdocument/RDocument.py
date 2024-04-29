from RTS_Documentations.doclayout import DocLayout


def RDocument():
    layout = DocLayout(path="/docs/rts_webuibuilder/rdocument")
    container = layout.container
    topbox = layout.topbox
    container.title.displaytext = "RDocument"
    topbox.moduleTitle.displaytext = "RTS Web UI Builder"

    layout.addCodeBlock("methods",'''# Method overview
.importFonts(font:str, fontURL:str) -> None
.defaultFont(font:str) -> None
                        
.compileDocument() -> str
# read more in RDocument > Dynamic 
                        
.asm() -> None
# read more in RDocument > Static 
''')

    layout.addText("compile", '''$yellow$compileDocument(); method is used to optain the compiled html of any $yellow$dynamic; document.''')
    layout.addText("asm", '''$yellow$asm(); method is used to compile a $yellow$static; document and store it in the cache.''')