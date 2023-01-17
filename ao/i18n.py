import locale

import i18n
import os

i18n.set("file_format", "json")
i18n.set("fallback", "en")
i18n.set("locale", locale.getdefaultlocale()[0])
i18n.load_path.append(os.path.join(os.path.dirname(__file__), "translations"))
i18n.set("filename_format", "{locale}.{format}")
i18n.set("translation_type", "file")
i18n.set("skip_locale_root_data", True)
i18n.set("enable", True)

_ = i18n.t
