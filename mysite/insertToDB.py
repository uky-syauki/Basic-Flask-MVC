from app import db
from app.models import Admin, Barang, Transaksi
from random import randint
from datetime import datetime
from calendar import monthrange
from sys import argv

class DB:
    def __init__(self):
        self.nama = Admin.query.all()
        self.barang = Barang.query.all()
    def random_tanggal(self,tahun=None,bulan=None):
        try:
            tahun = randint(2020, 2023) if tahun == None else int(tahun)
            bulan = randint(1,12) if bulan == None else int(bulan)
            tanggal = datetime(tahun, bulan, randint(1, monthrange(tahun, bulan)[1]), randint(0,23), randint(0,59), randint(0,59))
            return tanggal
        except:
            tahun = randint(2020, 2023)
            bulan = randint(1,12)
            tanggal = datetime(tahun, bulan, randint(1, monthrange(tahun, bulan)[1]), randint(0,23), randint(0,59), randint(0,59))
            return tanggal
    def InserDataPalsu(self,banyak):
        sebelum = len(Transaksi.query.all())
        print("Start insert to transaksi \nInsert: ")
        for i in range(banyak):
            print(f"\tke {i+1}:{' '*((2 + len(str(banyak))) - len(str(i+1)))}", end="")
            randTime = self.random_tanggal('2020', '0'+str(i))
            randAdmin = Admin.query.get(randint(1,len(self.nama)))
            randBarang = Barang.query.get(randint(1,len(self.barang)))
            db.session.add(Transaksi(timestamp=randTime,kode_barang=randBarang.kode_barang,harga_jual=randBarang.harga_jual,admin_id=randAdmin.id))
            print(f"timestamp={randTime}, kode_barang={randBarang.kode_barang}, admin_id={randAdmin.id}")
        
        db.session.commit()
        print()
        print("Stop insert to transaksi")
        print(f"Total Transaksi sebelumnya: {sebelum}")
        print("Total Transaksi sekarang  : ", len(Transaksi.query.all()))
        print("Selesai!!")

if __name__ == "__main__":
    print(type(argv[1]))
    Database = DB()
    Database.InserDataPalsu(int(argv[1]))
