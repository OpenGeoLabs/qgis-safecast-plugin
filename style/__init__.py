import os

from qgis.core import QgsStyle

class StyleError(Exception):
    pass

class Style:
    def __init__(self):
        self._styles = []
        
    def __getitem__(self, index):
        return self._styles[index]

    def __len__(self):
        return len(self._styles)

    def __iter__(self):
        return iter(self._styles)

    def _load_color_ramps(self, filename, attribute, classes=10):
        self._styleFactory = QgsStyle()
        self._styleFactory.importXml(filename)
        for styleName in self._styleFactory.colorRampNames():
            self._styles.append(
                {
                    'name' : styleName,
                    'colorramp' : self._styleFactory.colorRamp(styleName),
                    'classes' : classes,
                    'attribute' : attribute
                }
            )
