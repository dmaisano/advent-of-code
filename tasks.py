from invoke import task

@task
def test(ctx):
    ctx.run("python -m unittest discover -s tests", pty=True)
