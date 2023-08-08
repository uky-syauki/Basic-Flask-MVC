from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Login")


class FormFilter(FlaskForm):
    cari = StringField("Filter")
    kode_barang = SubmitField("by Kode")
    nama_barang = SubmitField("by Nama")


class FormDate(FlaskForm):
    tahun = StringField("Tahun")
    bulan = StringField("Bulan")
    submit = SubmitField("Tampilkan")


class TahunForm(FlaskForm):
    pilihan = RadioField('Tahun: ', choices=[
        ('opsi1','Opsi 1'),
        ('opsi2','Opsi 2'),
        ('opsi3','Opsi 3')
    ])
    submit = SubmitField("Submit")


class TransaksiForm(FlaskForm):
    kode_barang = StringField("Kode Barang")
    harga_jual = IntegerField("Harga Jual")
    submit = StringField("Kirim")


class BarangAddForm(FlaskForm):
    kode_barang = StringField("Kode Barang")
    nama_barang = StringField("Nama Baragn")
    harga_jual = IntegerField("Harga Jual")
    harga_modal = IntegerField("Harga Modal")
    stok = IntegerField("Stok")
    add = SubmitField("Add")
    update = SubmitField("Update")
    delete = SubmitField("Delete")
    add_stok = SubmitField("Add Stok")



# class BarangUpdate(FlaskForm):
#     kode_barang = StringField("Kode Barang")
#     nama_barang = StringField("Nama Baragn")
#     harga_jual = IntegerField("Harga Jual")
#     harga_modal = IntegerField("Harga Modal")
#     stok = IntegerField("Stok")
#     submit = SubmitField("Update")