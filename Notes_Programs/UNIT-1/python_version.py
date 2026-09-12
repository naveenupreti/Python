import sys
import platform
import keyword
print("Python version:",sys.version)
print("OS:",platform.system())
print("OS version:",platform.version())
print("Keywords List:",keyword.kwlist)
print("Number of Keywords:",len(keyword.kwlist))
