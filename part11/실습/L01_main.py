from appsettings import settings
import screen

screen.draw()
settings.theme = "dark"
screen.draw()

from appsettings import _Settings
other = _Settings()
print(other is settings, other.theme)
