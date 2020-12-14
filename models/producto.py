# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields

#Lorena
class Producto(models.Model):
    _name = 'flyshoesreserva.producto'

    descripcion = fields.Char(required=True)
    precio = fields.Float (required=True)
    imagen = fields.Binary(String = "Imagen del producto")
    
    reservas = fields.One2many ('flyshoesreserva.reserva','producto', string="Reservas", required=True)
    vendedores = fields.Many2many ('res.users', String="Vendedores", required=True)
    proveedor = fields.Many2one ('flyshoesreserva.proveedor', String = "Proveedor", required=True)

#SUGERENCIAS
#cantidad de este producto(Stock)
#tipo de producto ROPA/ZAPATILLAS ->SELECTION
#producto(modelo)-> ejm(AMD->proveedor Ryzen_3600->producto)
#talla ->Si es ropa (Letras),Si es zapatillas(Numero)