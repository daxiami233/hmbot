from .connector.adb import ADB
from .connector.hdc import HDC
from .automator.u2 import U2
from .automator.h2 import H2
from .explorer.dfs import DFS
from .proto import OperatingSystem, ExploreStrategy

system_rfl = {
    OperatingSystem.ANDROID: (ADB, U2),
    OperatingSystem.HARMONY: (HDC, H2)
}

strategy_rfl = {
    ExploreStrategy.DFS: DFS
}