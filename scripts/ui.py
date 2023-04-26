from module.kohya_config_webui import create_demo
from modules import script_callbacks

def ui_tab():
		return [(create_demo(), "kohya-config", "kohya_config_maker")]
		
script_callbacks.on_ui_tabs(ui_tab)