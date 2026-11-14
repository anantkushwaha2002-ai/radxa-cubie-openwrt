local http = require "luci.http"

module("luci.controller.quickstart", package.seeall)

function index()
    if luci.sys.call("pgrep quickstart >/dev/null") == 0 then
        entry({"admin", "quickstart"}, template("quickstart/home")).leaf = true
    else
        entry({"admin", "quickstart"}, call("redirect_fallback")).leaf = true
    end
end

function redirect_fallback()
    luci.http.redirect(luci.dispatcher.build_url("admin", "status"))
end

local function vue_lang()
    local i18n = require("luci.i18n")
    local lang = i18n.translate("quickstart_vue_lang")
    if lang == "quickstart_vue_lang" or lang == "" then
        lang = "en"
    end
    return lang
end

function quickstart_index(param)
    luci.template.render("quickstart/main", {prefix=luci.dispatcher.build_url(unpack(param.index)),lang=vue_lang()})
end
