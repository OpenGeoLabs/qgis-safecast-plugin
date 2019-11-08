from qgis.PyQt.QtWidgets import QTreeWidget, QTreeWidgetItem

class SafecastStats(QTreeWidget):
    def addParent(self, parent, title):
        item = QTreeWidgetItem(parent, [title])
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item
    
    def addChild(self, parent, title):
        item = QTreeWidgetItem(parent, [title])
        return item
    
    def setData(self, data):
        # create tree items
        self.clear()

        root = self.invisibleRootItem()
        for label in list(data.keys()):
            item = self.addParent(root, label)
            for key, value in data[label]:
                self.addChild(item, '{}: {}'.format(key, value))

            
