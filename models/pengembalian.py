from email.policy import default
from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'book.pengembalian'
    _description = 'Pengembalian Buku'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    order_id = fields.Many2one(comodel_name='book.order', string='Order')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['book.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan').name

    tgl_pengembalian = fields.Date(string='', default=fields.Date.today())
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.model
    def create(self,vals):
        record = super(Pengembalian, self).create(vals) 
        if record.tgl_pengembalian:
            self.env['book.order'].search([('id','=',record.order_id.id)]).write({'sudah_kembali':True}) 
            self.env['book.akunting'].create({'kredit' : record.tagihan, 'name': record.name})          
            return record

    def unlink(self):
        for x in self:
            self.env['book.order'].search([('id','=',x.order_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()
        
        
    
    