# -*- coding: utf-8 -*-

#Módulos que siempre se deben importar
from odoo import models, fields, api

#Crear clase del módelo  curso
class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='level',
                            selection=[('beginner','Begineer'),
                                      ('intermediate', 'Intermediate'),
                                      ('advanced','Advanced')],
                            copy=False)
    
    active = fields.Boolean(string='Active',default=True)