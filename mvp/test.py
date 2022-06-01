import sys
import io
# create file-like string to capture output
codeOut = io.StringIO()
codeErr = io.StringIO()
code = "df = 1+{}".format(1)
print("check")
# capture output and errors
sys.stdout = codeOut
sys.stderr = codeErr
print("check")
exec(code)
print("check")
# restore stdout and stderr
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__


output_error = codeErr.getvalue()
output = codeOut.getvalue()

codeOut.close()
codeErr.close()