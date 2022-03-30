from odoo import http, fields, models
from odoo.http import request
import json


class ListBukuCon(http.Controller):
        @http.route(['/listbuku','/listbuku/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
        def getListBuku(self, idnya=None, **kwargs):
            value = []
            if not idnya:
                buku = request.env['book.listbuku'].search([])            
                for a in buku:
                    value.append({"id" : a.id,
                                "judulbuku" : a.name,
                                "jenis" : a.jenis,
                                "penulis" : a.penulis,
                                "penerbit" : a.penerbit,
                                "stok_tersedia" : a.stok,
                                "harga" : a.harga})
                return json.dumps(value)
            else:
                bukuid = request.env['book.listbuku'].search([('id','=',idnya)])
                for a in bukuid:
                    value.append({"id" : a.id,
                                "judulbuku" : a.name,
                                "jenis" : a.jenis,
                                "penulis" : a.penulis,
                                "penerbit" : a.penerbit,
                                "stok_tersedia" : a.stok,
                                "harga" : a.harga})
                return json.dumps(value)
        
        @http.route('/createbuku',auth='user', type='json', methods=['POST'])
        def createBuku(self, **kw):
            if request.jsonrequest:
                if kw['name']:
                    vals = {
                        'name' : kw['name'],
                        'jenis' : kw['jenis'],
                        'penulis' : kw['penulis'],
                        'penerbit' : kw['penerbit'],
                        'stok' : kw['stok'],
                        'harga' : kw['harga'],
                    }
                    bukubaru = request.env['book.listbuku'].create(vals)
                    args = {'succeed': True, "ID" : bukubaru.id}
                    return args
                
        