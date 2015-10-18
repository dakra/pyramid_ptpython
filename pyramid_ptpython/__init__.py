def ptpython_shell_factory():
    from ptpython.repl import embed

    def ptpython_shell(env, help):
        print(help)
        return embed(locals=env)

    return ptpython_shell


def ptipython_shell_factory():
    from ptpython.ipython import embed

    def ptipython_shell(env, help):
        return embed(user_ns=env, banner2=help)

    return ptipython_shell
