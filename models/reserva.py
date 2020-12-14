# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import models,fields

class Reserva(models.Model):
    _name = 'flyshoes_reserva.reserva'
    name = fields.Char(String="Reserva")
    descripcion = fields.Text()
    #faltan muchos campos
    estado_reserva = fields.Selection([('cancelada', 'CANCELADA'),
                                      ('confirmada', 'CONFIRMADA'),
                                      ('finalizada', 'FINALIZADA')],
                                      string="Estado de la reserva",
                                      help="Por favor seleciona el estado de la reserva.",
                                      default='confirmada')
                                      
    #El cliente gestiona sus reservas
    cliente = fields.Many2one('res.users',
                                 ondelete='cascade', string="Cliente", required=True)
    #El producto
    producto = fields.Many2one('product.product',
                                  ondelete='cascade', string="Producto", required=True)
    
    
   #Lorena
   descripcion = fields.Char(required=True)
    estado = fields.Selection([
                              ('cancelada', 'CANCELADA'),
                              ('confirmada', 'CONFIRMADA'),
                              ('realizada', 'REALIZADA')
                              ])
    cantidad = fields.Integer(required=True, string="Cantidad del producto")
    
    cliente = fields.Many2one('res.users', string="Cliente", required=True)
    producto = fields.Many2one('flyshoesreserva.reserva', string="Producto", required=True)
    
    