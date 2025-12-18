import sys
from PySide6.QtWidgets import QApplication, QGraphicsPixmapItem, QGraphicsItem, QGraphicsScene, QMainWindow, QWidget, QVBoxLayout, QGraphicsView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

class Main_window(QMainWindow):
    def __init__(self, scene):
        super().__init__()
        self.setWindowTitle("Шахматы")
        self.setFixedSize(QSize(680, 680))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.scene = scene
        self.view = QGraphicsView(scene)
        self.layout.addWidget(self.view)

class fig_item(QGraphicsPixmapItem):
    def __init__(self, image, position, width, height):
        super().__init__()
        pixmap = QPixmap(image).scaled(width, height)
        if pixmap.isNull():
            print(f"Не удалось загрузить изображение {image}")
        self.setPixmap(pixmap)
        self.setPos(*position)
        # Включение перетаскивания
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        # Для хранения начальной точки при перемещении
        self._start_pos = None

    def mousePressEvent(self, event):
        # Запоминаем начальную позицию мыши в сцене
        self._start_pos = event.scenePos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._start_pos is not None:
            new_pos = event.scenePos()
            delta = new_pos - self._start_pos
            self.setPos(self.pos() + delta)
            self._start_pos = new_pos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

app = QApplication(sys.argv)
scene = QGraphicsScene()

# Создаём фигуры
Wking = fig_item("Project\\Wking.png", position=(240, 560), width=80, height=80)
scene.addItem(Wking)

Wqueen = fig_item("Project\\Wqueen.png", position=(160, 560), width=80, height=80)
scene.addItem(Wqueen)

Wknight1 = fig_item("Project\\Wknight.png", position=(80, 560), width=80, height=80)
scene.addItem(Wknight1)

Wknight2 = fig_item("Project\\Wknight.png", position=(320, 560), width=80, height=80)
scene.addItem(Wknight2)

Wbishop1 = fig_item("Project\\Wbishop.png", position=(240, 480), width=80, height=80)
scene.addItem(Wbishop1)

Wbishop2 = fig_item("Project\\Wbishop.png", position=(80, 480), width=80, height=80)
scene.addItem(Wbishop2)

Wrook1 = fig_item("Project\\Wrook.png", position=(400, 560), width=80, height=80)
scene.addItem(Wrook1)

Wrook2 = fig_item("Project\\Wrook.png", position=(560, 560), width=80, height=80)
scene.addItem(Wrook2)

Wpawn1 = fig_item("Project\\Wpawn.png", position=(0, 480), width=80, height=80)
scene.addItem(Wpawn1)

Wpawn2 = fig_item("Project\\Wpawn.png", position=(80, 480), width=80, height=80)
scene.addItem(Wpawn2)

Wpawn3 = fig_item("Project\\Wpawn.png", position=(160, 480), width=80, height=80)
scene.addItem(Wpawn3)

Wpawn4 = fig_item("Project\\Wpawn.png", position=(240, 480), width=80, height=80)
scene.addItem(Wpawn4)

Wpawn5 = fig_item("Project\\Wpawn.png", position=(320, 480), width=80, height=80)
scene.addItem(Wpawn5)

Wpawn6 = fig_item("Project\\Wpawn.png", position=(400, 480), width=80, height=80)
scene.addItem(Wpawn6)

Wpawn7 = fig_item("Project\\Wpawn.png", position=(480, 480), width=80, height=80)
scene.addItem(Wpawn7)

Wpawn8 = fig_item("Project\\Wpawn.png", position=(560, 480), width=80, height=80)
scene.addItem(Wpawn8)

# Аналогично создаёте фигуры черных (Bl, Bqueen, etc.)
# Например:
Blking = fig_item("Project\\Blking.png", position=(240, 0), width=80, height=80)
scene.addItem(Blking)

# Остальные фигуры для черных (Bqueen, Bknight, etc.) — добавьте аналогично

# Создаем окно
window = Main_window(scene)
window.show()

sys.exit(app.exec())