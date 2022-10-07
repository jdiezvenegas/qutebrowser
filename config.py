import setproctitle
from qutebrowser.api import interceptor
setproctitle.setproctitle("qutebrowser")
config.load_autoconfig(True)
# Bindings
config.bind("gi", "hint inputs")
config.bind("<f12>", "inspector")
config.unbind("+")
config.unbind("-")
config.unbind("=")
config.bind("<Ctrl++>", "zoom-in")
config.bind("<Ctrl+->", "zoom-out")
config.bind("<Ctrl+0>", "zoom")
config.unbind("O")
config.unbind("T")
config.unbind("th")
config.unbind("tl")
config.bind("O", "set-cmd-text :open {url:pretty}")
config.bind("T", "set-cmd-text :open -t {url:pretty}")
config.bind("t", "set-cmd-text -s :open -t")
config.unbind("<ctrl+tab>")
config.bind("<ctrl+tab>", "tab-next")
config.bind("<ctrl+shift+tab>", "tab-prev")
config.unbind("ZQ")
config.unbind("ZZ")
config.unbind("<ctrl+q>")
config.bind("<ctrl+q>", "wq")
config.unbind("d")
config.bind("<Ctrl+m>","tab-mute")
config.unbind("<Alt+m>")
config.bind("<Ctrl+o>","tab-give")
config.bind("<Alt+LEFT>","back")
config.bind("<Alt+RIGHT>","forward")
config.bind("<Alt+UP>","tab-next")
config.bind("<Alt+DOWN>","tab-prev")
config.bind("<Ctrl+1>","tab-select 1")
config.bind("<Ctrl+2>","tab-select 2")
config.bind("<Ctrl+3>","tab-select 3")
config.bind("<Ctrl+4>","tab-select 4")
config.bind("<Ctrl+5>","tab-select 5")
config.bind("<Ctrl+6>","tab-select 6")
config.bind("<Ctrl+7>","tab-select 7")
config.bind("<Ctrl+8>","tab-select 8")
config.bind("<Ctrl+9>","tab-select 9")
config.bind("<Ctrl+0>","tab-select 10")
config.bind("<Ctrl+f>","hint all tab-fg")
config.bind("<Ctrl+shift+f>","hint all tab-bg")
config.bind("<Ctrl+Alt+f>", "hint all yank")
config.bind("<Ctrl+w>","tab-close -n")
config.bind("<Shift+o>","open -t https://www.google.es")
config.unbind("<Ctrl+p>")
config.bind("<Ctrl+p>","print --pdf ~/Descargas/current.pdf")
config.bind("<Ctrl+h>","history")
# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
c.aliases = {
    "w": "session-save",
    "wq": "quit --save",
    "mpv": "spawn -d mpv --force-window=immediate {url}",
    "nicehash": "spawn --userscript nicehash",
    "pass": "spawn -d pass -c",
    "g": "open https://www.google.es/search?q={}",
	"bit" : "open https://vault.bitwarden.com/#/login"
}
# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = "green"
c.colors.statusbar.url.success.http.fg= "orange"
# Foreground color of unselected tabs.
c.colors.tabs.even.fg = "#2B2B2B"
c.colors.tabs.odd.fg = c.colors.tabs.even.fg
# The height of the completion, in px or as percentage of the window.
c.completion.height = "20%"
# When to show the autocompletion window.
# Valid values:
#   - always: Whenever a completion is available.
#   - auto: Whenever a completion is requested.
#   - never: Never.
c.completion.show = "always"
# Whether quitting the application requires a confirmation.
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ["downloads"]
# Value to send in the `Accept-Language` header.
c.content.headers.accept_language = "es-ES,en;q=0.8,fi;q=0.6"
# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don"t use any proxy
c.content.proxy = "none"
# Validate SSL handshakes.
# Valid values:
#   - true
#   - false
#   - ask
#c.content.ssl_strict = True
# A list of user stylesheet filenames to use.
#c.content.user_stylesheets = "style1.css"
# The directory to save downloads to. If unset, a sensible os-specific
# default is used.
c.downloads.location.directory = "~/Descargas"
# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
c.downloads.location.prompt = True
# Font used for the hints.
c.fonts.hints = "bold 13px 'Tlwg Mono'"
# Chars used for hint strings.
c.hints.chars = "asdfghjklie"
# Leave insert mode if a non-editable element is clicked.
c.input.insert_mode.auto_leave = True
# Automatically enter insert mode if an editable element is focused
# after loading the page.
c.input.insert_mode.auto_load = True
# Show a scrollbar.
c.scrolling.bar = "always"
# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
c.scrolling.smooth = False
# Open new tabs (middleclick/ctrl+click) in the background.
c.tabs.background = True
# Behavior when the last tab is closed.
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = "close"
# Padding around text for tabs
c.tabs.padding = {
    "left": 5,
    "right": 5,
    "top": 0,
    "bottom": 1,
}
# Which tab to select when the focused tab is removed.
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = "next"
# Width of the progress indicator (0 to disable).
#c.tabs.width.indicator = 0
# Always restore open sites when qutebrowser is reopened.
c.auto_save.session = True
# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = "gray"
#c.colors.statusbar.url.success.http.fg = "#fd9393"
# Foreground color of unselected tabs.
c.colors.tabs.even.bg="black"
c.colors.tabs.odd.bg=c.colors.tabs.even.bg
c.colors.tabs.even.fg = "gray"
c.colors.tabs.odd.fg = c.colors.tabs.even.fg
# The height of the completion, in px or as percentage of the window.
c.completion.height = "20%"
# Move on to the next part when there's only one possible completion
# left.
c.completion.quick = True
# Whether quitting the application requires a confirmation.
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ["downloads"]
# Value to send in the `Accept-Language` header.
c.content.headers.accept_language = "es-ES,en;q=0.8,fi;q=0.6"
# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don"t use any proxy
c.content.proxy = "none"
# Validate SSL handshakes.
# Valid values:
#   - true
#   - false
#   - ask
#c.content.ssl_strict = True
# The editor (and arguments) to use for the `open-editor` command. `{}`
# gets replaced by the filename of the file to be edited.
c.editor.command = ["geany","{}"]
monospace = "15px 'Tlwg Mono'"
# Font used in the completion categories.
c.fonts.completion.category = f"bold {monospace}"
# Font used in the completion widget.
c.fonts.completion.entry = monospace
# Font used for the debugging console.
c.fonts.debug_console = monospace
# Font used for the downloadbar.
c.fonts.downloads = monospace
# Font used in the keyhint widget.
c.fonts.keyhint = monospace
# Font used for error messages.
c.fonts.messages.error = monospace
# Font used for info messages.
c.fonts.messages.info = monospace
# Font used for warning messages.
c.fonts.messages.warning = monospace
# Font used for prompts.
c.fonts.prompts = monospace
# Font used in the statusbar.
c.fonts.statusbar = monospace
# Font used in the tab bar.
#c.fonts.tabs = monospace
# Chars used for hint strings.
c.hints.chars = "asdfghjklie"
# Leave insert mode if a non-editable element is clicked.
c.input.insert_mode.auto_leave = True
# Automatically enter insert mode if an editable element is focused
# after loading the page.
c.input.insert_mode.auto_load = True
# Show a scrollbar.
c.scrolling.bar = "always"
# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
c.scrolling.smooth = True
# Open new tabs (middleclick/ctrl+click) in the background.
c.tabs.background = True
# Behavior when the last tab is closed.
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = "close"
# Padding around text for tabs
c.tabs.padding = {
    "left": 5,
    "right": 5,
    "top": 0,
    "bottom": 1,
}
# Which tab to select when the focused tab is removed.
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = "prev"
# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
c.url.searchengines = {
"DEFAULT": "https://duckduckgo.com/?ia=web&q={}",
"g" : "https://www.google.es/search?q={}",
"y" : "https://www.youtube.com/results?search_query={}",
"d" : "https://duckduckgo.com/?ia=web&q={}",
"r" : "https://www.reddit.com/search?q={}",
"d" : "https://dle.rae.es/{}",
"w" : "https://en.wikipedia.org/wiki/{}",
"m" : "https://www.openstreetmap.org/search?query={}",
"gi" : "https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1",
"gh" : "https://github.com/search?q={}"
}
# The format to use for the window title. The following placeholders are
# defined:
#   * `{perc}`: The percentage as a string like `[10%]`.
#   * `{perc_raw}`: The raw percentage, e.g. `10`
#   * `{title}`: The title of the current web page
#   * `{title_sep}`: The string ` - ` if a title is set, empty otherwise.
#   * `{id}`: The internal window ID of this window.
#   * `{scroll_pos}`: The page scroll position.
#   * `{host}`: The host of the current web page.
#   * `{backend}`: Either ''webkit'' or ''webengine''
#   * `{private}` : Indicates when private mode is enabled.
c.window.title_format = "{private}{perc}{protocol}{title_sep}{current_title}"
c.tabs.title.format="{perc}{audio}{current_title}"
def filter_yt(info: interceptor.Request):
	url = info.request_url
	if (url.host() == 'www.youtube.com' and
			url.path() == '/get_video_info' and
			'&adformat=' in url.query()):
		info.block()
interceptor.register(filter_yt)
c.completion.timestamp_format="%d/%m/%Y - %H:%M:%S:%F"
c.colors.statusbar.command.bg="#000000"
c.colors.statusbar.command.fg="#FFFFFF"
c.colors.statusbar.normal.bg="black"
c.colors.statusbar.normal.fg="#FFFFFF"
c.colors.statusbar.url.success.https.fg="#00FF00"
c.colors.statusbar.url.success.http.fg="#FF0000"
c.content.autoplay=True
c.statusbar.widgets=["keypress","url","scroll"]
c.content.pdfjs=False
c.prompt.filebrowser=True
c.downloads.remove_finished=5000
c.colors.tabs.selected.even.bg="silver"
c.colors.tabs.selected.odd.bg=c.colors.tabs.selected.even.bg
c.colors.tabs.selected.even.fg="black"
c.colors.tabs.selected.odd.fg=c.colors.tabs.selected.even.fg
c.content.fullscreen.window = True
# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'no-unknown-3rdparty', 'chrome-devtools://*')
# Setting dark mode
config.set("colors.webpage.darkmode.enabled", True)
# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')
# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')
# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')
# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies# Setting default page for when opening new tabs or new windows with
# commands like :open -t and :open -w .
c.url.default_page = 'https://start.duckduckgo.com/'
c.url.start_pages = 'https://start.duckduckgo.com/'
c.fonts.default_family='12 px "Tlwg Mono"'
c.fonts.tabs.selected="15px 'Tlwg Mono'"
c.fonts.tabs.unselected="12px 'Tlwg Mono'"
c.fonts.prompts="12px 'Tlwg Mono'"
c.fonts.web.family.sans_serif='"12px" "Tlwg Mono"'
c.fonts.web.family.cursive="'12px''Tlwg Mono'"
c.fonts.web.family.fantasy="'12px' 'Tlwg Mono'"
c.fonts.web.family.serif="'12px' 'Tlwg Mono'"
c.fonts.web.family.standard="'12px' 'Tlwg Mono'"
c.tabs.show="multiple"
