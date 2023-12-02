```python
from odoo import models, fields

class Price(models.Model):
    _name = 'custom_pc_builder.price'
    _description = 'Price Model for Custom PC Builder'

    name = fields.Char(string='Component Name', required=True)
    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
    ], string='Component Type', required=True)
    price = fields.Float(string='Price', required=True)
    market_price = fields.Float(string='Market Price')

    def calculate_total_price(self, component_ids):
        components = self.browse(component_ids)
        total_price = sum(component.price for component in components)
        return total_price
```