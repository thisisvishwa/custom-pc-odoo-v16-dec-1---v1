```python
from odoo import http
from odoo.http import request

class CustomPCBuilder(http.Controller):

    @http.route('/custom_pc_builder/cpu', type='json', auth='user')
    def get_cpu(self):
        CPUs = request.env['custom_pc_builder.cpu'].search([])
        return CPUs.read()

    @http.route('/custom_pc_builder/gpu', type='json', auth='user')
    def get_gpu(self):
        GPUs = request.env['custom_pc_builder.gpu'].search([])
        return GPUs.read()

    @http.route('/custom_pc_builder/ram', type='json', auth='user')
    def get_ram(self):
        RAMs = request.env['custom_pc_builder.ram'].search([])
        return RAMs.read()

    @http.route('/custom_pc_builder/storage', type='json', auth='user')
    def get_storage(self):
        storages = request.env['custom_pc_builder.storage'].search([])
        return storages.read()

    @http.route('/custom_pc_builder/motherboard', type='json', auth='user')
    def get_motherboard(self):
        motherboards = request.env['custom_pc_builder.motherboard'].search([])
        return motherboards.read()

    @http.route('/custom_pc_builder/configuration', type='json', auth='user')
    def get_configuration(self):
        configurations = request.env['custom_pc_builder.configuration'].search([])
        return configurations.read()

    @http.route('/custom_pc_builder/configuration', type='json', auth='user', methods=['POST'], csrf=False)
    def save_configuration(self, **kwargs):
        configuration = request.env['custom_pc_builder.configuration'].create(kwargs)
        return configuration.id

    @http.route('/custom_pc_builder/order', type='json', auth='user')
    def get_order(self):
        orders = request.env['custom_pc_builder.order'].search([])
        return orders.read()

    @http.route('/custom_pc_builder/order', type='json', auth='user', methods=['POST'], csrf=False)
    def create_order(self, **kwargs):
        order = request.env['custom_pc_builder.order'].create(kwargs)
        return order.id
```