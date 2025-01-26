class Topic:
    def __init__(self, name: str):
        self.name = name
        self.b_name = name.encode('utf-8') 

class Topics:
    def __init__(self):
        self.actions = Topic("actions/json")
        self.robot_state = Topic("robot_state/json")
        self.v_battery = Topic("sensors/om_v_battery/data")

    def get_all(self):
        return [self.actions, self.robot_state, self.v_battery]

class Action:
    def __init__(self, id: str, name: str, enabled: bool):
        self.id = id
        self.name = name
        self.enabled = enabled

class Actions:
    def __init__(self, json_actions):
        self.reset_emergency = Action(None, None, False)
        self.start_mowing = Action(None, None, False)
        self.start_area_recording = Action(None, None, False)
        self.pause_mowing = Action(None, None, False)
        self.continue_mowing = Action(None, None, False)
        self.abort_mowing = Action(None, None, False)
        self.skip_area = Action(None, None, False)
        self.skip_path = Action(None, None, False)

        for json_action in json_actions:
            if json_action['action_id'] == "mower_logic/reset_emergency":
                self.reset_emergency = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:idle/start_mowing":
                self.start_mowing = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:idle/start_area_recording":
                self.start_area_recording = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:mowing/pause":
                self.pause_mowing = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:mowing/continue":
                self.continue_mowing = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:mowing/abort_mowing":
                self.abort_mowing = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:mowing/skip_area":
                self.skip_area = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])
            elif json_action['action_id'] == "mower_logic:mowing/skip_path":
                self.skip_path = Action(json_action['action_id'], json_action['action_name'], json_action['enabled'])

class Openmower:
    actions: Actions
    topics = Topics()

    def set_actions(json_actions):
        Openmower.actions = Actions(json_actions)