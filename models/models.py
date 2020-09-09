# -*- coding: utf-8 -*-

from odoo import _, models, fields, api

class lugarentrega_modelo(models.Model):
	_name='lugarentrega.modelo'

	name= fields.Char(size=200, help='Ingrese la descripción')
	direccion= fields.Char(size=200,help='Ingrese la dirección')
	referencia = fields.Char(size=200,help='Referencia de la dirección')
	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	

# class nombremodulo(models.Model):
#     _name = 'nombremodulo.nombremodulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100