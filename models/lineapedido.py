from odoo import models, fields, api
class lineapedido(models.Model):
    _name = 'odoo_basico.lineapedido'
    _description = 'exemplo de linea pedido'
    _order = "name asc"

    name = fields.Char(required=True, size=20, string="Identificador da Linea de Pedido:")
    descripcion = fields.Text(string="Descripción da Linea de Pedido:")
# Os campos Many2one crean un campo na BD
    pedido_id = fields.Many2one('odoo_basico.pedido',ondelete= "cascade",required=True)
