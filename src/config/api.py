"""This module loads the configurations related to the Tresorio API"""

import src.utils.json_rw as json
import src.config.paths as paths

IS_MOCKED = False
API_CONFIG = json.load(paths.TRESORIO_CONFIG_PATH)
