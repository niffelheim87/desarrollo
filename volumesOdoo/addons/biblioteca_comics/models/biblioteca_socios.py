from odoo import models, fields
from odoo.exceptions import ValidationError

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socios'
    _description = 'Socios'

    id = fields.Integer(string='ID', required=True)
    nombre = fields.Char(string='Nombre')
    apellidos = fields.Char(string='Apellidos')
    comic_id = fields.One2many('biblioteca.comics', 'socio_id', string='Comics')
