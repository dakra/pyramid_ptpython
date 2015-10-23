def ptpython_shell_runner(env, help):
    from ptpython.repl import embed

    print(help)
    return embed(locals=env)


def ptipython_shell_runner(env, help):
    try:
        from ptpython.ipython import embed
    except ImportError:
        print('You need to install the ipython package for ptipython to work')
        return

    return embed(user_ns=env, banner2=help)
