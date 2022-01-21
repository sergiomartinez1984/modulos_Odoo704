

from odoo import models, fields, api

class videojuegos(models.Model):
	_name = 'odoo704.videojuegos'
	_description = 'modelo videojuegos'

	name = fields.Char(string='Nombre', required=True)
	imagen = fields.Char(string='Imagen', required=True)
	precio = fields.Char(string='Precio', required=True)
	date = fields.Char(string="Fecha Salida", required=True)

class personajes(models.Model):
	_name = 'odoo704.personajes'
	_description = 'modelo personajes'

	name = fields.Char(string='Nombre', required=True)
	videojuego = fields.Char(string='Videojuego', required=True)


class empresa(models.Model):
	_name = 'odoo704.empresa'
	_description = 'modelo empresa'

	name = fields.Char(string='Nombre', required=True)
	ubicacion = fields.Char(string='Ubicacion', required=True)