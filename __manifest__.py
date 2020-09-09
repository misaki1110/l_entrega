# -*- coding: utf-8 -*-
{
    'name': "Crea Modulo Lugar de entrega",

    'summary': """
        Crea Modulo lugar de entrega y lo coloca dentro del menu configuraciones
        perteneciente al Modulo Compras""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Prosystem",
    'website': "http://www.contasql.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase',],

    # always loaded
    'data': [
<<<<<<< HEAD
        'security/ir.model.access.csv',
        'security/seguridad_entrega.xml',
        'views/res_config_herencia.xml',        
        'views/views.xml',                
=======
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
>>>>>>> d01b87de61345eafd21948cae912e75feed32bad
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}