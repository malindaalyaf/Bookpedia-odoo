from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'book.order'
    _description = 'Tabel untuk meminjam buku'

    orderdetail_ids = fields.One2many(
        comodel_name='book.order_detail', 
        inverse_name='order_id', 
        string='Detail Peminjaman')

    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan', default=fields.Datetime.now())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan',
        domain=[('is_customernya','=', True)])
    
    
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['book.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = a
    
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    def kembali_barang(self):
        pass
    
    
class OrderDetail(models.Model):
    _name = 'book.order_detail'
    _description = 'Detail peminjaman buku'

    order_id = fields.Many2one(comodel_name='book.order', string='Peminjaman')
    listbuku_id = fields.Many2one(comodel_name='book.listbuku', string='Buku')
    
    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    qty = fields.Integer(string='Jumlah')
    
    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['book.listbuku'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok buku yang dipilih tidak cukup")

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('listbuku_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.listbuku_id.harga
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(OrderDetail, self).create(vals) 
        if record.qty:
            self.env['book.listbuku'].search([('id','=',record.listbuku_id.id)]).write({'stok':record.listbuku_id.stok-record.qty})
            return record

