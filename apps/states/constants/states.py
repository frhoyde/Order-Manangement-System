class StateConstants:
    def __init__(self) -> None:
        self.default_states = [
            {
                'name': 'New Order',
                'value': 1,
                'is_initial': True,
                'is_final': False
            },
            {
                'name': 'First Call',
                'value': 2,
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Scheduled',
                'value': 3,
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Installation',
                'value': 4,
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Finalization',
                'value': 5,
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Completed',
                'value': 6,
                'is_initial': False,
                'is_final': True
            },
            {
                'name': 'Cancelled',
                'value': 7,
                'is_initial': False,
                'is_final': True
            }
        ]