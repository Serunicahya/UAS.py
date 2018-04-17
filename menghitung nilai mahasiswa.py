def se():
    print("menghitung nilai mahasiswa")

NAMA=raw_input("\tMasukan Nama  :")
UTS =input    ("\tNilai UTS     :")
UAS =input    ("\tNilai UAS     :")
TUGAS=input   ("\tNilai Tugas   :")

print "-----------------------------"
print "\tNama          : ", NAMA
print "\tNilai UTS     : ", UTS
print "\tNilai UAS     : ", UAS
print "\tNilai Tugas   : ", TUGAS
akhir =(UTS+UAS+TUGAS)/3
print "\tNilai Akhir   : ", akhir

print "-----------------------------"
if akhir >80:
    print "\tNilai Huruf   : A"
    print "\tKeterangan    : Lulus"
elif akhir >=70 and akhir <=80:
    print "\tNilai Huruf   : B"
    print "\tKeterangan    : Lulus"
elif akhir >=60 and akhir <=70:
    print "\tNilai Huruf   : C"
    print "\tKeterangan    : Tidak Lulus"
elif akhir >=40 and akhir <=50:
    print "\tNilai Akhir   : D"
    print "\tKeterangan    : Tidak Lulus"
elif akhir >=0 and akhir <=30:
    print "\tNilai Akhir   : E"
    print "\tKeterangan    : Tidak Lulus"
    
