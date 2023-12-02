```python
from odoo import models, fields

class Ram(models.Model):
    _name = 'custom_pc_builder.ram'
    _description = 'RAM Model'

    name = fields.Char(string='RAM Name', required=True)
    speed = fields.Integer(string='Speed (MHz)', required=True)
    capacity = fields.Integer(string='Capacity (GB)', required=True)
    latency = fields.Float(string='Latency (CL)', required=True)
    price = fields.Float(string='Price', required=True)

    def check_compatibility(self, cpu_id, gpu_id):
        # Implement compatibility check logic here
        pass

    def suggest_optimal_size(self, cpu_id, gpu_id):
        # Implement optimal size suggestion logic here
        pass
```