```python
from odoo import models, fields, api

class Order(models.Model):
    _name = 'custom_pc_builder.order'
    _description = 'Order'

    user_id = fields.Many2one('res.users', string='User')
    configuration_id = fields.Many2one('custom_pc_builder.configuration', string='Configuration')
    total_price = fields.Float(compute='_compute_total_price', string='Total Price')
    order_date = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ], default='draft', string='Status')

    @api.depends('configuration_id')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.configuration_id.total_price
```
