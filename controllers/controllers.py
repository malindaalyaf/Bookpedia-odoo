# -*- coding: utf-8 -*-
# from odoo import http


# class Bookpedia(http.Controller):
#     @http.route('/bookpedia/bookpedia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookpedia/bookpedia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookpedia.listing', {
#             'root': '/bookpedia/bookpedia',
#             'objects': http.request.env['bookpedia.bookpedia'].search([]),
#         })

#     @http.route('/bookpedia/bookpedia/objects/<model("bookpedia.bookpedia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookpedia.object', {
#             'object': obj
#         })
