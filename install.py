import launch

# TODO: early init

# TODO: add deps here
if not launch.is_installed("toml"):
    launch.run_pip("install toml")
    print("Installing toml...")

