# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
class Proveedor(models.Model):
    _name = 'flyshoesreserva.proveedor'
    
    tipo = fields.Selection[(
                             ('zapatillas', 'ZAPATILLAS'),
                             ('ropa', 'ROPA')
                             )]
    empresa = fields.Char(required=True)
    email = fields.Char(required=True)
    telefono = fields.Char(required=True)
    descripcion = fields.Char()
    
    administrador = fields.Many2one ('res.users', string="Administrador", required=True)
    producto = fields.One2many ('flyshoesreserva.producto', 'proveedor', string="Producto", required=True)
