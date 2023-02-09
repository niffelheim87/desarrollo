from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socios'
    _description = 'Socios'
    _rec_name = 'full_name'

    id = fields.Integer(string='ID', required=True)
    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    full_name = fields.Char(string='Nombre completo', compute='_compute_full_name')
    comic_id = fields.Many2many('biblioteca.comics', string='Comics', through='biblioteca.prestamos')

    @api.depends('nombre', 'apellido')
    def _compute_full_name(self):
        for record in self:
            record.full_name = record.nombre + ' ' + record.apellido