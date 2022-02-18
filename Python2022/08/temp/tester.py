

with open('TExt_files/python.jpg', 'rb') as file:
  with open('TExt_files/python.jpg', 'wb') as wfile:
    chunk_size = 4096
    file_chunk = file.read(chunk_size)
    while len(file_chunk) > 0:
      wfile.write(file_chunk)
      file_chunk = file.read(chunk_size)