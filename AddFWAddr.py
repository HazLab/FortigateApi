import FortigateApi

fgt = FortigateApi.Fortigate('192.168.123.120', 'root', 'admin', 'NeverKnow1@3$')

fgt.AddFwAddress('NEW1', '192.121.1.1/32', '', '')

