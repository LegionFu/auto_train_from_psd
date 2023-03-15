import launch

if not launch.is_installed("psd_tools"):
    launch.run_pip("install psd_tools==1.9.24", "psd_tools")