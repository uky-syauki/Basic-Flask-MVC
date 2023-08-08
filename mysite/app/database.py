from app import db
from app.models import Barang


class DataBarang:
    def add(kode, nama, jual, modal, stok):
        try:
            barang = Barang(kode_barang=kode, nama_barang=nama, harga_jual=jual, harga_modal=modal, stok=stok)
            db.session.add(barang)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    def update(kode_barang=None, nama_barang=None, harga_jual=None, harga_modal=None, stok=None):
        try:
            curren_barang = db.session.query(Barang).filter_by(kode_barang=kode_barang).first()
            curren_barang.kode_barang = kode_barang if kode_barang != None else curren_barang.kode_barang
            curren_barang.nama_barang = nama_barang if nama_barang != None else curren_barang.nama_barang
            curren_barang.harga_jual = harga_jual if harga_jual != None else curren_barang.harga_jual
            curren_barang.harga_modal = harga_modal if harga_modal != None else curren_barang.harga_modal
            curren_barang.stok = stok if stok != None else curren_barang.stok
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    def delete(kode):
        try:
            current_barang = db.session.query(Barang).filter_by(kode_barang=kode).first()
            db.session.delete(current_barang)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    def add_stok(kode,stok):
        try:
            current_barang = db.session.query(Barang).filter_by(kode_barang=kode).first()
            current_barang.stok = current_barang.stok + stok
            db.session.commit()
            print(f"Succes Add stok {kode},{stok}")
        except:
            print(f"Gagal Add stok {kode},{stok}")
            db.session.rollback()
    def cek(kode):
        hasil = db.session.query(Barang).filter_by(kode_barang=kode).first()
        return True if hasil else False




