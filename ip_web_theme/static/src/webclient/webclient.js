import { patch } from '@web/core/utils/patch';
import { WebClient } from '@web/webclient/webclient';
import { AppsBar } from './appsbar/appsbar';
import { session } from "@web/session";
import { cookie } from "@web/core/browser/cookie";

patch(WebClient.prototype, {
    setup() {
        super.setup();
        this.updateTheme();
    },

    updateTheme() {
        const theme = session.theme_mode || 'light';
        document.body.classList.remove('mk_theme_mode_light', 'mk_theme_mode_dark');
        document.body.classList.add(`mk_theme_mode_${theme}`);
        cookie.set("color_scheme", document.body.classList.contains('mk_theme_mode_dark') ? "dark" : "light", 365);

    }
});

patch(WebClient, {
    components: {
        ...WebClient.components,
        AppsBar,
    },
});