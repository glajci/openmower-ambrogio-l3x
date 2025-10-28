from openmower import Action, Openmower

class MenuItem:
    def __init__(self, index: int, title: str, subtitle: str, action: Action, children, parent):
        self.index = index
        self.title = title
        self.subtitle = subtitle
        self.action = action
        self.children = children
        self.parent = parent

class Menu:
    def __init__(self):
        self.current_item = None
        self.main_menu_item = MenuItem(0, None, None, None, [None], None)

    def set_actions(self):
        self.main_menu_item.children = []
        if Openmower.actions.reset_emergency.id:
            emergency_menu_item = MenuItem(len(self.main_menu_item.children), "Emergency", f'{Openmower.actions.reset_emergency.name}?', Openmower.actions.reset_emergency, [None], self.main_menu_item) 
            self.main_menu_item.children.append(emergency_menu_item)
        if Openmower.actions.skip_area.id:
            skip_area_menu_item = MenuItem(len(self.main_menu_item.children), "Area", f'{Openmower.actions.skip_area.name}?', Openmower.actions.skip_area, [None], self.main_menu_item)
            self.main_menu_item.children.append(skip_area_menu_item)
        if Openmower.actions.skip_path.id:
            skip_path_menu_item = MenuItem(len(self.main_menu_item.children), "Path", f'{Openmower.actions.skip_path.name}?', Openmower.actions.skip_path, [None], self.main_menu_item)
            self.main_menu_item.children.append(skip_path_menu_item)
        self.current_item = self.main_menu_item

    def go_down(self):
        if self.current_item == self.main_menu_item:
            self.current_item = self.current_item.children[0]
        elif self.current_item.index == len(self.current_item.parent.children) - 1: 
            self.current_item = self.main_menu_item
        else:
            self.current_item = self.current_item.parent.children[self.current_item.index + 1]

    def go_up(self):
        if self.current_item == self.main_menu_item:
            self.current_item = self.current_item.children[len(self.current_item.children) - 1]
        elif self.current_item.index == 0:
            self.current_item = self.main_menu_item
        else:
            self.current_item = self.current_item.parent.children[self.current_item.index - 1]

    def enter(self) -> MenuItem:
        if self.current_item.action:
            self.current_item = self.current_item.parent
        elif self.current_item.children != [None]:
            self.current_item = self.current_item.children[0]
        else:
            self.current_item = self.current_item.parent

    def is_active(self) -> bool:
        return self.current_item != None and self.current_item.title != None
