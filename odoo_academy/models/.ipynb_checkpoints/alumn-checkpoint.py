# -*- coding: utf-8 -*-

#Módulos que siempre se deben importar
from odoo import models, fields, api

#[Ejercicio] Modelo Alumno

class Alumn(models.Model):
    _name = 'academy.alumn'
    _description = 'Info Alumn'

    numero_cuenta_alum = fields.Integer(string='Número de cuenta', required=True)
    nombre_per = fields.Char(string='Nombre', required=True)                   
    materno_per = fields.Char(string='Apellido materno', required=True)    			
    paterno_per = fields.Char(string='Apellido paterno', required=True)      				
    email_per = fields.Char(string='Correo electrónico', required=True)       				 	
    login_per = fields.Char(string='Usuario', required=True)         					
    password_per = fields.Char(string='Contraseña', required=True)       			   		
    fecha_nacimiento_per = fields.Date(string='Fecha de nacimiento', required=True)
    active = fields.Boolean(string='Activo',default=True)
    career = fields.Selection(string='Carrera',selection=[('computer','Computación'),
                                                            ('telecom', 'Telecomunicaciones'),
                                                            ('mechanic','Mecánica'),
                                                            ('electronic','Electronica')],
                                                            copy=False)