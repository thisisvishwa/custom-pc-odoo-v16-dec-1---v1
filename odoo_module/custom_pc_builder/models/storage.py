```python
from odoo import models, fields

class Storage(models.Model):
    _name = 'custom_pc_builder.storage'
    _description = 'Storage Model'

    name = fields.Char(string='Storage Name', required=True)
    storage_type = fields.Selection([
        ('ssd', 'SSD'),
        ('hdd', 'HDD'),
    ], string='Storage Type', required=True)
    capacity = fields.Integer(string='Capacity (GB)', required=True)
    speed = fields.Integer(string='Speed (MB/s)', required=True)
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')

    # Relations
    motherboard_id = fields.Many2one('custom_pc_builder.motherboard', string='Compatible Motherboards')

    def check_compatibility(self, motherboard):
        # Check compatibility with the given motherboard
        # This is a placeholder. Actual implementation will depend on the specific compatibility rules.
        return True
```