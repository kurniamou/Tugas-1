x = input('Masukkan nilai Teori: ')
y = input('Masukkan nilai Praktek ')

if int(x) >= 70 and int(y) >= 70:                   #lulus jika nilai teori dan praktek lebih atau sama dengan 70
    print('Selamat, anda lulus!')
elif int(x) >= 70 and int(y) < 70:                  #harus mengulang ujian praktek karena nilai praktek dibawah 70
    print('Anda harus mengulang ujian Praktek.')
elif int(x) < 70 and int(y) >= 70:                  #harus mengulang ujian Teori karena nilai teori dibawah 70
    print('Anda harus mengulang ujian Teori')       
elif int(x) < 70 and int(y) < 70:                   #harus mengulang ujian Teori dan praktek karena keduanya dibawah 70
    print('Anda harus mengulang ujian Teori dan Praktek')