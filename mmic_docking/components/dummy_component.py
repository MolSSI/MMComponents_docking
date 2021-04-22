from mmic_docking.models import DockInput, DockOutput
from mmic.components.blueprints import TacticComponent
from typing import List, Tuple, Optional, Set


__all__ = ["DockDummyComponent"]


class DockDummyComponent(TacticComponent):
    """
    A sample component that does nothing interesting. Follow the same structure
    to develop your own dock component. You can attach any helper method to this
    component as long as it does not overwrite the core methods in the :class:
    `SpecificComponent` class.
    """

    @classmethod
    def input(cls):
        return DockInput

    @classmethod
    def output(cls):
        return DockOutput

    def get_version(self):
        return ""

    def execute(
        self,
        inputs: DockInput,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, DockOutput]:

        return True, self.output()(proc_input=inputs, poses=inputs.molecule)
