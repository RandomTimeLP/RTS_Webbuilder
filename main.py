from RTS_WebUIBuilder import *
from threading import Thread
from aiohttp import web
from RTS_WebUIBuilder.docs.load import loadDocs

webserver = RWebserver(host="0.0.0.0", port=1992)

threa = Thread(target=loadDocs)
threa.start()

from loginpage import loginPage

loginPage()



async def loginPageHandler(request):
    return web.Response(text=rtswuib_cache.RAW_PAGES.get("/login").compileDocument(), content_type='text/html')


#webserver.add_route(path="/login", handler=loginPageHandler)



webserver.run()
