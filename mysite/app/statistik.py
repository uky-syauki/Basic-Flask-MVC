
from app import app, db
from app.models import Admin, Barang, Transaksi
from sqlalchemy import func
from datetime import datetime
from calendar import monthrange


# @app.app_context()

def toDict(arr):
    hasil = {}
    for isi in arr:
        hasil[isi[0]] = [isi[1],isi[2]]
    return hasil


class KelolaBarang:
    def __init__(self):
        self.barang = Barang.query.all()
    def getDaftar(self):
        hasil = []
        for isi in self.barang:
            hasil.append([isi.kode_barang, isi.nama_barang, isi.harga_jual, isi.harga_modal, isi.stok])
        
        jumlah = len(hasil)
        for i in range(jumlah):
            for j in range(jumlah):
                if hasil[i][4] < hasil[j][4]:
                    hasil[i], hasil[j] = hasil[j], hasil[i]
        hasilDict = {}
        for i in range(len(hasil)):
            hasilDict[hasil[i][0]] = hasil[i]

        return [hasil, hasilDict]


class DaftarBarang:
    def __init__(self):
        self.daftar = db.session.query(Barang.kode_barang, Barang.nama_barang, Barang.harga_jual).all()
        self.daftar = toDict(self.daftar)
        self.current_date = datetime.now()
    def instanceInfo(self):
        data = self.InfoToday()
        hasil = {
            'total':0,
            'total_nilai':0,
            'total_hasil':0
        }
        for isi in data:
            hasil['total'] += 1
            hasil['total_nilai'] += isi[3]
            hasil['total_hasil'] += isi[4]
        return hasil
    def InfoToday(self):
        current_date = datetime.now()
        current_date = [current_date.year, current_date.month, current_date.day]
        info_today = db.session.query(Transaksi.timestamp, Transaksi.kode_barang, Barang.nama_barang, Transaksi.harga_jual, Barang.harga_modal, Transaksi.admin_id).filter(
            func.extract('year', Transaksi.timestamp) == current_date[0],
            func.extract('month', Transaksi.timestamp) == current_date[1],
            func.extract('day', Transaksi.timestamp) == current_date[2]
        ).join(Barang).all()
        hasil = []
        for i in range(len(info_today)):
            tmp = []
            for j in range(len(info_today[i])):
                if j == len(info_today[i])-1:
                    nama = Admin.query.get(info_today[i][j])
                    tmp.append(nama.nama)
                else:
                    tmp.append(info_today[i][j])
            hasil.append(tmp)
        return hasil

class DataBase:
    def __init__(self):
        # self.data = Transaksi.query.all()
        self.allData = db.session.query(Transaksi.timestamp,Transaksi.kode_barang, Transaksi.harga_jual, Barang.harga_modal,Barang.nama_barang).join(Barang).all()
        self.total_asset = db.session.query(func.sum(Barang.harga_modal * Barang.stok)).scalar()
        self.total_asset_jual = db.session.query(func.sum(Barang.harga_jual * Barang.stok)).scalar()
        self.total_barang = db.session.query(func.sum(Barang.stok)).scalar()
    def kirim(self,kode=None, harga=None):
        print(f"Debug: {kode}, {harga}")
    def bulan(self,th):
        json = {
            'dpltx': [],
            'dpltv':[],
            'dnilai':[],
            'dpendapatan':[],
            'dbarang':[]
        }

        tampungan = {}
        for isi in self.allData:
            xth = isi[0].strftime("%Y")
            if xth == th:
                xbl = isi[0].strftime("%m")
                if xbl not in tampungan.keys():
                    tampungan[xbl] = {
                        'total_trx':0,
                        'nilai_penjualan':0,
                        'nilai_pendapatan':0,
                        'barang_terjual':{}
                    }
                tampungan[xbl]['total_trx'] += 1
                tampungan[xbl]['nilai_penjualan'] += isi[2]
                tampungan[xbl]['nilai_pendapatan'] += (isi[2] - isi[3])
                if isi[4] not in tampungan[xbl]['barang_terjual'].keys():
                    tampungan[xbl]['barang_terjual'][isi[4]] = 0
                tampungan[xbl]['barang_terjual'][isi[4]] += 1

        for key in tampungan.keys():
            json['dpltx'].append(key)
            json['dpltv'].append(tampungan[key]['total_trx'])
            json['dnilai'].append(tampungan[key]['nilai_penjualan'])
            json['dpendapatan'].append(tampungan[key]['nilai_pendapatan'])
            json['dbarang'].append(tampungan[key]['barang_terjual'])

        return json
    def tahun(self):
        json = {
            'dpltx': [],
            'dpltv':[],
            'dnilai':[],
            'dpendapatan':[],
            'dbarang':[]
        }

        tampungan = {}
        for isi in self.allData:
            th = isi[0].strftime("%Y")
            if th not in tampungan.keys():
                tampungan[th] = {
                    'total_trx':0,
                    'nilai_penjualan':0,
                    'nilai_pendapatan':0,
                    'barang_terjual':{}
                }
            tampungan[th]['total_trx'] += 1
            tampungan[th]['nilai_penjualan'] += isi[2]
            tampungan[th]['nilai_pendapatan'] += (isi[2] - isi[3])
            if isi[4] not in tampungan[th]['barang_terjual'].keys():
                tampungan[th]['barang_terjual'][isi[4]] = 0
            tampungan[th]['barang_terjual'][isi[4]] += 1

        for key in tampungan.keys():
            json['dpltx'].append(key)
            json['dpltv'].append(tampungan[key]['total_trx'])
            json['dnilai'].append(tampungan[key]['nilai_penjualan'])
            json['dpendapatan'].append(tampungan[key]['nilai_pendapatan'])
            json['dbarang'].append(tampungan[key]['barang_terjual'])
        # del tampungan

        return json
    def tanggal(self,th,bl):
        bl = int(bl)
        if bl < 10:
            bl = f"0{bl}"
        else:
            bl = str(bl)
        json = {
            'dpltx': [],
            'dpltv':[],
            'dnilai':[],
            'dpendapatan':[],
            'dbarang':[]
        }
        tampungan = {}
        for isi in self.allData:
            xth = isi[0].strftime("%Y")
            if xth == th:
                xbl = isi[0].strftime("%m")
                if xbl == bl:
                    tgl = isi[0].strftime("%d")
                    if tgl not in tampungan.keys():
                        tampungan[tgl] = {
                            'total_trx':0,
                            'nilai_penjualan':0,
                            'nilai_pendapatan':0,
                            'barang_terjual':{}
                        }
                    tampungan[tgl]['total_trx'] += 1
                    tampungan[tgl]['nilai_penjualan'] += isi[2]
                    tampungan[tgl]['nilai_pendapatan'] += (isi[2] - isi[3])
                    if isi[4] not in tampungan[tgl]['barang_terjual'].keys():
                        tampungan[tgl]['barang_terjual'][isi[4]] = 0
                    tampungan[tgl]['barang_terjual'][isi[4]] += 1
        for key in tampungan.keys():
            json['dpltx'].append(key)
            json['dpltv'].append(tampungan[key]['total_trx'])
            json['dnilai'].append(tampungan[key]['nilai_penjualan'])
            json['dpendapatan'].append(tampungan[key]['nilai_pendapatan'])
            json['dbarang'].append(tampungan[key]['barang_terjual'])

        return json


app.app_context().push()
class DataStatistik:
    def __init__(self):
        self.totaltransaksi = db.session.query(func.count(Transaksi.id)).scalar()
        self.totalnilaitransaksi = db.session.query(Transaksi).join(Barang).with_entities(func.sum(Transaksi.harga_jual - Barang.harga_modal)).scalar()
        self.totalnilai = db.session.query(func.sum(Transaksi.harga_jual)).scalar()
        self.totalnilaibersih = self.totalnilaitransaksi - self.totalnilai
    def getTotalTransaksi(self):
        return self.totaltransaksi
    def getTotalNilaiTransaksi(self):
        return self.totalnilaitransaksi
    def getTotalNilai(self):
        return self.totalnilai
    def getNilaiBersih(self):
        return self.totalnilaibersih


# print(DataStatistik.get())

