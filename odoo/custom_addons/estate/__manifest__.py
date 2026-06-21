# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Advertisement',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and advertisements',
    'description': """
        Long description of Odoo Real Estate module tutorial.
        - Create properties
        - Set generic attributes
        - Access rights and basic UI views
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}