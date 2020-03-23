# Tugas 4

- melihat list file (list)
- meletakkan file (upload)
- mengambil file (download)

## PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

## FITUR

- list : untuk list file pada direktori tertentu
  request : list
  parameter : tidak ada
  response : berhasil -> berhasil

- upload : untuk meletakkan file
  request: upload
  parameter : source, destination
  response: berhasil -> berhasil
            gagal -> File sudah tersedia
            
- download : untuk mengambil file
  request: download
  parameter: filename, nama yang akan disimpan
  response: berhasil -> berhasil
            gagal -> File tidak ditemukan

- jika perintah tidak dikenali akan merespon dengan Perintah salah

