from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db
from app.statistik import DataBase, DaftarBarang, KelolaBarang
from app.database import DataBarang
from app.forms import *
from datetime import datetime

# @app.app_context()

@app.route('/api/tambah', methods=['GET','POST'])
def apiTambah():
    if request.method == 'GET':
        return 

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    daftar = [1,2,3]
    if form.validate_on_submit():
        user = db.session.query()
        flash(f'Login reques untuk user {form.username.data}, remember_me {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form, daftar=daftar)

@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    database = DaftarBarang()
    form = TransaksiForm()
    daftar = database.daftar
    data = ["TSK1","TSK2","TSK3"]
    history = database.InfoToday()
    instansInfo = database.instanceInfo()
    if form.validate_on_submit():
        database.kirim(form.kode_barang.data, form.harga_jual.data)
    return render_template('index.html',form=form,data=data, daftar=daftar,history=history,instansInfo=instansInfo)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route("/statistik", methods=['GET','POST'])
def statistik():
    return render_template("statistik.html")


@app.route('/user',methods=['GET','POST'])
def user():
    database = DataBase()
    form = FormDate()
    tahun = database.tahun()
    data_default = {
        'pltx': tahun['dpltx'],
        'pltv': tahun['dpltv'],
        'dnilai': tahun['dnilai'],
        'dpendapatan': tahun['dpendapatan'],
        'total': sum(tahun['dnilai']),
        'total_keuntungan': sum(tahun['dpendapatan']),
        'total_terjual': sum(tahun['dpltv']),
        'total_asset': database.total_asset,
        'total_asset_jual' : database.total_asset_jual,
        'total_barang' : database.total_barang
    }
    if request.method == 'POST' and form.validate_on_submit():
        try:
            if int(form.tahun.data) <= int(datetime.utcnow().strftime("%Y")) and int(form.tahun.data) >= 2019:
                print(bool(form.tahun.data))
                print(bool(form.bulan.data))
                if form.tahun.data and form.bulan.data:
                    print("Trua tahun dan bulan")
                    tanggal = database.tanggal(form.tahun.data,form.bulan.data)
                    # if int(form.bulan.data) <= 12 and int(form.bulan.data) >= 1:
                    data_default = {
                        'pltx': tanggal['dpltx'],
                        'pltv': tanggal['dpltv'],
                        'dnilai': tanggal['dnilai'],
                        'dpendapatan': tanggal['dpendapatan'],
                        'total': sum(tanggal['dnilai']),
                        'total_keuntungan': sum(tanggal['dpendapatan']),
                        'total_terjual': sum(tanggal['dpltv']),
                        'total_asset': database.total_asset,
                        'total_asset_jual' : database.total_asset_jual,
                        'total_barang' : database.total_barang
                        }
                elif form.tahun.data:
                    bulan = database.bulan(form.tahun.data)
                    data_default = {
                        'pltx': bulan['dpltx'],
                        'pltv': bulan['dpltv'],
                        'dnilai':bulan['dnilai'],
                        'dpendapatan': bulan['dpendapatan'],
                        'total': sum(bulan['dnilai']),
                        'total_keuntungan': sum(bulan['dpendapatan']),
                        'total_terjual': sum(bulan['dpltv']),
                        'total_asset': database.total_asset,
                        'total_asset_jual' : database.total_asset_jual,
                        'total_barang' : database.total_barang
                        }
                else:
                    pass
        except:
            pass
    return render_template("user.html",form=form,data_char=data_default)


@app.route('/dasboard', methods=['GET','POST'])
def dasboard():

    database = DataBase()
    form = FormDate()
    tahun = database.tahun()
    data_default = {
        'pltx': tahun['dpltx'],
        'pltv': tahun['dpltv'],
        'dnilai': tahun['dnilai'],
        'dpendapatan': tahun['dpendapatan'],
        'total': sum(tahun['dnilai']),
        'total_keuntungan': sum(tahun['dpendapatan']),
        'total_terjual': sum(tahun['dpltv']),
        'total_asset': database.total_asset,
        'total_asset_jual' : database.total_asset_jual,
        'total_barang' : database.total_barang
    }
    if request.method == 'POST' and form.validate_on_submit():
        try:
            if int(form.tahun.data) <= int(datetime.utcnow().strftime("%Y")) and int(form.tahun.data) >= 2019:
                print(bool(form.tahun.data))
                print(bool(form.bulan.data))
                if form.tahun.data and form.bulan.data:
                    print("Trua tahun dan bulan")
                    tanggal = database.tanggal(form.tahun.data,form.bulan.data)
                    # if int(form.bulan.data) <= 12 and int(form.bulan.data) >= 1:
                    data_default = {
                        'pltx': tanggal['dpltx'],
                        'pltv': tanggal['dpltv'],
                        'dnilai': tanggal['dnilai'],
                        'dpendapatan': tanggal['dpendapatan'],
                        'total': sum(tanggal['dnilai']),
                        'total_keuntungan': sum(tanggal['dpendapatan']),
                        'total_terjual': sum(tanggal['dpltv']),
                        'total_asset': database.total_asset,
                        'total_asset_jual' : database.total_asset_jual,
                        'total_barang' : database.total_barang
                        }
                elif form.tahun.data:
                    bulan = database.bulan(form.tahun.data)
                    data_default = {
                        'pltx': bulan['dpltx'],
                        'pltv': bulan['dpltv'],
                        'dnilai':bulan['dnilai'],
                        'dpendapatan': bulan['dpendapatan'],
                        'total': sum(bulan['dnilai']),
                        'total_keuntungan': sum(bulan['dpendapatan']),
                        'total_terjual': sum(bulan['dpltv']),
                        'total_asset': database.total_asset,
                        'total_asset_jual' : database.total_asset_jual,
                        'total_barang' : database.total_barang
                        }
                else:
                    pass
        except:
            pass
    return render_template("dasboard.html",form=form,data_char=data_default)


@app.route('/kelola', methods=['GET', 'POST'])
def kelola():
    formAdd = BarangAddForm()
    filterForm = FormFilter()
    if request.method == 'POST':
        if formAdd.add.data:
            if formAdd.kode_barang.data and formAdd.nama_barang.data and formAdd.harga_jual.data and formAdd.harga_modal.data and formAdd.stok.data:
                if DataBarang.cek(formAdd.kode_barang.data):
                    flash(f"Error: {formAdd.kode_barang.data} Telah Tersedia","warning")
                else:
                    DataBarang.add(formAdd.kode_barang.data, formAdd.nama_barang.data, formAdd.harga_jual.data, formAdd.harga_modal.data, formAdd.stok.data)
                    flash(f"Berhasil Menambahkan {formAdd.kode_barang.data}","success")
            else:
                flash(f"Error: {formAdd.kode_barang.data} Periksa Inputan","danger")
        elif formAdd.update.data:
            if formAdd.kode_barang.data and (formAdd.nama_barang.data or formAdd.harga_jual.data or formAdd.harga_modal.data or formAdd.stok.data):
                if DataBarang.cek(formAdd.kode_barang.data):
                    try:
                        DataBarang.update(kode_barang=formAdd.kode_barang.data,nama_barang=formAdd.nama_barang.data, harga_jual=formAdd.harga_jual.data, harga_modal=formAdd.harga_modal.data, stok=formAdd.stok.data)
                        flash(f"Update: {formAdd.kode_barang.data}", "success")
                    except:
                        flash(f"Update Err: {formAdd.kode_barang.data}","warning")
                else:
                    flash(f"Err: kode barang {formAdd.kode_barang} tidak terdaftar!","danger")
            else:
                flash(f"Err: Inputan Salah sugest( anda harus mengisi kode barang serta apa yang di update)","danger")
            print(f"Form input kode barang harus di isi")
        elif formAdd.delete.data:
            if formAdd.kode_barang.data:
                if DataBarang.cek(formAdd.kode_barang.data):
                    try:
                        DataBarang.delete(formAdd.kode_barang.data)
                        flash(f"Delete: {formAdd.kode_barang.data} succes!", "success")
                    except:
                        flash(f"Delete: {formAdd.kode_barang.data} Err!", "danger")
                else:
                    flash("Err: Kode Barang tidak terdaftar","danger")
            else:
                flash("Mohon isi form kode barang untuk barang yang ingin di hapus dari daftar","danger")
        elif formAdd.add_stok.data:
            if formAdd.kode_barang.data:
                if formAdd.stok.data:
                    if DataBarang.cek(formAdd.kode_barang.data):
                        DataBarang.add_stok(formAdd.kode_barang.data,formAdd.stok.data)
                        flash(f"Stok {formAdd.kode_barang.data} ditambah {formAdd.stok.data}","success")
                    else:
                        flash(f"Barang {formAdd.kode_barang.data} tidak ditemukan!","danger")
                else:
                    flash(f"Err: Anda tidak mengisi input stok!", "danger")
            else:
                flash(f"Err: anda tidak mengisi input kode barang","danger")
    
    dataBarang = KelolaBarang().getDaftar()
    return render_template('kelola.html',formAdd=formAdd,filterForm=filterForm,dataBarang=dataBarang)


@app.route("/plot", methods=['GET'])
def get_data():
    plot = {
        'Xlabel':['satu','dua','3'],
        'nilai': [1,2,3,4]
    }
    return jsonify(plot)