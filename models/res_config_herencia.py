from odoo import api, fields, models, _


class ResConfigSettingsHerencia(models.TransientModel):
	_inherit = 'res.config.settings'

	group_aparece_entrega = fields.Boolean("Manage multiple companies", implied_group='prosystemperu_lentrega_crea.group_aparece_entrega')