class StateConstants:
    def __init__(self) -> None:
        self.default_states = [
            {
                'name': 'New Order',
                'is_initial': True,
                'is_final': False
            },
            {
                'name': 'First Call',
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Scheduled',
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Installation',
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Finalization',
                'is_initial': False,
                'is_final': False
            },
            {
                'name': 'Completed',
                'is_initial': False,
                'is_final': True
            },
            {
                'name': 'Cancelled',
                'is_initial': False,
                'is_final': True
            }
        ]