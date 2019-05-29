import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-sandbox",
    description="Meta package for oca-sandbox Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-odoo_module',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
