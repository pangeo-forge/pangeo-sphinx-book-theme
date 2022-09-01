import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", "docs", "docs/_build/html"]

@nox.session(python="3.9")
def docs(session):
    session.install("-e", ".")
    session.run("sphinx-build", *build_command)

@nox.session(name="docs-live", python="3.9")
def docs_live(session):
    session.install("-e", ".")
    session.install("ipython")
    session.install("sphinx-autobuild")

    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command)
    session.run(*cmd)
