```python
from odoo import models, fields

class CPU(models.Model):
    _name = 'custom_pc_builder.cpu'
    _description = 'CPU Model'

    name = fields.Char(string='CPU Name', required=True)
    cores = fields.Integer(string='Cores', required=True)
    clock_speed = fields.Float(string='Clock Speed (GHz)', required=True)
    cache = fields.Integer(string='Cache (MB)', required=True)
    compatible_with = fields.Many2many('custom_pc_builder.gpu', string='Compatible GPUs')

    def check_compatibility(self, gpu_id):
        compatible_gpus = self.compatible_with.ids
        if gpu_id in compatible_gpus:
            return True
        else:
            return False
```