import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-acsone-sandbox",
    description="Meta package for acsone-sandbox Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-odoo_module',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
