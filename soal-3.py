x = input('Masukkan nilai Teori: ')
y = input('Masukkan nilai Praktek ')

if int(x) >= 70 and int(y) >= 70:
    print('Selamat, anda lulus!')
elif int(x) >= 70 and int(y) < 70:
    print('Anda harus mengulang ujian Praktek.')
elif int(x) < 70 and int(y) >= 70:
    print('Anda harus mengulang ujian Teori')
elif int(x) < 70 and int(y) < 70:
    print('Anda harus mengulang ujian Teori dan Praktek')