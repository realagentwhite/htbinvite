curl -s -XPOST https://www.hackthebox.eu/api/invite/generate | sed -e 's/{"success":1,"data":{"code":"//g'|sed -e 's/","format":"encoded"},"0":200}//g' | base64 -d
