from invoke import task

@task
def start(ctx):
    ctx.run("python src/task_service.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")


