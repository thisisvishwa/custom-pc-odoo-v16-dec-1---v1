```python
from odoo import models, fields

class CustomPCBuilderUser(models.Model):
    _inherit = 'res.users'

    configurations = fields.One2many('custom_pc_builder.configuration', 'user_id', string='Configurations')
    orders = fields.One2many('custom_pc_builder.order', 'user_id', string='Orders')

    def create_guest_user(self):
        guest_user = self.create({
            'login': 'guest',
            'password': 'guest',
            'name': 'Guest User',
        })
        return guest_user

    def convert_guest_to_registered(self, guest_user_id, login, password, name):
        guest_user = self.browse(guest_user_id)
        guest_user.write({
            'login': login,
            'password': password,
            'name': name,
        })
        return guest_user
```