def any_arrows(arrows):
    return any(not i.get("damaged", False) for i in arrows)
