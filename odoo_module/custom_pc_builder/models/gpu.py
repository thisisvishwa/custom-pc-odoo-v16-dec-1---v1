```python
from odoo import models, fields

class GPU(models.Model):
    _name = 'custom_pc_builder.gpu'
    _description = 'Graphics Processing Unit'

    name = fields.Char(string='GPU Name', required=True)
    vram = fields.Integer(string='VRAM (in GB)', required=True)
    clock_speed = fields.Float(string='Clock Speed (in GHz)', required=True)
    cuda_cores = fields.Integer(string='CUDA Cores', required=True)
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')

    def check_compatibility(self, cpu_id):
        # Implement compatibility check with CPU
        pass
```