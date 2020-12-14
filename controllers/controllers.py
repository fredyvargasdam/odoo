# -*- coding: utf-8 -*-
from odoo import http

# class FlyshoesReserva(http.Controller):
#     @http.route('/flyshoes_reserva/flyshoes_reserva/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flyshoes_reserva/flyshoes_reserva/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flyshoes_reserva.listing', {
#             'root': '/flyshoes_reserva/flyshoes_reserva',
#             'objects': http.request.env['flyshoes_reserva.flyshoes_reserva'].search([]),
#         })

#     @http.route('/flyshoes_reserva/flyshoes_reserva/objects/<model("flyshoes_reserva.flyshoes_reserva"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flyshoes_reserva.object', {
#             'object': obj
#         })