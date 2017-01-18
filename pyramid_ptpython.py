import os

def ptpython_shell_runner(env, help):
    from ptpython.repl import embed, run_config

    history = os.path.expanduser('~/.ptpython_history')
    print(help)
    return embed(locals=env.copy(), history_filename=history, configure=run_config)


def ptipython_shell_runner(env, help):
    try:
        from ptpython.repl import run_config
        from ptpython.ipython import embed
    except ImportError:
        print('You need to install the ipython package for ptipython to work')
        return

    history = os.path.expanduser('~/.ptpython_history')
    return embed(user_ns=env.copy(), banner2=help, history_filename=history, configure=run_config)
