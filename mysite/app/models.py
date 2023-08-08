from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Admin(db.Model):
    print("admin")
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(25))
    password = Column(String(25))
    email = Column(String(25))
    transaksi = relationship('Transaksi', back_populates="admin")


class Barang(db.Model):
    print("Barang")
    __tablename__ = "barang"
    id = Column(Integer, primary_key=True, autoincrement=True)
    kode_barang = Column(String(10), index=True, unique=True)
    nama_barang = Column(String(25))
    harga_modal = Column(Integer)
    harga_jual = Column(Integer)
    stok = Column(Integer)
    transaksi = relationship('Transaksi', back_populates="barang")


class Transaksi(db.Model):
    print("transaksi")
    __tablename__ = "transaksi"
    id = Column(Integer, index=True, primary_key=True, unique=True)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    kode_barang = Column(String(10), ForeignKey("barang.kode_barang"))
    harga_jual = Column(Integer)
    admin_id = Column(Integer, ForeignKey("admin.id"))

    admin = relationship("Admin", back_populates="transaksi")
    barang = relationship("Barang", back_populates="transaksi")

class RecordUang(db.Model):
    __tablename__ = "recorduang"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    ket = Column(String(10))
    nilai = Column(Integer)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)