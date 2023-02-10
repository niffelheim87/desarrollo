from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BibliotecaPrestamos(models.Model):
    _name = 'biblioteca.prestamos'
    _description = 'Prestamos'
    socio_id = fields.Many2one('biblioteca.socios', string='Socio', required=True)
    comic_id = fields.Many2one('biblioteca.comics', string='Cómic', required=True)
    fecha_prestamo = fields.Date(string='Fecha de préstamo', required=True)
    fecha_devolucion = fields.Date(string='Fecha de devolución', required=True)
    
    @api.constrains('fecha_prestamo')
    def _check_fecha_prestamo(self):
        for prestamo in self:
            if prestamo.fecha_prestamo > fields.Date.today():
                raise models.ValidationError('La fecha de préstamo no puede ser posterior a la fecha actual.')
            
    @api.constrains('fecha_devolucion')
    def _check_fecha_devolucion(self):
        for prestamo in self:
            if prestamo.fecha_devolucion < fields.Date.today():
                raise models.ValidationError('La fecha de devolución no puede ser anterior a la fecha actual.')