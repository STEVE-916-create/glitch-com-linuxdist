#!/usr/bin/python3

import os
this_py_file_path = os.path.abspath(".")+"/"
from http.server import HTTPServer, SimpleHTTPRequestHandler
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        SimpleHTTPRequestHandler.__init__(self, request, client_address, server, directory=this_py_file_path+"out/")
print("make[1]: target is python haha")
if os.path.exists(this_py_file_path+"deb/"):
    os.makedirs(this_py_file_path+"out/", exist_ok=True)
    print("Creating glitch.tar.gz...")
    with open(this_py_file_path+"compile.cache.sh", "wt") as f:
        f.write("#!/usr/bin/bash\n")
        f.write("\n")
        f.write("cd "+this_py_file_path+"deb\n")
        f.write("tar -czf "+this_py_file_path+"out/glitch.tar.gz "+this_py_file_path+"deb/*.deb\n")
    os.system("bash "+this_py_file_path+"compile.cache.sh")
    os.system("rm "+this_py_file_path+"compile.cache.sh")
    print("Summoning glitch.tar.gz...")
    print("Writing boot.sh...")
    with open(this_py_file_path+"out/boot.sh", "wt") as f:
        f.write("#!/usr/bin/bash\n")
        f.write("\n")
        f.write("# Change this variable.\n")
        f.write("GLITCH_COM_TAR_GZ=\"\"\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("# Unpack if no exist.\n")
        f.write("if [ ! -d \"/tmp/glvfs\" ]\n")
        f.write("then\n")
        f.write("  mkdir /tmp/glvfs/\n")
        f.write("  mkdir /tmp/glvfs/debs/\n")
        f.write("  cd /tmp/glvfs/\n")
        f.write("  wget -O /tmp/glvfs/glitch.tar.xz $GLITCH_COM_TAR_GZ\n")
        f.write("  cd /tmp/glvfs/debs/\n")
        f.write("  tar -xzf /tmp/glvfs/glitch.tar.xz\n")
        f.write("  cd /tmp/glvfs/\n")
        f.write("  find /tmp/glvfs/debs -maxdepth 1 -type f -exec dpkg --extract {} /tmp/glvfs/ \\;\n")
        f.write("fi\n")
        f.write("# Environment variables. Do. Not. Touch. Unless you know what you're doing.\n")
        f.write("export PATH=\"/tmp/glvfs/bin:/tmp/glvfs/usr/bin:/tmp/glvfs/usr/local/bin:/tmp/glvfs/sbin:$PATH\" \n")
        f.write("export CPATH=\"/tmp/glvfs/include:/tmp/glvfs/usr/include:$CPATH\" \n")
        f.write("export LD_LIBRARY_PATH=\"/tmp/glvfs/usr/lib:/tmp/glvfs/lib:/tmp/glvfs/lib:$LD_LIBRARY_PATH\" \n")
        f.write("export LIBRARY_PATH=\"/tmp/glvfs/usr/lib:/tmp/glvfs/lib:/tmp/glvfs/lib:$LIBRARY_PATH\" \n")
    print("boot.sh is good.")
    print("Hosting server...")
    print("Pro-Tip: hit Ctrl+C to exit")
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
else:
    print("Non-existent deb folder. Used apt.py yet?")