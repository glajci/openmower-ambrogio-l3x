from openmower import Action, Openmower

class MenuItem:
    def __init__(self, index: int, title: str, action: Action, children, parent):
        self.index = index
        self.title = title
        self.action = action
        self.children = children
        self.parent = parent


class Menu:
    def __init__(self):
        self.main_menu_item = MenuItem(0, None, None, [None], None)

    def set_actions(self):
        self.main_menu_item.children = []
        if Openmower.actions.reset_emergency.id:
            emergency_menu_item = MenuItem(len(self.main_menu_item.children), "Emergency", None, [None], self.main_menu_item) 
            emergency_menu_item.children = [MenuItem(0, Openmower.actions.reset_emergency.name, Openmower.actions.reset_emergency, [None], emergency_menu_item), MenuItem(1, "Back", None, [None], emergency_menu_item)]
            self.main_menu_item.children.append(emergency_menu_item)
        if Openmower.actions.skip_area.id:
            skip_area_menu_item = MenuItem(len(self.main_menu_item.children), "Skip area", None, [None], self.main_menu_item)
            skip_area_menu_item.children = [MenuItem(0, Openmower.actions.skip_area.name, Openmower.actions.skip_area, [None], skip_area_menu_item), MenuItem(1, "Back", None, [None], skip_area_menu_item)]
            self.main_menu_item.children.append(skip_area_menu_item)
        if Openmower.actions.skip_path.id:
            skip_path_menu_item = MenuItem(len(self.main_menu_item.children), "Skip path", None, [None], self.main_menu_item)
            skip_path_menu_item.children = [MenuItem(0, Openmower.actions.skip_path.name, Openmower.actions.skip_path, [None], skip_path_menu_item), MenuItem(1, "Back", None, [None], skip_path_menu_item)]
            self.main_menu_item.children.append(skip_path_menu_item)
        back_menu_item = MenuItem(len(self.main_menu_item.children), "Back", None, [None], self.main_menu_item)
        self.main_menu_item.children.append(back_menu_item)
        self.current_item = self.main_menu_item

    def go_down(self):
        if self.current_item == self.main_menu_item: return
        if self.current_item.index == len(self.current_item.parent.children) - 1: 
            self.current_item = self.current_item.parent.children[0]
        else:
            self.current_item = self.current_item.parent.children[self.current_item.index + 1]

    def go_up(self):
        if self.current_item == self.main_menu_item: return
        if self.current_item.index == 0:
            self.current_item = self.current_item.parent.children[len(self.current_item.parent.children) - 1]
        else:
            self.current_item = self.current_item.parent.children[self.current_item.index - 1]

    def enter(self) -> MenuItem:
        if self.current_item.title == None:
            self.current_item = self.current_item.children[0]
        elif self.current_item.action:
            self.current_item = self.current_item.parent
        elif self.current_item.title == "Back":
            self.current_item = self.current_item.parent
        else:
            self.current_item = self.current_item.children[0]

    def is_active(self) -> bool:
        return self.current_item.title != None      
