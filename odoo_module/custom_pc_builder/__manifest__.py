{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'eCommerce',
    'summary': 'Module for building custom PCs',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/cpu_view.xml',
        'views/gpu_view.xml',
        'views/ram_view.xml',
        'views/storage_view.xml',
        'views/motherboard_view.xml',
        'views/price_view.xml',
        'views/configuration_view.xml',
        'views/user_view.xml',
        'views/order_view.xml',
        'data/initial_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
    This module allows users to build custom PCs by selecting individual components.
    Features include component selection, price calculation, visual representation, save/load configurations, user authentication, and order management.
    """
}