"""
Use livereload to serve the talk slides for local inspection.
"""
import livereload

watch = [
    "index.html",
    "slides.md",
    "css",
    "images",
]

server = livereload.Server()
for path in watch:
    server.watch(path)
server.serve(root=".", port=8000, host="localhost", open_url_delay=1)
