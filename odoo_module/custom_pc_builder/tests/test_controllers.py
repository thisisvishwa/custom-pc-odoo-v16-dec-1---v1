```python
from odoo.tests import HttpCase

class TestControllers(HttpCase):

    def setUp(self):
        super(TestControllers, self).setUp()
        self.CPU = self.env['custom_pc_builder.cpu']
        self.GPU = self.env['custom_pc_builder.gpu']
        self.RAM = self.env['custom_pc_builder.ram']
        self.Storage = self.env['custom_pc_builder.storage']
        self.Motherboard = self.env['custom_pc_builder.motherboard']
        self.Price = self.env['custom_pc_builder.price']
        self.Configuration = self.env['custom_pc_builder.configuration']
        self.User = self.env['custom_pc_builder.user']
        self.Order = self.env['custom_pc_builder.order']

    def test_component_selection(self):
        # Test CPU selection
        cpu = self.CPU.create({'name': 'Test CPU', 'cores': 4, 'clock_speed': 3.5, 'cache': 8})
        self.assertEqual(cpu.name, 'Test CPU')

        # Test GPU selection
        gpu = self.GPU.create({'name': 'Test GPU', 'vram': 8, 'clock_speed': 1.5, 'cuda_cores': 2048})
        self.assertEqual(gpu.name, 'Test GPU')

        # Test RAM selection
        ram = self.RAM.create({'name': 'Test RAM', 'speed': 3200, 'capacity': 16, 'latency': 16})
        self.assertEqual(ram.name, 'Test RAM')

        # Test Storage selection
        storage = self.Storage.create({'name': 'Test Storage', 'type': 'SSD', 'capacity': 500, 'speed': 550})
        self.assertEqual(storage.name, 'Test Storage')

        # Test Motherboard selection
        motherboard = self.Motherboard.create({'name': 'Test Motherboard', 'form_factor': 'ATX', 'chipset': 'Z390', 'ports': 'USB 3.1, HDMI, Ethernet'})
        self.assertEqual(motherboard.name, 'Test Motherboard')

    def test_price_calculation(self):
        # Test price calculation
        price = self.Price.create({'cpu_price': 200, 'gpu_price': 400, 'ram_price': 80, 'storage_price': 100, 'motherboard_price': 150})
        self.assertEqual(price.total_price, 930)

    def test_save_load_configurations(self):
        # Test save and load configurations
        configuration = self.Configuration.create({'name': 'Test Configuration', 'cpu_id': cpu.id, 'gpu_id': gpu.id, 'ram_id': ram.id, 'storage_id': storage.id, 'motherboard_id': motherboard.id})
        self.assertEqual(configuration.name, 'Test Configuration')

    def test_user_authentication(self):
        # Test user authentication
        user = self.User.create({'name': 'Test User', 'email': 'test@example.com', 'password': 'test123'})
        self.assertEqual(user.name, 'Test User')

    def test_order_management(self):
        # Test order management
        order = self.Order.create({'user_id': user.id, 'configuration_id': configuration.id, 'status': 'Processing'})
        self.assertEqual(order.status, 'Processing')
```