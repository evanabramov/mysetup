import subprocess
import os
from qutebrowser.api import interceptor

'''
qutebrowser settings for video
for more settings check out
https://qutebrowser.org/doc/help/settings.html
'''

# ================== Youtube Add Blocking ======================= {{{
def filter_yt(info: interceptor.Request):
    '''Block the given request if necessary.'''
    url = info.request_url
    if (
        url.host() == 'www.youtube.com'
        and url.path() == '/get_video_info'
        and '&adformat=' in url.query()
    ):
        info.block()


interceptor.register(filter_yt)
# }}}
# ====================== xresources ======================= {{{
# taken from https://qutebrowser.org/doc/help/configuring.html
def read_xresources(prefix):
    '''
    read settings from xresources
    '''
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props


xresources = read_xresources('*')

#c.colors.statusbar.normal.bg = xresources['*.background']
c.colors.statusbar.command.bg = xresources['*.background']
c.colors.statusbar.command.fg = xresources['*.foreground']
c.colors.statusbar.normal.fg = xresources['*.foreground']
c.statusbar.show = 'always'

c.colors.tabs.even.bg = xresources['*.background']
c.colors.tabs.odd.bg = xresources['*.background']
c.colors.tabs.even.fg = xresources['*.foreground']
c.colors.tabs.odd.fg = xresources['*.foreground']
c.colors.tabs.selected.even.bg = xresources['*.color5']
c.colors.tabs.selected.odd.bg = xresources['*.color5']
c.colors.hints.bg = xresources['*.background']
c.colors.hints.fg = xresources['*.foreground']
c.tabs.show = 'multiple'

# change title format
c.tabs.title.format = '{audio}{current_title}'
# fonts
c.fonts.web.size.default = 20


c.colors.tabs.indicator.stop = xresources['*.color14']
c.colors.completion.odd.bg = xresources['*.background']
c.colors.completion.even.bg = xresources['*.background']
c.colors.completion.fg = xresources['*.foreground']
c.colors.completion.category.bg = xresources['*.background']
c.colors.completion.category.fg = xresources['*.foreground']
c.colors.completion.item.selected.bg = xresources['*.background']
c.colors.completion.item.selected.fg = xresources['*.foreground']

# If not in light theme
if xresources['*.background'] != '#ffffff':
    # c.qt.args = ['blink-settings=darkMode=4']
    # c.colors.webpage.prefers_color_scheme_dark = True
    c.colors.webpage.darkmode.enabled = True
    c.hints.border = '1px solid #FFFFFF'


# USERSCRIPTS
#
# personally I use
# - for password managment
#   - qute-pass
# - for chrome casting I use
#   - cast
#   - I have been looking at using catt instead of castnow

# }}}

# some settings
c.qt.highdpi = True

config.load_autoconfig(True)

c.auto_save.session = True
c.confirm_quit = ["always"]

c.aliases['b'] = "back"
c.aliases['q'] = "adblock-update"
c.aliases['c'] = "tab-close"

config.bind('<Windows-1>', 'tab-focus 1')
config.bind('<Windows-2>', 'tab-focus 2')
config.bind('<Windows-3>', 'tab-focus 3')
config.bind('<Windows-4>', 'tab-focus 4')
config.bind('<Windows-5>', 'tab-focus 5')
config.bind('<Windows-6>', 'tab-focus 6')
config.bind('<Windows-7>', 'tab-focus 7')
config.bind('<Windows-8>', 'tab-focus 8')
config.bind('<Windows-9>', 'tab-focus 9')
