```python
from odoo.tests import common

class TestModels(common.TransactionCase):

    def setUp(self):
        super(TestModels, self).setUp()
        self.CPU = self.env['custom_pc_builder.cpu']
        self.GPU = self.env['custom_pc_builder.gpu']
        self.RAM = self.env['custom_pc_builder.ram']
        self.Storage = self.env['custom_pc_builder.storage']
        self.Motherboard = self.env['custom_pc_builder.motherboard']
        self.Price = self.env['custom_pc_builder.price']
        self.Configuration = self.env['custom_pc_builder.configuration']
        self.User = self.env['custom_pc_builder.user']
        self.Order = self.env['custom_pc_builder.order']

    def test_cpu_creation(self):
        cpu = self.CPU.create({
            'name': 'Test CPU',
            'cores': 4,
            'clock_speed': 3.5,
            'cache': 8
        })
        self.assertEqual(cpu.name, 'Test CPU')

    def test_gpu_creation(self):
        gpu = self.GPU.create({
            'name': 'Test GPU',
            'vram': 8,
            'clock_speed': 1.5,
            'cuda_cores': 3072
        })
        self.assertEqual(gpu.name, 'Test GPU')

    def test_ram_creation(self):
        ram = self.RAM.create({
            'name': 'Test RAM',
            'speed': 3200,
            'capacity': 16,
            'latency': 16
        })
        self.assertEqual(ram.name, 'Test RAM')

    def test_storage_creation(self):
        storage = self.Storage.create({
            'name': 'Test Storage',
            'type': 'SSD',
            'capacity': 512,
            'speed': 550
        })
        self.assertEqual(storage.name, 'Test Storage')

    def test_motherboard_creation(self):
        motherboard = self.Motherboard.create({
            'name': 'Test Motherboard',
            'form_factor': 'ATX',
            'chipset': 'Z490',
            'ports': 'USB 3.2, HDMI, Ethernet'
        })
        self.assertEqual(motherboard.name, 'Test Motherboard')

    def test_price_calculation(self):
        price = self.Price.create({
            'component': 'Test CPU',
            'price': 200
        })
        self.assertEqual(price.component, 'Test CPU')

    def test_configuration_creation(self):
        configuration = self.Configuration.create({
            'name': 'Test Configuration',
            'cpu': 'Test CPU',
            'gpu': 'Test GPU',
            'ram': 'Test RAM',
            'storage': 'Test Storage',
            'motherboard': 'Test Motherboard'
        })
        self.assertEqual(configuration.name, 'Test Configuration')

    def test_user_creation(self):
        user = self.User.create({
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(user.name, 'Test User')

    def test_order_creation(self):
        order = self.Order.create({
            'user': 'Test User',
            'configuration': 'Test Configuration',
            'status': 'Processing'
        })
        self.assertEqual(order.user, 'Test User')
```