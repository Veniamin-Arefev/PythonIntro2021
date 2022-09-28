import re
import zipfile
import io
import sys

file = zipfile.ZipFile(io.BytesIO(bytes.fromhex(re.sub("\s", "", sys.stdin.read()))), 'r')
print(f"{sum(map(lambda x: not x.is_dir(), file.infolist()))} {sum(map(lambda x: x.file_size, file.infolist()))}")
