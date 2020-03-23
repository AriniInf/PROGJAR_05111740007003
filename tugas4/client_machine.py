import json
import base64
from files import Files

'''
PROTOCOL FORMAT
setiap paket request memiliki format json dan selalu memuat key "cmd" 
yang merupakan command request

FITUR:
- list : melihat daftar file
  command   : list
  parameter : none
  response  : { 'res' : 'OK', 'list' : daftar file }
- put : meletakkan file
  command   : put
  parameter : filename, content
  response  : berhasil          -> { 'res' : 'OK'}
              gagal (duplicate) -> { 'res' : 'ERRDUP' }
- get : mengambil file
  command   : get
  parameter : filename
  response  : berhasil          -> { 'res' : 'OK', 'content' : isi file }
              gagal (Not Found) -> { 'res' : 'ERRNF', 'content' : None }
- jika command tidak dikenali
  response  : { 'res' : 'ERRCMD' }
'''

class Client_machine:
    def __init__(self):
        self.files = Files()
    
    def run(self, json_proses):
        objek = json.loads(json_proses)
        massage = {}
        # try:
        perintah = objek['perintah']
        if perintah == 'list':
            massage['list'] = self.files.list_file()
            respon = 'Berhasil'
        elif perintah == 'upload':
            filename = objek['filename']
            data = objek['isi']
            isi = data.encode()
            ret_val = self.files.upload_file(filename, isi)
            respon = 'Berhasil' if ret_val else 'ERRDUP'
        elif perintah == 'download':
            filename = objek['filename']
            ret_val, binary = self.files.download_file(filename)
            isi = binary.decode()
            massage['isi'] = isi
            respon = 'Berhasil' if ret_val else 'ERRNF'
        else:
            respon = 'ERRCMD'
        # except:
        #   print(e.what())
        #   respon = 'ERROR'
        # finally:
        massage['respon'] = respon
        return json.dumps(massage)
if __name__=='__main__':
    cm = Client_machine()