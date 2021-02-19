from FFxivPythonTrigger import FFxivPythonTrigger
from plugin.FFxivMemory import FFxivMemory
from plugin.GayMagician import GayMagicianPlugin
from plugin.Command import Command
from plugin.NamazuServer import NamazuServer
from plugin.WebChat import WebChat


fpt = FFxivPythonTrigger([
    FFxivMemory,
    GayMagicianPlugin,
    WebChat,
    NamazuServer,
    Command,
])
fpt.start()
