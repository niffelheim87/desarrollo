# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPacientes(models.Model):

    _name = 'hospital_pacientes'
    _description = 'Lista de pacientes'
    _rec_name = 'nombre_completo'

   
    nombre = fields.Char()
    apellido = fields.Char()
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)
    sintomas = fields.Many2many('hospital.sintomas', string='Síntomas')
    
    @api.constrains('nombre', 'apellido')
    def _check_nombre_apellido(self):
        for paciente in self:
            if not paciente.nombre or not paciente.apellido:
                raise ValidationError("Los campos Nombre y Apellido son obligatorios")
    
    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = record.nombre + " " + record.apellido
            
class HospitalSintomas(models.Model):
    _name = 'hospital.sintomas'
    _description = 'Síntomas'

    name = fields.Char(string='Nombre', required=True)
    
    
    


    


    



    
