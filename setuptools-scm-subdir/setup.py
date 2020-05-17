from setuptools import setup


setup(
    name="setuptools-scm-sudir",
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "root": "..",
        "relative_to": __file__,
    },
)
