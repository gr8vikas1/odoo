import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';
import { url } from '@web/core/utils/urls';

import { NavBar } from '@web/webclient/navbar/navbar';
import { AppsMenu } from "@ip_web_theme/webclient/appsmenu/appsmenu";

patch(NavBar.prototype, {
    setup() {
        super.setup();
        this.companyService = useService('company');

        this.appMenuService = useService('app_menu');
        if (this.companyService.currentCompany.has_appsbar_image) {
            this.sidebarImageUrl = url('/web/image', {
                model: 'res.company',
                field: 'appbar_image',
                id: this.companyService.currentCompany.id,
            });
        } else {
            this.sidebarImageUrl = '/base/static/img/res_company_logo.png';
        }
    },

});

patch(NavBar, {
    components: {
        ...NavBar.components,
        AppsMenu,
    },
});
