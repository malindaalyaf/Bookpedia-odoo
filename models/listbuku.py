from odoo import api, fields, models


class ListBuku(models.Model):
    _name = 'book.listbuku'
    _description = 'Daftar Buku Yang Tersedia'

    name = fields.Char(string='Name', required=True)
    penulis = fields.Char(string='Nama Penulis', required=True)
    penerbit = fields.Char(string='Nama Penerbit')
    jenis = fields.Selection(string='Jenis Buku', selection=[('non fiksi', 'Non Fiksi'), ('fiksi', 'Fiksi')])
    harga = fields.Integer(string='Harga', required=True)
    stok = fields.Integer(string='Stok', required=True)
    
    
    
    
    
