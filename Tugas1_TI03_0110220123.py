ulg = 'y'
while (ulg == 'Y') or (ulg == 'y'):
    print("Fitur Kalkulator Biaya Kuliah")
    nim = input("Masukkan nim : ")
    tahun = eval(nim[5:7])
    tambahsks = 0

    def biaya_kuliah():
        bop = 0
        if tahun == 20:
            bop += 4000000
        elif tahun == 19:
            bop += 3500000
        elif tahun == 18:
            bop += 3200000
        elif tahun == 17:
            bop += 2800000
        return bop

    def sks(sks):
        global tambahsks
        def tambahan():
            print("Biaya tambahan untuk ", sks - 15, " sks: ", "Rp.", tambahsks, sep='')
        def tidak_tambah():
            print("Tidak ada tambahan biaya")
        if sks > 15:
            if (tahun <= 20) and (tahun >= 15):
                if tahun == 20:
                    tambahsks = (sks - 15) * 200000
                elif tahun == 19:
                    tambahsks = (sks - 15) * 175000
                elif tahun == 18:
                    tambahsks = (sks - 15) * 150000
                elif tahun == 17:
                    tambahsks = (sks - 15) * 130000
                tambahan()
            else:
                tidak_tambah()
        return tambahsks

    def subsidi(pilih):
        if (pilih == 'y') or (pilih == 'Y'):
            semester = eval(input("Semester berapa Anda sekarang? : "))
            if (semester >= 2) and (semester <= 8):
                subsidi = 0
                for ips in range(semester - 1):
                    ips = 'Masukkan IP ke ' + str(ips + 1) + ' : '
                    subsidi += eval(input(ips))
                subsidi /= (semester - 1)
                print("Anda mendapat subsidi sebesar ", subsidi/4*1000000)
                return subsidi/4*1000000
        print("Anda tidak bisa mengajukan subsidi biaya kuliah")
        return 0
    if (tahun >= 15) and (tahun <= 20):
        print("BOP angkatan 20", tahun, " adalah ", "Rp.", biaya_kuliah(), sep='')
        sks = sks(eval(input("\nJumlah SKS yang diambil semester ini : ")))
        print("Total biaya kuliah : ", "Rp.", biaya_kuliah() + sks, sep='')
        sub = subsidi(
            input("\nApakah Anda ingin mengajukan subsidi biaya kuliah? (Y/T): "))
        print("Total biaya kuliah : ", "Rp.", biaya_kuliah() + sks - eval("sub"))
    else:
        print("Anda Bukan Mahasiswa")
        print("Program Berhenti..")