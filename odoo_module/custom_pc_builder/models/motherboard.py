```python
from odoo import models, fields

class Motherboard(models.Model):
    _name = 'custom_pc_builder.motherboard'
    _description = 'Motherboard Model'

    name = fields.Char(string='Motherboard Name', required=True)
    form_factor = fields.Selection([
        ('atx', 'ATX'),
        ('micro_atx', 'Micro ATX'),
        ('mini_itx', 'Mini ITX'),
        ], string='Form Factor', default='atx', required=True)
    chipset = fields.Char(string='Chipset', required=True)
    ports = fields.Text(string='Available Ports')
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')

    # Dynamic compatibility matrix displaying supported components
    cpu_ids = fields.Many2many('custom_pc_builder.cpu', string='Compatible CPUs')
    gpu_ids = fields.Many2many('custom_pc_builder.gpu', string='Compatible GPUs')
    ram_ids = fields.Many2many('custom_pc_builder.ram', string='Compatible RAMs')
    storage_ids = fields.Many2many('custom_pc_builder.storage', string='Compatible Storages')
```
