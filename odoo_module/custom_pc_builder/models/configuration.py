```python
from odoo import models, fields

class Configuration(models.Model):
    _name = 'custom_pc_builder.configuration'
    _description = 'PC Configuration'

    name = fields.Char(string='Configuration Name', required=True)
    user_id = fields.Many2one('res.users', string='User')
    cpu_id = fields.Many2one('custom_pc_builder.cpu', string='CPU')
    gpu_id = fields.Many2one('custom_pc_builder.gpu', string='GPU')
    ram_id = fields.Many2one('custom_pc_builder.ram', string='RAM')
    storage_id = fields.Many2one('custom_pc_builder.storage', string='Storage')
    motherboard_id = fields.Many2one('custom_pc_builder.motherboard', string='Motherboard')
    price_id = fields.Many2one('custom_pc_builder.price', string='Price')

    def save_configuration(self):
        self.ensure_one()
        # Implement logic to save the current configuration

    def load_configuration(self, configuration_id):
        # Implement logic to load a saved configuration
        pass
```